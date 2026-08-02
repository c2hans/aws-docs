---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeSenderIds.html
---

# DescribeSenderIds
<a name="API_DescribeSenderIds"></a>

Describes the specified SenderIds or all SenderIds associated with your AWS account.

If you specify SenderIds, the output includes information for only the specified SenderIds. If you specify filters, the output includes information for only those SenderIds that meet the filter criteria. If you don't specify SenderIds or filters, the output includes information for all SenderIds.

f you specify a sender ID that isn't valid, an error is returned.

## Request Syntax
<a name="API_DescribeSenderIds_RequestSyntax"></a>

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
   "Owner": "{{string}}",
   "SenderIds": [
      {
         "IsoCountryCode": "{{string}}",
         "SenderId": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_DescribeSenderIds_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeSenderIds_RequestSyntax) **   <a name="pinpoint-DescribeSenderIds-request-Filters"></a>
An array of SenderIdFilter objects to filter the results.
Type: Array of [SenderIdFilter](API_SenderIdFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [MaxResults](#API_DescribeSenderIds_RequestSyntax) **   <a name="pinpoint-DescribeSenderIds-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeSenderIds_RequestSyntax) **   <a name="pinpoint-DescribeSenderIds-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [Owner](#API_DescribeSenderIds_RequestSyntax) **   <a name="pinpoint-DescribeSenderIds-request-Owner"></a>
Use `SELF` to filter the list of Sender Ids to ones your account owns or use `SHARED` to filter on Sender Ids shared with your account. The `Owner` and `SenderIds` parameters can't be used at the same time.
Type: String
Valid Values: `SELF | SHARED`
Required: No

 ** [SenderIds](#API_DescribeSenderIds_RequestSyntax) **   <a name="pinpoint-DescribeSenderIds-request-SenderIds"></a>
An array of SenderIdAndCountry objects to search for.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: Array of [SenderIdAndCountry](API_SenderIdAndCountry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## Response Syntax
<a name="API_DescribeSenderIds_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SenderIds": [
      {
         "DeletionProtectionEnabled": boolean,
         "IsoCountryCode": "string",
         "MessageTypes": [ "string" ],
         "MonthlyLeasingPrice": "string",
         "Registered": boolean,
         "RegistrationId": "string",
         "SenderId": "string",
         "SenderIdArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSenderIds_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeSenderIds_ResponseSyntax) **   <a name="pinpoint-DescribeSenderIds-response-NextToken"></a>
The token to be used for the next set of paginated results. If this field is empty then there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [SenderIds](#API_DescribeSenderIds_ResponseSyntax) **   <a name="pinpoint-DescribeSenderIds-response-SenderIds"></a>
An array of SernderIdInformation objects that contain the details for the requested SenderIds.
Type: Array of [SenderIdInformation](API_SenderIdInformation.md) objects

## Errors
<a name="API_DescribeSenderIds_Errors"></a>

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
<a name="API_DescribeSenderIds_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeSenderIds)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeSenderIds)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeSenderIds)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeSenderIds)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeSenderIds)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeSenderIds)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeSenderIds)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeSenderIds)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeSenderIds)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeSenderIds)
