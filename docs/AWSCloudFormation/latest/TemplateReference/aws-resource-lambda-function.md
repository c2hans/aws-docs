---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function
<a name="aws-resource-lambda-function"></a>

The `AWS::Lambda::Function` resource creates a Lambda function. To create a function, you need a [deployment package](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html) and an [execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html). The deployment package is a .zip file archive or container image that contains your function code. The execution role grants the function permission to use AWS services, such as Amazon CloudWatch Logs for log streaming and AWS X-Ray for request tracing.

You set the package type to `Image` if the deployment package is a [container image](https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html). For these functions, include the URI of the container image in the Amazon ECR registry in the [`ImageUri` property of the `Code` property](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-imageuri). You do not need to specify the handler and runtime properties.

You set the package type to `Zip` if the deployment package is a [.zip file archive](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html#gettingstarted-package-zip). For these functions, specify the Amazon S3 location of your .zip file in the `Code` property. Alternatively, for Node.js and Python functions, you can define your function inline in the [`ZipFile` property of the `Code` property](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-zipfile). In both cases, you must also specify the handler and runtime properties.

You can use [code signing](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html) if your deployment package is a .zip file archive. To enable code signing for this function, specify the ARN of a code-signing configuration. When a user attempts to deploy a code package with `UpdateFunctionCode`, Lambda checks that the code package has a valid signature from a trusted publisher. The code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.

When you update a `AWS::Lambda::Function` resource, CloudFormation calls the [UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionConfiguration.html) and [UpdateFunctionCode](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionCode.html)Lambda APIs under the hood. Because these calls happen sequentially, and invocations can happen between these calls, your function may encounter errors in the time between the calls. For example, if you remove an environment variable, and the code that references that environment variable in the same CloudFormation update, you may see invocation errors related to a missing environment variable. To work around this, you can invoke your function against a version or alias by default, rather than the `$LATEST` version.

Note that you configure [ provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) on a `AWS::Lambda::Version` or a `AWS::Lambda::Alias`.

For a complete introduction to Lambda functions, see [What is Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/lambda-welcome.html) in the *Lambda developer guide.*

## Syntax
<a name="aws-resource-lambda-function-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-function-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::Function",
  "Properties" : {
      "[Architectures](#cfn-lambda-function-architectures)" : {{[ String, ... ]}},
      "[CapacityProviderConfig](#cfn-lambda-function-capacityproviderconfig)" : {{CapacityProviderConfig}},
      "[Code](#cfn-lambda-function-code)" : {{Code}},
      "[CodeSigningConfigArn](#cfn-lambda-function-codesigningconfigarn)" : {{String}},
      "[DeadLetterConfig](#cfn-lambda-function-deadletterconfig)" : {{DeadLetterConfig}},
      "[Description](#cfn-lambda-function-description)" : {{String}},
      "[DurableConfig](#cfn-lambda-function-durableconfig)" : {{DurableConfig}},
      "[Environment](#cfn-lambda-function-environment)" : {{Environment}},
      "[EphemeralStorage](#cfn-lambda-function-ephemeralstorage)" : {{EphemeralStorage}},
      "[FileSystemConfigs](#cfn-lambda-function-filesystemconfigs)" : {{[ FileSystemConfig, ... ]}},
      "[FunctionName](#cfn-lambda-function-functionname)" : {{String}},
      "[FunctionScalingConfig](#cfn-lambda-function-functionscalingconfig)" : {{FunctionScalingConfig}},
      "[Handler](#cfn-lambda-function-handler)" : {{String}},
      "[ImageConfig](#cfn-lambda-function-imageconfig)" : {{ImageConfig}},
      "[KmsKeyArn](#cfn-lambda-function-kmskeyarn)" : {{String}},
      "[Layers](#cfn-lambda-function-layers)" : {{[ String, ... ]}},
      "[LoggingConfig](#cfn-lambda-function-loggingconfig)" : {{LoggingConfig}},
      "[MemorySize](#cfn-lambda-function-memorysize)" : {{Integer}},
      "[PackageType](#cfn-lambda-function-packagetype)" : {{String}},
      "[PublishToLatestPublished](#cfn-lambda-function-publishtolatestpublished)" : {{Boolean}},
      "[RecursiveLoop](#cfn-lambda-function-recursiveloop)" : {{String}},
      "[ReservedConcurrentExecutions](#cfn-lambda-function-reservedconcurrentexecutions)" : {{Integer}},
      "[Role](#cfn-lambda-function-role)" : {{String}},
      "[Runtime](#cfn-lambda-function-runtime)" : {{String}},
      "[RuntimeManagementConfig](#cfn-lambda-function-runtimemanagementconfig)" : {{RuntimeManagementConfig}},
      "[SnapStart](#cfn-lambda-function-snapstart)" : {{SnapStart}},
      "[Tags](#cfn-lambda-function-tags)" : {{[ Tag, ... ]}},
      "[TenancyConfig](#cfn-lambda-function-tenancyconfig)" : {{TenancyConfig}},
      "[Timeout](#cfn-lambda-function-timeout)" : {{Integer}},
      "[TracingConfig](#cfn-lambda-function-tracingconfig)" : {{TracingConfig}},
      "[VpcConfig](#cfn-lambda-function-vpcconfig)" : {{VpcConfig}}
    }
}
```

### YAML
<a name="aws-resource-lambda-function-syntax.yaml"></a>

```
Type: AWS::Lambda::Function
Properties:
  [Architectures](#cfn-lambda-function-architectures): {{
    - String}}
  [CapacityProviderConfig](#cfn-lambda-function-capacityproviderconfig): {{
    CapacityProviderConfig}}
  [Code](#cfn-lambda-function-code): {{
    Code}}
  [CodeSigningConfigArn](#cfn-lambda-function-codesigningconfigarn): {{String}}
  [DeadLetterConfig](#cfn-lambda-function-deadletterconfig): {{
    DeadLetterConfig}}
  [Description](#cfn-lambda-function-description): {{String}}
  [DurableConfig](#cfn-lambda-function-durableconfig): {{
    DurableConfig}}
  [Environment](#cfn-lambda-function-environment): {{
    Environment}}
  [EphemeralStorage](#cfn-lambda-function-ephemeralstorage): {{
    EphemeralStorage}}
  [FileSystemConfigs](#cfn-lambda-function-filesystemconfigs): {{
    - FileSystemConfig}}
  [FunctionName](#cfn-lambda-function-functionname): {{String}}
  [FunctionScalingConfig](#cfn-lambda-function-functionscalingconfig): {{
    FunctionScalingConfig}}
  [Handler](#cfn-lambda-function-handler): {{String}}
  [ImageConfig](#cfn-lambda-function-imageconfig): {{
    ImageConfig}}
  [KmsKeyArn](#cfn-lambda-function-kmskeyarn): {{String}}
  [Layers](#cfn-lambda-function-layers): {{
    - String}}
  [LoggingConfig](#cfn-lambda-function-loggingconfig): {{
    LoggingConfig}}
  [MemorySize](#cfn-lambda-function-memorysize): {{Integer}}
  [PackageType](#cfn-lambda-function-packagetype): {{String}}
  [PublishToLatestPublished](#cfn-lambda-function-publishtolatestpublished): {{Boolean}}
  [RecursiveLoop](#cfn-lambda-function-recursiveloop): {{String}}
  [ReservedConcurrentExecutions](#cfn-lambda-function-reservedconcurrentexecutions): {{Integer}}
  [Role](#cfn-lambda-function-role): {{String}}
  [Runtime](#cfn-lambda-function-runtime): {{String}}
  [RuntimeManagementConfig](#cfn-lambda-function-runtimemanagementconfig): {{
    RuntimeManagementConfig}}
  [SnapStart](#cfn-lambda-function-snapstart): {{
    SnapStart}}
  [Tags](#cfn-lambda-function-tags): {{
    - Tag}}
  [TenancyConfig](#cfn-lambda-function-tenancyconfig): {{
    TenancyConfig}}
  [Timeout](#cfn-lambda-function-timeout): {{Integer}}
  [TracingConfig](#cfn-lambda-function-tracingconfig): {{
    TracingConfig}}
  [VpcConfig](#cfn-lambda-function-vpcconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-resource-lambda-function-properties"></a>

`Architectures`  <a name="cfn-lambda-function-architectures"></a>
The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86\_64). The default value is `x86_64`.
*Required*: No
*Type*: Array of String
*Allowed values*: `x86_64 | arm64`
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityProviderConfig`  <a name="cfn-lambda-function-capacityproviderconfig"></a>
Configuration for the capacity provider that manages compute resources for Lambda functions.
*Required*: No
*Type*: [CapacityProviderConfig](aws-properties-lambda-function-capacityproviderconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Code`  <a name="cfn-lambda-function-code"></a>
The code for the function. You can define your function code in multiple ways:
+ For .zip deployment packages, you can specify the Amazon S3 location of the .zip file in the `S3Bucket`, `S3Key`, and `S3ObjectVersion` properties.
+ For .zip deployment packages, you can alternatively define the function code inline in the `ZipFile` property. This method works only for Node.js and Python functions.
+ For container images, specify the URI of your container image in the Amazon ECR registry in the `ImageUri` property.
*Required*: Yes
*Type*: [Code](aws-properties-lambda-function-code.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodeSigningConfigArn`  <a name="cfn-lambda-function-codesigningconfigarn"></a>
To enable code signing for this function, specify the ARN of a code-signing configuration. A code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws[a-zA-Z-]*)?:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:code-signing-config:csc-[a-z0-9]{17}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeadLetterConfig`  <a name="cfn-lambda-function-deadletterconfig"></a>
A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see [Dead-letter queues](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq).
*Required*: No
*Type*: [DeadLetterConfig](aws-properties-lambda-function-deadletterconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-lambda-function-description"></a>
A description of the function.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DurableConfig`  <a name="cfn-lambda-function-durableconfig"></a>
Configuration settings for [durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), including execution timeout, retention period for execution history, and an optional ARN of the AWS Key Management Service (AWS KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.
*Required*: No
*Type*: [DurableConfig](aws-properties-lambda-function-durableconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Environment`  <a name="cfn-lambda-function-environment"></a>
Environment variables that are accessible from function code during execution.
*Required*: No
*Type*: [Environment](aws-properties-lambda-function-environment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EphemeralStorage`  <a name="cfn-lambda-function-ephemeralstorage"></a>
The size of the function's `/tmp` directory in MB. The default value is 512, but it can be any whole number between 512 and 10,240 MB.
*Required*: No
*Type*: [EphemeralStorage](aws-properties-lambda-function-ephemeralstorage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FileSystemConfigs`  <a name="cfn-lambda-function-filesystemconfigs"></a>
Connection settings for an Amazon EFS or Amazon S3 Files file system. To connect a function to a file system, a mount target must be available in every Availability Zone that your function connects to. If your template contains an [AWS::EFS::MountTarget](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html) or [AWS::S3Files::MountTarget](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-mounttarget.html) resource, you must also specify a `DependsOn` attribute to ensure that the mount target is created or updated before the function.
For more information about using the `DependsOn` attribute, see [DependsOn Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html).
*Required*: No
*Type*: Array of [FileSystemConfig](aws-properties-lambda-function-filesystemconfig.md)
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionName`  <a name="cfn-lambda-function-functionname"></a>
The name of the Lambda function, up to 64 characters in length. If you don't specify a name, CloudFormation generates one.
If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FunctionScalingConfig`  <a name="cfn-lambda-function-functionscalingconfig"></a>
Configuration that defines the scaling behavior for a Lambda Managed Instances function, including the minimum and maximum number of execution environments that can be provisioned.
*Required*: No
*Type*: [FunctionScalingConfig](aws-properties-lambda-function-functionscalingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Handler`  <a name="cfn-lambda-function-handler"></a>
The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see [Lambda programming model](https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html).
*Required*: No
*Type*: String
*Pattern*: `^[^\s]+$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageConfig`  <a name="cfn-lambda-function-imageconfig"></a>
Configuration values that override the container image Dockerfile settings. For more information, see [Container image settings](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms).
*Required*: No
*Type*: [ImageConfig](aws-properties-lambda-function-imageconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-lambda-function-kmskeyarn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt the following resources:
+ The function's [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption).
+ The function's [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html) snapshots.
+ When used with `SourceKMSKeyArn`, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see [ Specifying a customer managed key for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption).
+ The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see [Function lifecycle](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle).
If you don't provide a customer managed key, Lambda uses an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) or an [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk).
*Required*: No
*Type*: String
*Pattern*: `^(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Layers`  <a name="cfn-lambda-function-layers"></a>
A list of [function layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) to add to the function's execution environment. Specify each layer by its ARN, including the version.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoggingConfig`  <a name="cfn-lambda-function-loggingconfig"></a>
The function's Amazon CloudWatch Logs configuration settings.
*Required*: No
*Type*: [LoggingConfig](aws-properties-lambda-function-loggingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemorySize`  <a name="cfn-lambda-function-memorysize"></a>
The amount of [memory available to the function](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-memory-console) at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB. Note that new AWS accounts have reduced concurrency and memory quotas. AWS raises these quotas automatically based on your usage. You can also request a quota increase.
*Required*: No
*Type*: Integer
*Minimum*: `128`
*Maximum*: `32768`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PackageType`  <a name="cfn-lambda-function-packagetype"></a>
The type of deployment package. Set to `Image` for container image and set `Zip` for .zip file archive.
*Required*: No
*Type*: String
*Allowed values*: `Image | Zip`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PublishToLatestPublished`  <a name="cfn-lambda-function-publishtolatestpublished"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecursiveLoop`  <a name="cfn-lambda-function-recursiveloop"></a>
The status of your function's recursive loop detection configuration.
When this value is set to `Allow`and Lambda detects your function being invoked as part of a recursive loop, it doesn't take any action.
When this value is set to `Terminate` and Lambda detects your function being invoked as part of a recursive loop, it stops your function being invoked and notifies you.
*Required*: No
*Type*: String
*Allowed values*: `Allow | Terminate`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReservedConcurrentExecutions`  <a name="cfn-lambda-function-reservedconcurrentexecutions"></a>
The number of simultaneous executions to reserve for the function.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Role`  <a name="cfn-lambda-function-role"></a>
The Amazon Resource Name (ARN) of the function's execution role.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Runtime`  <a name="cfn-lambda-function-runtime"></a>
The identifier of the function's [ runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.
The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels).
For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported).
*Required*: No
*Type*: String
*Allowed values*: `nodejs | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs10.x | nodejs12.x | nodejs14.x | nodejs16.x | java8 | java8.al2 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | python3.9 | dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | dotnetcore3.1 | dotnet6 | dotnet8 | nodejs4.3-edge | go1.x | ruby2.5 | ruby2.7 | provided | provided.al2 | nodejs18.x | python3.10 | java17 | ruby3.2 | ruby3.3 | ruby3.4 | python3.11 | nodejs20.x | provided.al2023 | python3.12 | java21 | python3.13 | nodejs22.x | nodejs24.x | python3.14 | java25 | dotnet10 | ruby4.0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeManagementConfig`  <a name="cfn-lambda-function-runtimemanagementconfig"></a>
Sets the runtime management configuration for a function's version. For more information, see [Runtime updates](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html).
*Required*: No
*Type*: [RuntimeManagementConfig](aws-properties-lambda-function-runtimemanagementconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapStart`  <a name="cfn-lambda-function-snapstart"></a>
The function's [AWS Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) setting.
*Required*: No
*Type*: [SnapStart](aws-properties-lambda-function-snapstart.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-lambda-function-tags"></a>
A list of [tags](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html) to apply to the function.
You must have the `lambda:TagResource`, `lambda:UntagResource`, and `lambda:ListTags` permissions for your [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) to manage the CloudFormation stack. If you don't have these permissions, there might be unexpected behavior with stack-level tags propagating to the resource during resource creation and update.
*Required*: No
*Type*: Array of [Tag](aws-properties-lambda-function-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TenancyConfig`  <a name="cfn-lambda-function-tenancyconfig"></a>
The function's tenant isolation configuration settings. Determines whether the Lambda function runs on a shared or dedicated infrastructure per unique tenant.
*Required*: No
*Type*: [TenancyConfig](aws-properties-lambda-function-tenancyconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Timeout`  <a name="cfn-lambda-function-timeout"></a>
The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds. For more information, see [Lambda execution environment](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html).
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TracingConfig`  <a name="cfn-lambda-function-tracingconfig"></a>
Set `Mode` to `Active` to sample and trace a subset of incoming requests with [X-Ray](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html).
*Required*: No
*Type*: [TracingConfig](aws-properties-lambda-function-tracingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConfig`  <a name="cfn-lambda-function-vpcconfig"></a>
For network connectivity to AWS resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see [Configuring a Lambda function to access resources in a VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html).
*Required*: No
*Type*: [VpcConfig](aws-properties-lambda-function-vpcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lambda-function-return-values"></a>

### Ref
<a name="aws-resource-lambda-function-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-lambda-function-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-lambda-function-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the function.

`SnapStartResponse.ApplyOn`  <a name="SnapStartResponse.ApplyOn-fn::getatt"></a>
Property description not available.

`SnapStartResponse.OptimizationStatus`  <a name="SnapStartResponse.OptimizationStatus-fn::getatt"></a>
Property description not available.

## Examples
<a name="aws-resource-lambda-function--examples"></a>

**Topics**
+ [Function](#aws-resource-lambda-function--examples--Function)
+ [Inline Function](#aws-resource-lambda-function--examples--Inline_Function)
+ [VPC Function](#aws-resource-lambda-function--examples--VPC_Function)

### Function
<a name="aws-resource-lambda-function--examples--Function"></a>

Create a Node.js function.

#### JSON
<a name="aws-resource-lambda-function--examples--Function--json"></a>

```
"AMIIDLookup": {
    "Type": "AWS::Lambda::Function",
    "Properties": {
        "Handler": "index.handler",
        "Role": {
            "Fn::GetAtt": [
                "LambdaExecutionRole",
                "Arn"
            ]
        },
        "Code": {
            "S3Bucket": "amzn-s3-demo-bucket",
            "S3Key": "amilookup.zip"
        },
        "Runtime": "nodejs20.x",
        "Timeout": 25,
        "TracingConfig": {
            "Mode": "Active"
        }
    }
}
```

### Inline Function
<a name="aws-resource-lambda-function--examples--Inline_Function"></a>

Inline Node.js function that lists Amazon S3 buckets in ` us-east-1 `. Before using this example, make sure that your execution role has Amazon S3 read permissions.

#### YAML
<a name="aws-resource-lambda-function--examples--Inline_Function--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Lambda function ListBucketsCommand.
Resources:
  primer:
    Type: AWS::Lambda::Function
    Properties:
      Runtime: nodejs20.x
      Role: arn:aws:iam::111122223333:role/lambda-role
      Handler: index.handler
      Code:
        ZipFile: |
          const { S3Client, ListBucketsCommand } = require("@aws-sdk/client-s3");
          const s3 = new S3Client({ region: "us-east-1" }); // replace "us-east-1" with your AWS Region

          exports.handler = async function(event) {
            const command = new ListBucketsCommand({});
            const response = await s3.send(command);
            return response.Buckets;
          };
      Description: List Amazon S3 buckets in us-east-1.
      TracingConfig:
        Mode: Active
```

### VPC Function
<a name="aws-resource-lambda-function--examples--VPC_Function"></a>

Function connected to a VPC.

#### YAML
<a name="aws-resource-lambda-function--examples--VPC_Function--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Description: VPC function.
Resources:
  Function:
    Type: AWS::Lambda::Function
    Properties:
      Handler: index.handler
      Role: arn:aws:iam::111122223333:role/lambda-role
      Code:
        S3Bucket: amzn-s3-demo-bucket
        S3Key: function.zip
      Runtime: nodejs20.x
      Timeout: 5
      TracingConfig:
        Mode: Active
      VpcConfig:
        SecurityGroupIds:
          - sg-085912345678492fb
        SubnetIds:
          - subnet-071f712345678e7c8
          - subnet-07fd123456788a036
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
