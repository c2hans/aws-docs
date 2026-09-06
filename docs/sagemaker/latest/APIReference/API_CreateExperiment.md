---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateExperiment.html
---

# CreateExperiment
<a name="API_CreateExperiment"></a>

Creates a SageMaker *experiment*. An experiment is a collection of *trials* that are observed, compared and evaluated as a group. A trial is a set of steps, called *trial components*, that produce a machine learning model.

**Note**
In the Studio UI, trials are referred to as *run groups* and trial components are referred to as *runs*.

The goal of an experiment is to determine the components that produce the best model. Multiple trials are performed, each one isolating and measuring the impact of a change to one or more inputs, while keeping the remaining inputs constant.

When you use SageMaker Studio or the SageMaker Python SDK, all experiments, trials, and trial components are automatically tracked, logged, and indexed. When you use the AWS SDK for Python (Boto), you must use the logging APIs provided by the SDK.

You can add tags to experiments, trials, trial components and then use the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search for the tags.

To add a description to an experiment, specify the optional `Description` parameter. To add a description later, or to change the description, call the [UpdateExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateExperiment.html) API.

To get a list of all your experiments, call the [ListExperiments](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListExperiments.html) API. To view an experiment's properties, call the [DescribeExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeExperiment.html) API. To get a list of all the trials associated with an experiment, call the [ListTrials](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrials.html) API. To create a trial call the [CreateTrial](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrial.html) API.

## Request Syntax
<a name="API_CreateExperiment_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "ExperimentName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateExperiment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateExperiment_RequestSyntax) **   <a name="sagemaker-CreateExperiment-request-Description"></a>
The description of the experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** [DisplayName](#API_CreateExperiment_RequestSyntax) **   <a name="sagemaker-CreateExperiment-request-DisplayName"></a>
The name of the experiment as displayed. The name doesn't need to be unique. If you don't specify `DisplayName`, the value in `ExperimentName` is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** [ExperimentName](#API_CreateExperiment_RequestSyntax) **   <a name="sagemaker-CreateExperiment-request-ExperimentName"></a>
The name of the experiment. The name must be unique in your AWS account and is not case-sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

 ** [Tags](#API_CreateExperiment_RequestSyntax) **   <a name="sagemaker-CreateExperiment-request-Tags"></a>
A list of tags to associate with the experiment. You can use [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search on the tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateExperiment_ResponseSyntax"></a>

```
{
   "ExperimentArn": "string"
}
```

## Response Elements
<a name="API_CreateExperiment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExperimentArn](#API_CreateExperiment_ResponseSyntax) **   <a name="sagemaker-CreateExperiment-response-ExperimentArn"></a>
The Amazon Resource Name (ARN) of the experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment/.*`

## Errors
<a name="API_CreateExperiment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateExperiment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateExperiment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateExperiment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateExperiment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateExperiment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateExperiment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateExperiment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateExperiment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateExperiment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateExperiment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateExperiment)
