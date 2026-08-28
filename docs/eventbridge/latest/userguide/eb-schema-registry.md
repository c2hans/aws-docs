---
source_url: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema-registry.html
---

# Schema registries in Amazon EventBridge
<a name="eb-schema-registry"></a>

Schema registries are containers for schemas. Schema registries collect and organize schemas so that your schemas are in logical groups. The default schema registries are:
+ **All schemas** – All the schemas from the AWS event, discovered, and custom schema registries.
+ **AWS event schema registry** – The built-in schemas.
+ **Discovered schema registry** – The schemas discovered by Schema discovery.

You can create custom registries to organize the schemas you create or upload.

**Note**
Exporting custom schemas from the EventBridge Schema Registry is not supported.

**To create a custom registry**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. In the navigation pane, choose **Schemas** and then choose **Create registry**.

1. On the **Registry details** page, enter a **Name**.

1. (Optional) Enter a description for your new registry.

1. Choose **Create**.

To [create a custom schema](eb-schema-create.md) in your new registry, select **Create custom schema**. To add a schema to your registry, select that registry when you're creating a new schema.

To create a registry by using the API, use [`CreateRegistry`](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname.html#v1-registries-name-registryname-http-methods). For more information, see [Amazon EventBridge Schema Registry API Reference](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/index.html).

For information about using the EventBridge schema registry through AWS CloudFormation, see [EventSchemas Resource Type Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EventSchemas.html) in CloudFormation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
