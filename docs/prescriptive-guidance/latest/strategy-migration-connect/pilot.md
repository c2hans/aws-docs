---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/pilot.html
---

# Running a pilot
<a name="pilot"></a>

Completing an end-to-end migration project for a small business area allows for fast deployment without the risk of large-scale business disruption. This experience builds confidence in the value proposition (capability, operations, and cost) for a relatively small outlay and can be used to justify a larger release of funds and resources for a full-scale project.

Pilots gather lessons for a full-scale deployment based on how end-users react to the new platform. They help stakeholders answer important questions with real-life data such as the following:
+ Is the training we're providing suitable and sufficient?
+ Do new processes work properly when end-users take real calls?
+ Are users distracted by other applications on their device?
+ Does an architecture or pattern work as expected in the live environment?

## Best practices
<a name="pilot-best-practices"></a>
+ Ideally, pilots should become part of the initial minimum lovable product (MLP) delivery in an early sprint.
+ Participants in a pilot should include technical users, business users, and end-users.
+ Interview stakeholders to get anecdotal feedback on how they use the system, and capture data on average handle time, abandonment rate, and so on, to compare the new system with previous platforms.
+ Make sure that tweaks and amendments that are identified during the pilot are tracked to completion.
+ Define your success criteria and next steps before the pilot begins. Success criteria should be data-driven to enable conclusive scoring to reach a success/fail decision. If stakeholders sign off on the pilot and the delivery plan for any amendments, the predefined next step (for example, to start a full-scale deployment) is initiated.
+ Be positive when your pilot reveals areas that have to be changed or even redesigned. This is a valuable outcome of the pilot and builds the foundation for a successful go-live deployment. Do not aim for a pilot with zero recommendations―this outcome would raise concerns on the validity of the pilot.

## Selecting a pilot group
<a name="select-pilot-group"></a>

The business area you select to pilot the solution would ideally demonstrate all capabilities in scope of the minimum lovable product (MLP) to meet business outcomes. The successful delivery of the MLP becomes the starting point for building out complexity and adding service capabilities. The MLP pilot group should:
+ Represent a non-critical business area (for example, an internal help desk or a notification of change of circumstances).
+ Handle a low volume of calls, so users have the time to learn the new platform and to record their feedback and observations.
+ Be trusted by the project team and stakeholders, to ensure that feedback is fair, accurate, and objective. This helps instill confidence in the outcome of the pilot and helps create a collaborative development environment.
+ Perform the majority of in-scope platform functions. There is little value or relevance in a pilot that uses only 10 percent of the functions that are in scope of the full-scale deployment.
+ Perform a function that might have been excluded from, or not fully integrated in, the old platform because of technical limitations (such as remote work) or licensing. By starting with a group that has no reports or recordings in the old system, you might be able to avoid building legacy integrations or migrating legacy data. However, you should make sure that the pilot continues to represent the full-scale deployment.

In reality, you might have to compromise on some of these factors, depending on the ability and willingness of teams in your organization to take part in a pilot.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
