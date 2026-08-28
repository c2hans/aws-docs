---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/instance-choice.html
---

# Choosing the instance type
<a name="instance-choice"></a>

F5 supports multiple instance types and choosing which one to use can be a complex decision. For most migrations, `c5n.2xl` and `c5n.4xl` will be the most common instance choices because they offer a mix of network performance, CPU density, interface density, and the number of IPs that can be supported on the instance. The following diagram provides examples of which instances to choose, based on the F5 products you are using.

![Process flow for choosing which instance type to use.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/images/guide-img/migration-f5-big-ip/images/F5-instance-choice.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
