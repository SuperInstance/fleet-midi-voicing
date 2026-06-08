# Student Guide: fleet-midi-voicing

_Learn how the voicing agent works and how to use it._

---

## What You'll Learn

1. What the voicing musical concept is
2. How ternary decomposition applies to voicing
3. How to query the agent
4. How to interpret the response

## Step 1: Start the Agent

```bash
python3 engine.py --port 2162
```

## Step 2: Query the Agent

```bash
curl -s http://localhost:2162/health | python3 -m json.tool
```

You should see:

```json
{
  "status": "ok",
  "agent": "fleet-midi-voicing",
  "port": 2162
}
```

## Step 3: Send Musical Data

```bash
curl -s -X POST http://localhost:2162/agent \
  -H 'Content-Type: application/json' \
  -d '{"input": "test"}' | python3 -m json.tool
```

## Step 4: Interpret the Ternary Vector

The response includes a `ternary_vector` field. Each position represents a
musical dimension:

- `ternary[0]`: The primary classification (approve/reject/observe)
- Remaining positions: Secondary attributes

## Exercise

Experiment with different inputs and observe how the ternary vector changes.
What inputs produce [+1, 0, 0]? What produces [-1, 0, 0]?

---

_This is part of the educational supplement for the [Live Paradigm Fleet](https://github.com/SuperInstance/sailor-workspace)._
