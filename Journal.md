---
title: "Off-Grid Survival Emotionally Intelligent Bot"
author: "max1 on highway slack"
description: "A self-contained (no internet) self-powered (solar) voice bot, exactly the one you need for survaval critical missions"
created_at: "2025-06-28"
---

28 June 2025

Ideas.. ideas.. ideas...

Idea: create "animated face"

29 June 2025

Today is DEADLINE.

Clarify the idea:

- use LLM and Raspberry Pi
- how about Gemma 3n from Google, there is 6B version which should fir 8GB Raspberry Pi 5
- we need text to speech, oh, well we can use [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)
- we can animate the face and mouth with little servos
- let's also add 8x8 LEDs for eyes!

30 June 2025

- I asked Gemma 3n E2B

```txt
how to make shelter in the woods for 1 person
```
using text Gemma 3n E2B outputted:
```md
Okay, here's how to build a basic shelter for one person in the woods:

1.  **Find a site:** Look for a protected spot – avoid low-lying areas prone to flooding.  Consider wind direction.
2.  **Lean-to:** Find a sturdy branch or fallen tree. Lean branches against it at a 45-degree angle.
3.  **Cover:**  Pile leaves, pine needles, ferns, or other debris over the branches for insulation and weather protection. 
4.  **Insulate:** Add extra layers of insulation at the base. 

**Stay dry & warm.  Prioritize fire safety!**
```

Here is the audio using Kokoro-82M:
<audio controls>
  <source src="https://github.com/max1vol/emo-survaval-bot/raw/refs/heads/main/samples/survaval-response-sample1.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>
