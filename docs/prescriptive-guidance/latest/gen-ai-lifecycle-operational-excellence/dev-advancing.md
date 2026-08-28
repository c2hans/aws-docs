---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-advancing.html
---

# Advancing a generative AI PoC to preproduction
<a name="dev-advancing"></a>

The culmination of the PoC stage is a critical decision gate. It's the moment where the initial hypotheses are measured against real-world data. You make a formal, evidence-based decision about the future of the initiative. This is not a moment for intuition—it is a structured evaluation that determines whether to proceed with further investment, pivot the approach, or halt the project.

**This section contains the following topics:**
+ [Evaluating the PoC outcome](#dev-advancing-evaluation)
+ [Making a go or no-go decision](#dev-advancing-decision)
+ [Preparing for preproduction](#dev-advancing-preparation)

## Evaluating the PoC outcome
<a name="dev-advancing-evaluation"></a>

You must present the final evaluation in the language of business value. Directly reference the objectives and measures that you established at the project's outset.

Consider the following when evaluating the success of the PoC:
+ **Performance against key performance indicators (KPIs)** – The most important step is to measure the PoC's performance against the predefined success metrics. For example, did the solution achieve the target time reduction, or did it meet the required accuracy or faithfulness scores? This quantitative analysis provides an objective measure of success.
+ **Qualitative feedback and user experience** – What was the feedback from stakeholders and test users? Was the tool intuitive? Did it solve their problem in a way they found valuable? Qualitative insights often reveal critical nuances that metrics alone cannot capture.
+ **Technical stability and scalability** – Did the PoC architecture perform reliably? While the PoC platform is minimal, this is the time to identify any fundamental technical roadblocks or scalability concerns that were discovered. This includes assessing latency, cost per interaction, and the reliability of data pipelines.
+ **Key learnings and required changes** – No PoC is perfect. A core outcome is a list of key learnings. What assumptions were wrong? What new challenges were discovered? This analysis is crucial for accurately scoping the effort required for the next phase.

## Making a go or no-go decision
<a name="dev-advancing-decision"></a>

With the evaluation complete, the team and stakeholders must make a formal go or no-go decision. This decision should be guided by a clear set of criteria that is revisited from the initial planning phase. To help you make this decision, answer the following questions:
+ Has the PoC demonstrated that it can deliver meaningful business value and solve the intended problem?
+ Is the technical solution viable, and is the path to a more robust implementation clear?
+ Based on the PoC's performance and cost metrics, does the solution still have a positive ROI?
+ Does the solution still align with the company's broader strategic goals?

If you confidently answer yes to these questions, then the project is ready to move from your development environment to a preproduction environment.

## Preparing for preproduction
<a name="dev-advancing-preparation"></a>

The transition from development to preproduction environments marks a significant step in maturity. To prepare for this transition, do the following to ready your PoC:
+ **Formalize the architecture** – Evolve the lightweight PoC architecture into a more robust, modular, and secure design suitable for a pilot with real users.
+ **Establish formal generative AI operations (GenAIOps)** – Implement a formal CI/CD pipeline for all AI artifacts, including prompts, configurations, and evaluation datasets. This helps you test and deploy changes in a controlled and repeatable manner.
+ **Expand the evaluation suite** – Enhance your evaluation dataset with learnings from the PoC, including new edge cases and failure modes that you discovered during testing.
+ **Prepare for a pilot** – Develop a simple but functional user interface and prepare to onboard a small group of pilot users to gather real-world feedback. This is the first step in the journey from a validated concept to a true minimum viable product.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
