---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/parameters-loggerdefinitionversionidparam.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# LoggerDefinitionVersionId
<a name="parameters-loggerdefinitionversionidparam"></a>

```
{
"LoggerDefinitionVersionId": "string"
}
```

LoggerDefinitionVersionId
The ID of the logger definition version. This value maps to the `Version` property of the corresponding `VersionInformation` object, which is returned by `ListLoggerDefinitionVersions` requests. If the version is the last one that was associated with a logger definition, the value also maps to the `LatestVersion` property of the corresponding `DefinitionInformation` object.
in: path
required: true
type: string
