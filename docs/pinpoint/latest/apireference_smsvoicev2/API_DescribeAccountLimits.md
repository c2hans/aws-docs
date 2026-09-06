---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeAccountLimits.html
---

# DescribeAccountLimits
<a name="API_DescribeAccountLimits"></a>

Describes the current AWS End User Messaging SMS SMS Voice V2 resource quotas for your account. The description for a quota includes the quota name, current usage toward that quota, and the quota's maximum value.

When you establish an AWS account, the account has initial quotas on the maximum number of configuration sets, opt-out lists, phone numbers, and pools that you can create in a given Region. For more information see [Quotas ](https://docs.aws.amazon.com/sms-voice/latest/userguide/quotas.html) in the * AWS End User Messaging SMS User Guide*.

## Request Syntax
<a name="API_DescribeAccountLimits_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAccountLimits_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeAccountLimits_RequestSyntax) **   <a name="pinpoint-DescribeAccountLimits-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeAccountLimits_RequestSyntax) **   <a name="pinpoint-DescribeAccountLimits-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

## Response Syntax
<a name="API_DescribeAccountLimits_ResponseSyntax"></a>

```
{
   "AccountLimits": [
      {
         "Max": number,
         "Name": "string",
         "Used": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAccountLimits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountLimits](#API_DescribeAccountLimits_ResponseSyntax) **   <a name="pinpoint-DescribeAccountLimits-response-AccountLimits"></a>
An array of AccountLimit objects that show the current spend limits.
Type: Array of [AccountLimit](API_AccountLimit.md) objects

 ** [NextToken](#API_DescribeAccountLimits_ResponseSyntax) **   <a name="pinpoint-DescribeAccountLimits-response-NextToken"></a>
The token to be used for the next set of paginated results. If this field is empty then there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

## Errors
<a name="API_DescribeAccountLimits_Errors"></a>

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
<a name="API_DescribeAccountLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountLimits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountLimits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountLimits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountLimits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountLimits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountLimits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountLimits)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountLimits)
