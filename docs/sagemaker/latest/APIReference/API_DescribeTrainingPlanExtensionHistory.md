---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingPlanExtensionHistory.html
---

# DescribeTrainingPlanExtensionHistory
<a name="API_DescribeTrainingPlanExtensionHistory"></a>

Retrieves the extension history for a specified training plan. The response includes details about each extension, such as the offering ID, start and end dates, status, payment status, and cost information.

## Request Syntax
<a name="API_DescribeTrainingPlanExtensionHistory_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TrainingPlanArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTrainingPlanExtensionHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeTrainingPlanExtensionHistory_RequestSyntax) **   <a name="sagemaker-DescribeTrainingPlanExtensionHistory-request-MaxResults"></a>
The maximum number of extensions to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeTrainingPlanExtensionHistory_RequestSyntax) **   <a name="sagemaker-DescribeTrainingPlanExtensionHistory-request-NextToken"></a>
A token to continue pagination if more results are available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [TrainingPlanArn](#API_DescribeTrainingPlanExtensionHistory_RequestSyntax) **   <a name="sagemaker-DescribeTrainingPlanExtensionHistory-request-TrainingPlanArn"></a>
The Amazon Resource Name (ARN); of the training plan to retrieve extension history for.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`
Required: Yes

## Response Syntax
<a name="API_DescribeTrainingPlanExtensionHistory_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TrainingPlanExtensions": [
      {
         "AvailabilityZone": "string",
         "AvailabilityZoneId": "string",
         "CurrencyCode": "string",
         "DurationHours": number,
         "EndDate": number,
         "ExtendedAt": number,
         "PaymentStatus": "string",
         "StartDate": number,
         "Status": "string",
         "TrainingPlanExtensionOfferingId": "string",
         "UpfrontFee": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeTrainingPlanExtensionHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeTrainingPlanExtensionHistory_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlanExtensionHistory-response-NextToken"></a>
A token to continue pagination if more results are available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [TrainingPlanExtensions](#API_DescribeTrainingPlanExtensionHistory_ResponseSyntax) **   <a name="sagemaker-DescribeTrainingPlanExtensionHistory-response-TrainingPlanExtensions"></a>
A list of extensions for the specified training plan.
Type: Array of [TrainingPlanExtension](API_TrainingPlanExtension.md) objects
Array Members: Minimum number of 0 items.

## Errors
<a name="API_DescribeTrainingPlanExtensionHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTrainingPlanExtensionHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeTrainingPlanExtensionHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeTrainingPlanExtensionHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeTrainingPlanExtensionHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeTrainingPlanExtensionHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeTrainingPlanExtensionHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeTrainingPlanExtensionHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeTrainingPlanExtensionHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeTrainingPlanExtensionHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeTrainingPlanExtensionHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeTrainingPlanExtensionHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
