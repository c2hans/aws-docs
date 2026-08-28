---
source_url: https://docs.aws.amazon.com/glue/latest/dg/rest-api-configuring.html
---

# Configuring a REST API ConnectionType
<a name="rest-api-configuring"></a>

 Before you can use AWS Glue to transfer data from the REST API-based data source, you must meet these requirements:

## Minimum requirements
<a name="rest-api-configuring-min-requirements"></a>

The following are the minimum requirements:
+  You have configured and registered an AWS Glue REST API connection type. See [Connecting to REST APIs](https://docs.aws.amazon.com/glue/latest/dg/rest-api-connections.html).
+  If using OAuth2 Client Credentials, Authorization Code or JWT, configure the client app accordingly.

 If you meet these requirements, you're ready to connect AWS Glue to your REST API-based data source. Typically, no further configurations are needed on the REST API side.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
