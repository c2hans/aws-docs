---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeAccountAttributes.html
---

# DescribeAccountAttributes
<a name="API_DescribeAccountAttributes"></a>

Describes attributes of your AWS account. The supported account attributes include account tier, which indicates whether your account is in the sandbox or production environment. When you're ready to move your account out of the sandbox, create an AWS Support case for a service limit increase request.

New accounts are placed into an SMS or voice sandbox. The sandbox protects both AWS end recipients and SMS or voice recipients from fraud and abuse.

## Request Syntax
<a name="API_DescribeAccountAttributes_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAccountAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeAccountAttributes_RequestSyntax) **   <a name="pinpoint-DescribeAccountAttributes-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeAccountAttributes_RequestSyntax) **   <a name="pinpoint-DescribeAccountAttributes-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

## Response Syntax
<a name="API_DescribeAccountAttributes_ResponseSyntax"></a>

```
{
   "AccountAttributes": [
      {
         "Name": "string",
         "Value": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAccountAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountAttributes](#API_DescribeAccountAttributes_ResponseSyntax) **   <a name="pinpoint-DescribeAccountAttributes-response-AccountAttributes"></a>
An array of AccountAttributes objects.
Type: Array of [AccountAttribute](API_AccountAttribute.md) objects

 ** [NextToken](#API_DescribeAccountAttributes_ResponseSyntax) **   <a name="pinpoint-DescribeAccountAttributes-response-NextToken"></a>
The token to be used for the next set of paginated results. If this field is empty then there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

## Errors
<a name="API_DescribeAccountAttributes_Errors"></a>

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
<a name="API_DescribeAccountAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeAccountAttributes)
