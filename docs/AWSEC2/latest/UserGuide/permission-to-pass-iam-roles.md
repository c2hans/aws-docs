---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permission-to-pass-iam-roles.html
---

# Grant permissions to attach an IAM role to an instance
<a name="permission-to-pass-iam-roles"></a>

The identities in your AWS account, such as IAM users, must have specific permissions to launch an Amazon EC2 instance with an IAM role, attach an IAM role to an instance, replace the IAM role for an instance, or detach an IAM role from an instance. You must grant permission to use the following API actions as required:
+ `iam:PassRole`
+ `ec2:AssociateIamInstanceProfile`
+ `ec2:DisassociateIamInstanceProfile`
+ `ec2:ReplaceIamInstanceProfileAssociation`

**Note**
If you specify the resource for `iam:PassRole` as `*`, this would grant access to pass any of your IAM roles to an instance. To follow the best practice of [least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege), specify the ARNs of specific IAM roles with `iam:PassRole`, as shown in the example policy below.

**Example policy for programmatic access**
The following IAM policy grants permissions to launch instances with an IAM role, attach an IAM role to an instance, or replace the IAM role for an instance using the AWS CLI or the Amazon EC2 API.

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
         "ec2:RunInstances",
         "ec2:AssociateIamInstanceProfile",
         "ec2:DisassociateIamInstanceProfile",
         "ec2:ReplaceIamInstanceProfileAssociation"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::{{123456789012}}:role/{{DevTeam}}*"
    }
  ]
}
```

------

**Additional requirement for console access**
To grant permissions to complete the same tasks using the Amazon EC2 console, you must also include the `iam:ListInstanceProfiles` API action.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
