---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/tagresource-post.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# TagResource
<a name="tagresource-post"></a>

Adds tags to a Greengrass resource. Valid resources are `Group`, `ConnectorDefinition`, `CoreDefinition`, `DeviceDefinition`, `FunctionDefinition`, `LoggerDefinition`, `ResourceDefinition`, `SubscriptionDefinition`, and `BulkDeployment`.

URI: `POST /tags/{{resource-arn}}`

Produces: application/json

## CLI:
<a name="tagresource-post-cli"></a>

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
"tags": {
  "keyName0": "string",
  "keyName1": "string",
  "keyName2": "string"
}
}
```

## Parameters:
<a name="tagresource-post-params"></a>

[**ResourceArn**](parameters-resourcearnparam.md)
The Amazon Resource Name (ARN) of the resource to attach the tags to.
where used: path; required: true
type: string

[**tags**](parameters-tagsparam.md)
A map of the key-value pairs for the resource tag.
where used: body; required: true
type: tags

## Responses:
<a name="tagresource-post-resp"></a>

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
