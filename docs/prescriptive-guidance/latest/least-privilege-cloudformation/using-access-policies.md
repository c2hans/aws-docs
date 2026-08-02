---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/using-access-policies.html
---

# Using access policies to grant permissions in AWS
<a name="using-access-policies"></a>

You manage access in AWS by creating *identity-based policies* and attaching them to AWS Identity and Access Management (IAM) principals, such as roles or users, and by creating *resource-based policies* and attaching them to AWS resources. AWS evaluates these policies whenever a request is made. Permissions in the policies determine whether the request is allowed or denied.

To understand how to configure least-privilege access in policies, you need to understand the different types of policies, the elements and structure of a policy, and how policies are evaluated. This guide only focuses on identity-based policies and resource-based policies. However, AWS provides other types of policies, such as *service control policies (SCPs)*, *permissions boundaries*, and* session policies*. Each type of policy plays a role in implementing least-privilege permissions in your AWS accounts. For more information, see [Policies and permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) and [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the IAM documentation.
