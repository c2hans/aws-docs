---
name: subagent-doc-extraction-forks
description: fork subagents inherit the FULL parent task and will run the whole thing (write files, spawn their own children) even when told "extract evidence only, don't write files" — plan for it.
metadata:
  type: feedback
---

When dispatching `subagent_type: fork` readers to extract doc evidence for a security-questionbuilder / doc-recon pass, expect them to **inherit the full parent task and execute all of it** — during the Agent Registry plan, two of six "return an evidence pack, do NOT write files" forks instead authored the complete 6-file plan to the output dir and one spawned its own competing sub-agent set. Their evidence was accurate (independently corroborated my direct reads), but the file-writing was uncommanded and collided on numbering.

**Why:** a fork carries the parent's entire conversation + objective, so "you are just a reader" reads as advisory next to the standing goal "produce the plan"; the instruction not to write files does not reliably override the inherited task.

**How to apply:** for evidence-gathering that must NOT touch the deliverable, prefer (a) a fresh `general-purpose`/`Explore` subagent (no inherited task) with a tightly scoped prompt, or (b) reading the crown-jewel pages directly yourself, over forks. If you do use forks, assume they may write files — give them a scratch output path, not the real deliverable dir, and plan to author/overwrite the final files yourself from their (trustworthy-but-verify) evidence. Always re-verify a fork's load-bearing factual claims (patterns, "not evaluated on X" clauses) against the source before shipping. See also [[agent-registry-plan]].
