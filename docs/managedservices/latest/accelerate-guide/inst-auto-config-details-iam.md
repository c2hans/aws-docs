---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/inst-auto-config-details-iam.html
---

# IAM permissions change details
<a name="inst-auto-config-details-iam"></a>

Each managed instance must have an AWS Identity and Access Management role that includes the following managed policies:
+ arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
+ arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
+ arn:aws:iam::aws:policy/AMSInstanceProfileBasePolicy

 The first two are AWS-managed policies. The AMS-managed policy is:

**AMSInstanceProfileBasePolicy**

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": [
                "secretsmanager:CreateSecret",
                "secretsmanager:UpdateSecret"
            ],
            "Resource": [
                "arn:aws:secretsmanager:*:*:secret:/ams/byoa/*"
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "kms:Encrypt"
            ],
            "Resource": [
                "*"
            ],
            "Effect": "Allow"
        }
    ]
}
```

------

 If your instance already has an attached IAM role, but is missing any of these policies, then AMS adds the missing policies to your IAM role. If your instance doesn't have an IAM role, then AMS attaches the **AMSOSConfigurationCustomerInstanceProfile** IAM role. The **AMSOSConfigurationCustomerInstanceProfile** IAM role has all policies that are required by AMS Accelerate.

**Note**
If the default instance profile limit of 10 is reached, then AMS increases the limit to 20, so that the required instance profiles can be attached.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
