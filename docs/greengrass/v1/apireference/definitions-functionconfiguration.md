---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-functionconfiguration.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# FunctionConfiguration
<a name="definitions-functionconfiguration"></a>

```
{
"Pinned": true,
"Executable": "string",
"ExecArgs": "string",
"MemorySize": 0,
"Timeout": 0,
"EncodingType": "binary|json",
"Environment": {
  "Variables": {
    "additionalProperty0": "string",
    "additionalProperty1": "string",
    "additionalProperty2": "string"
  },
  "ResourceAccessPolicies": [
    {
      "ResourceId": "string",
      "Permission": "ro|rw"
    }
  ],
  "AccessSysfs": true,
  "Execution": {
    "IsolationMode": "GreengrassContainer|NoContainer",
    "RunAs": {
      "Uid": 1001,
      "Gid": 1002
    }
  }
},
"FunctionRuntimeOverride": "string"
}
```

The configuration of the Lambda function.
type: object

Pinned
True if the function is pinned. Pinned means the function is long-lived and starts when the core starts.
type: boolean

Executable
The name of the function executable.
type: string

ExecArgs
The execution arguments.
type: string

MemorySize
The memory size, in KB, required by the function. This setting does not apply and should be cleared when you run the Lambda function without containerization.
type: integer

Timeout
The allowed function execution time, after which Lambda should terminate the function. This timeout still applies to pinned Lambda functions for each request.
type: integer

EncodingType
The expected encoding type of the input payload for the function. The default is `json`.
type: string
enum: ["binary", "json"]

Environment
The environment configuration of the function.
type: object

Variables
Environment variables for the Lambda function's configuration.
type: object
additionalProperties: An object with properties of type `string` that represent the environment variables.

ResourceAccessPolicies
A list of the resources, with their permissions, to which the Lambda function is granted access. A Lambda function can have at most 10 resources. ResourceAccessPolicies applies only when you run the Lambda function in a Greengrass container.
type: array
items: [ResourceAccessPolicy](definitions-resourceaccesspolicy.md)

ResourceAccessPolicy
A policy used by the function to access a resource.
type: object
required: ["ResourceId"]

ResourceId
The ID of the resource. (This ID is assigned to the resource when you create the resource definiton.)
type: string

Permission
The type of permission a function has to access a resource.
type: string
enum: ["ro", "rw"]

AccessSysfs
If true, the Lambda function is allowed to access the host's /sys folder. Use this when the Lambda function needs to read device information from /sys. This setting applies only when you run the Lambda function in a Greengrass container.
type: boolean

Execution
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

FunctionRuntimeOverride
The Lambda runtime supported by Greengrass which is to be used instead of the one specified in the Lambda function.
type: string

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
