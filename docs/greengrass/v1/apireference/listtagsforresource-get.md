---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/listtagsforresource-get.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# ListTagsForResource
<a name="listtagsforresource-get"></a>

Lists tags for a Greengrass resource. Valid resources are `Group`, `ConnectorDefinition`, `CoreDefinition`, `DeviceDefinition`, `FunctionDefinition`, `LoggerDefinition`, `ResourceDefinition`, `SubscriptionDefinition`, and `BulkDeployment`.

URI: `GET /tags/{{resource-arn}}`

Produces: application/json

## CLI:
<a name="listtagsforresource-get-cli"></a>

```
aws greengrass list-tags-for-resource  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

## Parameters:
<a name="listtagsforresource-get-params"></a>

[**ResourceArn**](parameters-resourcearnparam.md)
The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.
where used: path; required: true
type: string

## Responses:
<a name="listtagsforresource-get-resp"></a>

**200**
HTTP Status Code 200: OK.
 [ tags](definitions-tags.md)

```
{
  "tags": {
      "keyName0": "value0",
      "keyName1": "value1",
      "keyName2": "value2"
  }
}
```

The resource tags.
type: object
additionalProperties: The key-value pair for the resource tag. Type: string

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
