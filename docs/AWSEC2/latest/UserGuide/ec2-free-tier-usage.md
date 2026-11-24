---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-free-tier-usage.html
---

# Free Tier usage for Amazon EC2

When you create your AWS account, you can get started with Amazon EC2 for free using the [AWS Free Tier](https://aws.amazon.com/free). For more information, see [Explore AWS services with AWS Free Tier](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html) and [Tracking your AWS Free Tier usage](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html) in the *AWS Billing User Guide*.

The following table describes your Free Tier benefits for Amazon EC2:

| Free Tier benefit | Description |
| --- | --- |
| Instance types marked Free tier eligible | `t3.micro`, `t3.small`, `t4g.micro`, `t4g.small`, `t8i.micro`, `t8i.small`, `t9g.micro`, `t9g.small`, `c7i-flex.large`, `m7i-flex.large` |
| Amazon EBS volume types marked Free tier eligible | `standard`, `st1`, `sc1`, `gp2`, and `gp3` |
| AMIs marked Free tier eligible | Check for AMIs marked Free tier eligible. |
| Usage limit | Receive USD $100 sign-up credit and earn up to $100 in additional credits. |
| Free Tier duration | Your Free Tier lasts for 6 months from the date you created your account, or when your credits are used up, whichever happens first. You can't exceed your Free Tier limits. |

**To list the instance types that are free tier eligible**
Use the [describe-instance-types](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-types.html) command with the `free-tier-eligible` filter.

```bash
aws ec2 describe-instance-types \
    --filters Name=free-tier-eligible,Values=true \
    --query "InstanceTypes[*].[InstanceType]" \
    --output text | sort
```

**To list the AMIs that are free tier eligible**
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command with the `free-tier-eligible` filter.

```bash
aws ec2 describe-images \
    --filters Name=free-tier-eligible,Values=true \
    --query "Images[*].[ImageId]" \
    --output text | sort
```
