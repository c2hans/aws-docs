---
source_url: https://docs.aws.amazon.com/glue/latest/dg/instagram-ads-configuring.html
---

# Configuring Instagram Ads
<a name="instagram-ads-configuring"></a>

Before you can use AWS Glue to transfer data from Instagram Ads, you must meet these requirements:

## Minimum requirements
<a name="instagram-ads-configuring-min-requirements"></a>

The following are minimum requirements:
+ Instagram Standard accounts are accessed indirectly through Facebook.
+ User authentication is needed to generate the access token.
+ The Instagram Ads SDK connector will be implementing the *User Access Token OAuth* flow.
+ We are using OAuth2.0 to authenticate our API requests to Instagram Ads. This web-based authentication falls under the Multi-Factor Authentication (MFA) architecture, which is a superset of 2FA.
+ The user needs to grant permissions to access the end points. For accessing the user's data, endpoint authorization is handled through [permissions](https://developers.facebook.com/docs/permissions) and [features](https://developers.facebook.com/docs/features-reference).

## Getting OAuth 2.0 credentials
<a name="instagram-ads-configuring-creating-instagram-ads-oauth2-credentials"></a>

To obtain API credentials so that you can make authenticated calls to your instance, see [Graph API](https://developers.facebook.com/docs/graph-api/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
