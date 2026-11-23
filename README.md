# Multimodal Video Agent Pipeline

> An autonomous video generation and classification pipeline designed to eliminate character drift, hallucinations, and temporal inconsistency by combining deterministic 3D spatial anchors with generative diffusion video models.

---

## Architecture Overview

Pure generative AI video models often suffer from temporal inconsistency, morphing characters, and lip-sync degradation. This system solves these failure modes via a hybrid deterministic-generative architecture:

```
[ Narration Script ] ---> [ Pacing Optimizer (WPM / Beat Timing) ]
                                      |
[ Scene Storyboard ] ---> [ Shot Classification Agent ]
                               /              \
             (3D Anchors / Sync)            (Cinematics / Backgrounds)
                             v                        v
            Deterministic 3D Engine          Generative Diffusion Engine
                             \              /
                              v            v
                    [ Automated FFmpeg Compositor ]
                                   v
                             [ Final Output ]
```

### Core Components

1. **Shot Classification Agent (`pipeline/classifier.py`)**: Evaluates narrative beat, facial framing, and interaction complexity to assign each shot to the optimal rendering tier:
   - `DETERMINISTIC_3D`: High character fidelity, lip-sync, and choreography.
   - `GENERATIVE_ENHANCED`: 3D geometry reference frames enhanced via diffusion.
   - `GENERATIVE_FIRST`: Macro landscapes, volumetric atmospheres, and crowd life.
2. **Audio Pacing Optimizer (`pipeline/pacing_optimizer.py`)**: Computes words-per-minute (WPM), aligns audio beats with visual cuts, and eliminates narration lag.
3. **Pipeline Orchestrator (`pipeline/orchestrator.py`)**: Manages end-to-end manifest generation, validation, and render sequencing.

---

## Quickstart

```bash
# Clone the repository
git clone https://github.com/your-username/multimodal-video-agent-pipeline.git
cd multimodal-video-agent-pipeline

# Install dependencies
pip install -r requirements.txt

# Run the pipeline planner
python main.py
```

---

## License
MIT License
