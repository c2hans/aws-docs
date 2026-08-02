---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-definitioninformation.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# DefinitionInformation
<a name="definitions-definitioninformation"></a>

```
{
"Name": "string",
"Id": "string",
"Arn": "string",
"tags": {
  "additionalProperty0": "string",
  "additionalProperty1": "string",
  "additionalProperty2": "string"
},
"LastUpdatedTimestamp": "string",
"CreationTimestamp": "string",
"LatestVersion": "string",
"LatestVersionArn": "string"
}
```

DefinitionInformation
Information about a definition.
type: object

Name
The name of the definition.
type: string

Id
The ID of the definition.
type: string

Arn
The ARN of the definition.
type: string

tags
The resource tags.
type: object
additionalProperties: The key-value pair for the resource tag. Type: string

LastUpdatedTimestamp
The time, in milliseconds since the epoch, when the definition was last updated.
type: string

CreationTimestamp
The time, in milliseconds since the epoch, when the definition was created.
type: string

LatestVersion
The ID of the latest version associated with the definition.
type: string

LatestVersionArn
The ARN of the latest version associated with the definition.
type: string
