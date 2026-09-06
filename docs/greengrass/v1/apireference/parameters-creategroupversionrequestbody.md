---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/parameters-creategroupversionrequestbody.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateGroupVersionRequestBody
<a name="parameters-creategroupversionrequestbody"></a>

```
{
"CoreDefinitionVersionArn": "string",
"DeviceDefinitionVersionArn": "string",
"FunctionDefinitionVersionArn": "string",
"SubscriptionDefinitionVersionArn": "string",
"LoggerDefinitionVersionArn": "string",
"ResourceDefinitionVersionArn": "string",
"ConnectorDefinitionVersionArn": "string"
}
```

CreateGroupVersionRequestBody
in: body
required: true
schema: [GroupVersion](definitions-groupversion.md)

GroupVersion
Information about a group version.
type: object

CoreDefinitionVersionArn
The ARN of the core definition version for this group.
type: string

DeviceDefinitionVersionArn
The ARN of the client device definition version for this group.
type: string

FunctionDefinitionVersionArn
The ARN of the function definition version for this group.
type: string

SubscriptionDefinitionVersionArn
The ARN of the subscription definition version for this group.
type: string

LoggerDefinitionVersionArn
The ARN of the logger definition version for this group.
type: string

ResourceDefinitionVersionArn
The ARN of the resource definition version for this group.
type: string

ConnectorDefinitionVersionArn
The ARN of the connector definition version for this group.
type: string
