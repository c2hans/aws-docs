---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeSpendLimits.html
---

# DescribeSpendLimits
<a name="API_DescribeSpendLimits"></a>

Describes the current monthly spend limits for sending voice and text messages.

When you establish an AWS account, the account has initial monthly spend limit in a given Region. For more information on increasing your monthly spend limit, see [ Requesting increases to your monthly SMS, MMS, or Voice spending quota ](https://docs.aws.amazon.com/sms-voice/latest/userguide/awssupport-spend-threshold.html) in the * AWS End User Messaging SMS User Guide*.

## Request Syntax
<a name="API_DescribeSpendLimits_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSpendLimits_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeSpendLimits_RequestSyntax) **   <a name="pinpoint-DescribeSpendLimits-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeSpendLimits_RequestSyntax) **   <a name="pinpoint-DescribeSpendLimits-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

## Response Syntax
<a name="API_DescribeSpendLimits_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SpendLimits": [
      {
         "EnforcedLimit": number,
         "MaxLimit": number,
         "Name": "string",
         "Overridden": boolean
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSpendLimits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeSpendLimits_ResponseSyntax) **   <a name="pinpoint-DescribeSpendLimits-response-NextToken"></a>
The token to be used for the next set of paginated results. If this field is empty then there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [SpendLimits](#API_DescribeSpendLimits_ResponseSyntax) **   <a name="pinpoint-DescribeSpendLimits-response-SpendLimits"></a>
An array of SpendLimit objects that contain the details for the requested spend limits.
Type: Array of [SpendLimit](API_SpendLimit.md) objects

## Errors
<a name="API_DescribeSpendLimits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ThrottlingException **
An error that occurred because too many requests were sent during a certain amount of time.
HTTP Status Code: 400

 ** ValidationException **
A validation exception for a field.
 ** Fields **
The field that failed validation.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSpendLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeSpendLimits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeSpendLimits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeSpendLimits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeSpendLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeSpendLimits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeSpendLimits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeSpendLimits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeSpendLimits)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeSpendLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeSpendLimits)
