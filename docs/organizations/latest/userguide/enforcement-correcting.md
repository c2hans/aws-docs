---
source_url: https://docs.aws.amazon.com/organizations/latest/userguide/enforcement-correcting.html
---

# Correcting non-compliant tags in resources
<a name="enforcement-correcting"></a>

After finding non-compliant tags, make corrections using any of the following methods. You must be signed in to the account that has the resource with non-compliant tags:
+ Use the console or tagging API operations of the AWS service that created the non-compliant resources.
+ Use the AWS Resource Groups [TagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html) and [UntagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_UntagResources.html) operations to add tags that are compliant with the effective policy or to remove non-compliant tags.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
