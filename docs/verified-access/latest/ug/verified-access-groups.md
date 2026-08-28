---
source_url: https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-groups.html
---

# Verified Access groups
<a name="verified-access-groups"></a>

A Verified Access group consists of Verified Access endpoints and a Verified Access policy that applies to all endpoints in the group. By grouping together endpoints that have common security requirements, you can define a single group policy that meets the minimum security requirements of multiple endpoints. Therefore, you don't need create and maintain a policy for each endpoint.

For example, you can group all sales applications together and set a group-wide access policy. You can then use this policy to define a common set of minimum security requirements for all sales applications. This approach helps to simplify policy administration.

When you create a group, you are required to associate the group with a Verified Access instance. During the process of creating an endpoint, you will associate the endpoint with a group.

Another feature of Verified Access groups is the ability to share them with other AWS accounts using AWS RAM. This allows you to create and manage groups centrally in one account, then share them with multiple accounts.

**Topics**
+ [Create and manage a Verified Access group](create-verified-access-group.md)
+ [Modify a Verified Access group policy](modify-verified-access-group-policy.md)
+ [Share a group with another account](sharing-groups.md)
+ [Delete a Verified Access group](delete-verified-access-group.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Verified Access. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verified-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
