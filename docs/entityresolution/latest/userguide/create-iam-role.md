---
source_url: https://docs.aws.amazon.com/entityresolution/latest/userguide/create-iam-role.html
---

# Creating an IAM role for a console user
<a name="create-iam-role"></a>

Complete the following procedure if you are using the AWS Entity Resolution console.

**To create an IAM role**

1. Sign in to the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/)) with your administrator account.

1. Under **Access management**, choose **Roles**.

   You can use **Roles** to create short-term credentials, which is recommended for increased security. You can also choose **Users** to create long-term credentials.

1. Choose **Create role**.

1. In the **Create role** wizard, for **Trusted entity type**, choose **AWS account**.

1. Keep the option **This account** selected, and then choose **Next**.

1. For **Add permissions**, choose **Create Policy**.

   A new tab opens.

   1. Select the **JSON** tab, and then add policies depending on the abilities granted to the console user. AWS Entity Resolution offers the following managed policies based on common use cases:
      + [AWS managed policy: AWSEntityResolutionConsoleFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-fullaccess)
      + [AWS managed policy: AWSEntityResolutionConsoleReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-readonly)

   1. Choose **Next: Tags**, add tags (optional), and then choose **Next: Review**.

   1. For **Review policy**, enter a **Name** and **Description**, and review the **Summary**.

   1. Choose **Create policy**.

      You have created a policy for a collaboration member.

   1. Go back to your original tab and under **Add permissions**, enter the name of the policy that you just created. (You might need to reload the page.)

   1. Select the check box next to the name of the policy that you created, and then choose **Next**.

1. For **Name, review, and create**, enter the **Role name** and **Description**.

   1. Review **Select trusted entities**, enter the AWS account for the person or persons who will assume the role (if necessary).

   1. Review the permissions in **Add permissions**, and edit if necessary.

   1. Review the **Tags**, and add tags if necessary.

   1. Choose **Create role**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
