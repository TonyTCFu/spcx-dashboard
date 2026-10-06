# AGENTS.md

## Project Overview
* Project Name: SpaceX股票研究 (SpaceX Stock Research / Quant & Automations)
* Created Date: 2026-08-12
* Primary Stack: Python, Web Search, Research & Financial Analysis

## Rules & Standards
1. Follow user's global custom rules strictly.
2. Mandatory output structure with 5 modules for responses.
3. Information classification: Verified Facts / Logical Inferences / Subjective Judgments / Unverified.

## TypeSafe Skill Trigger Policy

1. At the start of every new project conversation, load the `jev` skill (TypeSafe; canonical skill `typesafe-ai`) before substantive work, regardless of task type. Use its semantic judgment workflow when a task introduces unstructured news, research reports, event narratives, or source documents that need event classification, claim-to-evidence verification, relevance ranking, or impact-priority scoring.
2. Use narrow typed judgments: `Choice` for an event category, `Noul` for a specific evidence check, and `Score` for a defined impact rubric. Surface uncertainty instead of treating a low-confidence answer as a market fact.
3. Keep TypeSafe outputs as research aids. They must not alter price ingestion, short-interest calculations, dashboard market metrics, or create a trading conclusion without independently verified source evidence.
4. Do not invoke TypeSafe for Yahoo/NASDAQ data ingestion, numeric calculations, JSON validation, dashboard rendering, or other deterministic operations. Keep credentials outside source code and logs.
