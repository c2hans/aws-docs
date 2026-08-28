---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/update-multiple-accounts.html
---

# Update multiple accounts in the same OU
<a name="update-multiple-accounts"></a>

Repeat these steps for each OU in your AWS Control Tower organization, if you need to update all of your accounts and OUs.

**To update multiple accounts in one OU, with one action**

1. Sign in to the AWS Control Tower console at [https://console.aws.amazon.com/controltower](https://console.aws.amazon.com/controltower).

1. In the left-pane navigation menu, choose **Organization **.

1. On the **Organization** page, choose any OU to view the **OU details** page.

1. If AWSControlTowerBaseline is enabled on the OU, select **Re-Register OU** under **Actions**. If AWSControlTowerBaseline is not enabled on the OU, select **Reset AWS Config baseline** under **Actions** to reset enabled baseline and select enabled controls and **Reset control** under "Enabled controls" section to reset enabled controls.

Alternatively, you can select any account that shows a status of **Update available** and then choose **Update account**, for as many accounts as needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
