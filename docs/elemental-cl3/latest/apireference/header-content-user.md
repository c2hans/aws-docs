---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/header-content-user.html
---

# Header Content for User Authentication
<a name="header-content-user"></a>

If your cluster deployment is configured for user authentication (users must log into Conductor Live), then the header must also include:
+ X-Auth-User header.
+ X-Auth-Expires header (optional).
+ X-Auth-Key header includes the API key of the individual user.

  For more information, see [Using the API with User Authentication Enabled](using-api-with-user-authentication-enabled.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
