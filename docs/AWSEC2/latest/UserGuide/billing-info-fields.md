---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html
---

# AMI billing information fields
<a name="billing-info-fields"></a>

The following fields provide billing information associated with an AMI:

Platform details
 The platform details associated with the billing code of the AMI. For example, `Red Hat Enterprise Linux`.

Usage operation
The operation of the Amazon EC2 instance and the billing code that is associated with the AMI. For example, `RunInstances:0010`. **Usage operation** corresponds to the [lineitem/Operation](https://docs.aws.amazon.com/cur/latest/userguide/Lineitem-columns.html#Lineitem-details-O-Operation) column on your AWS Cost and Usage Report (CUR) and in the [AWS Price List API](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html).

You can view these fields on the **Instances** or **AMIs** page in the Amazon EC2 console, or in the response that is returned by the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) or [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) command.

## Sample data: usage operation by platform
<a name="billing-info"></a>

The following table lists some of the platform details and usage operation values that can be displayed on the **Instances** or **AMIs** pages in the Amazon EC2 console, or in the response that is returned by the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) or [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) command.

| Platform details | Usage operation 2 |
| --- | --- |
| Linux/UNIX | RunInstances |
| Red Hat BYOL Linux | RunInstances:00g0 3 |
| Red Hat Enterprise Linux | RunInstances:0010 |
| Red Hat Enterprise Linux with HA | RunInstances:1010 |
| Red Hat Enterprise Linux with SQL Server Standard and HA | RunInstances:1014 |
| Red Hat Enterprise Linux with SQL Server Enterprise and HA | RunInstances:1110 |
| Red Hat Enterprise Linux with SQL Server Standard | RunInstances:0014 |
| Red Hat Enterprise Linux with SQL Server Web | RunInstances:0210 |
| Red Hat Enterprise Linux with SQL Server Enterprise | RunInstances:0110 |
| SQL Server Enterprise | RunInstances:0100 |
| SQL Server Standard | RunInstances:0004 |
| SQL Server Web | RunInstances:0200 |
| SUSE Linux | RunInstances:000g |
| Ubuntu Pro | RunInstances:0g00 |
| Windows | RunInstances:0002 |
| Windows BYOL | RunInstances:0800 |
| Windows with SQL Server Enterprise 1 | RunInstances:0102 |
| Windows with SQL Server Standard 1 | RunInstances:0006 |
| Windows with SQL Server Web 1 | RunInstances:0202 |

1 If two software licenses are associated with an AMI, the **Platform details** field shows both.

2 If you are running Spot Instances, the [lineitem/Operation](https://docs.aws.amazon.com/cur/latest/userguide/Lineitem-columns.html#Lineitem-details-O-Operation) on your AWS Cost and Usage Report might be different from the **Usage operation** value that is listed here. For example, if `[lineitem/Operation](https://docs.aws.amazon.com/cur/latest/userguide/Lineitem-columns.html#Lineitem-details-O-Operation)` displays `RunInstances:0010:SV006`, it means that Amazon EC2 is running Red Hat Enterprise Linux Spot Instance-hour in US East (N. Virginia) in Zone 6.

3 This appears as RunInstances (Linux/UNIX) in your usage reports.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
