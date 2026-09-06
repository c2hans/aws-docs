---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_FunctionConfiguration.html
---

# FunctionConfiguration
<a name="API_FunctionConfiguration"></a>

Details about a function's configuration.

## Contents
<a name="API_FunctionConfiguration_Contents"></a>

 ** Architectures **   <a name="lambda-Type-FunctionConfiguration-Architectures"></a>
The instruction set architecture that the function supports. Architecture is a string array with one of the valid values. The default architecture value is `x86_64`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `x86_64 | arm64`
Required: No

 ** CapacityProviderConfig **   <a name="lambda-Type-FunctionConfiguration-CapacityProviderConfig"></a>
Configuration for the capacity provider that manages compute resources for Lambda functions.
Type: [CapacityProviderConfig](API_CapacityProviderConfig.md) object
Required: No

 ** CodeSha256 **   <a name="lambda-Type-FunctionConfiguration-CodeSha256"></a>
The SHA256 hash of the function's deployment package.
Type: String
Required: No

 ** CodeSize **   <a name="lambda-Type-FunctionConfiguration-CodeSize"></a>
The size of the function's deployment package, in bytes.
Type: Long
Required: No

 ** ConfigSha256 **   <a name="lambda-Type-FunctionConfiguration-ConfigSha256"></a>
The SHA256 hash of the function configuration.
Type: String
Required: No

 ** DeadLetterConfig **   <a name="lambda-Type-FunctionConfiguration-DeadLetterConfig"></a>
The function's dead letter queue.
Type: [DeadLetterConfig](API_DeadLetterConfig.md) object
Required: No

 ** Description **   <a name="lambda-Type-FunctionConfiguration-Description"></a>
The function's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** DurableConfig **   <a name="lambda-Type-FunctionConfiguration-DurableConfig"></a>
The function's durable execution configuration settings, if the function is configured for durability.
Type: [DurableConfig](API_DurableConfig.md) object
Required: No

 ** Environment **   <a name="lambda-Type-FunctionConfiguration-Environment"></a>
The function's [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html). Omitted from AWS CloudTrail logs.
Type: [EnvironmentResponse](API_EnvironmentResponse.md) object
Required: No

 ** EphemeralStorage **   <a name="lambda-Type-FunctionConfiguration-EphemeralStorage"></a>
The size of the function's `/tmp` directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see [Configuring ephemeral storage (console)](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage).
Type: [EphemeralStorage](API_EphemeralStorage.md) object
Required: No

 ** FileSystemConfigs **   <a name="lambda-Type-FunctionConfiguration-FileSystemConfigs"></a>
