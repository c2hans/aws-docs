---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-localvolumeresourcedata.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# LocalVolumeResourceData
<a name="definitions-localvolumeresourcedata"></a>

```
{
"SourcePath": "string",
"DestinationPath": "string",
"GroupOwnerSetting": {
  "AutoAddGroupOwner": true,
  "GroupOwner": "string"
}
}
```

LocalVolumeResourceData
Attributes that define a local volume resource.
type: object

SourcePath
The local absolute path of the volume resource on the host. The source path for a volume resource type cannot start with `/sys`.
type: string

DestinationPath
The absolute local path of the resource inside the Lambda environment.
type: string

GroupOwnerSetting
Group owner related settings for local resources.
type: object

AutoAddGroupOwner
If true, AWS IoT Greengrass adds the specified Linux OS group owner of the resource to the Lambda process privileges. The Lambda process then has the file access permissions of the added Linux group.
type: boolean

GroupOwner
The name of the Linux OS group whose privileges are added to the Lambda process. This field is optional.
type: string
