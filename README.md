# Teaching Materials

Lesson slides, worksheets, answers and code from [Dr. Aoife Hughes](https://dr-hughes.uk/about/), free for everyone.
Browse them on **[dr-hughes.uk/teaching](https://dr-hughes.uk/teaching/)**: every download link on that page points here.

## Licence

[CC BY-NC 4.0](LICENSE): use, adapt and share these however you like, with credit. My only ask is that they are
**never sold or used in for-profit education**. Credit line: *"Adapted from Dr. Aoife Hughes, dr-hughes.uk, CC BY-NC 4.0"*.

## Layout

```
<subject>/<level>/<lesson>/
  lesson.yaml        what the lesson is, and a label for each file
  *.pptx *.pdf ...   the files themselves
```

- `subject`: `computer-science`, `creative-imedia`
- `level`: `ks3`, `gcse`, `a-level`, `workshops`
- `lesson`: `<year>-<topic>-<title>` in lowercase-with-hyphens, e.g. `y10-systems-architecture-inside-the-cpu`.
  Workshops with no year group are just `<title>`.

File names use lowercase and hyphens, no spaces, so links stay clean.

## lesson.yaml

```yaml
title: Inside the CPU            # shown on the site
subject: Computer Science        # Computer Science | Creative iMedia
level: GCSE                      # KS3 | GCSE | A-level | Workshop
year: Y10                        # Y7, Y10, Y10–11, Y12–13, Any ...
topic: Systems Architecture
description: One or two sentences. # optional
view: /slides/decks/<deck>/      # optional: a browser deck or tool on dr-hughes.uk
files:                           # in the order they should be listed
  - path: y10-inside-the-cpu.pptx
    label: Lesson slides (PowerPoint)
    kind: slides                 # slides | student | teacher
```

`kind: teacher` marks teacher versions and answers.

The site (`Dr-Hughes/dr-hughes.uk`, `apps/site/src/data/catalogue.yaml`) currently keeps its own copy of these entries.
The plan is to build that page straight from this repo, so keep this layout and `lesson.yaml` format.

## Adding a lesson

1. Make the folder and copy the files in.
2. Write `lesson.yaml`.
3. Run `python3 scripts/check.py` (every file listed exists, every file is listed, fields are valid).
4. Commit and push, then add the same entry to the site's catalogue.

Before committing, strip author metadata and speaker notes you don't want to publish from Office files.
