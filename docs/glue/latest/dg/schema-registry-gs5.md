---
source_url: https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs5.html
---

# Updating a schema or registry
<a name="schema-registry-gs5"></a>

Once created you can edit your schemas, schema versions, or registry.

## Updating a registry
<a name="schema-registry-gs5a"></a>

You can update a registry using the AWS Glue APIs or the AWS Glue console. The name of an existing registry cannot be edited. You can edit the description for a registry.

**AWS Glue APIs**
To update an existing registry, use the [UpdateRegistry action (Python: update\_registry)](aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-UpdateRegistry) API.

Specify a `RegistryId` structure to indicate the registry that you want to update. Pass a `Description` to change the description for a registry.

```
aws glue update-registry --description updatedDescription --registry-id RegistryArn="arn:aws:glue:us-east-2:901234567890:registry/registryName1"
```

**AWS Glue console**
To update a registry using the AWS Glue console:

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue\).

1. In the navigation pane, under **Data catalog**, choose **Schema registries**.

1. Choose a registry from the the list of registries, by checking its box.

1. In the **Action** menu, choose **Edit registry**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
