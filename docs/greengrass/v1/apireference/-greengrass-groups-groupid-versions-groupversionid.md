---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-groups-groupid-versions-groupversionid.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/groups/GroupId/versions/GroupVersionId
<a name="-greengrass-groups-groupid-versions-groupversionid"></a>

## GET
<a name="-greengrass-groups-groupid-versions-groupversionid-get"></a>

 `GET /greengrass/groups/{{GroupId}}/versions/{{GroupVersionId}}`

Operation ID: [GetGroupVersion](getgroupversion-get.md)

Retrieves information about a group version.

Produces: application/json

### Path Parameters
<a name="-greengrass-groups-groupid-versions-groupversionid-get-path"></a>

[**GroupId**](parameters-groupidparam.md)
The ID of the Greengrass group.
where used: path; required: true
type: string

[**GroupVersionId**](parameters-groupversionidparam.md)
The ID of the group version. This value maps to the `Version` property of the corresponding `VersionInformation` object, which is returned by `ListGroupVersions` requests. If the version is the last one that was associated with a group, the value also maps to the `LatestVersion` property of the corresponding `GroupInformation` object.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-groups-groupid-versions-groupversionid-get-cli"></a>

```
aws greengrass get-group-version \
  --group-id <value> \
  --group-version-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"GroupId": "string",
"GroupVersionId": "string"
}
```

### Responses
<a name="-greengrass-groups-groupid-versions-groupversionid-get-responses"></a>

**200**
Success.
 [ GetGroupVersionResponse](definitions-getgroupversionresponse.md)

```
{
"Arn": "string",
"Id": "string",
"Version": "string",
"CreationTimestamp": "string",
"Definition": {
  "CoreDefinitionVersionArn": "string",
  "DeviceDefinitionVersionArn": "string",
  "FunctionDefinitionVersionArn": "string",
  "SubscriptionDefinitionVersionArn": "string",
  "LoggerDefinitionVersionArn": "string",
  "ResourceDefinitionVersionArn": "string",
  "ConnectorDefinitionVersionArn": "string"
}
}
```
GetGroupVersionResponse
Information about a group version.
type: object
Arn
The ARN of the group version.
type: string
Id
The ID of the group that the version is associated with.
type: string
Version
The ID of the group version.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the group version was created.
type: string
Definition
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
