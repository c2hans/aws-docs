---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HumanLoopConfig.html
---

# HumanLoopConfig
<a name="API_HumanLoopConfig"></a>

Describes the work to be performed by human workers.

## Contents
<a name="API_HumanLoopConfig_Contents"></a>

 ** HumanTaskUiArn **   <a name="sagemaker-Type-HumanLoopConfig-HumanTaskUiArn"></a>
The Amazon Resource Name (ARN) of the human task user interface.
You can use standard HTML and Crowd HTML Elements to create a custom worker task template. You use this template to create a human task UI.
To learn how to create a custom HTML template, see [Create Custom Worker Task Template](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-custom-templates.html).
To learn how to create a human task UI, which is a worker task template that can be used in a flow definition, see [Create and Delete a Worker Task Templates](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-worker-template-console.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]+:[0-9]{12}:human-task-ui/.*`
Required: Yes

 ** TaskCount **   <a name="sagemaker-Type-HumanLoopConfig-TaskCount"></a>
The number of distinct workers who will perform the same task on each object. For example, if `TaskCount` is set to `3` for an image classification labeling job, three workers will classify each input image. Increasing `TaskCount` can improve label accuracy.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3.
Required: Yes

 ** TaskDescription **   <a name="sagemaker-Type-HumanLoopConfig-TaskDescription"></a>
A description for the human worker task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

 ** TaskTitle **   <a name="sagemaker-Type-HumanLoopConfig-TaskTitle"></a>
A title for the human worker task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\t\n\r -\uD7FF\uE000-\uFFFD]*`
Required: Yes

 ** WorkteamArn **   <a name="sagemaker-Type-HumanLoopConfig-WorkteamArn"></a>
Amazon Resource Name (ARN) of a team of workers. To learn more about the types of workforces and work teams you can create and use with Amazon A2I, see [Create and Manage Workforces](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:workteam/.*`
Required: Yes

 ** PublicWorkforceTaskPrice **   <a name="sagemaker-Type-HumanLoopConfig-PublicWorkforceTaskPrice"></a>
Defines the amount of money paid to an Amazon Mechanical Turk worker for each task performed.
Use one of the following prices for bounding box tasks. Prices are in US dollars and should be based on the complexity of the task; the longer it takes in your initial testing, the more you should offer.
+ 0.036
+ 0.048
+ 0.060
+ 0.072
+ 0.120
+ 0.240
+ 0.360
+ 0.480
+ 0.600
+ 0.720
+ 0.840
+ 0.960
+ 1.080
+ 1.200
Use one of the following prices for image classification, text classification, and custom tasks. Prices are in US dollars.
+ 0.012
+ 0.024
+ 0.036
+ 0.048
+ 0.060
+ 0.072
+ 0.120
+ 0.240
+ 0.360
+ 0.480
+ 0.600
+ 0.720
+ 0.840
+ 0.960
+ 1.080
+ 1.200
Use one of the following prices for semantic segmentation tasks. Prices are in US dollars.
+ 0.840
+ 0.960
+ 1.080
+ 1.200
Use one of the following prices for Textract AnalyzeDocument Important Form Key Amazon Augmented AI review tasks. Prices are in US dollars.
+ 2.400
+ 2.280
+ 2.160
+ 2.040
+ 1.920
+ 1.800
+ 1.680
+ 1.560
+ 1.440
+ 1.320
+ 1.200
+ 1.080
+ 0.960
+ 0.840
+ 0.720
+ 0.600
+ 0.480
+ 0.360
+ 0.240
+ 0.120
+ 0.072
+ 0.060
+ 0.048
+ 0.036
+ 0.024
+ 0.012
Use one of the following prices for Rekognition DetectModerationLabels Amazon Augmented AI review tasks. Prices are in US dollars.
+ 1.200
+ 1.080
+ 0.960
+ 0.840
+ 0.720
+ 0.600
+ 0.480
+ 0.360
+ 0.240
+ 0.120
+ 0.072
+ 0.060
+ 0.048
+ 0.036
+ 0.024
+ 0.012
Use one of the following prices for Amazon Augmented AI custom human review tasks. Prices are in US dollars.
+ 1.200
+ 1.080
+ 0.960
+ 0.840
+ 0.720
+ 0.600
+ 0.480
+ 0.360
+ 0.240
+ 0.120
+ 0.072
+ 0.060
+ 0.048
+ 0.036
+ 0.024
+ 0.012
Type: [PublicWorkforceTaskPrice](API_PublicWorkforceTaskPrice.md) object
Required: No

 ** TaskAvailabilityLifetimeInSeconds **   <a name="sagemaker-Type-HumanLoopConfig-TaskAvailabilityLifetimeInSeconds"></a>
The length of time that a task remains available for review by human workers.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** TaskKeywords **   <a name="sagemaker-Type-HumanLoopConfig-TaskKeywords"></a>
Keywords used to describe the task so that workers can discover the task.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[A-Za-z0-9]+( [A-Za-z0-9]+)*`
Required: No

 ** TaskTimeLimitInSeconds **   <a name="sagemaker-Type-HumanLoopConfig-TaskTimeLimitInSeconds"></a>
The amount of time that a worker has to complete a task. The default value is 3,600 seconds (1 hour).
Type: Integer
Valid Range: Minimum value of 30.
Required: No

## See Also
<a name="API_HumanLoopConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HumanLoopConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HumanLoopConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HumanLoopConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
