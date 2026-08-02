---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/getcoredefinition-get.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetCoreDefinition
<a name="getcoredefinition-get"></a>

Retrieves information about a core definition version.

URI: `GET /greengrass/definition/cores/{{CoreDefinitionId}}`

Produces: application/json

## CLI:
<a name="getcoredefinition-get-cli"></a>

```
aws greengrass get-core-definition \
  --core-definition-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"CoreDefinitionId": "string"
}
```

## Parameters:
<a name="getcoredefinition-get-params"></a>

[**CoreDefinitionId**](parameters-coredefinitionidparam.md)
The ID of the core definition.
where used: path; required: true
type: string

## Responses:
<a name="getcoredefinition-get-resp"></a>

**200** (GetCoreDefinitionResponse)

 [ DefinitionInformation](definitions-definitioninformation.md)

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

**400**
Invalid request.
 [ GeneralError](definitions-generalerror.md)

```
{
"Message": "string",
"ErrorDetails": [
  {
    "DetailedErrorCode": "string",
    "DetailedErrorMessage": "string"
  }
]
}
```
GeneralError
General error information.
type: object
required: ["Message"]
Message
A message that contains information about the error.
type: string
ErrorDetails
A list of error details.
type: array
items: [ErrorDetail](definitions-errordetail.md)
ErrorDetail
Details about the error.
type: object
DetailedErrorCode
A detailed error code.
type: string
DetailedErrorMessage
A detailed error message.
type: string
