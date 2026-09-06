---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-tags-resource-arn.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /tags/resource-arn
<a name="-tags-resource-arn"></a>

## GET
<a name="-tags-resource-arn-get"></a>

 `GET /tags/{{resource-arn}}`

Operation ID: [ListTagsForResource](listtagsforresource-get.md)

Lists tags for a Greengrass resource. Valid resources are `Group`, `ConnectorDefinition`, `CoreDefinition`, `DeviceDefinition`, `FunctionDefinition`, `LoggerDefinition`, `ResourceDefinition`, `SubscriptionDefinition`, and `BulkDeployment`.

Produces: application/json

### CLI
<a name="-tags-resource-arn-get-cli"></a>

```
aws greengrass list-tags-for-resource  \
  --resource-arn <value> \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"ResourceArn": "string"
}
```

### Parameters:
<a name="-tags-resource-arn-get-params"></a>

 [**ResourceArn**](parameters-resourcearnparam.md)
The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.
where used: path; required: true
type: string

### Responses
<a name="-tags-resource-arn-get-responses"></a>

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

## POST
<a name="-tags-resource-arn-post"></a>

 `POST /tags/{{resource-arn}}`

Operation ID: [TagResource](tagresource-post.md)

Adds tags to a Greengrass resource. Valid resources are `Group`, `ConnectorDefinition`, `CoreDefinition`, `DeviceDefinition`, `FunctionDefinition`, `LoggerDefinition`, `ResourceDefinition`, `SubscriptionDefinition`, and `BulkDeployment`.

Produces: application/json

### CLI
<a name="-tags-resource-arn-post-cli"></a>

```
aws greengrass tag-resource \
  --resource-arn <value> \
  [--tags <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"ResourceArn": "string",
"tags": {
  "additionalProperty0": "string",
  "additionalProperty1": "string",
  "additionalProperty2": "string"
}
}
```

### Parameters:
<a name="-tags-resource-arn-post-params"></a>

[**ResourceArn**](parameters-resourcearnparam.md)
The Amazon Resource Name (ARN) of the resource to attach the tags to.
where used: path; required: true
type: string

[**tags**](parameters-tagsparam.md)
A map of the key-value pairs for the resource tag.
where used: body; required: true
type: tags

### Responses
<a name="-tags-resource-arn-post-responses"></a>

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

## DELETE
<a name="-tags-resource-arn-delete"></a>

 `DELETE /tags/{{resource-arn}}`

Operation ID: [UntagResource](untagresource-delete.md)

Removes tags from a Greengrass resource. Valid resources are `Group`, `ConnectorDefinition`, `CoreDefinition`, `DeviceDefinition`, `FunctionDefinition`, `LoggerDefinition`, `ResourceDefinition`, `SubscriptionDefinition`, and `BulkDeployment`.

Produces: application/json

### CLI
<a name="-tags-resource-arn-delete-cli"></a>

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
  "string"
]
}
```

### Parameters:
<a name="-tags-resource-arn-delete-params"></a>

[**TagKeys**](parameters-tagkeysparam.md)
An array of tag keys to delete.
where used: query; required: true
type: array of strings

[**ResourceArn**](parameters-resourcearnparam.md)
The Amazon Resource Name (ARN) of the resource to remove the tags from.
where used: path; required: true
type: string

### Responses
<a name="-tags-resource-arn-delete-responses"></a>

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
