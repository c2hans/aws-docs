---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrainingSessions.html
---

# ListTrainingSessions
<a name="API_ListTrainingSessions"></a>

Lists training sessions in your account. You can filter results by creation time, name, and status. The operation paginates results. To retrieve additional results, use the `NextToken` parameter.

The following operations are related to `ListTrainingSessions`:
+  `CreateTrainingSession`
+  `DescribeTrainingSession`

## Request Syntax
<a name="API_ListTrainingSessions_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTrainingSessions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListTrainingSessions_RequestSyntax) **   <a name="sagemaker-ListTrainingSessions-request-CreationTimeAfter"></a>
A filter that returns only training sessions created after the specified time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListTrainingSessions_RequestSyntax) **   <a name="sagemaker-ListTrainingSessions-request-CreationTimeBefore"></a>
A filter that returns only training sessions created before the specified time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListTrainingSessions_RequestSyntax) **   <a name="sagemaker-ListTrainingSessions-request-MaxResults"></a>
The maximum number of training sessions to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListTrainingSessions_RequestSyntax) **   <a name="sagemaker-ListTrainingSessions-request-NameContains"></a>
A string in the training session name to filter results. Only sessions whose name contains the specified string are returned.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListTrainingSessions_RequestSyntax) **   <a name="sagemaker-ListTrainingSessions-request-NextToken"></a>
If the response was truncated, use the token returned in the previous response to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [StatusEquals](#API_ListTrainingSessions_RequestSyntax) **   <a name="sagemaker-ListTrainingSessions-request-StatusEquals"></a>
A filter that returns only training sessions with the specified status.
Type: String
Valid Values: `Created | Blocked | Running | Failed | Scheduled | Stopping | Stopped | Expired | Deleting | DeletionFailed`
Required: No

## Response Syntax
<a name="API_ListTrainingSessions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TrainingSessionSummaries": [
      {
         "CreationTime": number,
         "LastModifiedTime": number,
         "TrainingSessionArn": "string",
         "TrainingSessionStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTrainingSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTrainingSessions_ResponseSyntax) **   <a name="sagemaker-ListTrainingSessions-response-NextToken"></a>
If the response is truncated, this token retrieves the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [TrainingSessionSummaries](#API_ListTrainingSessions_ResponseSyntax) **   <a name="sagemaker-ListTrainingSessions-response-TrainingSessionSummaries"></a>
An array of `TrainingSessionSummary` objects that provide summary information about the training sessions.
Type: Array of [TrainingSessionSummary](API_TrainingSessionSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListTrainingSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListTrainingSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListTrainingSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListTrainingSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListTrainingSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListTrainingSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListTrainingSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListTrainingSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListTrainingSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListTrainingSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListTrainingSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListTrainingSessions)
