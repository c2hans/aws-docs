---
source_url: https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs5b.html
---

# Updating a schema
<a name="schema-registry-gs5b"></a>

You can update the description or compatibility setting for a schema.

To update an existing schema, use the [UpdateSchema action (Python: update\_schema)](aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-UpdateSchema) API.

Specify a `SchemaId` structure to indicate the schema that you want to update. One of `VersionNumber` or `Compatibility` has to be provided.

Code example 11:

```
aws glue update-schema --description testDescription --schema-id SchemaName="testSchema1",RegistryName="registryName1" --schema-version-number LatestVersion=true --compatibility NONE
```

```
aws glue update-schema --description testDescription --schema-id SchemaArn="arn:aws:glue:us-east-2:901234567890:schema/registryName1/testSchema1" --schema-version-number LatestVersion=true --compatibility NONE
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
