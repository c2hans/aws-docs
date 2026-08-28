---
source_url: https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeSpotDatafeedSubscription_section.html
---

# Use `DescribeSpotDatafeedSubscription` with a CLI
<a name="example_ec2_DescribeSpotDatafeedSubscription_section"></a>

The following code examples show how to use `DescribeSpotDatafeedSubscription`.

------
#### [ CLI ]

**AWS CLI**
**To describe Spot Instance datafeed subscription for an account**
This example command describes the data feed for the account.
Command:

```
aws ec2 describe-spot-datafeed-subscription
```
Output:

```
{
    "SpotDatafeedSubscription": {
        "OwnerId": "123456789012",
        "Prefix": "spotdata",
        "Bucket": "amzn-s3-demo-bucket",
        "State": "Active"
    }
}
```
+  For API details, see [DescribeSpotDatafeedSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-datafeed-subscription.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example describes your Spot instance data feed.**

```
Get-EC2SpotDatafeedSubscription
```
**Output:**

```
Bucket  : amzn-s3-demo-bucket
Fault   :
OwnerId : 123456789012
Prefix  : spotdata
State   : Active
```
+  For API details, see [DescribeSpotDatafeedSubscription](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example describes your Spot instance data feed.**

```
Get-EC2SpotDatafeedSubscription
```
**Output:**

```
Bucket  : amzn-s3-demo-bucket
Fault   :
OwnerId : 123456789012
Prefix  : spotdata
State   : Active
```
+  For API details, see [DescribeSpotDatafeedSubscription](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ec2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
