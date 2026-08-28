---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-creation-templates-custom.html
---

# Create a custom policy for repository creation templates
<a name="repository-creation-templates-custom"></a>

You can use the AWS Management Console to define a policy that will be subsequently associated with an IAM role. This IAM role can then be utilized as a repository creation role when configuring a repository creation template.

------
#### [ AWS Management Console ]

**To use the JSON policy editor to create a custom policy for repository creation templates.**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane on the left, choose **Policies**.

1. Choose **Create policy**.

1. In the **Policy editor** section, choose the **JSON** option.

1. Enter the following policy in the **JSON** field.

------
#### [ JSON ]

****

   ```
   {
           "Version":"2012-10-17",
           "Statement": [
               {
                   "Effect": "Allow",
                   "Action": [
                       "ecr:CreateRepository",
                       "ecr:ReplicateImage",
                       "ecr:TagResource"
                   ],
                   "Resource": "*"
               },
               {
                   "Effect": "Allow",
                   "Action": [
                       "kms:CreateGrant",
                       "kms:RetireGrant",
                       "kms:DescribeKey"
                   ],
                   "Resource": "*"
               }
            ]
   }
   ```

------

1. Resolve any security warnings, errors, or general warnings generated during [ policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html), and then choose **Next**.

1. When you are finished adding permissions to the policy, choose **Next**.

1. On the **Review and create** page, type a **Policy Name** and a **Description** (optional) for the policy that you are creating. Review **Permissions defined in this policy** to see the permissions that are granted by your policy.

1. Choose **Create policy** to save your new policy.

1. Create a role to assign this policy for the creation template, see [Create an IAM role for repository creation templates](repository-creation-templates-create-iam.md).

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
