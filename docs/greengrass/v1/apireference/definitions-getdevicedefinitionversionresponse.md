---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-getdevicedefinitionversionresponse.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetDeviceDefinitionVersionResponse
<a name="definitions-getdevicedefinitionversionresponse"></a>

```
{
"Arn": "string",
"Id": "string",
"Version": "string",
"CreationTimestamp": "string",
"Definition": {
  "Devices": [
    {
      "Id": "string",
      "ThingArn": "string",
      "CertificateArn": "string",
      "SyncShadow": true
    }
  ]
},
"NextToken": "string"
}
```

GetDeviceDefinitionVersionResponse
type: object

Arn
The ARN of the device definition version.
type: string

Id
The ID of the device definition version.
type: string

Version
The version of the device definition version.
type: string

CreationTimestamp
The time, in milliseconds since the epoch, when the device definition version was created.
type: string

Definition
Information about a device definition version.
type: object

Devices
A list of devices in the definition version.
type: array
items: [Device](definitions-device.md)

Device
Information about a device.
type: object
required: ["Id", "ThingArn", "CertificateArn"]

Id
A descriptive or arbitrary ID for the device. This value must be unique within the device definition version. Maximum length is 128 characters with the pattern `[a‑zA‑Z0‑9:_‑]+`.
type: string

ThingArn
The thing ARN of the device.
type: string

CertificateArn
The ARN of the certificate associated with the device.
type: string

SyncShadow
If true, the device's local shadow is synced with the cloud automatically.
type: boolean

NextToken
The token for the next set of results, or `null` if there are no more results.
type: string
