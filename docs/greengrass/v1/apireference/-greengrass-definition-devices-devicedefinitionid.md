---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-definition-devices-devicedefinitionid.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/definition/devices/DeviceDefinitionId
<a name="-greengrass-definition-devices-devicedefinitionid"></a>

## GET
<a name="-greengrass-definition-devices-devicedefinitionid-get"></a>

 `GET /greengrass/definition/devices/{{DeviceDefinitionId}}`

Operation ID: [GetDeviceDefinition](getdevicedefinition-get.md)

Retrieves information about a device definition.

Produces: application/json

### Path Parameters
<a name="-greengrass-definition-devices-devicedefinitionid-get-path"></a>

[**DeviceDefinitionId**](parameters-devicedefinitionidparam.md)
The ID of the device definition.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-definition-devices-devicedefinitionid-get-cli"></a>

```
aws greengrass get-device-definition \
  --device-definition-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"DeviceDefinitionId": "string"
}
```

### Responses
<a name="-greengrass-definition-devices-devicedefinitionid-get-responses"></a>

**200** (GetDeviceDefinitionResponse)

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

## DELETE
<a name="-greengrass-definition-devices-devicedefinitionid-delete"></a>

 `DELETE /greengrass/definition/devices/{{DeviceDefinitionId}}`

Operation ID: [DeleteDeviceDefinition](deletedevicedefinition-delete.md)

Deletes a device definition.

Produces: application/json

### Path Parameters
<a name="-greengrass-definition-devices-devicedefinitionid-delete-path"></a>

[**DeviceDefinitionId**](parameters-devicedefinitionidparam.md)
The ID of the device definition.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-definition-devices-devicedefinitionid-delete-cli"></a>

```
aws greengrass delete-device-definition \
  --device-definition-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"DeviceDefinitionId": "string"
}
```

### Responses
<a name="-greengrass-definition-devices-devicedefinitionid-delete-responses"></a>

**200**
Success.
 [ Empty](definitions-empty.md)

```
{
}
```
Empty Schema
Empty
type: object

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

## PUT
<a name="-greengrass-definition-devices-devicedefinitionid-put"></a>

 `PUT /greengrass/definition/devices/{{DeviceDefinitionId}}`

Operation ID: [UpdateDeviceDefinition](updatedevicedefinition-put.md)

Updates the name of a device definition. To update the list of available devices, use `CreateDeviceDefinitionVersion`.

Produces: application/json

### Body Parameters
<a name="-greengrass-definition-devices-devicedefinitionid-put-body"></a>

[**UpdateDefinitionRequestBody**](parameters-updatedefinitionrequestbody.md)

where used: body; required: true

```
{
"Name": "string"
}
```
Name
The name of the definition.
required: true
type: string

### Path Parameters
<a name="-greengrass-definition-devices-devicedefinitionid-put-path"></a>

[**DeviceDefinitionId**](parameters-devicedefinitionidparam.md)
The ID of the device definition.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-definition-devices-devicedefinitionid-put-cli"></a>

```
aws greengrass update-device-definition \
  --device-definition-id <value> \
  [--name <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"DeviceDefinitionId": "string",
"Name": "string"
}
```

### Responses
<a name="-greengrass-definition-devices-devicedefinitionid-put-responses"></a>

**200**
Success.
 [ Empty](definitions-empty.md)

```
{
}
```
Empty Schema
Empty
type: object

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
