---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/deletedevicedefinition-delete.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# DeleteDeviceDefinition
<a name="deletedevicedefinition-delete"></a>

Deletes a device definition.

URI: `DELETE /greengrass/definition/devices/{{DeviceDefinitionId}}`

Produces: application/json

## CLI:
<a name="deletedevicedefinition-delete-cli"></a>

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

## Parameters:
<a name="deletedevicedefinition-delete-params"></a>

[**DeviceDefinitionId**](parameters-devicedefinitionidparam.md)
The ID of the device definition.
where used: path; required: true
type: string

## Responses:
<a name="deletedevicedefinition-delete-resp"></a>

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
