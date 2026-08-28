---
source_url: https://docs.aws.amazon.com/workmail/latest/adminguide/mail_vs_folder.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

# About mailbox and folder permissions
<a name="mail_vs_folder"></a>

Mailbox permissions apply to all folders within a mailbox. These permissions can only be enabled by the AWS account holder or an IAM user authorized to call the Amazon WorkMail management API. To set and change permissions for mailboxes, or for groups as a whole, use the AWS Management Console or the Amazon WorkMail API. You can manage up to 100 mailbox and group permissions from the console. To manage permissions for more users and groups, use the Amazon WorkMail API.

Folder permissions apply only to a single folder. End users can set folder permissions by using an email client, or by using the Amazon WorkMail web application. For more information about using the Amazon WorkMail web application to share folders, see [Sharing folders and folder permissions](https://docs.aws.amazon.com/workmail/latest/userguide/share-folders.html) in the *Amazon WorkMail User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
