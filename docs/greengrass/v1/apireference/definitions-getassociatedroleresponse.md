---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-getassociatedroleresponse.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetAssociatedRoleResponse
<a name="definitions-getassociatedroleresponse"></a>

```
{
"AssociatedAt": "string",
"RoleArn": "string"
}
```

GetAssociatedRoleResponse
type: object

AssociatedAt
The time when the role was associated with the group.
type: string

RoleArn
The ARN of the role that is associated with the group.
type: string
