---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-functionrunasconfig.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# FunctionRunAsConfig
<a name="definitions-functionrunasconfig"></a>

```
{
"Uid": 1001,
"Gid": 1002
}
```

FunctionRunAsConfig
Specifies the user and group whose permissions are used when running the Lambda function. You can specify one or both values to override the default values. To minimize the risk of unintended changes or malicious attacks, we recommend that you avoid running as root unless absolutely necessary. To run as root, you must update config.json in `greengrass-root/config` to set `allowFunctionsToRunAsRoot` to `yes`.
type: object

Uid
The user ID whose permissions are used to run a Lambda function.
type: integer

Gid
The group ID whose permissions are used to run a Lambda function.
type: integer
