---
source_url: https://docs.aws.amazon.com/glue/latest/dg/mailchimp-configuring.html
---

# Configuring Mailchimp
<a name="mailchimp-configuring"></a>

Before you can use AWS Glue to transfer from Mailchimp, you must meet the following requirements:

## Minimum requirements
<a name="mailchimp-configuring-min-requirements"></a>
+ You have an Mailchimp account with email and password. For more information about creating an account, see [Creating a Mailchimp account](mailchimp-create-account.md).
+  You must have AWS Account created with the service access to AWS Glue.
+ Ensure you have created one of the following resources. These resources provide credentials that AWS Glue uses to securely access your data when making authenticated calls to your account:
  + A Developer App that supports OAuth 2.0 authentication. For more information about creating a Developer App, see [Creating a Mailchimp account](mailchimp-create-account.md).

If you meet these requirements, you’re ready to connect AWS Glue to your Mailchimp account. For typical connections, you don't need do anything else in Mailchimp.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
