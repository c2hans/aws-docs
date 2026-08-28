---
source_url: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-allocation-tags-timeline.html
---

# Understanding dates for cost allocation tags
<a name="cost-allocation-tags-timeline"></a>

**Prerequisites**
To view these dates in the **Cost allocation tags** page of the AWS Billing and Cost Management console, you must have the `ce:ListCostAllocationTags` permission.
For more information about updating your AWS Identity and Access Management (IAM) policies, see [Managing access permissions](migrate-granularaccess-whatis.md#migrate-control-access-billing).

When you use cost allocation tags, you can determine when the tags were last used or last updated with the following metadata fields:
+ **Last updated date** – The last date that the tag key was either activated or deactivated for cost allocation.

  For example, suppose that your tag key `lambda:createdby` changed from inactive to active on July 1, 2023. This means that the **Last updated date** column will show July 1, 2023.
+ **Last used month** – The last month that the tag key was used on an AWS resource.

  For example, suppose that your tag key `lambda:createdby` was last used on April 2023. The **Last used month** column will show April 2023. This means that the tag key hasn't been associated with any resource since that date.
**Notes**
The **Last updated date** column appears empty for newly created tag keys that haven't been activated.
The **Last used month** column shows **-** for tag keys that aren't currently associated with any resource.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awsaccountbilling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
