---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/startup-resiliency-baseline/stage-1.html
---

# Stage 1: Set objectives
<a name="stage-1"></a>

Imagine that your team is in the final sprint before a major product launch. The new features are groundbreaking, and investor excitement is building. Then, during a routine deployment, your core service goes down. As customer complaints flood your email, two questions become painfully clear: How long can you afford to be offline? What data can you afford to lose?

Hoping that everything will work fine isn't a good strategy. You need a systematic way to decide where resilience matters most and where it does not. This is where a business impact analysis (BIA) becomes critical. It helps you make informed decisions about where to invest in resilience. A BIA helps you understand which parts of your system truly need rock-solid reliability and which can tolerate some flexibility.

Start by mapping out your core user journeys. For each one, ask yourself the following:
+ What's the impact if this is disrupted?
+ How quickly must we restore service?
+ What data is critical to protect?

This isn't just a technical exercise; it helps you understand the business impact of reliability issues. Lost revenue is just the beginning. Consider how outages might erode customer trust, violate regulatory requirements, or give competitors an edge.

From this analysis, you'll derive two critical numbers for each user journey: recovery time objective (RTO) and recovery point objective (RPO). RTO defines how quickly you must restore that journey. RPO defines how much data loss your customers can tolerate. These business-driven targets then guide which components you choose and how you architect them, without over-engineering every part of the system.

The beauty of this approach is that it helps you focus your limited resources where they matter most. Perhaps your core transaction processing needs near-instant recovery and zero data loss, but your recommendation engine can tolerate longer downtime. By setting clear objectives, you create a framework that lets you continue rapid feature development while strategically building in resilience.

Document these objectives clearly. They're not just for your engineering team. When you're pitching to enterprise customers or going through technical due diligence with investors, this documentation demonstrates that you've thought critically about business continuity.

These targets evolve as your startup grows. The resilience needs of your first thousand users are different from those of your first enterprise client. Start with objectives that you can realistically meet today, but plan for how they'll tighten as you scale.

This guide explores how to implement resilience measures that meet these objectives. Setting these targets is your crucial first step. They're your compass for navigating the constant tension between innovation and stability, helping you build a system that dependably delivers value to your customers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
