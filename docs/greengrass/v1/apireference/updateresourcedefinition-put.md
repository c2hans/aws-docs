---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/updateresourcedefinition-put.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# UpdateResourceDefinition
<a name="updateresourcedefinition-put"></a>

Updates the name of a resource definition. To update the list of available resources, use `CreateResourceDefinitionVersion`.

URI: `PUT /greengrass/definition/resources/{{ResourceDefinitionId}}`

Produces: application/json

## CLI:
<a name="updateresourcedefinition-put-cli"></a>

```
aws greengrass update-resource-definition \
  --resource-definition-id <value> \
  [--name <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"ResourceDefinitionId": "string",
"Name": "string"
}
```

## Parameters:
<a name="updateresourcedefinition-put-params"></a>

[**ResourceDefinitionId**](parameters-resourcedefinitionidparam.md)
The ID of the resource definition.
where used: path; required: true
type: string

[**UpdateDefinitionRequestBody**](parameters-updatedefinitionrequestbody.md)

where used: body; required: true

```
{
"Name": "string"
}
```
schema:
Name
The name of the definition.
required: true
type: string

## Responses:
<a name="updateresourcedefinition-put-resp"></a>

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
