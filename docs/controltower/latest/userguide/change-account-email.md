---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/change-account-email.html
---

# Change email address of an enrolled account
<a name="change-account-email"></a>

 To change the email address of an enrolled member account in AWS Control Tower, follow the procedure in this section.

**Note**
 The following procedure doesn't allow you to change the email address of a **management account**, **log archive account**, or **audit account**. For more information about that, see [How do I change the email address associated with my AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/change-email-address/) or contact AWS Support.

**To change the email address of an account that AWS Control Tower creates**

1.  Recover the root user password for the account. You can follow the steps in the article [How do I recover a lost or forgotten AWS password?](https://aws.amazon.com/premiumsupport/knowledge-center/recover-aws-password/)

1.  Sign in to the account with the root user password.

1.  Change the email address as you would for any other AWS account, and wait for the change to reflect in AWS Organizations. You might experience a delay while the email address change finishes updating.

1.  Update the provisioned product in Service Catalog using the email address that previously belonged to the account. The process for updating the provisioned product includes associating the new email address with the provisioned product. This way the email address change takes effect in AWS Control Tower. Use the new email address for updates to subsequently provisioned products.

To change the password or email address of a member account that you created with AWS Organizations, see [Accessing a member account as the root user](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html#orgs_manage_accounts_access-as-root) in the *AWS Organizations User Guide*.

Alternatively, you can update the email address for an Account Factory or other member account from the AWS Organizations console without logging in as the root user. For more information, see [Updating the root user email address for a member account with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_update_primary_email.html) in the *AWS Organizations User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
