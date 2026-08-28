---
source_url: https://docs.aws.amazon.com/wavelength/latest/developerguide/wavelength-zones-describe.html
---

# Find your AWS Wavelength Zones
<a name="wavelength-zones-describe"></a>

The number and mapping of Wavelength Zones per Region might vary between AWS accounts. The following procedures demonstrate how to find the Wavelength Zones that are available to your account.

**To find your Wavelength Zones using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the navigation bar, choose the **Regions** selector and then choose the Region.

1. On the navigation pane, choose **EC2 Dashboard**.

1. In the upper-right corner of the page, choose **Account attributes**, **Zones**.

**To find your Wavelength Zones using the AWS CLI**
+ Use the [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) command as follows to describe the Wavelength Zones within the specified Region that are enabled for your account.

  ```
  aws ec2 describe-availability-zones --region {{region-name}}
  ```
+ Use the [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) command as follows to describe the Wavelength Zones regardless of the opt-in status.

  ```
  aws ec2 describe-availability-zones --all-availability-zones
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wavelength. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wavelength` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
