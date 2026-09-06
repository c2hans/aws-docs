---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribePhoneNumbers.html
---

# DescribePhoneNumbers
<a name="API_DescribePhoneNumbers"></a>

Describes the specified origination phone number, or all the phone numbers in your account.

If you specify phone number IDs, the output includes information for only the specified phone numbers. If you specify filters, the output includes information for only those phone numbers that meet the filter criteria. If you don't specify phone number IDs or filters, the output includes information for all phone numbers.

If you specify a phone number ID that isn't valid, an error is returned.

## Request Syntax
<a name="API_DescribePhoneNumbers_RequestSyntax"></a>

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
   "PhoneNumberIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribePhoneNumbers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribePhoneNumbers_RequestSyntax) **   <a name="pinpoint-DescribePhoneNumbers-request-Filters"></a>
An array of PhoneNumberFilter objects to filter the results.
Type: Array of [PhoneNumberFilter](API_PhoneNumberFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [MaxResults](#API_DescribePhoneNumbers_RequestSyntax) **   <a name="pinpoint-DescribePhoneNumbers-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribePhoneNumbers_RequestSyntax) **   <a name="pinpoint-DescribePhoneNumbers-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [Owner](#API_DescribePhoneNumbers_RequestSyntax) **   <a name="pinpoint-DescribePhoneNumbers-request-Owner"></a>
Use `SELF` to filter the list of phone numbers to ones your account owns or use `SHARED` to filter on phone numbers shared with your account. The `Owner` and `PhoneNumberIds` parameters can't be used at the same time.
Type: String
Valid Values: `SELF | SHARED`
Required: No

 ** [PhoneNumberIds](#API_DescribePhoneNumbers_RequestSyntax) **   <a name="pinpoint-DescribePhoneNumbers-request-PhoneNumberIds"></a>
The unique identifier of phone numbers to find information about. This is an array of strings that can be either the PhoneNumberId or PhoneNumberArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

## Response Syntax
<a name="API_DescribePhoneNumbers_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PhoneNumbers": [
      {
         "CreatedTimestamp": number,
         "DeletionProtectionEnabled": boolean,
         "InternationalSendingEnabled": boolean,
         "IsoCountryCode": "string",
         "MessageType": "string",
         "MonthlyLeasingPrice": "string",
         "NumberCapabilities": [ "string" ],
         "NumberType": "string",
         "OptOutListName": "string",
         "PhoneNumber": "string",
         "PhoneNumberArn": "string",
         "PhoneNumberId": "string",
         "PoolId": "string",
         "RegistrationId": "string",
         "SelfManagedOptOutsEnabled": boolean,
         "Status": "string",
         "TwoWayChannelArn": "string",
         "TwoWayChannelRole": "string",
         "TwoWayEnabled": boolean
      }
   ]
}
```

## Response Elements
<a name="API_DescribePhoneNumbers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribePhoneNumbers_ResponseSyntax) **   <a name="pinpoint-DescribePhoneNumbers-response-NextToken"></a>
The token to be used for the next set of paginated results. If this field is empty then there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [PhoneNumbers](#API_DescribePhoneNumbers_ResponseSyntax) **   <a name="pinpoint-DescribePhoneNumbers-response-PhoneNumbers"></a>
An array of PhoneNumberInformation objects that contain the details for the requested phone numbers.
Type: Array of [PhoneNumberInformation](API_PhoneNumberInformation.md) objects

## Errors
<a name="API_DescribePhoneNumbers_Errors"></a>

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
<a name="API_DescribePhoneNumbers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribePhoneNumbers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribePhoneNumbers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribePhoneNumbers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribePhoneNumbers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribePhoneNumbers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribePhoneNumbers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribePhoneNumbers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribePhoneNumbers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribePhoneNumbers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribePhoneNumbers)
