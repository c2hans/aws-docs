---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/inspector_limits.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Amazon Inspector Classic service limits
<a name="inspector_limits"></a>

 The following table shows the Amazon Inspector Classic limits for an AWS account.

**Important**
Currently, your assessment targets can consist only of EC2 instances.

The following are Amazon Inspector Classic limits per AWS account per region:

| Resource | Default Limit | Comments |
| --- | --- | --- |
| Instances in running assessments | 500 | The maximum number of EC2 instances that can be included across all running assessments per account per region. |
| Assessment runs | 50000 | The maximum number of assessment runs that you can create per account per region. You can have multiple assessment runs happening at the same time as long as the assessment targets used for these runs do not contain overlapping EC2 instances. |
| Assessment Templates | 500 | The maximum number of assessment templates that you can have at any given time per account per region. |
| Assessment Targets | 50 | The maximum number of assessment targets that you can have at any given time per account per region. |

Unless otherwise noted, these limits can be increased upon request by contacting the [AWS Support Center](https://console.aws.amazon.com/support/home#/).
