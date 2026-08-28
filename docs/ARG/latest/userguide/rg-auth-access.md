---
source_url: https://docs.aws.amazon.com/ARG/latest/userguide/rg-auth-access.html
---

# Learn more about AWS Resource Groups authorization and access control
<a name="rg-auth-access"></a>

Resource Groups supports the following.
+ **Action-based policies.** For example, you can create a policy that allows users to perform [**ListGroups**](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroups.html) operations, but no others.
+ **Resource-level permissions.** Resource Groups supports using [ARNs](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) to specify individual resources in the policy.
+ **Authorization based on tags.** Resource Groups supports using resource tags in the condition of a policy. For example, you can create a policy that allows Resource Groups users full access to a group that you have tagged.
+ **Temporary credentials.** Users can assume a role with a policy that allows AWS Resource Groups operations.

Resource Groups doesn't support resource-based policies.

For more information about how Resource Groups and Tag Editor integrate with AWS Identity and Access Management (IAM), see the following topics in the *AWS Identity and Access Management User Guide*.
+ [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html#management_svcs)
+ [Actions, resources, and condition keys for AWS Resource Groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsresourcegroups.html)
+ [Controlling access using policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_controlling.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
