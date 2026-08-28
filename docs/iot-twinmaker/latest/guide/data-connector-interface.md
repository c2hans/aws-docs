---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/guide/data-connector-interface.html
---

# AWS IoT TwinMaker data connectors
<a name="data-connector-interface"></a>

AWS IoT TwinMaker uses a connector-based architecture so that you can connect data from your own data store to AWS IoT TwinMaker. This means you don't need to migrate data prior to using AWS IoT TwinMaker. Currently, AWS IoT TwinMaker supports first-party connectors for AWS IoT SiteWise. If you store modeling and property data in AWS IoT SiteWise, then you don’t need to implement your own connectors. If you store your modeling or property data in other data stores, such as Timestream, DynamoDB, or Snowflake, then you must implement AWS Lambda connectors with the AWS IoT TwinMaker data connector interface so that AWS IoT TwinMaker can invoke your connector when necessary.

**Topics**
+ [AWS IoT TwinMaker data connectors](data-connector-interfaces.md)
+ [AWS IoT TwinMaker Athena tabular data connector](athena-tabular-data-connector.md)
+ [Developing AWS IoT TwinMaker time-series data connectors](time-series-data-connectors.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
