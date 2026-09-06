---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/parameters-devicedefinitionversionidparam.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# DeviceDefinitionVersionId
<a name="parameters-devicedefinitionversionidparam"></a>

```
{
"DeviceDefinitionVersionId": "string"
}
```

DeviceDefinitionVersionId
The ID of the device definition version. This value maps to the `Version` property of the corresponding `VersionInformation` object, which is returned by `ListDeviceDefinitionVersions` requests. If the version is the last one that was associated with a device definition, the value also maps to the `LatestVersion` property of the corresponding `DefinitionInformation` object.
in: path
required: true
type: string
