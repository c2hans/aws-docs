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
