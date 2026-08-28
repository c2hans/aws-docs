---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-auth-rules-database-emqx-broker-windows.html
---

# Configure authorization using the built-in database with Windows
<a name="add-auth-rules-database-emqx-broker-windows"></a>

This section covers configuring authorization rules using the built-in database for Windows deployments.

**To add basic authorization rules**

1. Verify that the EMQX broker is deployed and running.

1. Run the AWS IoT SiteWise EMQX CLI tool:

   ```
   C:\greengrass\v2\bin\swe-emqx-cli.ps1 acl init
   ```

   The tool automatically creates and applies ACL rules allowing connections from localhost (127.0.0.1) to the broker. It allows access to all topics. This includes the IoT SiteWise OPC UA collector and IoT SiteWise publisher.

1. Proceed to [Update the EMQX deployment configuration for authorization](update-emqx-broker-authorization.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
