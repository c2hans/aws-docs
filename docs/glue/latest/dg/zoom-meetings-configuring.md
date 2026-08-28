---
source_url: https://docs.aws.amazon.com/glue/latest/dg/zoom-meetings-configuring.html
---

# Configuring Zoom Meetings
<a name="zoom-meetings-configuring"></a>

Before you can use AWS Glue to transfer data from Zoom Meetings, you must meet these requirements:

## Minimum requirements
<a name="zoom-meetings-configuring-min-requirements"></a>

The following are minimum requirements:
+ You have a Zoom Meetings account.
+ Your Zoom account is enabled for API access.
+ You have created an OAuth2 app in your Zoom Meetings account. This integration provides the credentials that AWS Glue uses to access your data securely when it makes authenticated calls to your account. For more information, see [Configuring the Zoom Meetings client app](zoom-meetings-configuring-client-app.md).

If you meet these requirements, you’re ready to connect AWS Glue to your Zoom Meetings account. For typical connections, you don't need do anything else in Zoom Meetings.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
