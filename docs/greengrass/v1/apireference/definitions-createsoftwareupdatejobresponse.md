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
