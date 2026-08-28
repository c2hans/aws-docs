---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaExecutionParameters.html
---

# LambdaExecutionParameters
<a name="API_LambdaExecutionParameters"></a>

Contains parameters for a Lambda function that runs on AWS IoT Greengrass.

## Contents
<a name="API_LambdaExecutionParameters_Contents"></a>

 ** environmentVariables **   <a name="greengrassv2-Type-LambdaExecutionParameters-environmentVariables"></a>
The map of environment variables that are available to the Lambda function when it runs.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Required: No

 ** eventSources **   <a name="greengrassv2-Type-LambdaExecutionParameters-eventSources"></a>
The list of event sources to which to subscribe to receive work messages. The Lambda function runs when it receives a message from an event source. You can subscribe this function to local publish/subscribe messages and AWS IoT Core MQTT messages.
Type: Array of [LambdaEventSource](API_LambdaEventSource.md) objects
Required: No

 ** execArgs **   <a name="greengrassv2-Type-LambdaExecutionParameters-execArgs"></a>
The list of arguments to pass to the Lambda function when it runs.
Type: Array of strings
Required: No

 ** inputPayloadEncodingType **   <a name="greengrassv2-Type-LambdaExecutionParameters-inputPayloadEncodingType"></a>
The encoding type that the Lambda function supports.
Default: `json`
Type: String
Valid Values: `json | binary`
Required: No

 ** linuxProcessParams **   <a name="greengrassv2-Type-LambdaExecutionParameters-linuxProcessParams"></a>
The parameters for the Linux process that contains the Lambda function.
Type: [LambdaLinuxProcessParams](API_LambdaLinuxProcessParams.md) object
Required: No

 ** maxIdleTimeInSeconds **   <a name="greengrassv2-Type-LambdaExecutionParameters-maxIdleTimeInSeconds"></a>
The maximum amount of time in seconds that a non-pinned Lambda function can idle before the AWS IoT Greengrass Core software stops its process.
Type: Integer
Required: No

 ** maxInstancesCount **   <a name="greengrassv2-Type-LambdaExecutionParameters-maxInstancesCount"></a>
The maximum number of instances that a non-pinned Lambda function can run at the same time.
Type: Integer
Required: No

 ** maxQueueSize **   <a name="greengrassv2-Type-LambdaExecutionParameters-maxQueueSize"></a>
The maximum size of the message queue for the Lambda function component. The AWS IoT Greengrass core stores messages in a FIFO (first-in-first-out) queue until it can run the Lambda function to consume each message.
Type: Integer
Required: No

 ** pinned **   <a name="greengrassv2-Type-LambdaExecutionParameters-pinned"></a>
Whether or not the Lambda function is pinned, or long-lived.
+ A pinned Lambda function starts when AWS IoT Greengrass starts and keeps running in its own container.
+ A non-pinned Lambda function starts only when it receives a work item and exists after it idles for `maxIdleTimeInSeconds`. If the function has multiple work items, the AWS IoT Greengrass Core software creates multiple instances of the function.
Default: `true`
Type: Boolean
Required: No

 ** statusTimeoutInSeconds **   <a name="greengrassv2-Type-LambdaExecutionParameters-statusTimeoutInSeconds"></a>
The interval in seconds at which a pinned (also known as long-lived) Lambda function component sends status updates to the Lambda manager component.
Type: Integer
Required: No

 ** timeoutInSeconds **   <a name="greengrassv2-Type-LambdaExecutionParameters-timeoutInSeconds"></a>
The maximum amount of time in seconds that the Lambda function can process a work item.
Type: Integer
Required: No

## See Also
<a name="API_LambdaExecutionParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/LambdaExecutionParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/LambdaExecutionParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/LambdaExecutionParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
