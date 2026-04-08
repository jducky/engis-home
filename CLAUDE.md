# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static marketing website for **EnGIS** (엔지스), a Korean company specializing in public-sector GIS, DB systems, and AI solutions. There is no build system — files are served directly as-is.

## File Structure

- `index.html` — Main homepage (hero, services, AI solutions overview, cases, contact)
- `ai-solutions.html` — AI Solutions detail page (Knowledge, Insight, Vision products)
- `styles.css` — Single shared stylesheet for both pages
- `app.js` — Minimal JS: sticky header scroll state only
- `assets/` — SVG logo files (`engis-logo.svg`, `engis-mark.svg`)
- `docs/` — Internal planning documents (not served as pages)
- `backups/` — Backup snapshots

## Development

No build step. Open files directly in a browser or use any static file server:

```bash
python3 -m http.server 8080
# or
npx serve .
```

## Key Conventions

**CSS versioning**: `styles.css` is referenced with a cache-busting query string (e.g., `?v=20260327-4`). Bump this version string in **both** `index.html` and `ai-solutions.html` whenever `styles.css` changes.

**Design tokens**: All colors, shadows, and surfaces are defined as CSS custom properties at `:root` in `styles.css`. Edit tokens there rather than hardcoding values.

**Typography**: Body uses `Pretendard` (Korean) + `Noto Sans KR` fallback. Headings/labels use `Montserrat` (Latin). Both loaded from Google Fonts.

**Language**: All user-facing copy is Korean (`lang="ko"`). Section kickers and product names use English.

**No JS framework**: `app.js` is intentionally minimal. Avoid adding dependencies or a bundler unless the scope genuinely requires it.

## Architecture Notes

Both HTML pages share one stylesheet and follow the same header/nav/footer structure. The header is duplicated in each file (not shared via include or component). Changes to the header must be applied to both files.

The site is a redesign prototype (시안) of `http://en-gis.com`. The `docs/plan.md` file contains the analysis that drove the redesign decisions.
