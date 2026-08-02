---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/parameters-groupversionidparam.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GroupVersionId
<a name="parameters-groupversionidparam"></a>

```
{
"GroupVersionId": "string"
}
```

GroupVersionId
The ID of the group version. This value maps to the `Version` property of the corresponding `VersionInformation` object, which is returned by `ListGroupVersions` requests. If the version is the last one that was associated with a group, the value also maps to the `LatestVersion` property of the corresponding `GroupInformation` object.
in: path
required: true
type: string
