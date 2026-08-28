---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/creategroupversion-post.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateGroupVersion
<a name="creategroupversion-post"></a>

Creates a version of a group that has already been defined.

URI: `POST /greengrass/groups/{{GroupId}}/versions`

Produces: application/json

## CLI:
<a name="creategroupversion-post-cli"></a>

```
aws greengrass create-group-version \
  --group-id <value> \
  [--core-definition-version-arn <value>] \
  [--device-definition-version-arn <value>] \
  [--function-definition-version-arn <value>] \
  [--subscription-definition-version-arn <value>] \
  [--logger-definition-version-arn <value>] \
  [--resource-definition-version-arn <value>] \
  [--connector-definition-version-arn <value>] \
  [--amzn-client-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"GroupId": "string",
"CoreDefinitionVersionArn": "string",
"DeviceDefinitionVersionArn": "string",
"FunctionDefinitionVersionArn": "string",
"SubscriptionDefinitionVersionArn": "string",
"LoggerDefinitionVersionArn": "string",
"ResourceDefinitionVersionArn": "string",
"ConnectorDefinitionVersionArn": "string",
"AmznClientToken": "string"
}
```

## Parameters:
<a name="creategroupversion-post-params"></a>

[**GroupId**](parameters-groupidparam.md)
The ID of the Greengrass group.
where used: path; required: true
type: string

[**CreateGroupVersionRequestBody**](parameters-creategroupversionrequestbody.md)

where used: body; required: true

```
{
"CoreDefinitionVersionArn": "string",
"DeviceDefinitionVersionArn": "string",
"FunctionDefinitionVersionArn": "string",
"SubscriptionDefinitionVersionArn": "string",
"LoggerDefinitionVersionArn": "string",
"ResourceDefinitionVersionArn": "string",
"ConnectorDefinitionVersionArn": "string"
}
```
schema:
GroupVersion
Information about a group version.
type: object
CoreDefinitionVersionArn
The ARN of the core definition version for this group.
type: string
DeviceDefinitionVersionArn
The ARN of the client device definition version for this group.
type: string
FunctionDefinitionVersionArn
The ARN of the function definition version for this group.
type: string
SubscriptionDefinitionVersionArn
The ARN of the subscription definition version for this group.
type: string
LoggerDefinitionVersionArn
The ARN of the logger definition version for this group.
type: string
ResourceDefinitionVersionArn
The ARN of the resource definition version for this group.
type: string
ConnectorDefinitionVersionArn
The ARN of the connector definition version for this group.
type: string

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

## Responses:
<a name="creategroupversion-post-resp"></a>

**200** (CreateGroupVersionResponse)
Success. The response contains information about the group version.
 [ VersionInformation](definitions-versioninformation.md)

```
{
"Arn": "string",
"Id": "string",
"Version": "string",
"CreationTimestamp": "string"
}
```
VersionInformation
Information about a version.
type: object
Arn
The ARN of the version.
type: string
Id
The ID of the parent definition that the version is associated with.
type: string
Version
The ID of the version.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the version was created.
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
