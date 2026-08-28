---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-a-devsecops-mechanism/objectives.html
---

# Objectives
<a name="objectives"></a>

Design decisions regarding DevSecOps mechanisms are frequently made in isolation, which can lead to downstream challenges for users of the platform and other stakeholders. In traditional user story development, developers must imagine themselves in the users' shoes to determine which features to implement and how to best implement them within the given time frame.

Developers are accustomed to developing features and user stories in a typical [two-way-door fashion](https://aws.amazon.com/executive-insights/content/how-amazon-defines-and-operationalizes-a-day-1-culture/). However, DevOps and DevSecOps mechanisms have a much higher level of amplification and impact. These mechanisms typically affect the entire organization and often represent one-way doors. When they are designed in a way that doesn't meet the needs of the organization's users, there is resistance to adoption. As a result, the mechanisms might need to be rebuilt eventually, causing significant development delays and a loss of trust.

This guide seeks to alleviate the implementation challenges experienced by users and stakeholders of such mechanisms by providing additional tactical guidance to developers in designing and deploying these features.

After implementing the recommendations in this guide, you should be able to identify correctly the following:
+ How the mechanism can support various code authorship sources
+ How the mechanism can support various environment deployment strategies
+ How to manage the environment deployment state
+ How to implement appropriate security controls in a way that focuses on usability

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
