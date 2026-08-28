---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-createsoftwareupdatejobresponse.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateSoftwareUpdateJobResponse
<a name="definitions-createsoftwareupdatejobresponse"></a>

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
