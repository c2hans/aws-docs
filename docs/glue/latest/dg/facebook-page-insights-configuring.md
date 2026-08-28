---
source_url: https://docs.aws.amazon.com/glue/latest/dg/facebook-page-insights-configuring.html
---

# Configuring Facebook Page Insights
<a name="facebook-page-insights-configuring"></a>

Before you can use AWS Glue to transfer data from Facebook Page Insights, you must meet these requirements:

## Minimum requirements
<a name="facebook-page-insights-configuring-min-requirements"></a>

The following are minimum requirements:
+ Facebook Standard accounts are accessed directly through Facebook.
+ User authentication is needed to generate the access token.
+ The Facebook Page Insights connector implements the User Access Token OAuth flow.
+ The connector uses OAuth2.0 to authenticate our API requests to Facebook Page Insights. This falls under Multi-Factor Authentication (MFA) architecture, which is a superset of 2FA. It is web-based authentication.
+ User needs to grant permissions to access the endpoints. For accessing the user's data, endpoint authorization is handled through permissions and features.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
