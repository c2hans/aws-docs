---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/identity-based-policies-for-cloudformation.html
---

# Identity-based policies for CloudFormation
<a name="identity-based-policies-for-cloudformation"></a>

Consider the types of users who need access to AWS CloudFormation, and consider which actions those users need to perform in CloudFormation. You configure user permissions through identity-based policies, which you attach to an AWS Identity and Access Management (IAM) principal, such as a role or user.

When you configure an identity-based policy, the `Effect`, `Action`, and `Resource` elements are required. You can optionally define a `Condition` element too. For more information about these elements, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html).

**This section contains the following topics:**
+ [Best practices for configuring identity-based policies for least-privilege CloudFormation access](best-practices-identity-based-policies.md)
+ [Sample identity-based policies for CloudFormation](sample-id-policies-for-cloudformation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
