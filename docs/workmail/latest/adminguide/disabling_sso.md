---
source_url: https://docs.aws.amazon.com/workmail/latest/adminguide/disabling_sso.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

# Disabling IAM Identity Center
<a name="disabling_sso"></a>

You can disable IAM Identity Center from the Amazon WorkMail console. Once disabled, you cannot access the mailbox using the IAM Identity Center credentials or personal access tokens. It is recommended to reset all user passwords and the Amazon WorkMail users will revert to using the Amazon WorkMail Directory credentials.

**Note**
Check the following:
After disabling IAM Identity Center, your Amazon WorkMail and IAM Identity Center users and groups will remain unchanged.
The existing user associations will continue to exist.
Your authentication will revert to being managed by Amazon WorkMail directory, instead of IAM Identity Center.

**To disable IAM Identity Center, follow these steps.**

1. Under the **Identity Center Settings** page, choose **Disable**.

   The **Disable IAM Identity Center** page appears.

1. Choose **Confirm**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
