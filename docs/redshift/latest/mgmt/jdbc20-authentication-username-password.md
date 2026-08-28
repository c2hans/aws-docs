---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-authentication-username-password.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Using username and password only
<a name="jdbc20-authentication-username-password"></a>

If the server you are connecting to doesn't use SSL, then you only need to provide your Redshift username and password to authenticate the connection.

**To configure authentication using your Redshift username and password only**

1. Set the `UID` property to your Redshift username for accessing the Amazon Redshift server.

1. Set the PWD property to the password corresponding to your Redshift username.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
