---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/untagresource-delete.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# UntagResource
<a name="untagresource-delete"></a>

Removes tags from a Greengrass resource. Valid resources are `Group`, `ConnectorDefinition`, `CoreDefinition`, `DeviceDefinition`, `FunctionDefinition`, `LoggerDefinition`, `ResourceDefinition`, `SubscriptionDefinition`, and `BulkDeployment`.

URI: `DELETE /tags/{{resource-arn}}`

Produces: application/json

## CLI:
<a name="untagresource-delete-cli"></a>

```
aws greengrass untag-resource  \
  --resource-arn <value> \
  --tag-keys <value> \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"ResourceArn": "string",
"TagKeys": [
  "keyName0"
]
}
```

## Parameters:
<a name="untagresource-delete-params"></a>

[**TagKeys**](parameters-tagkeysparam.md)
An array of tag keys to delete.
where used: query; required: true
type: array of strings

[**ResourceArn**](parameters-resourcearnparam.md)
The Amazon Resource Name (ARN) of the resource to remove the tags from.
where used: path; required: true
type: string

## Responses:
<a name="untagresource-delete-resp"></a>

**204**
HTTP Status Code 204: Successful response.

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
