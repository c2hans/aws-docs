---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/introduction.html
---

# Decomposing legacy mainframe applications by using AWS Transform
<a name="introduction"></a>

*Mohan Karunanithi, Jayanthi Rajaraman, Sivasubramanian Ramani, and Santosh Kumar Singh, Amazon Web Services*

[AWS Transform for mainframe modernization](https://aws.amazon.com/transform/mainframe/) uses generative AI to accelerate the transformation of your workloads from COBOL-based legacy environments to modern, distributed Java systems. The transformation relies on application decomposition, which is a critical process that breaks down complex, interconnected code into manageable, business-aligned modules. This approach reduces your migration risks and lets you incrementally update your core business systems to ensure continuity and innovation.

This guide explains how to use the AWS Transform modules for code decomposition and how to plan your migration for efficiency. It explores the key challenges in mapping technical components to business domains, examines why decomposition is essential for successful modernization, and provides a step-by-step walkthrough of the AWS Transform process.

## Intended audience
<a name="audience"></a>

This guide is intended for technical teams and business stakeholders who are involved in mainframe modernization projects, including:
+ Application architects
+ Migration specialists
+ Technical decision-makers
+ Business analysts
+ Development teams who work on mainframe transformation initiatives

## Objectives
<a name="objectives"></a>

This guide discusses two primary outcomes: creating a decomposition strategy and developing migration wave plans.

The decomposition strategy:
+ Aligns technical components with business functions.
+ Enables incremental modernization.
+ Reduces migration risks.
+ Improves system maintainability.

The migration wave plans help you:
+ Estimate implementation costs.
+ Set realistic timelines.
+ Prioritize business-critical components.
+ Plan resource allocation.
+ Define measurable success criteria.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
