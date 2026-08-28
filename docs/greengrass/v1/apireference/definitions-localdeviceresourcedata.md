---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-localdeviceresourcedata.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# LocalDeviceResourceData
<a name="definitions-localdeviceresourcedata"></a>

```
{
"SourcePath": "string",
"GroupOwnerSetting": {
  "AutoAddGroupOwner": true,
  "GroupOwner": "string"
}
}
```

LocalDeviceResourceData
Attributes that define a local device resource.
type: object

SourcePath
The local absolute path of the device resource. The source path for a device resource can refer only to a character device or block device under `/dev`.
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
