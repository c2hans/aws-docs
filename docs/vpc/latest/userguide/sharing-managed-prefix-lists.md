---
source_url: https://docs.aws.amazon.com/vpc/latest/userguide/sharing-managed-prefix-lists.html
---

# Share customer-managed prefix lists
<a name="sharing-managed-prefix-lists"></a>

With AWS Resource Access Manager (AWS RAM), the owner of a customer-managed prefix list can share the prefix list with the following:
+ Specific AWS accounts inside or outside of its organization in AWS Organizations
+ An organizational unit inside its organization in AWS Organizations
+ An entire organization in AWS Organizations

Consumers with whom a prefix list has been shared can view the prefix list and its entries, and they can reference the prefix list in their AWS resources.

For more information about AWS RAM, see the [AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/). For more information quotas, see [Service quotas](https://docs.aws.amazon.com/general/latest/gr/ram.html#limits_ram) in the AWS RAM User Guide.

**Important**
There are no additional charges for sharing prefix lists.

**Topics**
+ [Shared prefix list permissions](sharing-perms.md)
+ [Work with shared prefix lists](work-with-shared-prefixes.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
