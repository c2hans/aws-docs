---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_customschematopic.html
---

Amazon Cloud Directory is no longer be open to new customers. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# Custom Schemas
<a name="schemas_customschematopic"></a>

The first step in creating a custom schema is to define exactly what fields you must index. These required fields form your schema's skeleton elements, to which you add your own fields. Map the name and type of each field (such as string, integer, Boolean) to your object's structure. You can define a schema with types and constraints and then apply them to a directory. Once defined, Cloud Directory performs validation for attributes.

For more information, see [Create a Schema](getting_started_create_schema.md).
