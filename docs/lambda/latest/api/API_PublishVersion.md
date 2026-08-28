---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_PublishVersion.html
---

# PublishVersion
<a name="API_PublishVersion"></a>

Creates a [version](https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html) from the current code and configuration of a function. Use versions to create a snapshot of your function code and configuration that doesn't change.

 AWS Lambda doesn't publish a version if the function's configuration and code haven't changed since the last version. Use [UpdateFunctionCode](API_UpdateFunctionCode.md) or [UpdateFunctionConfiguration](API_UpdateFunctionConfiguration.md) to update the function before publishing a version.

Clients can invoke versions directly or with an alias. To create an alias, use [CreateAlias](API_CreateAlias.md).

## Request Syntax
<a name="API_PublishVersion_RequestSyntax"></a>

```
POST /2015-03-31/functions/{{FunctionName}}/versions HTTP/1.1
Content-type: application/json

{
   "CodeSha256": "{{string}}",
   "Description": "{{string}}",
   "PublishTo": "{{string}}",
   "RevisionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PublishVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_PublishVersion_RequestSyntax) **   <a name="lambda-PublishVersion-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** - `MyFunction`.
+  **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`.
+  **Partial ARN** - `123456789012:function:MyFunction`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: Yes

## Request Body
<a name="API_PublishVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CodeSha256](#API_PublishVersion_RequestSyntax) **   <a name="lambda-PublishVersion-request-CodeSha256"></a>
Only publish a version if the hash value matches the value that's specified. Use this option to avoid publishing a version if the function code has changed since you last updated it. You can get the hash for the version that you uploaded from the output of [UpdateFunctionCode](API_UpdateFunctionCode.md).
Type: String
Required: No

 ** [Description](#API_PublishVersion_RequestSyntax) **   <a name="lambda-PublishVersion-request-Description"></a>
A description for the version to override the description in the function configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [PublishTo](#API_PublishVersion_RequestSyntax) **   <a name="lambda-PublishVersion-request-PublishTo"></a>
Specifies where to publish the function version or configuration.
Type: String
Valid Values: `LATEST_PUBLISHED`
Required: No

 ** [RevisionId](#API_PublishVersion_RequestSyntax) **   <a name="lambda-PublishVersion-request-RevisionId"></a>
Only update the function if the revision ID matches the ID that's specified. Use this option to avoid publishing a version if the function configuration has changed since you last updated it.
Type: String
Required: No

## Response Syntax
<a name="API_PublishVersion_ResponseSyntax"></a>

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
         "LocalMountPath": "string"
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
<a name="API_PublishVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Architectures](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-Architectures"></a>
The instruction set architecture that the function supports. Architecture is a string array with one of the valid values. The default architecture value is `x86_64`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `x86_64 | arm64`

 ** [CapacityProviderConfig](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-CapacityProviderConfig"></a>
Configuration for the capacity provider that manages compute resources for Lambda functions.
Type: [CapacityProviderConfig](API_CapacityProviderConfig.md) object

 ** [CodeSha256](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-CodeSha256"></a>
The SHA256 hash of the function's deployment package.
Type: String

 ** [CodeSize](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-CodeSize"></a>
The size of the function's deployment package, in bytes.
Type: Long

 ** [ConfigSha256](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-ConfigSha256"></a>
The SHA256 hash of the function configuration.
Type: String

 ** [DeadLetterConfig](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-DeadLetterConfig"></a>
The function's dead letter queue.
Type: [DeadLetterConfig](API_DeadLetterConfig.md) object

 ** [Description](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-Description"></a>
The function's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [DurableConfig](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-DurableConfig"></a>
The function's durable execution configuration settings, if the function is configured for durability.
Type: [DurableConfig](API_DurableConfig.md) object

 ** [Environment](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-Environment"></a>
The function's [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html). Omitted from AWS CloudTrail logs.
Type: [EnvironmentResponse](API_EnvironmentResponse.md) object

 ** [EphemeralStorage](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-EphemeralStorage"></a>
The size of the function's `/tmp` directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see [Configuring ephemeral storage (console)](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage).
Type: [EphemeralStorage](API_EphemeralStorage.md) object

 ** [FileSystemConfigs](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-FileSystemConfigs"></a>
Connection settings for an [Amazon EFS file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html) or an [Amazon S3 Files file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html).
Type: Array of [FileSystemConfig](API_FileSystemConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [FunctionArn](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-FunctionArn"></a>
The function's Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`

 ** [FunctionName](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-FunctionName"></a>
The name of the function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`

 ** [Handler](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-Handler"></a>
The function that Lambda calls to begin running your function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[^\s]+`

 ** [ImageConfigResponse](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-ImageConfigResponse"></a>
The function's image configuration values.
Type: [ImageConfigResponse](API_ImageConfigResponse.md) object

 ** [KMSKeyArn](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-KMSKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt the following resources:
+ The function's [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption).
+ The function's [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html) snapshots.
+ When used with `SourceKMSKeyArn`, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see [ Specifying a customer managed key for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption).
+ The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see [Function lifecycle](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle).
If you don't provide a customer managed key, Lambda uses an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) or an [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk).
Type: String
Pattern: `(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()`

 ** [LastModified](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-LastModified"></a>
The date and time that the function was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: String

 ** [LastUpdateStatus](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-LastUpdateStatus"></a>
The status of the last update that was performed on the function. This is first set to `Successful` after function creation completes.
Type: String
Valid Values: `Successful | Failed | InProgress`

 ** [LastUpdateStatusReason](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-LastUpdateStatusReason"></a>
The reason for the last update that was performed on the function.
Type: String

 ** [LastUpdateStatusReasonCode](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-LastUpdateStatusReasonCode"></a>
The reason code for the last update that was performed on the function.
Type: String
Valid Values: `EniLimitExceeded | InsufficientRolePermissions | InvalidConfiguration | InternalError | SubnetOutOfIPAddresses | InvalidSubnet | InvalidSecurityGroup | ImageDeleted | ImageAccessDenied | InvalidImage | KMSKeyAccessDenied | KMSKeyNotFound | InvalidStateKMSKey | DisabledKMSKey | EFSIOError | EFSMountConnectivityError | EFSMountFailure | EFSMountTimeout | InvalidRuntime | InvalidZipFileException | FunctionError | VcpuLimitExceeded | CapacityProviderScalingLimitExceeded | InsufficientCapacity | EC2RequestLimitExceeded | FunctionError.InitTimeout | FunctionError.RuntimeInitError | FunctionError.ExtensionInitError | FunctionError.InvalidEntryPoint | FunctionError.InvalidWorkingDirectory | FunctionError.PermissionDenied | FunctionError.TooManyExtensions | FunctionError.InitResourceExhausted | DisallowedByVpcEncryptionControl | DependencyError`

 ** [Layers](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-Layers"></a>
The function's [layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).
Type: Array of [Layer](API_Layer.md) objects

 ** [LoggingConfig](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-LoggingConfig"></a>
The function's Amazon CloudWatch Logs configuration settings.
Type: [LoggingConfig](API_LoggingConfig.md) object

 ** [MasterArn](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-MasterArn"></a>
For Lambda@Edge functions, the ARN of the main function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`

 ** [MemorySize](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-MemorySize"></a>
The amount of memory available to the function at runtime.
Type: Integer
Valid Range: Minimum value of 128. Maximum value of 32768.

 ** [PackageType](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-PackageType"></a>
The type of deployment package. Set to `Image` for container image and set `Zip` for .zip file archive.
Type: String
Valid Values: `Zip | Image`

 ** [RevisionId](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-RevisionId"></a>
The latest updated revision of the function or alias.
Type: String

 ** [Role](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-Role"></a>
The function's execution role.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [Runtime](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-Runtime"></a>
The identifier of the function's [ runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.
The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels).
For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported).
Type: String
Valid Values: `nodejs | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs10.x | nodejs12.x | nodejs14.x | nodejs16.x | java8 | java8.al2 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | python3.9 | dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | dotnetcore3.1 | dotnet6 | dotnet8 | nodejs4.3-edge | go1.x | ruby2.5 | ruby2.7 | provided | provided.al2 | nodejs18.x | python3.10 | java17 | ruby3.2 | ruby3.3 | ruby3.4 | python3.11 | nodejs20.x | provided.al2023 | python3.12 | java21 | python3.13 | nodejs22.x | nodejs24.x | python3.14 | java25 | dotnet10 | ruby4.0`

 ** [RuntimeVersionConfig](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-RuntimeVersionConfig"></a>
The ARN of the runtime and any errors that occured.
Type: [RuntimeVersionConfig](API_RuntimeVersionConfig.md) object

 ** [SigningJobArn](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-SigningJobArn"></a>
The ARN of the signing job.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

 ** [SigningProfileVersionArn](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-SigningProfileVersionArn"></a>
The ARN of the signing profile version.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`

 ** [SnapStart](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-SnapStart"></a>
Set `ApplyOn` to `PublishedVersions` to create a snapshot of the initialized execution environment when you publish a function version. For more information, see [Improving startup performance with Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html).
Type: [SnapStartResponse](API_SnapStartResponse.md) object

 ** [State](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-State"></a>
The current state of the function. When the state is `Inactive`, you can reactivate the function by invoking it.
Type: String
Valid Values: `Pending | Active | Inactive | Failed | Deactivating | Deactivated | ActiveNonInvocable | Deleting`

 ** [StateReason](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-StateReason"></a>
The reason for the function's current state.
Type: String

 ** [StateReasonCode](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-StateReasonCode"></a>
The reason code for the function's current state. When the code is `Creating`, you can't invoke or modify the function.
Type: String
Valid Values: `Idle | Creating | Restoring | EniLimitExceeded | InsufficientRolePermissions | InvalidConfiguration | InternalError | SubnetOutOfIPAddresses | InvalidSubnet | InvalidSecurityGroup | ImageDeleted | ImageAccessDenied | InvalidImage | KMSKeyAccessDenied | KMSKeyNotFound | InvalidStateKMSKey | DisabledKMSKey | EFSIOError | EFSMountConnectivityError | EFSMountFailure | EFSMountTimeout | InvalidRuntime | InvalidZipFileException | FunctionError | DrainingDurableExecutions | VcpuLimitExceeded | CapacityProviderScalingLimitExceeded | InsufficientCapacity | EC2RequestLimitExceeded | FunctionError.InitTimeout | FunctionError.RuntimeInitError | FunctionError.ExtensionInitError | FunctionError.InvalidEntryPoint | FunctionError.InvalidWorkingDirectory | FunctionError.PermissionDenied | FunctionError.TooManyExtensions | FunctionError.InitResourceExhausted | DisallowedByVpcEncryptionControl | DependencyError`

 ** [TenancyConfig](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-TenancyConfig"></a>
The function's tenant isolation configuration settings. Determines whether the Lambda function runs on a shared or dedicated infrastructure per unique tenant.
Type: [TenancyConfig](API_TenancyConfig.md) object

 ** [Timeout](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-Timeout"></a>
The amount of time in seconds that Lambda allows a function to run before stopping it.
Type: Integer
Valid Range: Minimum value of 1.

 ** [TracingConfig](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-TracingConfig"></a>
The function's AWS X-Ray tracing configuration.
Type: [TracingConfigResponse](API_TracingConfigResponse.md) object

 ** [Version](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-Version"></a>
The version of the Lambda function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(\$LATEST|[0-9]+)`

 ** [VpcConfig](#API_PublishVersion_ResponseSyntax) **   <a name="lambda-PublishVersion-response-VpcConfig"></a>
The function's networking configuration.
Type: [VpcConfigResponse](API_VpcConfigResponse.md) object

## Errors
<a name="API_PublishVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CodeStorageExceededException **
Your AWS account has exceeded its maximum total code size. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).
 ** Type **
The exception type.
HTTP Status Code: 400

 ** FunctionVersionsPerCapacityProviderLimitExceededException **
The maximum number of function versions that can be associated with a single capacity provider has been exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).
 ** Type **
The exception type.
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
<a name="API_PublishVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/PublishVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/PublishVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/PublishVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/PublishVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/PublishVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/PublishVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/PublishVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/PublishVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/PublishVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/PublishVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
