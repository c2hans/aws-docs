---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-id.html
---

# Viewing your AWS account ID
<a name="console-account-id"></a>

If you are signed into the console, you can view the account ID for your AWS account using the following methods.

## To view your AWS account ID
<a name="console-account-id-section-1"></a>

------
#### [ Console ]

The AWS account ID is displayed when you go to the IAM **Dashboard** in the AWS account section. You can also view your account ID in the navigation bar at the upper right. Choose your user name, and the account ID is displayed above your user name.

![Account information drop-down box with account ID highlighted.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/find-account-id.png)

------
#### [ AWS CLI ]

Use the following command to view your user ID, account ID, and your user ARN:
+ [aws sts get-caller-identity](https://docs.aws.amazon.com/cli/latest/reference/sts/get-caller-identity.html)

------
#### [ API ]

Use the following API to view your user ID, account ID, and your user ARN:
+ [GetCallerIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html)

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
