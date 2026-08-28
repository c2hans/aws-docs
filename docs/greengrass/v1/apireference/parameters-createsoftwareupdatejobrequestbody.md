---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/parameters-createsoftwareupdatejobrequestbody.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateSoftwareUpdateJobRequestBody
<a name="parameters-createsoftwareupdatejobrequestbody"></a>

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

CreateSoftwareUpdateJobRequestBody
in: body
required: true
schema: [CreateSoftwareUpdateJobRequest](definitions-createsoftwareupdatejobrequest.md)

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
