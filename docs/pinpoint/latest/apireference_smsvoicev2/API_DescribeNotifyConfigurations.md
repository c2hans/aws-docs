---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeNotifyConfigurations.html
---

# DescribeNotifyConfigurations
<a name="API_DescribeNotifyConfigurations"></a>

Describes the specified notify configurations or all notify configurations in your account.

If you specify notify configuration IDs, the output includes information for only the specified notify configurations. If you specify filters, the output includes information for only those notify configurations that meet the filter criteria. If you don't specify notify configuration IDs or filters, the output includes information for all notify configurations.

If you specify a notify configuration ID that isn't valid, an error is returned.

## Request Syntax
<a name="API_DescribeNotifyConfigurations_RequestSyntax"></a>

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
   "NotifyConfigurationIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeNotifyConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeNotifyConfigurations_RequestSyntax) **   <a name="pinpoint-DescribeNotifyConfigurations-request-Filters"></a>
An array of NotifyConfigurationFilter objects to filter the results on.
Type: Array of [NotifyConfigurationFilter](API_NotifyConfigurationFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [MaxResults](#API_DescribeNotifyConfigurations_RequestSyntax) **   <a name="pinpoint-DescribeNotifyConfigurations-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeNotifyConfigurations_RequestSyntax) **   <a name="pinpoint-DescribeNotifyConfigurations-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [NotifyConfigurationIds](#API_DescribeNotifyConfigurations_RequestSyntax) **   <a name="pinpoint-DescribeNotifyConfigurations-request-NotifyConfigurationIds"></a>
An array of notify configuration IDs to describe.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

## Response Syntax
<a name="API_DescribeNotifyConfigurations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "NotifyConfigurations": [
      {
         "CreatedTimestamp": number,
         "DefaultTemplateId": "string",
         "DeletionProtectionEnabled": boolean,
         "DisplayName": "string",
         "EnabledChannels": [ "string" ],
         "EnabledCountries": [ "string" ],
         "NotifyConfigurationArn": "string",
         "NotifyConfigurationId": "string",
         "PoolId": "string",
         "RejectionReason": "string",
         "Status": "string",
         "Tier": "string",
         "TierUpgradeStatus": "string",
         "UseCase": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeNotifyConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeNotifyConfigurations_ResponseSyntax) **   <a name="pinpoint-DescribeNotifyConfigurations-response-NextToken"></a>
The token to be used for the next set of paginated results. If this field is empty then there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [NotifyConfigurations](#API_DescribeNotifyConfigurations_ResponseSyntax) **   <a name="pinpoint-DescribeNotifyConfigurations-response-NotifyConfigurations"></a>
An array of NotifyConfigurationInformation objects that contain the results.
Type: Array of [NotifyConfigurationInformation](API_NotifyConfigurationInformation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

## Errors
<a name="API_DescribeNotifyConfigurations_Errors"></a>

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
<a name="API_DescribeNotifyConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeNotifyConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeNotifyConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeNotifyConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeNotifyConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeNotifyConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeNotifyConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeNotifyConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeNotifyConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeNotifyConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeNotifyConfigurations)
