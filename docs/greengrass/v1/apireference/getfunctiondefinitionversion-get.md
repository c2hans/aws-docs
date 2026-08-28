---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/getfunctiondefinitionversion-get.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetFunctionDefinitionVersion
<a name="getfunctiondefinitionversion-get"></a>

Retrieves information about a Lambda function definition version, including which Lambda functions are included in the version and their configurations.

URI: `GET /greengrass/definition/functions/{{FunctionDefinitionId}}/versions/{{FunctionDefinitionVersionId}}`

Produces: application/json

## CLI:
<a name="getfunctiondefinitionversion-get-cli"></a>

```
aws greengrass get-function-definition-version \
  --function-definition-id <value> \
  --function-definition-version-id <value> \
  [--next-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"FunctionDefinitionId": "string",
"FunctionDefinitionVersionId": "string",
"NextToken": "string"
}
```

## Parameters:
<a name="getfunctiondefinitionversion-get-params"></a>

[**FunctionDefinitionId**](parameters-functiondefinitionidparam.md)
The ID of the function definition.
where used: path; required: true
type: string

[**FunctionDefinitionVersionId**](parameters-functiondefinitionversionidparam.md)
The ID of the function definition version. This value maps to the `Version` property of the corresponding `VersionInformation` object, which is returned by `ListFunctionDefinitionVersions` requests. If the version is the last one that was associated with a function definition, the value also maps to the `LatestVersion` property of the corresponding `DefinitionInformation` object.
where used: path; required: true
type: string

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

## Responses:
<a name="getfunctiondefinitionversion-get-resp"></a>

**200**
Success.
 [ GetFunctionDefinitionVersionResponse](definitions-getfunctiondefinitionversionresponse.md)

```
{
"Arn": "string",
"Id": "string",
"Version": "string",
"CreationTimestamp": "string",
"Definition": {
  "DefaultConfig": {
    "Execution": {
      "IsolationMode": "GreengrassContainer|NoContainer",
      "RunAs": {
        "Uid": 1001,
        "Gid": 1002
      }
    }
  },
  "Functions": [
    {
      "Id": "string",
      "FunctionArn": "string",
      "FunctionConfiguration": {
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
    }
  ]
},
"NextToken": "string"
}
```
GetFunctionDefinitionVersionResponse
Information about a function definition version.
type: object
Arn
The ARN of the function definition version.
type: string
Id
The ID of the function definition version.
type: string
Version
The version of the function definition version.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the function definition version was created.
type: string
Definition
Information about a function definition version.
type: object
DefaultConfig
The default configuration that applies to all Lambda functions in the group. Individual Lambda functions can override these settings.
type: object
Execution
Configuration information that specifies how a Lambda function runs.
Functions
A list of Lambda functions in this function definition version.
type: array
items: [Function](definitions-function.md)

Information about a Lambda function.
type: object
required: ["Id"]
Id
A descriptive or arbitrary ID for the function. This value must be unique within the function definition version. Maximum length is 128 characters with the pattern `[a‑zA‑Z0‑9:_‑]+`.
type: string
FunctionArn
The ARN of the alias (recommended) or version of the target Lambda function.
type: string
FunctionConfiguration
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
NextToken
The token for the next set of results, or `null` if there are no more results.
type: string

**400**
Invalid request.
 [ GeneralError](definitions-generalerror.md)

```
{
"Message": "string",
"ErrorDetails": [
  {
    "DetailedErrorCode": "string",
    "DetailedErrorMessage": "string"
  }
]
}
```
GeneralError
General error information.
type: object
required: ["Message"]
Message
A message that contains information about the error.
type: string
ErrorDetails
A list of error details.
type: array
items: [ErrorDetail](definitions-errordetail.md)
ErrorDetail
Details about the error.
type: object
DetailedErrorCode
A detailed error code.
type: string
DetailedErrorMessage
A detailed error message.
type: string

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
