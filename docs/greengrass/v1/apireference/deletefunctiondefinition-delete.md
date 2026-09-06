---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/deletefunctiondefinition-delete.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# DeleteFunctionDefinition
<a name="deletefunctiondefinition-delete"></a>

Deletes a Lambda function definition.

URI: `DELETE /greengrass/definition/functions/{{FunctionDefinitionId}}`

Produces: application/json

## CLI:
<a name="deletefunctiondefinition-delete-cli"></a>

```
aws greengrass delete-function-definition \
  --function-definition-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"FunctionDefinitionId": "string"
}
```

## Parameters:
<a name="deletefunctiondefinition-delete-params"></a>

[**FunctionDefinitionId**](parameters-functiondefinitionidparam.md)
The ID of the function definition.
where used: path; required: true
type: string

## Responses:
<a name="deletefunctiondefinition-delete-resp"></a>

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
