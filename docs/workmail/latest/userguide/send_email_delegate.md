---
source_url: https://docs.aws.amazon.com/workmail/latest/userguide/send_email_delegate.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

# Sending email on behalf of someone else
<a name="send_email_delegate"></a>

You can send email on another user's behalf if they've made you their delegate.

**To send email on behalf of someone else**

1. In the Amazon WorkMail web application, on the shortcut bar, choose the mail icon.

1. On the menu bar, choose **\+ New item**, **New email**.
**Tip**
You can also choose the plus sign (**\+**) on the tab bar.

1. Under the **To** field, choose **From**.

1. For **From**, enter the name of the person for whom you are sending email.

1. In the contents pane, type your message and choose **Send**.

The mailbox owner appears in the **From:** header, and you appear in the **Sender:** header.

**Note**
If you have not been granted delegation permissions for the person you specified in the **From** field, you receive an email message in your own inbox indicating that you don't have the required permissions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
