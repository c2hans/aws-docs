---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-definition-loggers-loggerdefinitionid-versions-loggerdefinitionversionid.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/definition/loggers/LoggerDefinitionId/versions/LoggerDefinitionVersionId
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-loggerdefinitionversionid"></a>

## GET
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-loggerdefinitionversionid-get"></a>

 `GET /greengrass/definition/loggers/{{LoggerDefinitionId}}/versions/{{LoggerDefinitionVersionId}}`

Operation ID: [GetLoggerDefinitionVersion](getloggerdefinitionversion-get.md)

Retrieves information about a logger definition version.

Produces: application/json

### Path Parameters
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-loggerdefinitionversionid-get-path"></a>

[**LoggerDefinitionVersionId**](parameters-loggerdefinitionversionidparam.md)
The ID of the logger definition version. This value maps to the `Version` property of the corresponding `VersionInformation` object, which is returned by `ListLoggerDefinitionVersions` requests. If the version is the last one that was associated with a logger definition, the value also maps to the `LatestVersion` property of the corresponding `DefinitionInformation` object.
where used: path; required: true
type: string

[**LoggerDefinitionId**](parameters-loggerdefinitionidparam.md)
The ID of the logger definition.
where used: path; required: true
type: string

### Query Parameters
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-loggerdefinitionversionid-get-query"></a>

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

### CLI
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-loggerdefinitionversionid-get-cli"></a>

```
aws greengrass get-logger-definition-version \
  --logger-definition-version-id <value> \
  --logger-definition-id <value> \
  [--next-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"LoggerDefinitionVersionId": "string",
"LoggerDefinitionId": "string",
"NextToken": "string"
}
```

### Responses
<a name="-greengrass-definition-loggers-loggerdefinitionid-versions-loggerdefinitionversionid-get-responses"></a>

**200** (GetLoggerDefinitionVersionResponse)
Success.
 [ GetLoggerDefinitionVersionResponse](definitions-getloggerdefinitionversionresponse.md)

```
{
"Arn": "string",
"Id": "string",
"Version": "string",
"CreationTimestamp": "string",
"Definition": {
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
}
```
GetLoggerDefinitionVersionResponse
Information about a logger definition version.
type: object
Arn
The ARN of the logger definition version.
type: string
Id
The ID of the logger definition version.
type: string
Version
The version of the logger definition version.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the logger definition version was created.
type: string
Definition
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
