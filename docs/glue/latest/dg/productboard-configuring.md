---
source_url: https://docs.aws.amazon.com/glue/latest/dg/productboard-configuring.html
---

# Configuring Productboard
<a name="productboard-configuring"></a>

Before you can use AWS Glue to transfer from Productboard, you must meet the following requirements:

## Minimum requirements
<a name="productboard-configuring-min-requirements"></a>
+ You have an Productboard account with email and password. For more information about creating an account, see [Creating a Productboard account](productboard-create-account.md).
+  You must have AWS Account created with the service access to AWS Glue.
+ You have a Productboard account’s authentication details - either JWT Token if one want to use Custom Auth or Client ID and secret if one want to use OAuth2.0.
+ If user wants to use `OAuth2.0`, [Register your application with Productboard](https://app.productboard.com/oauth2/applications/new) and setup the application by following the instructions at, [How to integrate with Productboard via OAuth2 - developer documentation](https://developer.productboard.com/docs/how-to-integrate-with-productboard-via-oauth2-developer-documentation).

If you meet these requirements, you’re ready to connect AWS Glue to your Productboard account. For typical connections, you don't need do anything else in Productboard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
