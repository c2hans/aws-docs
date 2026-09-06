---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-resourcedownloadownersetting.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# ResourceDownloadOwnerSetting
<a name="definitions-resourcedownloadownersetting"></a>

```
{
"GroupOwner": "string",
"GroupPermission": "ro|rw"
}
```

ResourceDownloadOwnerSetting
The owner setting for the downloaded machine learning resource.
type: object
required: ["GroupOwner", "GroupPermission"]

GroupOwner
The group owner of the resource. This is the group ID (GID) of an existing Linux OS group on the system. The group's permissions are added to the Lambda process.
type: string

GroupPermission
The permissions that the group owner has to the resource. Valid values are `rw` (read-write) or `ro` (read-only).
type: string
enum: ["ro", "rw"]