Connection settings for an [Amazon EFS file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html) or an [Amazon S3 file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html).
Type: Array of [FileSystemConfig](API_FileSystemConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** FunctionArn **   <a name="lambda-Type-FunctionConfiguration-FunctionArn"></a>
The function's Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: No

 ** FunctionName **   <a name="lambda-Type-FunctionConfiguration-FunctionName"></a>
The name of the function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: No

 ** Handler **   <a name="lambda-Type-FunctionConfiguration-Handler"></a>
The function that Lambda calls to begin running your function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[^\s]+`
Required: No

 ** ImageConfigResponse **   <a name="lambda-Type-FunctionConfiguration-ImageConfigResponse"></a>
The function's image configuration values.
Type: [ImageConfigResponse](API_ImageConfigResponse.md) object
Required: No

 ** KMSKeyArn **   <a name="lambda-Type-FunctionConfiguration-KMSKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt the following resources:
+ The function's [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption).
+ The function's [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html) snapshots.
+ When used with `SourceKMSKeyArn`, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see [ Specifying a customer managed key for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption).
+ The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see [Function lifecycle](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle).
If you don't provide a customer managed key, Lambda uses an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) or an [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk).
Type: String
Pattern: `(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()`
Required: No

 ** LastModified **   <a name="lambda-Type-FunctionConfiguration-LastModified"></a>
The date and time that the function was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: String
Required: No

 ** LastUpdateStatus **   <a name="lambda-Type-FunctionConfiguration-LastUpdateStatus"></a>
The status of the last update that was performed on the function. This is first set to `Successful` after function creation completes.
Type: String
Valid Values: `Successful | Failed | InProgress`
Required: No

 ** LastUpdateStatusReason **   <a name="lambda-Type-FunctionConfiguration-LastUpdateStatusReason"></a>
The reason for the last update that was performed on the function.
Type: String
Required: No

 ** LastUpdateStatusReasonCode **   <a name="lambda-Type-FunctionConfiguration-LastUpdateStatusReasonCode"></a>
The reason code for the last update that was performed on the function.
Type: String
Valid Values: `EniLimitExceeded | InsufficientRolePermissions | InvalidConfiguration | InternalError | SubnetOutOfIPAddresses | InvalidSubnet | InvalidSecurityGroup | ImageDeleted | ImageAccessDenied | InvalidImage | KMSKeyAccessDenied | KMSKeyNotFound | InvalidStateKMSKey | DisabledKMSKey | EFSIOError | EFSMountConnectivityError | EFSMountFailure | EFSMountTimeout | InvalidRuntime | InvalidZipFileException | FunctionError | VcpuLimitExceeded | CapacityProviderScalingLimitExceeded | InsufficientCapacity | EC2RequestLimitExceeded | FunctionError.InitTimeout | FunctionError.RuntimeInitError | FunctionError.ExtensionInitError | FunctionError.InvalidEntryPoint | FunctionError.InvalidWorkingDirectory | FunctionError.PermissionDenied | FunctionError.TooManyExtensions | FunctionError.InitResourceExhausted | DisallowedByVpcEncryptionControl | DependencyError`
Required: No

 ** Layers **   <a name="lambda-Type-FunctionConfiguration-Layers"></a>
The function's [layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).
Type: Array of [Layer](API_Layer.md) objects
Required: No

 ** LoggingConfig **   <a name="lambda-Type-FunctionConfiguration-LoggingConfig"></a>
The function's Amazon CloudWatch Logs configuration settings.
Type: [LoggingConfig](API_LoggingConfig.md) object
Required: No

 ** MasterArn **   <a name="lambda-Type-FunctionConfiguration-MasterArn"></a>
For Lambda@Edge functions, the ARN of the main function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: No

 ** MemorySize **   <a name="lambda-Type-FunctionConfiguration-MemorySize"></a>
The amount of memory available to the function at runtime.
Type: Integer
Valid Range: Minimum value of 128. Maximum value of 32768.
Required: No

 ** PackageType **   <a name="lambda-Type-FunctionConfiguration-PackageType"></a>
The type of deployment package. Set to `Image` for container image and set `Zip` for .zip file archive.
Type: String
Valid Values: `Zip | Image`
Required: No

 ** RevisionId **   <a name="lambda-Type-FunctionConfiguration-RevisionId"></a>
The latest updated revision of the function or alias.
Type: String
Required: No

 ** Role **   <a name="lambda-Type-FunctionConfiguration-Role"></a>
The function's execution role.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** Runtime **   <a name="lambda-Type-FunctionConfiguration-Runtime"></a>
The identifier of the function's [ runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.
The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels).
For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported).
Type: String
Valid Values: `nodejs | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs10.x | nodejs12.x | nodejs14.x | nodejs16.x | java8 | java8.al2 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | python3.9 | dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | dotnetcore3.1 | dotnet6 | dotnet8 | nodejs4.3-edge | go1.x | ruby2.5 | ruby2.7 | provided | provided.al2 | nodejs18.x | python3.10 | java17 | ruby3.2 | ruby3.3 | ruby3.4 | python3.11 | nodejs20.x | provided.al2023 | python3.12 | java21 | python3.13 | nodejs22.x | nodejs24.x | python3.14 | java25 | dotnet10 | ruby4.0`
Required: No

 ** RuntimeVersionConfig **   <a name="lambda-Type-FunctionConfiguration-RuntimeVersionConfig"></a>
The ARN of the runtime and any errors that occured.
Type: [RuntimeVersionConfig](API_RuntimeVersionConfig.md) object
Required: No

 ** SigningJobArn **   <a name="lambda-Type-FunctionConfiguration-SigningJobArn"></a>
The ARN of the signing job.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
Required: No

 ** SigningProfileVersionArn **   <a name="lambda-Type-FunctionConfiguration-SigningProfileVersionArn"></a>
The ARN of the signing profile version.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
Required: No

 ** SnapStart **   <a name="lambda-Type-FunctionConfiguration-SnapStart"></a>
Set `ApplyOn` to `PublishedVersions` to create a snapshot of the initialized execution environment when you publish a function version. For more information, see [Improving startup performance with Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html).
Type: [SnapStartResponse](API_SnapStartResponse.md) object
Required: No

 ** State **   <a name="lambda-Type-FunctionConfiguration-State"></a>
The current state of the function. When the state is `Inactive`, you can reactivate the function by invoking it.
Type: String
Valid Values: `Pending | Active | Inactive | Failed | Deactivating | Deactivated | ActiveNonInvocable | Deleting`
Required: No

 ** StateReason **   <a name="lambda-Type-FunctionConfiguration-StateReason"></a>
The reason for the function's current state.
Type: String
Required: No

 ** StateReasonCode **   <a name="lambda-Type-FunctionConfiguration-StateReasonCode"></a>
The reason code for the function's current state. When the code is `Creating`, you can't invoke or modify the function.
Type: String
Valid Values: `Idle | Creating | Restoring | EniLimitExceeded | InsufficientRolePermissions | InvalidConfiguration | InternalError | SubnetOutOfIPAddresses | InvalidSubnet | InvalidSecurityGroup | ImageDeleted | ImageAccessDenied | InvalidImage | KMSKeyAccessDenied | KMSKeyNotFound | InvalidStateKMSKey | DisabledKMSKey | EFSIOError | EFSMountConnectivityError | EFSMountFailure | EFSMountTimeout | InvalidRuntime | InvalidZipFileException | FunctionError | DrainingDurableExecutions | VcpuLimitExceeded | CapacityProviderScalingLimitExceeded | InsufficientCapacity | EC2RequestLimitExceeded | FunctionError.InitTimeout | FunctionError.RuntimeInitError | FunctionError.ExtensionInitError | FunctionError.InvalidEntryPoint | FunctionError.InvalidWorkingDirectory | FunctionError.PermissionDenied | FunctionError.TooManyExtensions | FunctionError.InitResourceExhausted | DisallowedByVpcEncryptionControl | DependencyError`
Required: No

 ** TenancyConfig **   <a name="lambda-Type-FunctionConfiguration-TenancyConfig"></a>
The function's tenant isolation configuration settings. Determines whether the Lambda function runs on a shared or dedicated infrastructure per unique tenant.
Type: [TenancyConfig](API_TenancyConfig.md) object
Required: No

 ** Timeout **   <a name="lambda-Type-FunctionConfiguration-Timeout"></a>
The amount of time in seconds that Lambda allows a function to run before stopping it.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** TracingConfig **   <a name="lambda-Type-FunctionConfiguration-TracingConfig"></a>
The function's AWS X-Ray tracing configuration.
Type: [TracingConfigResponse](API_TracingConfigResponse.md) object
Required: No

 ** Version **   <a name="lambda-Type-FunctionConfiguration-Version"></a>
The version of the Lambda function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(\$LATEST|[0-9]+)`
Required: No

 ** VpcConfig **   <a name="lambda-Type-FunctionConfiguration-VpcConfig"></a>
The function's networking configuration.
Type: [VpcConfigResponse](API_VpcConfigResponse.md) object
Required: No

## See Also
<a name="API_FunctionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/FunctionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/FunctionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/FunctionConfiguration)
