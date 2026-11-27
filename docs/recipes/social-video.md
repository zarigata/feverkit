# Short-form video marketing recipe

Select the marketing profile in a project you control:

```bash
python3 tools/feverkit.py plan --project /path/to/brand-project --profile marketing
```

Review the generated plan, then use the existing apply workflow documented in README. This installs only FeverKit Markdown. External engines are optional and independently audited.

## Agent prompt

> Use FeverKit's social-video-studio and visualizemy-motion skills. Study my product and brand assets, propose three honest hooks, storyboard a 25-second vertical Reel/TikTok, then render the approved concept locally with original visuals, real product footage when applicable, captions and authorized audio. Deliver MP4, editable project, cover, platform copy and QC evidence. No posting, paid calls, uploads or third-party installs without approval.

## Choose a pipeline

| Goal | Tools | Notes |
|---|---|---|
| Branded animated explainer | Remotion or HyperFrames + FFmpeg | Best default; deterministic editable scenes. |
| Typography short | Remotion Shorts Skill | Inspect upstream skill before use; disable posting. |
| Real product demo | Playwright + Remotion/HyperFrames | Use a test account with synthetic data. |
| Faceless stock footage | MoneyPrinterTurbo | Check provider credentials and commercial asset rights. |
| AI-generated B-roll | ComfyUI + compatible LTX-Video model | Optional GPU worker; verify model license, VRAM and runtime. |
| Talking-head editing | Claude Content Kit + faster-whisper + FFmpeg | Only authorized recordings. |
| Long-to-short repurposing | Existing AutoClip | Review clip boundaries and captions. |

VisualizeMy (https://visualizemy.com/) is a manually usable creative reference, not an assumed API or bundled service. Its free tools include animated text, glitch, audio visualizers and other styles. Create original scenes locally or use approved website exports.

## Agent orchestration

A low-resource controller can generate briefs, queue work on an authorized render host and inspect returned reports. Keep one manifest per video, including language, duration, storyboard, input sources, model and cost, output paths and approval state. Use separate render and QC stages; do not expose render APIs publicly or store secrets in source control. No automatic publishing by default.

## Acceptance

A reviewable 1080x1920 H.264/AAC MP4, normally 30 fps, with synced captions and audio, no clipped text or unlicensed assets. Check ffprobe metadata, representative frames, full playback when possible, rights and factual claims. Report missing runtime tests rather than claiming successful rendering.
