---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-functionexecutionconfig.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# FunctionExecutionConfig
<a name="definitions-functionexecutionconfig"></a>

```
{
"IsolationMode": "GreengrassContainer|NoContainer",
"RunAs": {
  "Uid": 1001,
  "Gid": 1002
}
}
```

FunctionExecutionConfig
Configuration information that specifies how a Lambda function runs.
type: object

IsolationMode
Specifies whether the Lambda function runs in a Greengrass container (default) or without containerization. Unless your scenario requires that you run without containerization, we recommend that you run in a Greengrass container. Omit this value to run the Lambda function with the default containerization for the group.
type: string
enum: ["GreengrassContainer", "NoContainer"]

RunAs
Specifies the user and group whose permissions are used when running the Lambda function. You can specify one or both values to override the default values. To minimize the risk of unintended changes or malicious attacks, we recommend that you avoid running as root unless absolutely necessary. To run as root, you must update config.json in `greengrass-root/config` to set `allowFunctionsToRunAsRoot` to `yes`.
type: object

Uid
The user ID whose permissions are used to run a Lambda function.
type: integer

Gid
The group ID whose permissions are used to run a Lambda function.
type: integer
