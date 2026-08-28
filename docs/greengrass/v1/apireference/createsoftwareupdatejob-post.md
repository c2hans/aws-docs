---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/createsoftwareupdatejob-post.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateSoftwareUpdateJob
<a name="createsoftwareupdatejob-post"></a>

Creates a software update for a core or group of cores (specified as an IoT thing group.) Use this to update the OTA agent and the Greengrass core software. It uses the AWS IoT Jobs feature, which provides more commands for managing a Greengrass Core software update job.

URI: `POST /greengrass/updates`

Produces: application/json

## CLI:
<a name="createsoftwareupdatejob-post-cli"></a>

```
aws greengrass create-software-update-job \
  [--update-targets-architecture <value>] \
  [--update-targets <value>] \
  [--software-to-update <value>] \
  [--s3-url-signer-role <value>] \
  [--update-agent-log-level <value>] \
  [--update-targets-operating-system <value>] \
  [--amzn-client-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"UpdateTargetsArchitecture": "armv6l|armv7l|x86_64|aarch64",
"UpdateTargets": [
  "string"
],
"SoftwareToUpdate": "core|ota_agent",
"S3UrlSignerRole": "string",
"UpdateAgentLogLevel": "NONE|TRACE|DEBUG|VERBOSE|INFO|WARN|ERROR|FATAL",
"UpdateTargetsOperatingSystem": "ubuntu|raspbian|amazon_linux|openwrt",
"AmznClientToken": "string"
}
```

## Parameters:
<a name="createsoftwareupdatejob-post-params"></a>

[**CreateSoftwareUpdateJobRequestBody**](parameters-createsoftwareupdatejobrequestbody.md)

where used: body; required: true

```
{
"UpdateTargetsArchitecture": "armv6l|armv7l|x86_64|aarch64",
"UpdateTargets": [
  "string"
],
"SoftwareToUpdate": "core|ota_agent",
"S3UrlSignerRole": "string",
"UpdateAgentLogLevel": "NONE|TRACE|DEBUG|VERBOSE|INFO|WARN|ERROR|FATAL",
"UpdateTargetsOperatingSystem": "ubuntu|raspbian|amazon_linux|openwrt"
}
```
schema:
CreateSoftwareUpdateJobRequest
Request for the CreateSoftwareUpdateJob API.
type: object
required: ["UpdateTargetsArchitecture", "UpdateTargets", "SoftwareToUpdate", "S3UrlSignerRole", "UpdateTargetsOperatingSystem"]
UpdateTargetsArchitecture
The architecture of the cores that are the targets of an update.
type: string
enum: ["armv6l", "armv7l", "x86\_64", "aarch64"]
UpdateTargets
The ARNs of the targets (IoT things or IoT thing groups) that this update is applied to.
type: array

SoftwareToUpdate
The piece of software on the Greengrass core that will be updated.
type: string
enum: ["core", "ota\_agent"]
S3UrlSignerRole
The IAM role that Greengrass uses to create presigned URLs that point to the update artifact.
type: string
UpdateAgentLogLevel
The minimum level of log statements that should be logged by the OTA agent during an update.
type: string
enum: ["NONE", "TRACE", "DEBUG", "VERBOSE", "INFO", "WARN", "ERROR", "FATAL"]
UpdateTargetsOperatingSystem
The operating system of the cores that are the targets of an update.
type: string
enum: ["ubuntu", "raspbian", "amazon\_linux", "openwrt"]

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

## Responses:
<a name="createsoftwareupdatejob-post-resp"></a>

**200**
Success.
 [ CreateSoftwareUpdateJobResponse](definitions-createsoftwareupdatejobresponse.md)

```
{
"IotJobId": "string",
"IotJobArn": "string",
"PlatformSoftwareVersion": "string"
}
```
CreateSoftwareUpdateJobResponse
type: object
IotJobId
The IoT job ID that corresponds to this update.
type: string
IotJobArn
The IoT job ARN that corresponds to this update.
type: string
PlatformSoftwareVersion
The software version installed on the device or devices after the update.
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

**500**
Server error.
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
