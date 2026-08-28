---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-definition-loggers-loggerdefinitionid-versions.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/definition/loggers/LoggerDefinitionId/versions
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions"></a>

## POST
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-post"></a>

 `POST /greengrass/definition/loggers/{{LoggerDefinitionId}}/versions`

Operation ID: [CreateLoggerDefinitionVersion](createloggerdefinitionversion-post.md)

Creates a version of a logger definition that has already been defined.

Produces: application/json

### Body Parameters
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-post-body"></a>

[**CreateLoggerDefinitionVersionRequestBody**](parameters-createloggerdefinitionversionrequestbody.md)

where used: body; required: true

```
{
"Loggers": [
  {
    "Id": "string",
    "Type": "FileSystem|AWSCloudWatch",
    "Component": "GreengrassSystem|Lambda",
    "Level": "DEBUG|INFO|WARN|ERROR|FATAL",
    "Space": 0
  }
]
}
```
LoggerDefinitionVersion
Information about a logger definition version.
type: object
Loggers
A list of loggers.
type: array
items: [Logger](definitions-logger.md)
Logger
Information about a logger
type: object
required: ["Id", "Type", "Component", "Level"]
Id
A descriptive or arbitrary ID for the logger. This value must be unique within the logger definition version. Maximum length is 128 characters with the pattern `[a‑zA‑Z0‑9:_‑]+`.
type: string
Type
type: string
enum: ["FileSystem", "AWSCloudWatch"]
Component
type: string
enum: ["GreengrassSystem", "Lambda"]
Level
type: string
enum: ["DEBUG", "INFO", "WARN", "ERROR", "FATAL"]
Space
The amount of file space, in KB, to use if the local file system is used for logging purposes.
type: integer

### Header Parameters
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-post-header"></a>

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

### Path Parameters
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-post-path"></a>

[**LoggerDefinitionId**](parameters-loggerdefinitionidparam.md)
The ID of the logger definition.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-post-cli"></a>

```
aws greengrass create-logger-definition-version \
  --logger-definition-id <value> \
  [--loggers <value>] \
  [--amzn-client-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"LoggerDefinitionId": "string",
"Loggers": [
  {
    "Id": "string",
    "Type": "FileSystem|AWSCloudWatch",
    "Component": "GreengrassSystem|Lambda",
    "Level": "DEBUG|INFO|WARN|ERROR|FATAL",
    "Space": "integer"
  }
],
"AmznClientToken": "string"
}
```

### Responses
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-post-responses"></a>

**200** (CreateLoggerDefinitionVersionResponse)

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

## GET
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-get"></a>

 `GET /greengrass/definition/loggers/{{LoggerDefinitionId}}/versions`

Operation ID: [ListLoggerDefinitionVersions](listloggerdefinitionversions-get.md)

Lists the versions of a logger definition.

Produces: application/json

### Path Parameters
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-get-path"></a>

[**LoggerDefinitionId**](parameters-loggerdefinitionidparam.md)
The ID of the logger definition.
where used: path; required: true
type: string

### Query Parameters
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-get-query"></a>

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

[**MaxResults**](parameters-maxresultsparam.md)
The maximum number of results to be returned per request.
where used: query; required: false
type: integer

### CLI
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-get-cli"></a>

```
aws greengrass list-logger-definition-versions \
  --logger-definition-id <value> \
  [--next-token <value>] \
  [--max-results <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"LoggerDefinitionId": "string",
"NextToken": "string",
"MaxResults": "integer"
}
```

### Responses
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-get-responses"></a>

**200** (ListLoggerDefinitionVersionsResponse)

 [ ListVersionsResponse](definitions-listversionsresponse.md)

```
{
"Versions": [
  {
    "Arn": "string",
    "Id": "string",
    "Version": "string",
    "CreationTimestamp": "string"
  }
],
"NextToken": "string"
}
```
ListVersionsResponse
A list of versions.
type: object
Versions
Information about a version.
type: array
items: [VersionInformation](definitions-versioninformation.md)
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
NextToken
The token for the next set of results, or `null` if there are no more results.
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
