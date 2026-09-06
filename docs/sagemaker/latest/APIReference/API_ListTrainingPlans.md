---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrainingPlans.html
---

# ListTrainingPlans
<a name="API_ListTrainingPlans"></a>

Retrieves a list of training plans for the current account.

## Request Syntax
<a name="API_ListTrainingPlans_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StartTimeAfter": {{number}},
   "StartTimeBefore": {{number}}
}
```

## Request Parameters
<a name="API_ListTrainingPlans_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListTrainingPlans_RequestSyntax) **   <a name="sagemaker-ListTrainingPlans-request-Filters"></a>
Additional filters to apply to the list of training plans.
Type: Array of [TrainingPlanFilter](API_TrainingPlanFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_ListTrainingPlans_RequestSyntax) **   <a name="sagemaker-ListTrainingPlans-request-MaxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListTrainingPlans_RequestSyntax) **   <a name="sagemaker-ListTrainingPlans-request-NextToken"></a>
A token to continue pagination if more results are available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListTrainingPlans_RequestSyntax) **   <a name="sagemaker-ListTrainingPlans-request-SortBy"></a>
The training plan field to sort the results by (e.g., StartTime, Status).
Type: String
Valid Values: `TrainingPlanName | StartTime | Status`
Required: No

 ** [SortOrder](#API_ListTrainingPlans_RequestSyntax) **   <a name="sagemaker-ListTrainingPlans-request-SortOrder"></a>
The order to sort the results (Ascending or Descending).
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StartTimeAfter](#API_ListTrainingPlans_RequestSyntax) **   <a name="sagemaker-ListTrainingPlans-request-StartTimeAfter"></a>
Filter to list only training plans with an actual start time after this date.
Type: Timestamp
Required: No

 ** [StartTimeBefore](#API_ListTrainingPlans_RequestSyntax) **   <a name="sagemaker-ListTrainingPlans-request-StartTimeBefore"></a>
Filter to list only training plans with an actual start time before this date.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_ListTrainingPlans_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TrainingPlanSummaries": [
      {
         "AvailableInstanceCount": number,
         "CurrencyCode": "string",
         "DurationHours": number,
         "DurationMinutes": number,
         "EndTime": number,
         "InUseInstanceCount": number,
         "ReservedCapacitySummaries": [
            {
               "AvailabilityZone": "string",
               "AvailabilityZoneId": "string",
               "DurationHours": number,
               "DurationMinutes": number,
               "EndTime": number,
               "InstanceType": "string",
               "ReservedCapacityArn": "string",
               "ReservedCapacityType": "string",
               "StartTime": number,
               "Status": "string",
               "TotalInstanceCount": number,
               "UltraServerCount": number,
               "UltraServerType": "string"
            }
         ],
         "StartTime": number,
         "Status": "string",
         "StatusMessage": "string",
         "TargetResources": [ "string" ],
         "TotalInstanceCount": number,
         "TotalUltraServerCount": number,
         "TrainingPlanArn": "string",
         "TrainingPlanName": "string",
         "UpfrontFee": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTrainingPlans_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTrainingPlans_ResponseSyntax) **   <a name="sagemaker-ListTrainingPlans-response-NextToken"></a>
A token to continue pagination if more results are available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [TrainingPlanSummaries](#API_ListTrainingPlans_ResponseSyntax) **   <a name="sagemaker-ListTrainingPlans-response-TrainingPlanSummaries"></a>
A list of summary information for the training plans.
Type: Array of [TrainingPlanSummary](API_TrainingPlanSummary.md) objects

## Errors
<a name="API_ListTrainingPlans_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListTrainingPlans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListTrainingPlans)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListTrainingPlans)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListTrainingPlans)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListTrainingPlans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListTrainingPlans)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListTrainingPlans)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListTrainingPlans)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListTrainingPlans)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListTrainingPlans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListTrainingPlans)
