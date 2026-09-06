---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-17.html
---

# ACCT.17 Restrict AWS API calls to used Regions only
<a name="acct-17"></a>

Create an [IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) that denies API calls in AWS Regions you do not use. This helps prevent attackers from creating resources, such as compute instances for cryptocurrency mining, in Regions where you have no monitoring or visibility. This control extends [ACCT.09 Delete unused VPCs, subnets, and security groups](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-09.html) by restricting all resource creation in unused Regions, not only VPC-related resources.

Use the `aws:RequestedRegion` condition key in a deny policy. The policy must exclude global services such as [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM), [AWS Security Token Service (AWS STS)](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html), [Amazon CloudFront](https://aws.amazon.com/cloudfront/), and [Amazon Route 53](https://aws.amazon.com/route53/) because these services do not operate in a specific Region. Use `NotAction` to list the global services that are excluded from the Region restriction.

**To restrict API calls to specific Regions**

Create an IAM policy using the following template. Replace the Regions in the `aws:RequestedRegion` condition with the Regions you use:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyAllOutsideAllowedRegions",
            "Effect": "Deny",
            "NotAction": [
                "iam:*",
                "sts:*",
                "cloudfront:*",
                "route53:*",
                "route53domains:*",
                "support:*",
                "trustedadvisor:*",
                "health:*",
                "organizations:*",
                "budgets:*",
                "ce:*",
                "cur:*",
                "aws-portal:*",
                "pricing:*",
                "waf:*",
                "wafv2:*",
                "shield:*",
                "globalaccelerator:*",
                "networkmanager:*"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:RequestedRegion": [
                        "us-east-1",
                        "us-west-2"
                    ]
                }
            }
        }
    ]
}
```

Attach the policy to each IAM role and IAM user in your account, or attach it as a permissions boundary. For more information about permissions boundaries, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the [IAM documentation](https://docs.aws.amazon.com/iam/).

For more information about the `aws:RequestedRegion` condition key, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the IAM documentation. For a complete example, see [AWS: Denies access to AWS based on the requested Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-requested-region.html) in the IAM documentation.

**Note**
There is no additional charge for IAM policies. If you later adopt [AWS Organizations](https://aws.amazon.com/organizations/), you can implement this same restriction as a [Service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) for centralized enforcement across accounts.
