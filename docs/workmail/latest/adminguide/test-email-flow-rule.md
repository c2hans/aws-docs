---
source_url: https://docs.aws.amazon.com/workmail/latest/adminguide/test-email-flow-rule.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

# Testing an email flow rule
<a name="test-email-flow-rule"></a>

To check your current rule configuration, you can test how the configuration behaves against specific email addresses.

**To test an email flow rule**

1. Open the Amazon WorkMail console at [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/).

   If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Regions and endpoints](http://docs.aws.amazon.com/general/latest/gr/index.html?rande.html) in the *Amazon Web Services General Reference*.

1. In the navigation pane, choose **Organizations**, and then choose the name of your organization.

1. In the navigation pane, choose **Organization settings**, **Inbound/Outbound rules**.

1. Next to **Test configuration**, enter the full email addresses of both the sender and recipient that you want to test.

1. Choose **Test**. The action to be taken for the provided email address is displayed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
