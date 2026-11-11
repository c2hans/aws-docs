---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/azure-to-aws-platform-migration/best-practices.html
---

# Best Practices
<a name="best-practices"></a>

## Use AI for what it's good at, scripts for what it's not
<a name="use-ai-for-what-it-s-good-at--scripts-for-what-it-s-not.ced5783f-fcf1-50a4-815c-37fe95b7f2c0"></a>

AI excels at reading across large datasets, recognizing patterns, classifying resources, synthesizing prose, and generating diagrams. Scripts excel at counting, completeness checking, and mechanical validation. Humans excel at judgment, architectural decisions, and interpreting ambiguous information. The most common failure mode is letting these roles blur. Keep the boundaries sharp.

## Design focused, single-purpose prompts
<a name="design-focused--single-purpose-prompts.a9d011fc-89bc-5530-9b9a-fdb2d54e94e3"></a>

A prompt that says "document the cloud environment" will produce plausible-looking but unverifiable content. A prompt that says "read these specific CSVs, populate these specific inventory templates, and produce these specific output files" produces traceable, verifiable content.

Keep each prompt focused on one task with explicit inputs and outputs. A single meeting transcript can consume the full context window — don't try to process all transcripts in one prompt. The same applies to subscription analysis, acceptance criteria filling, and enrichment. Smaller, focused prompts produce better results than large multi-step ones.

## Never let AI count — always pre-compute
<a name="never-let-ai-count---always-pre-compute.00689d13-613d-57fa-9a01-595e35342517"></a>

AI tools are unreliable counters. They may count 47 resources when there are 52, or state "3 DEV, 5 Non-PRD" when the actual breakdown is "4 DEV, 4 Non-PRD." These errors are subtle and hard to catch in review.

Generate authoritative counts with validation scripts and instruct AI to reference those counts rather than counting independently. Every prompt that touches inventory data should include the rule: "Do NOT count resources yourself."

## Work on one acceptance criteria at a time
<a name="work-on-one-acceptance-criteria-at-a-time.8b8c2e63-be52-5efd-a64f-fc74b39e090b"></a>

Each acceptance criteria file is a focused, self-contained task. AI reads one AC plus its supporting data, makes changes, and moves on. This keeps the context small and prevents AI from corrupting adjacent sections in a large document. The rollup script assembles the individual acceptance criteria into deliverables after they're validated — not before.

## Enrich from the bottom up
<a name="enrich-from-the-bottom-up.e3968d93-c49e-5538-88df-8d653abd05d1"></a>

Enrich the lowest-level source data first, then build higher-level documents from the enriched data. If a cloud resource inventory needs to reference which pipeline deploys it, the pipeline inventory must be enriched with Domain, Purpose, and Deploys To before the cloud resource enrichment runs. The same principle applies throughout: raw CSVs get enriched before relationship docs are built, relationship docs exist before acceptance criteria are filled, and current-state acceptance criteria are accurate before target-state work begins. Each layer depends on the accuracy of the layer below it.

## Approve the high-level architecture before detailed acceptance criteria work
<a name="approve-the-high-level-architecture-before-detailed-acceptance-criteria-work.3b628cb3-52e1-5c56-87f2-5a6ab3ffed4b"></a>

Do not let AI fill target-state acceptance criteria without an approved high-level architecture document. Without it, each acceptance criterion makes independent architectural decisions that may contradict each other. Generate the high-level target state architecture first, get architect approval, then use it as the guiding constraint for every detailed acceptance criterion.

## Maintain source data provenance
<a name="maintain-source-data-provenance.b73e15e4-2ddb-55ee-bc42-003decc2d6cb"></a>

Every claim in a deliverable should be traceable back through the full chain to raw source data:

```
Target State Deliverable (Migration Strategy)
  → references current-state acceptance criteria counts and resource names
    → acceptance criteria reference enriched inventory CSV rows
      → enriched inventory CSVs have raw_scrape_origin linking to extraction CSVs
        → extraction CSVs come from live environment API calls
```

This chain means a reviewer can take any statement in a target-state document — "migrate 4 production App Services to AWS App Runner" — and trace it back through the current-state acceptance criteria that listed those 4 App Services, to the inventory CSV rows with their Domain, Purpose, and Deployed By columns, to the specific raw extraction CSV and row number from the source subscription. If any link in the chain breaks, the validation scripts catch it.

## Invest in transcript indexing early
<a name="invest-in-transcript-indexing-early.02ca8f7e-bb09-516f-a09a-37b1de9c1bcc"></a>

Meeting transcripts are the richest source of architectural context, operational knowledge, and decision rationale — but also the most expensive content to process. Create companion indexes immediately after each meeting, while the content is fresh. Build the root index after all companion indexes are done. This upfront investment pays off throughout the engagement as AI needs to reference specific discussions without loading entire transcripts.

## Validate continuously, not just at the end
<a name="validate-continuously--not-just-at-the-end.2aaf8c02-8788-5495-89ce-a09a30baf32e"></a>

Run validation scripts after every AI session, not just before delivery. Early detection of count mismatches or hallucinated resource names is much cheaper to fix than late detection. The validation loop — AI writes → script validates → corrections applied — typically runs 2-3 iterations per acceptance criterion before all counts align.
