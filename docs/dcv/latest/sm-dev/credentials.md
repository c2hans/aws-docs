---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-dev/credentials.html
---

# Step 2: Register your client API
<a name="credentials"></a>

API requests use an access token to verify your credentials. These credentials are based on a client ID and client password that is generated when your client is registered with the Broker.

To access this token, you need to register with the Broker. Use [register-api-client](https://docs.aws.amazon.com/dcv/latest/sm-admin/register-api-client.html) to register client API.

If you don't have a client ID and client password for your client, you must request them from your Broker administrator.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
