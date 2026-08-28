---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-groups.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/groups
<a name="-greengrass-groups"></a>

## GET
<a name="-greengrass-groups-get"></a>

 `GET /greengrass/groups`

Operation ID: [ListGroups](listgroups-get.md)

Retrieves a list of groups.

Produces: application/json

### Query Parameters
<a name="-greengrass-groups-get-query"></a>

[**MaxResults**](parameters-maxresultsparam.md)
The maximum number of results to be returned per request.
where used: query; required: false
type: integer

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

### CLI
<a name="-greengrass-groups-get-cli"></a>

```
aws greengrass list-groups \
  [--max-results <value>] \
  [--next-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"MaxResults": "integer",
"NextToken": "string"
}
```

### Responses
<a name="-greengrass-groups-get-responses"></a>

**200** (ListGroupsResponse)

 [ ListGroupsResponse](definitions-listgroupsresponse.md)

```
{
"Groups": [
  {
    "Name": "string",
    "Id": "string",
    "Arn": "string",
    "LastUpdatedTimestamp": "string",
    "CreationTimestamp": "string",
    "LatestVersion": "string",
    "LatestVersionArn": "string"
  }
],
"NextToken": "string"
}
```
ListGroupsResponse
type: object
Groups
Information about a group.
type: array
items: [GroupInformation](definitions-groupinformation.md)
GroupInformation
Information about a group.
type: object
Name
The name of the group.
type: string
Id
The ID of the group.
type: string
Arn
The ARN of the group.
type: string
LastUpdatedTimestamp
The time, in milliseconds since the epoch, when the group was last updated.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the group was created.
type: string
LatestVersion
The ID of the latest version associated with the group.
type: string
LatestVersionArn
The ARN of the latest version associated with the group.
type: string
NextToken
The token for the next set of results, or `null` if there are no more results.
type: string

## POST
<a name="-greengrass-groups-post"></a>

 `POST /greengrass/groups`

Operation ID: [CreateGroup](creategroup-post.md)

Creates a group. You can provide the initial version of the group or use `CreateGroupVersion` later. Tip: You can use the `gg_group_setup` package (https://github.com/awslabs/aws-greengrass-group-setup) as a library or command-line application to create and deploy Greengrass groups.

Produces: application/json

### Body Parameters
<a name="-greengrass-groups-post-body"></a>

[**CreateGroupRequestBody**](parameters-creategrouprequestbody.md)

where used: body; required: true

```
{
"Name": "string",
"InitialVersion": {
  "CoreDefinitionVersionArn": "string",
  "DeviceDefinitionVersionArn": "string",
  "FunctionDefinitionVersionArn": "string",
  "SubscriptionDefinitionVersionArn": "string",
  "LoggerDefinitionVersionArn": "string",
  "ResourceDefinitionVersionArn": "string",
  "ConnectorDefinitionVersionArn": "string"
},
"tags": {
  "keyName0": "string",
  "keyName1": "string",
  "keyName2": "string"
}
}
```
Name
The name of the group.
type: string
InitialVersion
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
tags
The resource tags.
type: object
additionalProperties: The key-value pair for the resource tag. Type: string

### Header Parameters
<a name="-greengrass-groups-post-header"></a>

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

### CLI
<a name="-greengrass-groups-post-cli"></a>

```
aws greengrass create-group \
  --name <value> \
  [--initial-version <value>] \
  [--tags <value>] \
  [--amzn-client-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"Name": "string",
"InitialVersion": {
  "CoreDefinitionVersionArn": "string",
  "DeviceDefinitionVersionArn": "string",
  "FunctionDefinitionVersionArn": "string",
  "SubscriptionDefinitionVersionArn": "string",
  "LoggerDefinitionVersionArn": "string",
  "ResourceDefinitionVersionArn": "string",
  "ConnectorDefinitionVersionArn": "string"
},
"tags": {
  "additionalProperty0": "string",
  "additionalProperty1": "string",
  "additionalProperty2": "string"
},
"AmznClientToken": "string"
}
```

### Responses
<a name="-greengrass-groups-post-responses"></a>

**200** (CreateGroupResponse)
Success. The group was created.
 [ DefinitionInformation](definitions-definitioninformation.md)

```
{
"Name": "string",
"Id": "string",
"Arn": "string",
"LastUpdatedTimestamp": "string",
"CreationTimestamp": "string",
"LatestVersion": "string",
"LatestVersionArn": "string"
}
```
DefinitionInformation
Information about a definition.
type: object
Name
The name of the definition.
type: string
Id
The ID of the definition.
type: string
Arn
The ARN of the definition.
type: string
LastUpdatedTimestamp
The time, in milliseconds since the epoch, when the definition was last updated.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the definition was created.
type: string
LatestVersion
The ID of the latest version associated with the definition.
type: string
LatestVersionArn
The ARN of the latest version associated with the definition.
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
