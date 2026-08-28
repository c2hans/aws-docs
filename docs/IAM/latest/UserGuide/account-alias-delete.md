---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/account-alias-delete.html
---

# Deleting an account alias
<a name="account-alias-delete"></a>

To perform the following steps, you must have at least the following IAM permissions:
+ `iam:ListAccountAliases`
+ `iam:DeleteAccountAlias`

## To delete an account alias
<a name="console-account-alias-section-2"></a>

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Dashboard**.

1. In the **AWS Account** section, next to **Account Alias**, choose **Delete**.

------
#### [ AWS CLI ]

To delete an AWS account ID alias, run the following command:
+ `[aws iam delete-account-alias](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-account-alias.html)`

To confirm that the account alias is deleted, attempt to display your AWS account ID alias, by running the following command:
+ `[aws iam list-account-aliases](https://docs.aws.amazon.com/cli/latest/reference/iam/list-account-aliases.html)`

------
#### [ API ]

To delete an AWS account ID alias, call the following operation:
+ `[DeleteAccountAlias](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteAccountAlias.html)`

To confirm that the account alias is deleted attempt to display your AWS account ID alias, by calling the following operation:
+ `[ListAccountAliases](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccountAliases.html)`

------

**Note**
After deleting your account alias, the only sign-in URL for your account is based off your account ID. Any attempts to connect to the alias URL will fail and are not redirected.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
