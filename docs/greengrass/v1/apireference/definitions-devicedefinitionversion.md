---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-devicedefinitionversion.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# DeviceDefinitionVersion
<a name="definitions-devicedefinitionversion"></a>

```
{
"Devices": [
  {
    "Id": "string",
    "ThingArn": "string",
    "CertificateArn": "string",
    "SyncShadow": true
  }
]
}
```

DeviceDefinitionVersion
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
