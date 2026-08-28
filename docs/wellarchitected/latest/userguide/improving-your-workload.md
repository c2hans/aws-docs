---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/improving-your-workload.html
---

# Improving your workload
<a name="improving-your-workload"></a>

 At this point, you've prepared for the WAFR, completed a review, and assessed your workload against AWS best practices.

 The output from the WAFR will have identified architectural risks based on the answers captured during the review. These risks are categorized as *high risk issues (HRIs)* and *medium risk issues (MRIs)*.

 During the last phase, you will create an improvement plan that involves creating a list of risks, understanding their impact on your business, identifying solutions, and implementing those solutions according to your organization's priorities.

 The following sections provide detailed guidance on the workload improvement process:
+  Identify and understand risks
+  Determine prescriptive solutions
+  Prioritize improvements
+  Implement and track improvements

 The following cycle shows the main steps included in the *improvement* phase of the WAFR.

![Improvement cycle](http://docs.aws.amazon.com/wellarchitected/latest/userguide/images/improvement_cycle.png)

## Timeline after the WAFR
<a name="timeline-after-the-wafr"></a>

 **One day after the WAFR:**

1. Create a recap email with the improvement plan, and summarize:
   + Who was in the review
   + Key findings
   + Timeline for next steps

1. Attach the improvement plan

1. Orient the teams to plan

 **Two to three days after the WAFR:**

1. Create an HRI prioritization meeting, and prioritize HRIs:
   + By effort
   + By impact
   + With the teams responsible for the workloads

1. Collaborate on what really matters most to the business

 **One week after the WAFR:**

1. Begin the improvement plan

1. Consider the following recommendations:
   + **Duration:** 90 or 180 days
   + Identify priority HRIs
   + Develop mitigations for each
   + Try to maximize initiatives to solve multiple HRIs

 **Routine tasks:**

1. Build a cadence for follow-up meetings regarding the improvement plan

1. Review actions to take to improve the workload

1. Consider the following recommendations:
   + Set attendee expectations
   + Send them WA question links
   + Conduct follow up reviews

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
