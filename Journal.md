---
title: "Off-Grid Survival Emotionally Intelligent Bot"
author: "max1 on highway slack"
description: "A self-contained (no internet) self-powered (solar) voice bot, exactly the one you need for survaval critical missions"
created_at: "2025-06-28"
---

Total time spent: 27h

## 28 June 2025

> Spent: 1h

Ideas.. ideas.. ideas...

Idea: create "animated face"

## 29 June 2025

> Spent: 2h

Today is DEADLINE.

Clarify the idea:

- use LLM and Raspberry Pi
- how about Gemma 3n from Google, there is 6B version which should fir 8GB Raspberry Pi 5
- we need text to speech, oh, well we can use [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)
- we can animate the face and mouth with little servos
- let's also add 8x8 LEDs for eyes!

## 30 June 2025

> Spent: 2h

- I asked Gemma 3n E2B

```txt
how to make shelter in the woods for 1 person
```

using text Gemma 3n E2B outputted:

```md
Okay, here's how to build a basic shelter for one person in the woods:

1.  **Find a site:** Look for a protected spot – avoid low-lying areas prone to flooding. Consider wind direction.
2.  **Lean-to:** Find a sturdy branch or fallen tree. Lean branches against it at a 45-degree angle.
3.  **Cover:** Pile leaves, pine needles, ferns, or other debris over the branches for insulation and weather protection.
4.  **Insulate:** Add extra layers of insulation at the base.

**Stay dry & warm. Prioritize fire safety!**
```

Here is the audio using Kokoro-82M: [audio](https://github.com/max1vol/emo-survaval-bot/blob/main/samples/survaval-response-sample1.wav)

## 30 June 2025 (evening)

> Spent: 3h

- Started learning how to do a CAD model!

<img width="637" alt="image" src="https://github.com/user-attachments/assets/4bb23068-0d29-4b3c-803b-e87bd1571cb7" />
  
- Squares at the top are eyes (8x8 LEDs)
<img width="349" alt="image" src="https://github.com/user-attachments/assets/d3387a8c-0872-43b7-8194-b5bf8ae0187d" />

- The mouth will be animated by
- The horizontal rod is a mouth :)

## 1 June 2025

> Spent: 4h

- Successfully running Gemma 3n E2B with text, it works!
- Experiemnted with running Gemma 3n E2B with _audio_ -- does not work
- Text-to-speech module (Kokoro) -- works!

## 2 June 2025

> Spent: 2h

- Change of plans: instead of Gemma "native audio", I'll use ASR+TTS and LLM for text only
- Experiments with Whisper-turbo

## 3 June 2025

> Spent: 3h

- Trying to figure out how solar panel charging a batter would work
- Realized that BOM does not include battery (!)
- Got old Raspberry Pi 3, trying to setup 1B llama

## 4 June 2025

> Spent: 2h

- Got Google Voice Kit (from my sister)
- Experiemnting with voice input/output

## 5 June 2025

> Spent: 2h

- Got Kokoro TTS workin in INT8 locally using ONXX!!

See https://github.com/max1vol/emo-survaval-bot/blob/main/tts/tts.py
And https://github.com/max1vol/emo-survaval-bot/blob/main/tts/audio.wav

## 6 June 2025

> Spent: 6h

- LLM is working!
- Experimented with Qwen3-0.6B, it's a thinking model
- Experimented with Google's Gemma 3 1B Q4 quantization
- Aiming to run Gemma3-1B as thinking model might be not great for real-time chat
- Got ASR (automatic speech recognition) working using Whisper/tiny.en
