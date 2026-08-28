---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/updatefunctiondefinition-put.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# UpdateFunctionDefinition
<a name="updatefunctiondefinition-put"></a>

Updates the name of a function definition. To update the list of available functions, use `CreateFunctionDefinitionVersion`.

URI: `PUT /greengrass/definition/functions/{{FunctionDefinitionId}}`

Produces: application/json

## CLI:
<a name="updatefunctiondefinition-put-cli"></a>

```
aws greengrass update-function-definition \
  --function-definition-id <value> \
  [--name <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"FunctionDefinitionId": "string",
"Name": "string"
}
```

## Parameters:
<a name="updatefunctiondefinition-put-params"></a>

[**FunctionDefinitionId**](parameters-functiondefinitionidparam.md)
The ID of the function definition.
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
<a name="updatefunctiondefinition-put-resp"></a>

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
