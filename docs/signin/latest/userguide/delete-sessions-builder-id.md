---
source_url: https://docs.aws.amazon.com/signin/latest/userguide/delete-sessions-builder-id.html
---

# Delete all active sessions for your AWS Builder ID
<a name="delete-sessions-builder-id"></a>

Under **Signed in devices**, you can view all the devices that you're currently signed in to. If you don't recognize a device, as a security best practice, first [change your password](https://docs.aws.amazon.com/signin/latest/userguide/change-password-aws_builder_id.html) and then sign out everywhere. You can sign out from all devices by deleting all your active sessions on the **Security** page for your AWS Builder ID.

**Note**
AWS Builder ID supports 90 day extended sessions for Amazon Q Developer in an IDE. For each new IDE sign in, you can see two session entries. When you sign out of your IDE, you may continue to see IDE sessions listed under **Signed in devices** even though they are no longer valid. These sessions disappear once the 90 days expire.

**To delete all active sessions**

1. Sign in to your AWS Builder ID profile at [https://profile.aws.amazon.com](https://profile.aws.amazon.com).

1. Choose **Security**.

1. On the **Security** page, choose **Delete all active sessions**.

1. In the **Delete all sessions** dialog box, enter *delete all*. By deleting all your sessions, you sign out of all devices that you may have signed into using your AWS Builder ID, including different browsers. Then choose **Delete all sessions**.

**Note**
When using a social login account like Google or Apple, deleting active AWS Builder ID sessions will not log you out of your social login account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Sign-In. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
