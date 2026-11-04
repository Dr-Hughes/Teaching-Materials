#!/usr/bin/env python3
"""Check every lesson.yaml: required fields, allowed values, and that the files
it lists and the files in its folder match exactly. Exit 1 on any problem."""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ['title', 'subject', 'level', 'year', 'topic']
LEVELS = {'ks3': 'KS3', 'gcse': 'GCSE', 'a-level': 'A-level', 'workshops': 'Workshop'}
SUBJECTS = {'computer-science': 'Computer Science', 'creative-imedia': 'Creative iMedia'}
KINDS = {'slides', 'student', 'teacher'}

problems = []
lessons = sorted(ROOT.glob('*/*/*/lesson.yaml'))
for meta in lessons:
    rel = meta.parent.relative_to(ROOT)
    subject_dir, level_dir, _ = rel.parts
    data = yaml.safe_load(meta.read_text())
    for key in REQUIRED:
        if not data.get(key):
            problems.append(f'{rel}: missing {key}')
    if SUBJECTS.get(subject_dir) != data.get('subject'):
        problems.append(f'{rel}: subject {data.get("subject")!r} does not match folder {subject_dir}')
    if LEVELS.get(level_dir) != data.get('level'):
        problems.append(f'{rel}: level {data.get("level")!r} does not match folder {level_dir}')
    listed = []
    for f in data.get('files') or []:
        if f.get('kind') not in KINDS:
            problems.append(f'{rel}: {f.get("path")} has kind {f.get("kind")!r}')
        if not f.get('label'):
            problems.append(f'{rel}: {f.get("path")} has no label')
        if ' ' in f['path']:
            problems.append(f'{rel}: {f["path"]} has a space in its name')
        listed.append(f['path'])
    on_disk = {p.name for p in meta.parent.iterdir() if p.is_file() and p.name not in ('lesson.yaml', '.DS_Store')}
    for missing in sorted(set(listed) - on_disk):
        problems.append(f'{rel}: lists {missing}, which is not in the folder')
    for extra in sorted(on_disk - set(listed)):
        problems.append(f'{rel}: {extra} is in the folder but not listed in lesson.yaml')

stray = [p for p in ROOT.glob('*/*/*') if p.is_dir() and not (p / 'lesson.yaml').exists() and '.git' not in p.parts]
problems += [f'{p.relative_to(ROOT)}: folder has no lesson.yaml' for p in stray]

print('\n'.join(problems) or f'{len(lessons)} lessons OK')
sys.exit(1 if problems else 0)
