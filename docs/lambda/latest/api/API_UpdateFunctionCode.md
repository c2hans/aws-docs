---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionCode.html
---

# UpdateFunctionCode
<a name="API_UpdateFunctionCode"></a>

Updates a Lambda function's code. If code signing is enabled for the function, the code package must be signed by a trusted publisher. For more information, see [Configuring code signing for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html).

If the function's package type is `Image`, then you must specify the code package in `ImageUri` as the URI of a [container image](https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html) in the Amazon ECR registry.

If the function's package type is `Zip`, then you must specify the deployment package as a [.zip file archive](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html#gettingstarted-package-zip). Enter the Amazon S3 bucket and key of the code .zip file location. You can also provide the function code inline using the `ZipFile` field.

The code in the deployment package must be compatible with the target instruction set architecture of the function (`x86-64` or `arm64`).

The function's code is locked when you publish a version. You can't modify the code of a published version, only the unpublished version.

**Note**
For a function defined as a container image, Lambda resolves the image tag to an image digest. In Amazon ECR, if you update the image tag to a new image, Lambda does not automatically update the function.

## Request Syntax
<a name="API_UpdateFunctionCode_RequestSyntax"></a>

```
PUT /2015-03-31/functions/{{FunctionName}}/code HTTP/1.1
Content-type: application/json

{
   "Architectures": [ "{{string}}" ],
   "DryRun": {{boolean}},
   "ImageUri": "{{string}}",
   "Publish": {{boolean}},
   "PublishTo": "{{string}}",
   "RevisionId": "{{string}}",
   "S3Bucket": "{{string}}",
   "S3Key": "{{string}}",
   "S3ObjectStorageMode": "{{string}}",
   "S3ObjectVersion": "{{string}}",
   "SourceKMSKeyArn": "{{string}}",
   "ZipFile": {{blob}}
}
```

## URI Request Parameters
<a name="API_UpdateFunctionCode_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_UpdateFunctionCode_RequestSyntax) **   <a name="lambda-UpdateFunctionCode-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** – `my-function`.
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: Yes

