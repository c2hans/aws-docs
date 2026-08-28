---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-a-devsecops-mechanism/reusable-artifacts.html
---

# Reusable artifacts
<a name="reusable-artifacts"></a>

Reusable artifacts allow your organization to save time and improve the [Don't repeat yourself (DRY)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (Wikipedia) level in the organization. Using reusable artifacts includes the following common challenges:
+ Not using Git release versioning
  + This issue can cause outages and project delays when an application team references the source repository, and the source repository has a breaking change.
+ Writing code that is of inferior quality
  + Consider a task to deliver a central AWS security group repository. Now, imagine assigning that task to a developer who isn't competent with modern infrastructure language features and design. Rather than using dynamic variables, stored parameters, and imbued calculations, they deliver an artifact that requires 50 input variables to implement and is prone to breaking. Now every application in your organization that must use an AWS security group must also add 50 input variables to their source code to use the dependent artifact. Writing code that is of inferior quality amplifies that code's impact.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
