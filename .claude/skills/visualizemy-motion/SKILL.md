---
name: feverkit-visualizemy-motion
description: Design original VisualizeMy-inspired animated explainers, stickman and low-poly scenes, kinetic typography, glitch effects, and audio visualizers for short-form marketing.
---

# VisualizeMy-inspired motion design

Use this skill when asked for animated social clips, faceless explainers, visualizers, or a reference from https://visualizemy.com/. This is an independent FeverKit prompt, not the site's proprietary prompt or an official integration.

1. Identify the intended audience, product benefit, brand kit, language, platform, duration, and CTA. Default to vertical 1080x1920, 15–35 seconds, and a single clear message. Ask only for blockers; label assumptions.
2. Choose a visual system: expressive stick figures with readable silhouettes; original low-poly scenes; kinetic typography; waveform/spectrum animation driven by actual audio; CRT/glitch/datamosh as brief transitions; or clean product motion graphics. Avoid copying third-party assets or exact branded designs.
3. Draft a timed storyboard with visual action, narration, on-screen text, audio cues, easing and transitions for each shot. Start with an honest hook, deliver value, then a specific CTA. Keep important elements away from platform UI; review safe zones per platform.
4. Prefer deterministic local rendering: Remotion (React/SVG/Canvas), HyperFrames (HTML/CSS), Blender if already available for 3D, and FFmpeg for audio and mastering. Use actual product captures when showing product features. For waveform animation use decoded audio samples, not arbitrary motion.
5. VisualizeMy can be used manually for supported free exports when the user approves the upload and asset rights; do not assume a public API, scrape paid prompts, bypass limitations, or upload confidential files. Local recreation is the default. Do not claim a third-party service generated anything unless verified.
6. Implement editable scenes, reusable brand tokens, captions, and audio timing. Use licensed original or authorized assets and record their provenance. Limit flashes, avoid unreadable text, and offer reduced-motion variants when appropriate.
7. Render a draft, inspect a contact sheet at scene cuts and captions, play the full clip when possible, check voice/music balance, confirm duration and dimensions with ffprobe, and fix defects before final export. Report unperformed checks honestly.

Deliver: storyboard, editable source, MP4 H.264/AAC, cover image, caption copy, optional SRT, and asset/license notes. If no renderer is installed, deliver the storyboard and a proposed setup rather than claiming a video was rendered. Never install upstream dependencies, spend credits, or publish without approval.
