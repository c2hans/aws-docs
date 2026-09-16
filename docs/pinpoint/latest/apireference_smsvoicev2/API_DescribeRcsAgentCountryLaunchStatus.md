---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRcsAgentCountryLaunchStatus.html
---

# DescribeRcsAgentCountryLaunchStatus
<a name="API_DescribeRcsAgentCountryLaunchStatus"></a>

Retrieves the per-country launch status of an RCS agent, including carrier-level details for each country.

## Request Syntax
<a name="API_DescribeRcsAgentCountryLaunchStatus_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "IsoCountryCodes": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RcsAgentId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeRcsAgentCountryLaunchStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeRcsAgentCountryLaunchStatus_RequestSyntax) **   <a name="pinpoint-DescribeRcsAgentCountryLaunchStatus-request-Filters"></a>
An array of CountryLaunchStatusFilter objects to filter the results.
Type: Array of [CountryLaunchStatusFilter](API_CountryLaunchStatusFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [IsoCountryCodes](#API_DescribeRcsAgentCountryLaunchStatus_RequestSyntax) **   <a name="pinpoint-DescribeRcsAgentCountryLaunchStatus-request-IsoCountryCodes"></a>
An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, to filter the results.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: No

 ** [MaxResults](#API_DescribeRcsAgentCountryLaunchStatus_RequestSyntax) **   <a name="pinpoint-DescribeRcsAgentCountryLaunchStatus-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeRcsAgentCountryLaunchStatus_RequestSyntax) **   <a name="pinpoint-DescribeRcsAgentCountryLaunchStatus-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [RcsAgentId](#API_DescribeRcsAgentCountryLaunchStatus_RequestSyntax) **   <a name="pinpoint-DescribeRcsAgentCountryLaunchStatus-request-RcsAgentId"></a>
The unique identifier of the RCS agent. You can use either the RcsAgentId or RcsAgentArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeRcsAgentCountryLaunchStatus_ResponseSyntax"></a>

```
{
   "CountryLaunchStatus": [
      {
         "CarrierStatus": [
            {
               "CarrierName": "string",
               "Status": "string"
            }
         ],
         "IsoCountryCode": "string",
         "RcsPlatformId": "string",
         "RegistrationId": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string",
   "RcsAgentArn": "string",
   "RcsAgentId": "string"
}
```

## Response Elements
<a name="API_DescribeRcsAgentCountryLaunchStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CountryLaunchStatus](#API_DescribeRcsAgentCountryLaunchStatus_ResponseSyntax) **   <a name="pinpoint-DescribeRcsAgentCountryLaunchStatus-response-CountryLaunchStatus"></a>
An array of CountryLaunchStatusInformation objects that contain the per-country launch status details.
Type: Array of [CountryLaunchStatusInformation](API_CountryLaunchStatusInformation.md) objects

 ** [NextToken](#API_DescribeRcsAgentCountryLaunchStatus_ResponseSyntax) **   <a name="pinpoint-DescribeRcsAgentCountryLaunchStatus-response-NextToken"></a>
The token to be used for the next set of paginated results. If this field is empty then there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [RcsAgentArn](#API_DescribeRcsAgentCountryLaunchStatus_ResponseSyntax) **   <a name="pinpoint-DescribeRcsAgentCountryLaunchStatus-response-RcsAgentArn"></a>
The Amazon Resource Name (ARN) of the RCS agent.
Type: String

 ** [RcsAgentId](#API_DescribeRcsAgentCountryLaunchStatus_ResponseSyntax) **   <a name="pinpoint-DescribeRcsAgentCountryLaunchStatus-response-RcsAgentId"></a>
The unique identifier for the RCS agent.
Type: String

## Errors
<a name="API_DescribeRcsAgentCountryLaunchStatus_Errors"></a>

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
<a name="API_DescribeRcsAgentCountryLaunchStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgentCountryLaunchStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgentCountryLaunchStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgentCountryLaunchStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgentCountryLaunchStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgentCountryLaunchStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgentCountryLaunchStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgentCountryLaunchStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgentCountryLaunchStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgentCountryLaunchStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRcsAgentCountryLaunchStatus)
