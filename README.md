# copecoder.com

My personal website: portfolio, writing and CV.

Cloudflare Pages rebuilds and publishes the site automatically every time a change is saved to this repository.

## Where things live

| File | What it holds | How often you'll touch it |
|---|---|---|
| `content.py` | All the text: bio, project and post titles, dates, write-ups, links, sources | Most often |
| `style.css` | The look: colours, fonts, sizes, spacing, phone layout | Sometimes |
| `assets/` | Images and the CV PDF | When adding a post, project or new CV |
| `build.py` | Turns `content.py` and `style.css` into the finished pages | Rarely |

## Common edits

**Fix a typo or change wording.** Open `content.py` on GitHub, click the pencil icon, edit the text between the quotation marks, then click **Commit changes**. The live site updates in a minute or two.

**Replace the CV.** Upload the new PDF into `assets/` with the exact name `Shiloh_Ayala_CV.pdf` so it replaces the old one.

**Add a post or project.** Upload its image into `assets/`, then copy an existing entry in `POSTS` or `PROJECTS` in `content.py` and change the details. Newest goes first in each list. Each entry needs its own `slug`, which becomes the page address.

**Change a colour.** The colours are at the top of `style.css`: the first block is light mode, the two blocks after it are dark mode.

## Careful with

- Quotation marks and commas in `content.py`: each piece of text sits inside quotes, and entries are separated by commas. If one goes missing, the build fails and the live site simply stays on the previous version until it's fixed. Cloudflare's deployment page shows the error.
- Curly apostrophes (’) are used in the text on purpose. Straight ones (') also work inside double quotes.

## Building on your own computer (optional)

With Python 3 installed, run `python3 build.py`, then open `site/index.html` in a browser.

## Cloudflare Pages settings

- Build command: `python3 build.py site`
- Build output directory: `site`
- Production branch: `main`
