---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_CreateFunction.html
---

# CreateFunction
<a name="API_CreateFunction"></a>

Creates a Lambda function. To create a function, you need a [deployment package](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html) and an [execution role](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html#lambda-intro-execution-role). The deployment package is a .zip file archive or container image that contains your function code. The execution role grants the function permission to use AWS services, such as Amazon CloudWatch Logs for log streaming and AWS X-Ray for request tracing.

If the deployment package is a [container image](https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html), then you set the package type to `Image`. For a container image, the code property must include the URI of a container image in the Amazon ECR registry. You do not need to specify the handler and runtime properties.

If the deployment package is a [.zip file archive](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html#gettingstarted-package-zip), then you set the package type to `Zip`. For a .zip file archive, the code property specifies the location of the .zip file. You must also specify the handler and runtime properties. The code in the deployment package must be compatible with the target instruction set architecture of the function (`x86-64` or `arm64`). If you do not specify the architecture, then the default value is `x86-64`.

When you create a function, Lambda provisions an instance of the function and its supporting resources. If your function connects to a VPC, this process can take a minute or so. During this time, you can't invoke or modify the function. The `State`, `StateReason`, and `StateReasonCode` fields in the response from [GetFunctionConfiguration](API_GetFunctionConfiguration.md) indicate when the function is ready to invoke. For more information, see [Lambda function states](https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html).

A function has an unpublished version, and can have published versions and aliases. The unpublished version changes when you update your function's code and configuration. A published version is a snapshot of your function code and configuration that can't be changed. An alias is a named resource that maps to a version, and can be changed to map to a different version. Use the `Publish` parameter to create version `1` of your function from its initial configuration.

The other parameters let you configure version-specific and function-level settings. You can modify version-specific settings later with [UpdateFunctionConfiguration](API_UpdateFunctionConfiguration.md). Function-level settings apply to both the unpublished and published versions of the function, and include tags ([TagResource](API_TagResource.md)) and per-function concurrency limits ([PutFunctionConcurrency](API_PutFunctionConcurrency.md)).

You can use code signing if your deployment package is a .zip file archive. To enable code signing for this function, specify the ARN of a code-signing configuration. When a user attempts to deploy a code package with [UpdateFunctionCode](API_UpdateFunctionCode.md), Lambda checks that the code package has a valid signature from a trusted publisher. The code-signing configuration includes set of signing profiles, which define the trusted publishers for this function.

If another AWS account or an AWS service invokes your function, use [AddPermission](API_AddPermission.md) to grant permission by creating a resource-based AWS Identity and Access Management (IAM) policy. You can grant permissions at the function level, on a version, or on an alias.

To invoke your function directly, use [Invoke](API_Invoke.md). To invoke your function in response to events in other AWS services, create an event source mapping ([CreateEventSourceMapping](API_CreateEventSourceMapping.md)), or configure a function trigger in the other service. For more information, see [Invoking Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html).

## Request Syntax
<a name="API_CreateFunction_RequestSyntax"></a>

```
POST /2015-03-31/functions HTTP/1.1
Content-type: application/json

{
   "Architectures": [ "{{string}}" ],
   "CapacityProviderConfig": {
      "LambdaManagedInstancesCapacityProviderConfig": {
         "CapacityProviderArn": "{{string}}",
         "ExecutionEnvironmentMemoryGiBPerVCpu": {{number}},
         "PerExecutionEnvironmentMaxConcurrency": {{number}}
      }
   },
   "Code": {
      "ImageUri": "{{string}}",
      "S3Bucket": "{{string}}",
      "S3Key": "{{string}}",
      "S3ObjectStorageMode": "{{string}}",
      "S3ObjectVersion": "{{string}}",
      "SourceKMSKeyArn": "{{string}}",
      "ZipFile": {{blob}}
   },
   "CodeSigningConfigArn": "{{string}}",
   "DeadLetterConfig": {
      "TargetArn": "{{string}}"
   },
   "Description": "{{string}}",
   "DurableConfig": {
      "ExecutionTimeout": {{number}},
      "KMSKeyArn": "{{string}}",
      "RetentionPeriodInDays": {{number}}
   },
   "Environment": {
      "Variables": {
         "{{string}}" : "{{string}}"
      }
   },
   "EphemeralStorage": {
      "Size": {{number}}
   },
   "FileSystemConfigs": [
      {
         "Arn": "{{string}}",
         "LocalMountPath": "{{string}}",
         "S3FilesConfig": {
            "DirectS3Read": "{{string}}"
         }
      }
   ],
   "FunctionName": "{{string}}",
   "Handler": "{{string}}",
   "ImageConfig": {
      "Command": [ "{{string}}" ],
      "EntryPoint": [ "{{string}}" ],
      "WorkingDirectory": "{{string}}"
   },
   "KMSKeyArn": "{{string}}",
   "Layers": [ "{{string}}" ],
   "LoggingConfig": {
      "ApplicationLogLevel": "{{string}}",
      "LogFormat": "{{string}}",
      "LogGroup": "{{string}}",
      "SystemLogLevel": "{{string}}"
   },
   "MemorySize": {{number}},
   "PackageType": "{{string}}",
   "Publish": {{boolean}},
   "PublishTo": "{{string}}",
   "Role": "{{string}}",
   "Runtime": "{{string}}",
   "SnapStart": {
      "ApplyOn": "{{string}}"
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TenancyConfig": {
      "TenantIsolationMode": "{{string}}"
   },
   "Timeout": {{number}},
   "TracingConfig": {
      "Mode": "{{string}}"
   },
   "VpcConfig": {
      "Ipv6AllowedForDualStack": {{boolean}},
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_CreateFunction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateFunction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Architectures](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-Architectures"></a>
The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86\_64). The default value is `x86_64`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `x86_64 | arm64`
Required: No

 ** [CapacityProviderConfig](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-CapacityProviderConfig"></a>
Configuration for the capacity provider that manages compute resources for Lambda functions.
Type: [CapacityProviderConfig](API_CapacityProviderConfig.md) object
Required: No

 ** [Code](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-Code"></a>
The code for the function.
Type: [FunctionCode](API_FunctionCode.md) object
Required: Yes

 ** [CodeSigningConfigArn](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-CodeSigningConfigArn"></a>
To enable code signing for this function, specify the ARN of a code-signing configuration. A code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:code-signing-config:csc-[a-z0-9]{17}`
Required: No

 ** [DeadLetterConfig](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-DeadLetterConfig"></a>
A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see [Dead-letter queues](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq).
Type: [DeadLetterConfig](API_DeadLetterConfig.md) object
Required: No

 ** [Description](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-Description"></a>
A description of the function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [DurableConfig](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-DurableConfig"></a>
Configuration settings for durable functions. Enables creating functions with durability that can remember their state and continue execution even after interruptions.
Type: [DurableConfig](API_DurableConfig.md) object
Required: No

 ** [Environment](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-Environment"></a>
Environment variables that are accessible from function code during execution.
Type: [Environment](API_Environment.md) object
Required: No

 ** [EphemeralStorage](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-EphemeralStorage"></a>
The size of the function's `/tmp` directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see [Configuring ephemeral storage (console)](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage).
Type: [EphemeralStorage](API_EphemeralStorage.md) object
Required: No

 ** [FileSystemConfigs](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-FileSystemConfigs"></a>
Connection settings for an Amazon EFS file system or an Amazon S3 Files file system.
Type: Array of [FileSystemConfig](API_FileSystemConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** [FunctionName](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** – `my-function`.
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** [Handler](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-Handler"></a>
The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see [Lambda programming model](https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[^\s]+`
Required: No

 ** [ImageConfig](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-ImageConfig"></a>
Container image [configuration values](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms) that override the values in the container image Dockerfile.
Type: [ImageConfig](API_ImageConfig.md) object
Required: No

 ** [KMSKeyArn](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-KMSKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt the following resources:
+ The function's [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption).
+ The function's [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html) snapshots.
+ When used with `SourceKMSKeyArn`, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see [ Specifying a customer managed key for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption).
+ The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see [Function lifecycle](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle).
If you don't provide a customer managed key, Lambda uses an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) or an [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk).
Type: String
Pattern: `(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()`
Required: No

 ** [Layers](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-Layers"></a>
A list of [function layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) to add to the function's execution environment. Specify each layer by its ARN, including the version.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+:[0-9]+`
Required: No

 ** [LoggingConfig](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-LoggingConfig"></a>
The function's Amazon CloudWatch Logs configuration settings.
Type: [LoggingConfig](API_LoggingConfig.md) object
Required: No

 ** [MemorySize](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-MemorySize"></a>
The amount of [memory available to the function](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-memory-console) at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB.
Type: Integer
Valid Range: Minimum value of 128. Maximum value of 32768.
Required: No

 ** [PackageType](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-PackageType"></a>
The type of deployment package. Set to `Image` for container image and set to `Zip` for .zip file archive.
Type: String
Valid Values: `Zip | Image`
Required: No

 ** [Publish](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-Publish"></a>
Set to true to publish the first version of the function during creation.
Type: Boolean
Required: No

 ** [PublishTo](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-PublishTo"></a>
Specifies where to publish the function version or configuration.
Type: String
Valid Values: `LATEST_PUBLISHED`
Required: No

 ** [Role](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-Role"></a>
The Amazon Resource Name (ARN) of the function's execution role.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [Runtime](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-Runtime"></a>
The identifier of the function's [ runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.
The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels).
For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported).
Type: String
Valid Values: `nodejs | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs10.x | nodejs12.x | nodejs14.x | nodejs16.x | java8 | java8.al2 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | python3.9 | dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | dotnetcore3.1 | dotnet6 | dotnet8 | nodejs4.3-edge | go1.x | ruby2.5 | ruby2.7 | provided | provided.al2 | nodejs18.x | python3.10 | java17 | ruby3.2 | ruby3.3 | ruby3.4 | python3.11 | nodejs20.x | provided.al2023 | python3.12 | java21 | python3.13 | nodejs22.x | nodejs24.x | python3.14 | java25 | dotnet10 | ruby4.0`
Required: No

 ** [SnapStart](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-SnapStart"></a>
The function's [SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) setting.
Type: [SnapStart](API_SnapStart.md) object
Required: No

 ** [Tags](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-Tags"></a>
A list of [tags](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html) to apply to the function.
Type: String to string map
Required: No

 ** [TenancyConfig](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-TenancyConfig"></a>
Configuration for multi-tenant applications that use Lambda functions. Defines tenant isolation settings and resource allocations. Required for functions supporting multiple tenants.
Type: [TenancyConfig](API_TenancyConfig.md) object
Required: No

 ** [Timeout](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-Timeout"></a>
The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds, and the maximum allowed value is 900 seconds. For functions using Lambda Managed Instances, asynchronous invocations and event source mapping invocations (except Amazon MQ and Amazon DocumentDB) support a maximum allowed value of 5,400 seconds (90 minutes). For more information, see [Lambda execution environment](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [TracingConfig](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-TracingConfig"></a>
Set `Mode` to `Active` to sample and trace a subset of incoming requests with [X-Ray](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html).
Type: [TracingConfig](API_TracingConfig.md) object
Required: No

 ** [VpcConfig](#API_CreateFunction_RequestSyntax) **   <a name="lambda-CreateFunction-request-VpcConfig"></a>
For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see [Configuring a Lambda function to access resources in a VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateFunction_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Architectures": [ "string" ],
   "CapacityProviderConfig": {
      "LambdaManagedInstancesCapacityProviderConfig": {
         "CapacityProviderArn": "string",
         "ExecutionEnvironmentMemoryGiBPerVCpu": number,
         "PerExecutionEnvironmentMaxConcurrency": number
      }
   },
   "CodeSha256": "string",
   "CodeSize": number,
   "ConfigSha256": "string",
   "DeadLetterConfig": {
      "TargetArn": "string"
   },
   "Description": "string",
   "DurableConfig": {
      "ExecutionTimeout": number,
      "KMSKeyArn": "string",
      "RetentionPeriodInDays": number
   },
   "Environment": {
      "Error": {
         "ErrorCode": "string",
         "Message": "string"
      },
      "Variables": {
         "string" : "string"
      }
   },
   "EphemeralStorage": {
      "Size": number
   },
   "FileSystemConfigs": [
      {
         "Arn": "string",
         "LocalMountPath": "string",
         "S3FilesConfig": {
            "DirectS3Read": "string"
         }
      }
   ],
   "FunctionArn": "string",
   "FunctionName": "string",
   "Handler": "string",
   "ImageConfigResponse": {
      "Error": {
         "ErrorCode": "string",
         "Message": "string"
      },
      "ImageConfig": {
         "Command": [ "string" ],
         "EntryPoint": [ "string" ],
         "WorkingDirectory": "string"
      }
   },
   "KMSKeyArn": "string",
   "LastModified": "string",
   "LastUpdateStatus": "string",
   "LastUpdateStatusReason": "string",
   "LastUpdateStatusReasonCode": "string",
   "Layers": [
      {
         "Arn": "string",
         "CodeSize": number,
         "SigningJobArn": "string",
         "SigningProfileVersionArn": "string"
      }
   ],
   "LoggingConfig": {
      "ApplicationLogLevel": "string",
      "LogFormat": "string",
      "LogGroup": "string",
      "SystemLogLevel": "string"
   },
   "MasterArn": "string",
   "MemorySize": number,
   "PackageType": "string",
   "RevisionId": "string",
   "Role": "string",
   "Runtime": "string",
   "RuntimeVersionConfig": {
      "Error": {
         "ErrorCode": "string",
         "Message": "string"
      },
      "RuntimeVersionArn": "string"
   },
   "SigningJobArn": "string",
   "SigningProfileVersionArn": "string",
   "SnapStart": {
      "ApplyOn": "string",
      "OptimizationStatus": "string"
   },
   "State": "string",
   "StateReason": "string",
   "StateReasonCode": "string",
   "TenancyConfig": {
      "TenantIsolationMode": "string"
   },
   "Timeout": number,
   "TracingConfig": {
      "Mode": "string"
   },
   "Version": "string",
   "VpcConfig": {
      "Ipv6AllowedForDualStack": boolean,
      "SecurityGroupIds": [ "string" ],
      "SubnetIds": [ "string" ],
      "VpcId": "string"
   }
}
```

## Response Elements
<a name="API_CreateFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Architectures](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-Architectures"></a>
The instruction set architecture that the function supports. Architecture is a string array with one of the valid values. The default architecture value is `x86_64`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `x86_64 | arm64`

 ** [CapacityProviderConfig](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-CapacityProviderConfig"></a>
Configuration for the capacity provider that manages compute resources for Lambda functions.
Type: [CapacityProviderConfig](API_CapacityProviderConfig.md) object

 ** [CodeSha256](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-CodeSha256"></a>
The SHA256 hash of the function's deployment package.
Type: String

 ** [CodeSize](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-CodeSize"></a>
The size of the function's deployment package, in bytes.
Type: Long

 ** [ConfigSha256](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-ConfigSha256"></a>
The SHA256 hash of the function configuration.
Type: String

 ** [DeadLetterConfig](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-DeadLetterConfig"></a>
The function's dead letter queue.
Type: [DeadLetterConfig](API_DeadLetterConfig.md) object

 ** [Description](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-Description"></a>
The function's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [DurableConfig](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-DurableConfig"></a>
The function's durable execution configuration settings, if the function is configured for durability.
Type: [DurableConfig](API_DurableConfig.md) object

 ** [Environment](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-Environment"></a>
The function's [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html). Omitted from AWS CloudTrail logs.
Type: [EnvironmentResponse](API_EnvironmentResponse.md) object

 ** [EphemeralStorage](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-EphemeralStorage"></a>
The size of the function's `/tmp` directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see [Configuring ephemeral storage (console)](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage).
Type: [EphemeralStorage](API_EphemeralStorage.md) object

 ** [FileSystemConfigs](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-FileSystemConfigs"></a>
Connection settings for an [Amazon EFS file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html) or an [Amazon S3 file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html).
Type: Array of [FileSystemConfig](API_FileSystemConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [FunctionArn](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-FunctionArn"></a>
The function's Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`

 ** [FunctionName](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-FunctionName"></a>
The name of the function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`

 ** [Handler](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-Handler"></a>
The function that Lambda calls to begin running your function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[^\s]+`

 ** [ImageConfigResponse](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-ImageConfigResponse"></a>
The function's image configuration values.
Type: [ImageConfigResponse](API_ImageConfigResponse.md) object

 ** [KMSKeyArn](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-KMSKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt the following resources:
+ The function's [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption).
+ The function's [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html) snapshots.
+ When used with `SourceKMSKeyArn`, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see [ Specifying a customer managed key for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption).
+ The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see [Function lifecycle](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle).
If you don't provide a customer managed key, Lambda uses an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) or an [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk).
Type: String
Pattern: `(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()`

 ** [LastModified](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-LastModified"></a>
The date and time that the function was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: String

 ** [LastUpdateStatus](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-LastUpdateStatus"></a>
The status of the last update that was performed on the function. This is first set to `Successful` after function creation completes.
Type: String
Valid Values: `Successful | Failed | InProgress`

 ** [LastUpdateStatusReason](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-LastUpdateStatusReason"></a>
The reason for the last update that was performed on the function.
Type: String

 ** [LastUpdateStatusReasonCode](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-LastUpdateStatusReasonCode"></a>
The reason code for the last update that was performed on the function.
Type: String
Valid Values: `EniLimitExceeded | InsufficientRolePermissions | InvalidConfiguration | InternalError | SubnetOutOfIPAddresses | InvalidSubnet | InvalidSecurityGroup | ImageDeleted | ImageAccessDenied | InvalidImage | KMSKeyAccessDenied | KMSKeyNotFound | InvalidStateKMSKey | DisabledKMSKey | EFSIOError | EFSMountConnectivityError | EFSMountFailure | EFSMountTimeout | InvalidRuntime | InvalidZipFileException | FunctionError | VcpuLimitExceeded | CapacityProviderScalingLimitExceeded | InsufficientCapacity | EC2RequestLimitExceeded | FunctionError.InitTimeout | FunctionError.RuntimeInitError | FunctionError.ExtensionInitError | FunctionError.InvalidEntryPoint | FunctionError.InvalidWorkingDirectory | FunctionError.PermissionDenied | FunctionError.TooManyExtensions | FunctionError.InitResourceExhausted | DisallowedByVpcEncryptionControl | DependencyError`

 ** [Layers](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-Layers"></a>
The function's [layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).
Type: Array of [Layer](API_Layer.md) objects

 ** [LoggingConfig](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-LoggingConfig"></a>
The function's Amazon CloudWatch Logs configuration settings.
Type: [LoggingConfig](API_LoggingConfig.md) object

 ** [MasterArn](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-MasterArn"></a>
For Lambda@Edge functions, the ARN of the main function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`

 ** [MemorySize](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-MemorySize"></a>
The amount of memory available to the function at runtime.
Type: Integer
Valid Range: Minimum value of 128. Maximum value of 32768.

 ** [PackageType](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-PackageType"></a>
The type of deployment package. Set to `Image` for container image and set `Zip` for .zip file archive.
Type: String
Valid Values: `Zip | Image`

 ** [RevisionId](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-RevisionId"></a>
The latest updated revision of the function or alias.
Type: String

 ** [Role](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-Role"></a>
The function's execution role.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [Runtime](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-Runtime"></a>
The identifier of the function's [ runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.
The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels).
For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported).
Type: String
Valid Values: `nodejs | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs10.x | nodejs12.x | nodejs14.x | nodejs16.x | java8 | java8.al2 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | python3.9 | dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | dotnetcore3.1 | dotnet6 | dotnet8 | nodejs4.3-edge | go1.x | ruby2.5 | ruby2.7 | provided | provided.al2 | nodejs18.x | python3.10 | java17 | ruby3.2 | ruby3.3 | ruby3.4 | python3.11 | nodejs20.x | provided.al2023 | python3.12 | java21 | python3.13 | nodejs22.x | nodejs24.x | python3.14 | java25 | dotnet10 | ruby4.0`

 ** [RuntimeVersionConfig](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-RuntimeVersionConfig"></a>
The ARN of the runtime and any errors that occured.
Type: [RuntimeVersionConfig](API_RuntimeVersionConfig.md) object

 ** [SigningJobArn](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-SigningJobArn"></a>
The ARN of the signing job.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

 ** [SigningProfileVersionArn](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-SigningProfileVersionArn"></a>
The ARN of the signing profile version.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

 ** [SnapStart](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-SnapStart"></a>
Set `ApplyOn` to `PublishedVersions` to create a snapshot of the initialized execution environment when you publish a function version. For more information, see [Improving startup performance with Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html).
Type: [SnapStartResponse](API_SnapStartResponse.md) object

 ** [State](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-State"></a>
The current state of the function. When the state is `Inactive`, you can reactivate the function by invoking it.
Type: String
Valid Values: `Pending | Active | Inactive | Failed | Deactivating | Deactivated | ActiveNonInvocable | Deleting`

 ** [StateReason](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-StateReason"></a>
The reason for the function's current state.
Type: String

 ** [StateReasonCode](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-StateReasonCode"></a>
The reason code for the function's current state. When the code is `Creating`, you can't invoke or modify the function.
Type: String
Valid Values: `Idle | Creating | Restoring | EniLimitExceeded | InsufficientRolePermissions | InvalidConfiguration | InternalError | SubnetOutOfIPAddresses | InvalidSubnet | InvalidSecurityGroup | ImageDeleted | ImageAccessDenied | InvalidImage | KMSKeyAccessDenied | KMSKeyNotFound | InvalidStateKMSKey | DisabledKMSKey | EFSIOError | EFSMountConnectivityError | EFSMountFailure | EFSMountTimeout | InvalidRuntime | InvalidZipFileException | FunctionError | DrainingDurableExecutions | VcpuLimitExceeded | CapacityProviderScalingLimitExceeded | InsufficientCapacity | EC2RequestLimitExceeded | FunctionError.InitTimeout | FunctionError.RuntimeInitError | FunctionError.ExtensionInitError | FunctionError.InvalidEntryPoint | FunctionError.InvalidWorkingDirectory | FunctionError.PermissionDenied | FunctionError.TooManyExtensions | FunctionError.InitResourceExhausted | DisallowedByVpcEncryptionControl | DependencyError`

 ** [TenancyConfig](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-TenancyConfig"></a>
The function's tenant isolation configuration settings. Determines whether the Lambda function runs on a shared or dedicated infrastructure per unique tenant.
Type: [TenancyConfig](API_TenancyConfig.md) object

 ** [Timeout](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-Timeout"></a>
The amount of time in seconds that Lambda allows a function to run before stopping it.
Type: Integer
Valid Range: Minimum value of 1.

 ** [TracingConfig](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-TracingConfig"></a>
The function's AWS X-Ray tracing configuration.
Type: [TracingConfigResponse](API_TracingConfigResponse.md) object

 ** [Version](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-Version"></a>
The version of the Lambda function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(\$LATEST|[0-9]+)`

 ** [VpcConfig](#API_CreateFunction_ResponseSyntax) **   <a name="lambda-CreateFunction-response-VpcConfig"></a>
The function's networking configuration.
Type: [VpcConfigResponse](API_VpcConfigResponse.md) object

## Errors
<a name="API_CreateFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CodeSigningConfigNotFoundException **
The specified code signing configuration does not exist.
HTTP Status Code: 404

 ** CodeStorageExceededException **
Your AWS account has exceeded its maximum total code size. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).
 ** Type **
The exception type.
HTTP Status Code: 400

 ** CodeVerificationFailedException **
The code signature failed one or more of the validation checks for signature mismatch or expiry, and the code signing policy is set to ENFORCE. Lambda blocks the deployment.
HTTP Status Code: 400

 ** FunctionVersionsPerCapacityProviderLimitExceededException **
The maximum number of function versions that can be associated with a single capacity provider has been exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).
 ** Type **
The exception type.
HTTP Status Code: 400

 ** InvalidCodeSignatureException **
The code signature failed the integrity check. If the integrity check fails, then Lambda blocks deployment, even if the code signing policy is set to WARN.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceConflictException **
The resource already exists, or another operation is in progress.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_CreateFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/CreateFunction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/CreateFunction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/CreateFunction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/CreateFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/CreateFunction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/CreateFunction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/CreateFunction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/CreateFunction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/CreateFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/CreateFunction)
