---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/add-custom-resource-type-cli.html
---

# Record Configuration Items with AWS Config for Third-Party Resources using the AWS CLI
<a name="add-custom-resource-type-cli"></a>

Record a configuration item for a third-party resource or a custom resource type using the following procedure:

Ensure you register the resource type `MyCustomNamespace::Testing::WordPress` with its matching schema.

1. Open a command prompt or a terminal window.

1. Enter the following command:

   ```
   aws configservice put-resource-config --resource-type MyCustomNamespace::Testing::WordPress --resource-id resource-001 --schema-version-id 00000001 --configuration  '{
     "Id": "resource-001",
     "Name": "My example custom resource.",
     "PublicAccess": false
   }'
   ```

**Note**
As defined in the type schema, `writeOnlyProperties` will be removed from the configuration prior to being recorded by AWS Config. This means that these values will not be present when the configuration is obtained from read APIs. For more information on `writeOnlyProperties`, see [Resource type schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