## Request Body
<a name="API_UpdateFunctionCode_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Architectures](#API_UpdateFunctionCode_RequestSyntax) **   <a name="lambda-UpdateFunctionCode-request-Architectures"></a>
The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86\_64). The default value is `x86_64`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `x86_64 | arm64`
Required: No

 ** [DryRun](#API_UpdateFunctionCode_RequestSyntax) **   <a name="lambda-UpdateFunctionCode-request-DryRun"></a>
Set to true to validate the request parameters and access permissions without modifying the function code.
Type: Boolean
Required: No

 ** [ImageUri](#API_UpdateFunctionCode_RequestSyntax) **   <a name="lambda-UpdateFunctionCode-request-ImageUri"></a>
URI of a container image in the Amazon ECR registry. Do not use for a function defined with a .zip file archive.
Type: String
Required: No

 ** [Publish](#API_UpdateFunctionCode_RequestSyntax) **   <a name="lambda-UpdateFunctionCode-request-Publish"></a>
Set to true to publish a new version of the function after updating the code. This has the same effect as calling [PublishVersion](API_PublishVersion.md) separately.
Type: Boolean
Required: No

 ** [PublishTo](#API_UpdateFunctionCode_RequestSyntax) **   <a name="lambda-UpdateFunctionCode-request-PublishTo"></a>
Specifies where to publish the function version or configuration.
Type: String
Valid Values: `LATEST_PUBLISHED`
Required: No

 ** [RevisionId](#API_UpdateFunctionCode_RequestSyntax) **   <a name="lambda-UpdateFunctionCode-request-RevisionId"></a>
Update the function only if the revision ID matches the ID that's specified. Use this option to avoid modifying a function that has changed since you last read it.
Type: String
Required: No

 ** [S3Bucket](#API_UpdateFunctionCode_RequestSyntax) **   <a name="lambda-UpdateFunctionCode-request-S3Bucket"></a>
An Amazon S3 bucket in the same AWS Region as your function. The bucket can be in a different AWS account. Use only with a function defined with a .zip file archive deployment package.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[0-9A-Za-z\.\-_]*(?<!\.)`
Required: No

 ** [S3Key](#API_UpdateFunctionCode_RequestSyntax) **   <a name="lambda-UpdateFunctionCode-request-S3Key"></a>
The Amazon S3 key of the deployment package. Use only with a function defined with a .zip file archive deployment package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [S3ObjectStorageMode](#API_UpdateFunctionCode_RequestSyntax) **   <a name="lambda-UpdateFunctionCode-request-S3ObjectStorageMode"></a>
Specifies how the deployment package is stored. Valid values:
+  `COPY` (default) – Uploads a copy of your deployment package to Lambda.
+  `REFERENCE` – Lambda references the deployment package from the specified Amazon S3 bucket.
Type: String
Valid Values: `COPY | REFERENCE`
Required: No

 ** [S3ObjectVersion](#API_UpdateFunctionCode_RequestSyntax) **   <a name="lambda-UpdateFunctionCode-request-S3ObjectVersion"></a>
For versioned objects, the version of the deployment package object to use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [SourceKMSKeyArn](#API_UpdateFunctionCode_RequestSyntax) **   <a name="lambda-UpdateFunctionCode-request-SourceKMSKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt your function's .zip deployment package. If you don't provide a customer managed key, Lambda uses an AWS managed key.
Type: String
Pattern: `(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()`
Required: No

 ** [ZipFile](#API_UpdateFunctionCode_RequestSyntax) **   <a name="lambda-UpdateFunctionCode-request-ZipFile"></a>
The base64-encoded contents of the deployment package. AWS SDK and AWS CLI clients handle the encoding for you. Use only with a function defined with a .zip file archive deployment package.
Type: Base64-encoded binary data object
Required: No

## Response Syntax
<a name="API_UpdateFunctionCode_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateFunctionCode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Architectures](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-Architectures"></a>
The instruction set architecture that the function supports. Architecture is a string array with one of the valid values. The default architecture value is `x86_64`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `x86_64 | arm64`

 ** [CapacityProviderConfig](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-CapacityProviderConfig"></a>
Configuration for the capacity provider that manages compute resources for Lambda functions.
Type: [CapacityProviderConfig](API_CapacityProviderConfig.md) object

 ** [CodeSha256](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-CodeSha256"></a>
The SHA256 hash of the function's deployment package.
Type: String

 ** [CodeSize](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-CodeSize"></a>
The size of the function's deployment package, in bytes.
Type: Long

 ** [ConfigSha256](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-ConfigSha256"></a>
The SHA256 hash of the function configuration.
Type: String

 ** [DeadLetterConfig](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-DeadLetterConfig"></a>
The function's dead letter queue.
Type: [DeadLetterConfig](API_DeadLetterConfig.md) object

 ** [Description](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-Description"></a>
The function's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [DurableConfig](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-DurableConfig"></a>
The function's durable execution configuration settings, if the function is configured for durability.
Type: [DurableConfig](API_DurableConfig.md) object

 ** [Environment](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-Environment"></a>
The function's [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html). Omitted from AWS CloudTrail logs.
Type: [EnvironmentResponse](API_EnvironmentResponse.md) object

 ** [EphemeralStorage](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-EphemeralStorage"></a>
The size of the function's `/tmp` directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see [Configuring ephemeral storage (console)](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage).
Type: [EphemeralStorage](API_EphemeralStorage.md) object

 ** [FileSystemConfigs](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-FileSystemConfigs"></a>
Connection settings for an [Amazon EFS file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html) or an [Amazon S3 file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html).
Type: Array of [FileSystemConfig](API_FileSystemConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [FunctionArn](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-FunctionArn"></a>
The function's Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`

 ** [FunctionName](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-FunctionName"></a>
The name of the function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`

 ** [Handler](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-Handler"></a>
The function that Lambda calls to begin running your function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[^\s]+`

 ** [ImageConfigResponse](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-ImageConfigResponse"></a>
The function's image configuration values.
Type: [ImageConfigResponse](API_ImageConfigResponse.md) object

 ** [KMSKeyArn](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-KMSKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt the following resources:
+ The function's [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption).
+ The function's [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html) snapshots.
+ When used with `SourceKMSKeyArn`, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see [ Specifying a customer managed key for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption).
+ The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see [Function lifecycle](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle).
If you don't provide a customer managed key, Lambda uses an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) or an [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk).
Type: String
Pattern: `(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()`

 ** [LastModified](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-LastModified"></a>
The date and time that the function was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: String

 ** [LastUpdateStatus](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-LastUpdateStatus"></a>
The status of the last update that was performed on the function. This is first set to `Successful` after function creation completes.
Type: String
Valid Values: `Successful | Failed | InProgress`

 ** [LastUpdateStatusReason](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-LastUpdateStatusReason"></a>
The reason for the last update that was performed on the function.
Type: String

 ** [LastUpdateStatusReasonCode](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-LastUpdateStatusReasonCode"></a>
The reason code for the last update that was performed on the function.
Type: String
Valid Values: `EniLimitExceeded | InsufficientRolePermissions | InvalidConfiguration | InternalError | SubnetOutOfIPAddresses | InvalidSubnet | InvalidSecurityGroup | ImageDeleted | ImageAccessDenied | InvalidImage | KMSKeyAccessDenied | KMSKeyNotFound | InvalidStateKMSKey | DisabledKMSKey | EFSIOError | EFSMountConnectivityError | EFSMountFailure | EFSMountTimeout | InvalidRuntime | InvalidZipFileException | FunctionError | VcpuLimitExceeded | CapacityProviderScalingLimitExceeded | InsufficientCapacity | EC2RequestLimitExceeded | FunctionError.InitTimeout | FunctionError.RuntimeInitError | FunctionError.ExtensionInitError | FunctionError.InvalidEntryPoint | FunctionError.InvalidWorkingDirectory | FunctionError.PermissionDenied | FunctionError.TooManyExtensions | FunctionError.InitResourceExhausted | DisallowedByVpcEncryptionControl | DependencyError`

 ** [Layers](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-Layers"></a>
The function's [layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).
Type: Array of [Layer](API_Layer.md) objects

 ** [LoggingConfig](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-LoggingConfig"></a>
The function's Amazon CloudWatch Logs configuration settings.
Type: [LoggingConfig](API_LoggingConfig.md) object

 ** [MasterArn](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-MasterArn"></a>
For Lambda@Edge functions, the ARN of the main function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`

 ** [MemorySize](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-MemorySize"></a>
The amount of memory available to the function at runtime.
Type: Integer
Valid Range: Minimum value of 128. Maximum value of 32768.

 ** [PackageType](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-PackageType"></a>
The type of deployment package. Set to `Image` for container image and set `Zip` for .zip file archive.
Type: String
Valid Values: `Zip | Image`

 ** [RevisionId](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-RevisionId"></a>
The latest updated revision of the function or alias.
Type: String

 ** [Role](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-Role"></a>
The function's execution role.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [Runtime](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-Runtime"></a>
The identifier of the function's [ runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.
The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels).
For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported).
Type: String
Valid Values: `nodejs | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs10.x | nodejs12.x | nodejs14.x | nodejs16.x | java8 | java8.al2 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | python3.9 | dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | dotnetcore3.1 | dotnet6 | dotnet8 | nodejs4.3-edge | go1.x | ruby2.5 | ruby2.7 | provided | provided.al2 | nodejs18.x | python3.10 | java17 | ruby3.2 | ruby3.3 | ruby3.4 | python3.11 | nodejs20.x | provided.al2023 | python3.12 | java21 | python3.13 | nodejs22.x | nodejs24.x | python3.14 | java25 | dotnet10 | ruby4.0`

 ** [RuntimeVersionConfig](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-RuntimeVersionConfig"></a>
The ARN of the runtime and any errors that occured.
Type: [RuntimeVersionConfig](API_RuntimeVersionConfig.md) object

 ** [SigningJobArn](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-SigningJobArn"></a>
The ARN of the signing job.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

 ** [SigningProfileVersionArn](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-SigningProfileVersionArn"></a>
The ARN of the signing profile version.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

 ** [SnapStart](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-SnapStart"></a>
Set `ApplyOn` to `PublishedVersions` to create a snapshot of the initialized execution environment when you publish a function version. For more information, see [Improving startup performance with Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html).
Type: [SnapStartResponse](API_SnapStartResponse.md) object

 ** [State](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-State"></a>
The current state of the function. When the state is `Inactive`, you can reactivate the function by invoking it.
Type: String
Valid Values: `Pending | Active | Inactive | Failed | Deactivating | Deactivated | ActiveNonInvocable | Deleting`

 ** [StateReason](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-StateReason"></a>
The reason for the function's current state.
Type: String

 ** [StateReasonCode](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-StateReasonCode"></a>
The reason code for the function's current state. When the code is `Creating`, you can't invoke or modify the function.
Type: String
Valid Values: `Idle | Creating | Restoring | EniLimitExceeded | InsufficientRolePermissions | InvalidConfiguration | InternalError | SubnetOutOfIPAddresses | InvalidSubnet | InvalidSecurityGroup | ImageDeleted | ImageAccessDenied | InvalidImage | KMSKeyAccessDenied | KMSKeyNotFound | InvalidStateKMSKey | DisabledKMSKey | EFSIOError | EFSMountConnectivityError | EFSMountFailure | EFSMountTimeout | InvalidRuntime | InvalidZipFileException | FunctionError | DrainingDurableExecutions | VcpuLimitExceeded | CapacityProviderScalingLimitExceeded | InsufficientCapacity | EC2RequestLimitExceeded | FunctionError.InitTimeout | FunctionError.RuntimeInitError | FunctionError.ExtensionInitError | FunctionError.InvalidEntryPoint | FunctionError.InvalidWorkingDirectory | FunctionError.PermissionDenied | FunctionError.TooManyExtensions | FunctionError.InitResourceExhausted | DisallowedByVpcEncryptionControl | DependencyError`

 ** [TenancyConfig](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-TenancyConfig"></a>
The function's tenant isolation configuration settings. Determines whether the Lambda function runs on a shared or dedicated infrastructure per unique tenant.
Type: [TenancyConfig](API_TenancyConfig.md) object

 ** [Timeout](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-Timeout"></a>
The amount of time in seconds that Lambda allows a function to run before stopping it.
Type: Integer
Valid Range: Minimum value of 1.

 ** [TracingConfig](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-TracingConfig"></a>
The function's AWS X-Ray tracing configuration.
Type: [TracingConfigResponse](API_TracingConfigResponse.md) object

 ** [Version](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-Version"></a>
The version of the Lambda function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(\$LATEST|[0-9]+)`

 ** [VpcConfig](#API_UpdateFunctionCode_ResponseSyntax) **   <a name="lambda-UpdateFunctionCode-response-VpcConfig"></a>
The function's networking configuration.
Type: [VpcConfigResponse](API_VpcConfigResponse.md) object

## Errors
<a name="API_UpdateFunctionCode_Errors"></a>

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

 ** PreconditionFailedException **
The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.
+  **For AddPermission and RemovePermission API operations:** Call `GetPolicy` to retrieve the latest RevisionId for your resource.
+  **For all other API operations:** Call `GetFunction` or `GetAlias` to retrieve the latest RevisionId for your resource.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 412

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
<a name="API_UpdateFunctionCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/UpdateFunctionCode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/UpdateFunctionCode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/UpdateFunctionCode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/UpdateFunctionCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/UpdateFunctionCode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/UpdateFunctionCode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/UpdateFunctionCode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/UpdateFunctionCode)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/UpdateFunctionCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/UpdateFunctionCode)
