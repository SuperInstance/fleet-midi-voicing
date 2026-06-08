# fleet-midi-voicing

_Voicing analyzer — how wide are your intervals?_

_One of 16 ternary MIDI agents in the [Live Paradigm Fleet](https://github.com/SuperInstance/sailor-workspace)._

---

## Philosophy — Why Ternary?

The Live Paradigm treats musical gestures as ternary operations. Where binary logic
gives yes/no, ternary gives **approve/reject/observe** — a richer cognitive substrate
that maps naturally to music theory, emotional tension, and conversational flow.

This agent implements **ternary decomposition for voicing**.

## Architecture

Position in the fleet pipeline:

```
🎤 Voice → OpenSMILE (25 features) → Ghost Track (T-0..T-4 CR predictions)
  → tminus-dispatcher (cue scheduling) → Fleet Conductor (routing)
  → voicing (port 2162)
```

## API Reference

| Method | Path | Description |
|--------|------|-------------|
| GET | /health | Health check + agent identity |
| POST | /agent with `{"type":"probe"}` | Liveness probe for fleet-conductor |
| POST | /agent | Process musical data, return ternary analysis |
| POST | / | Direct query with JSON body |

### Response Format

```json
{
  "status": "ok",
  "agent": "fleet-midi-voicing",
  "port": 2162,
  "ternary_vector": [0, 0, 0],
  "ternary_invariant": 0,
  "closed_gesture": false
}
```

## Ternary Logic

| Position | +1 | 0 | -1 |
|----------|------|------|------|
| ternary[0] | open (wide intervals) | medium | closed (tight intervals) |

## Educational Supplement

Voicing is the way notes of a chord are arranged across the keyboard (or frequency spectrum).
The same chord (say, C major) can be voiced in dozens of ways, each with a different
texture and emotional quality.

### Closed Voicing
All notes within one octave: C-E-G (root position, three notes packed together).
Sounds thick, dense, "traditional."

### Open Voicing
Notes spread across multiple octaves: C-G-E-C.
Sounds airy, spacious, "modern."

Ternary captures this: +1 for open (approving space), -1 for closed (rejecting space).

## Fleet Integration

- **Port**: 2162
- **Roles**: note, velocity
- **Conductor ID**: `voicing`
- **Protocol**: HTTP POST to `/2162/agent` with JSON body, 5s timeout
- **Conservation Law**: Σ(Δ_midi) = 4 × Σ(ternary) — closed gestures return to start

## Starting

Local development:

```bash
python3 engine.py --port 2162
```

Or via the fleet start script:

```bash
./scripts/start-fleet-agents.sh
```

## Credits

**Part of the Live Paradigm Fleet** — A ternary cognitive architecture for musical AI.
GitHub: github.com/SuperInstance
Fleet conductor: [sailor-workspace](https://github.com/SuperInstance/sailor-workspace)
