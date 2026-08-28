---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-chaos-engineering-journey/goals-roi.html
---

# The shift from goals to measuring ROI
<a name="goals-roi"></a>

As the practices mature and the initial goals are achieved, the focus eventually shifts from setting goals toward quantifying the tangible financial benefits of chaos engineering—the return on investment (ROI). The shift stems from two primary reasons:
+ Economic considerations
+ Preserving customer experience and trust

## Economic considerations
<a name="economics"></a>

In times of economic growth and healthy finances, companies often don't need extensive justification to set specific goals for chaos engineering strategies. However, changes in the financial landscape have led many organizations to reevaluate their investments, and chaos engineering implementations need to provide quantified ROI.

These companies are now tasked with setting clear, traditional ROI metrics to demonstrate the value and impact of chaos engineering practices. This challenge is further complicated by the [prevention paradox](strategic-necessity.md#prevention-paradox). The prevention paradox occurs when successful prevention of incidents makes it harder to justify the investment, because stakeholders tend to undervalue avoided catastrophes. Even organizations with a deeply ingrained culture of operational excellence face pressure to use ROI metrics to justify the continued adoption of chaos engineering.

## Preserving customer experience and trust
<a name="cx-trust"></a>

Sustaining goal-driven resilience can be challenging over the long term. After an initial goal such as achieving a recovery time target is met, justifying continuous chaos engineering investment becomes difficult until the next major outage. The flow and ebb of investment creates a reactive saw-tooth cycle. For each new outage, investment in resilience spikes with a new goal addressing the root cause. After the new goal is met, investment drops until the next incident, restarting the reactive loop.

The outages that drive this reactive approach negatively impact customers. The key question: How many major outages will customers tolerate before they abandon a service provider in favor of a more resilient competitor?

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
