---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/awsapps-remove.html
---

# Disabling an AWS managed application
<a name="awsapps-remove"></a>

To prevent users from authenticating to an AWS managed application, you can disable the application in the IAM Identity Center console.

**To disable an AWS managed application**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Applications**.

1. On the **Applications** page, under **AWS managed applications**, choose the application that you want to disable.

1. With the application selected, choose **Actions**, and then choose **Disable**.

1. In the **Disable application** dialog box, choose **Disable**.

1. In the **AWS managed applications** list, the application status appears as **Inactive**.

**Note**
If an AWS managed application is disabled, you can restore users abilty to authenticate to the application by choosing **Actions** and then **Enable**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
