---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ContainerTaskConfiguration.html
---

# ContainerTaskConfiguration
<a name="API_ContainerTaskConfiguration"></a>

Configuration for a container task, including the container image, IAM role, and compute settings.

## Contents
<a name="API_ContainerTaskConfiguration_Contents"></a>

 ** ecrUri **   <a name="iotsitewise-Type-ContainerTaskConfiguration-ecrUri"></a>
The Amazon ECR image URI for the task container.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `((\d{12}\.dkr\.ecr\.[a-z0-9-]+\.[a-z.]+)|public\.ecr\.aws/[a-z][a-z0-9]+([._-][a-z0-9]+)*)/[a-z0-9]+((\.||__|_|-+)[a-z0-9]+)*(/[a-z0-9]+((\.||__|_|-+)[a-z0-9]+)*)*(:[a-zA-Z0-9._-]+|@sha256:[a-f0-9]{64})?`
Required: Yes

 ** processingType **   <a name="iotsitewise-Type-ContainerTaskConfiguration-processingType"></a>
The processing type for compute resources.
Type: String
Valid Values: `GENERIC_COMPUTE_PROCESSING | HARDWARE_ACCELERATED_PROCESSING`
Required: Yes

 ** processingUnit **   <a name="iotsitewise-Type-ContainerTaskConfiguration-processingUnit"></a>
The processing unit allocation that determines the vCPU, memory, and GPU resources.
Type: String
Valid Values: `UNITS_2 | UNITS_4 | UNITS_8 | UNITS_12 | UNITS_16 | UNITS_24 | UNITS_32 | UNITS_36 | UNITS_48 | UNITS_60 | UNITS_64 | UNITS_72 | UNITS_84 | UNITS_96`
Required: Yes

 ** taskExecutionRole **   <a name="iotsitewise-Type-ContainerTaskConfiguration-taskExecutionRole"></a>
The ARN of the IAM role that grants the containerized workload permissions to access resources.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-cn|-us-gov)?:iam::\d{12}:role/[\w+=,.@/-]+`
Required: Yes

 ** command **   <a name="iotsitewise-Type-ContainerTaskConfiguration-command"></a>
The command to execute in the container.
Type: Array of strings
Required: No

 ** environmentVariables **   <a name="iotsitewise-Type-ContainerTaskConfiguration-environmentVariables"></a>
Environment variables passed to the container at runtime.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `(?!(?i)AWS_)[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** timeoutSeconds **   <a name="iotsitewise-Type-ContainerTaskConfiguration-timeoutSeconds"></a>
The timeout in seconds for task execution. Default: 3600 (1 hour).
Type: Long
Valid Range: Minimum value of 60. Maximum value of 86400.
Required: No

## See Also
<a name="API_ContainerTaskConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ContainerTaskConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ContainerTaskConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ContainerTaskConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
