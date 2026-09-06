---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ExecuteCommandConfiguration.html
---

# ExecuteCommandConfiguration
<a name="API_ExecuteCommandConfiguration"></a>

The details of the execute command configuration.

## Contents
<a name="API_ExecuteCommandConfiguration_Contents"></a>

 ** kmsKeyId **   <a name="ECS-Type-ExecuteCommandConfiguration-kmsKeyId"></a>
Specify an AWS Key Management Service key ID to encrypt the data between the local client and the container.
Type: String
Required: No

 ** logConfiguration **   <a name="ECS-Type-ExecuteCommandConfiguration-logConfiguration"></a>
The log configuration for the results of the execute command actions. The logs can be sent to CloudWatch Logs or an Amazon S3 bucket. When `logging=OVERRIDE` is specified, a `logConfiguration` must be provided.
Type: [ExecuteCommandLogConfiguration](API_ExecuteCommandLogConfiguration.md) object
Required: No

 ** logging **   <a name="ECS-Type-ExecuteCommandConfiguration-logging"></a>
The log setting to use for redirecting logs for your execute command results. The following log settings are available.
+  `NONE`: The execute command session is not logged.
+  `DEFAULT`: The `awslogs` configuration in the task definition is used. If no logging parameter is specified, it defaults to this value. If no `awslogs` log driver is configured in the task definition, the output won't be logged.
+  `OVERRIDE`: Specify the logging details as a part of `logConfiguration`. If the `OVERRIDE` logging option is specified, the `logConfiguration` is required.
Type: String
Valid Values: `NONE | DEFAULT | OVERRIDE`
Required: No

## See Also
<a name="API_ExecuteCommandConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ExecuteCommandConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ExecuteCommandConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ExecuteCommandConfiguration)
