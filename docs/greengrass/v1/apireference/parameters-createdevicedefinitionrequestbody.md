---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/parameters-createdevicedefinitionrequestbody.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateDeviceDefinitionRequestBody
<a name="parameters-createdevicedefinitionrequestbody"></a>

```
{
"Name": "string",
"InitialVersion": {
  "Devices": [
    {
      "Id": "string",
      "ThingArn": "string",
      "CertificateArn": "string",
      "SyncShadow": true
    }
  ]
},
"tags": {
  "additionalProperty0": "string",
  "additionalProperty1": "string",
  "additionalProperty2": "string"
}
}
```

CreateDeviceDefinitionRequestBody
Information required to create a device definition.
in: body
required: true

properties
Name: The name of the device definition. Type: string
InitialVersion: Information about the initial version of the device definition. Type: DeviceDefinitionVersion
tags: The tags to attach to the new resource. Type: tags
