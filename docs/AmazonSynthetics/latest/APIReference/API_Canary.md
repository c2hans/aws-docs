---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_Canary.html
---

# Canary
<a name="API_Canary"></a>

This structure contains all information about one canary in your account.

## Contents
<a name="API_Canary_Contents"></a>

 ** ArtifactConfig **   <a name="synthetics-Type-Canary-ArtifactConfig"></a>
A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.
Type: [ArtifactConfigOutput](API_ArtifactConfigOutput.md) object
Required: No

 ** ArtifactS3Location **   <a name="synthetics-Type-Canary-ArtifactS3Location"></a>
The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary. Artifacts include the log file, screenshots, and HAR files.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** BrowserConfigs **   <a name="synthetics-Type-Canary-BrowserConfigs"></a>
A structure that specifies the browser type to use for a canary run. CloudWatch Synthetics supports running canaries on both `CHROME` and `FIREFOX` browsers.
If not specified, `browserConfigs` defaults to Chrome.
Type: Array of [BrowserConfig](API_BrowserConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** Code **   <a name="synthetics-Type-Canary-Code"></a>
This structure contains information about the canary's Lambda handler and where its code is stored by CloudWatch Synthetics.
Type: [CanaryCodeOutput](API_CanaryCodeOutput.md) object
Required: No

 ** DryRunConfig **   <a name="synthetics-Type-Canary-DryRunConfig"></a>
Returns the dry run configurations for a canary.
Type: [DryRunConfigOutput](API_DryRunConfigOutput.md) object
Required: No

 ** EngineArn **   <a name="synthetics-Type-Canary-EngineArn"></a>
The ARN of the Lambda function that is used as your canary's engine. For more information about Lambda ARN format, see [Resources and Conditions for Lambda Actions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2,4}(-[a-z]{2,4})?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: No

 ** EngineConfigs **   <a name="synthetics-Type-Canary-EngineConfigs"></a>
A list of engine configurations for the canary, one for each browser type that the canary is configured to run on.
All runtime versions `syn-nodejs-puppeteer-11.0` and above, and `syn-nodejs-playwright-3.0` and above, use `engineConfigs` only. You can no longer use `engineArn` in these versions.
Runtime versions older than `syn-nodejs-puppeteer-11.0` and `syn-nodejs-playwright-3.0` continue to support `engineArn` to ensure backward compatibility.
Type: Array of [EngineConfig](API_EngineConfig.md) objects
Required: No

 ** ExecutionRoleArn **   <a name="synthetics-Type-Canary-ExecutionRoleArn"></a>
The ARN of the IAM role used to run the canary. This role must include `lambda.amazonaws.com` as a principal in the trust policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** FailureRetentionPeriodInDays **   <a name="synthetics-Type-Canary-FailureRetentionPeriodInDays"></a>
The number of days to retain data about failed runs of this canary.
This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html), as well as the range of information displayed in the Synthetics console.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

 ** Id **   <a name="synthetics-Type-Canary-Id"></a>
The unique ID of this canary.
Type: String
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** MultiLocationConfig **   <a name="synthetics-Type-Canary-MultiLocationConfig"></a>
If this canary is part of a multi-location configuration, this structure contains information about the canary's location type, primary location, and replicas.
Type: [MultiLocationConfig](API_MultiLocationConfig.md) object
Required: No

 ** Name **   <a name="synthetics-Type-Canary-Name"></a>
The name of the canary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[0-9a-z_\-]+$`
Required: No

 ** ProvisionedResourceCleanup **   <a name="synthetics-Type-Canary-ProvisionedResourceCleanup"></a>
Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted. If it is `AUTOMATIC`, the Lambda functions and layers will be deleted when the canary is deleted.
If the value of this parameter is `OFF`, then the value of the `DeleteLambda` parameter of the [DeleteCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html) operation determines whether the Lambda functions and layers will be deleted.
Type: String
Valid Values: `AUTOMATIC | OFF`
Required: No

 ** RunConfig **   <a name="synthetics-Type-Canary-RunConfig"></a>
A structure that contains information about a canary run.
Type: [CanaryRunConfigOutput](API_CanaryRunConfigOutput.md) object
Required: No

 ** RuntimeVersion **   <a name="synthetics-Type-Canary-RuntimeVersion"></a>
Specifies the runtime version to use for the canary. For more information about runtime versions, see [ Canary Runtime Versions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Schedule **   <a name="synthetics-Type-Canary-Schedule"></a>
A structure that contains information about how often the canary is to run, and when these runs are to stop.
Type: [CanaryScheduleOutput](API_CanaryScheduleOutput.md) object
Required: No

 ** Status **   <a name="synthetics-Type-Canary-Status"></a>
A structure that contains information about the canary's status.
Type: [CanaryStatus](API_CanaryStatus.md) object
Required: No

 ** SuccessRetentionPeriodInDays **   <a name="synthetics-Type-Canary-SuccessRetentionPeriodInDays"></a>
The number of days to retain data about successful runs of this canary.
This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html), as well as the range of information displayed in the Synthetics console.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1024.
Required: No

 ** Tags **   <a name="synthetics-Type-Canary-Tags"></a>
The list of key-value pairs that are associated with the canary.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** Timeline **   <a name="synthetics-Type-Canary-Timeline"></a>
A structure that contains information about when the canary was created, modified, and most recently run.
Type: [CanaryTimeline](API_CanaryTimeline.md) object
Required: No

 ** VisualReference **   <a name="synthetics-Type-Canary-VisualReference"></a>
If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run to use as the baseline for screenshots, and the coordinates of any parts of the screen to ignore during the visual monitoring comparison.
Type: [VisualReferenceOutput](API_VisualReferenceOutput.md) object
Required: No

 ** VisualReferences **   <a name="synthetics-Type-Canary-VisualReferences"></a>
A list of visual reference configurations for the canary, one for each browser type that the canary is configured to run on. Visual references are used for visual monitoring comparisons.
 `syn-nodejs-puppeteer-11.0` and above, and `syn-nodejs-playwright-3.0` and above, only supports `visualReferences`. `visualReference` field is not supported.
Versions older than `syn-nodejs-puppeteer-11.0` supports both `visualReference` and `visualReferences` for backward compatibility. It is recommended to use `visualReferences` for consistency and future compatibility.
Type: Array of [VisualReferenceOutput](API_VisualReferenceOutput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** VpcConfig **   <a name="synthetics-Type-Canary-VpcConfig"></a>
If this canary is to test an endpoint in a VPC, this structure contains information about the subnets and security groups of the VPC endpoint. For more information, see [ Running a Canary in a VPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html).
Type: [VpcConfigOutput](API_VpcConfigOutput.md) object
Required: No

## See Also
<a name="API_Canary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/Canary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/Canary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/Canary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
