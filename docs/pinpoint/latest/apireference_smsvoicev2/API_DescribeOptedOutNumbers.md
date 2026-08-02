---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeOptedOutNumbers.html
---

# DescribeOptedOutNumbers
<a name="API_DescribeOptedOutNumbers"></a>

Describes the specified opted out destination numbers or all opted out destination numbers in an opt-out list.

If you specify opted out numbers, the output includes information for only the specified opted out numbers. If you specify filters, the output includes information for only those opted out numbers that meet the filter criteria. If you don't specify opted out numbers or filters, the output includes information for all opted out destination numbers in your opt-out list.

If you specify an opted out number that isn't valid, an exception is returned.

## Request Syntax
<a name="API_DescribeOptedOutNumbers_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OptedOutNumbers": [ "{{string}}" ],
   "OptOutListName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeOptedOutNumbers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeOptedOutNumbers_RequestSyntax) **   <a name="pinpoint-DescribeOptedOutNumbers-request-Filters"></a>
An array of OptedOutFilter objects to filter the results on.
Type: Array of [OptedOutFilter](API_OptedOutFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [MaxResults](#API_DescribeOptedOutNumbers_RequestSyntax) **   <a name="pinpoint-DescribeOptedOutNumbers-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeOptedOutNumbers_RequestSyntax) **   <a name="pinpoint-DescribeOptedOutNumbers-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [OptedOutNumbers](#API_DescribeOptedOutNumbers_RequestSyntax) **   <a name="pinpoint-DescribeOptedOutNumbers-request-OptedOutNumbers"></a>
An array of phone numbers to search for in the OptOutList.
If you specify an opted out number that isn't valid, an exception is returned.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: No

 ** [OptOutListName](#API_DescribeOptedOutNumbers_RequestSyntax) **   <a name="pinpoint-DescribeOptedOutNumbers-request-OptOutListName"></a>
The OptOutListName or OptOutListArn of the OptOutList. You can use [DescribeOptOutLists](API_DescribeOptOutLists.md) to find the values for OptOutListName and OptOutListArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeOptedOutNumbers_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "OptedOutNumbers": [
      {
         "EndUserOptedOut": boolean,
         "OptedOutNumber": "string",
         "OptedOutTimestamp": number
      }
   ],
   "OptOutListArn": "string",
   "OptOutListName": "string"
}
```

## Response Elements
<a name="API_DescribeOptedOutNumbers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeOptedOutNumbers_ResponseSyntax) **   <a name="pinpoint-DescribeOptedOutNumbers-response-NextToken"></a>
The token to be used for the next set of paginated results. If this field is empty then there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [OptedOutNumbers](#API_DescribeOptedOutNumbers_ResponseSyntax) **   <a name="pinpoint-DescribeOptedOutNumbers-response-OptedOutNumbers"></a>
An array of OptedOutNumbersInformation objects that provide information about the requested OptedOutNumbers.
Type: Array of [OptedOutNumberInformation](API_OptedOutNumberInformation.md) objects

 ** [OptOutListArn](#API_DescribeOptedOutNumbers_ResponseSyntax) **   <a name="pinpoint-DescribeOptedOutNumbers-response-OptOutListArn"></a>
The Amazon Resource Name (ARN) of the OptOutList.
Type: String

 ** [OptOutListName](#API_DescribeOptedOutNumbers_ResponseSyntax) **   <a name="pinpoint-DescribeOptedOutNumbers-response-OptOutListName"></a>
The name of the OptOutList.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

## Errors
<a name="API_DescribeOptedOutNumbers_Errors"></a>

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

 ** ResourceNotFoundException **
A requested resource couldn't be found.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

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
<a name="API_DescribeOptedOutNumbers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeOptedOutNumbers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeOptedOutNumbers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeOptedOutNumbers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeOptedOutNumbers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeOptedOutNumbers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeOptedOutNumbers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeOptedOutNumbers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeOptedOutNumbers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeOptedOutNumbers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeOptedOutNumbers)
