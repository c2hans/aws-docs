---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_GetProtectConfigurationCountryRuleSet.html
---

# GetProtectConfigurationCountryRuleSet
<a name="API_GetProtectConfigurationCountryRuleSet"></a>

Retrieve the CountryRuleSet for the specified NumberCapability from a protect configuration.

## Request Syntax
<a name="API_GetProtectConfigurationCountryRuleSet_RequestSyntax"></a>

```
{
   "NumberCapability": "{{string}}",
   "ProtectConfigurationId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetProtectConfigurationCountryRuleSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NumberCapability](#API_GetProtectConfigurationCountryRuleSet_RequestSyntax) **   <a name="pinpoint-GetProtectConfigurationCountryRuleSet-request-NumberCapability"></a>
The capability type to return the CountryRuleSet for. Valid values are `SMS`, `VOICE`, or `MMS`.
Type: String
Valid Values: `SMS | VOICE | MMS | RCS`
Required: Yes

 ** [ProtectConfigurationId](#API_GetProtectConfigurationCountryRuleSet_RequestSyntax) **   <a name="pinpoint-GetProtectConfigurationCountryRuleSet-request-ProtectConfigurationId"></a>
The unique identifier for the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_GetProtectConfigurationCountryRuleSet_ResponseSyntax"></a>

```
{
   "CountryRuleSet": {
      "string" : {
         "ProtectStatus": "string"
      }
   },
   "NumberCapability": "string",
   "ProtectConfigurationArn": "string",
   "ProtectConfigurationId": "string"
}
```

## Response Elements
<a name="API_GetProtectConfigurationCountryRuleSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CountryRuleSet](#API_GetProtectConfigurationCountryRuleSet_ResponseSyntax) **   <a name="pinpoint-GetProtectConfigurationCountryRuleSet-response-CountryRuleSet"></a>
A map of ProtectConfigurationCountryRuleSetInformation objects that contain the details for the requested NumberCapability. The Key is the two-letter ISO country code. For a list of supported ISO country codes, see [Supported countries and regions (SMS channel)](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-by-country.html) in the AWS End User Messaging SMS User Guide.
Type: String to [ProtectConfigurationCountryRuleSetInformation](API_ProtectConfigurationCountryRuleSetInformation.md) object map
Map Entries: Maximum number of 300 items.
Key Length Constraints: Fixed length of 2.
Key Pattern: `[A-Z]{2}`

 ** [NumberCapability](#API_GetProtectConfigurationCountryRuleSet_ResponseSyntax) **   <a name="pinpoint-GetProtectConfigurationCountryRuleSet-response-NumberCapability"></a>
The capability type associated with the returned ProtectConfigurationCountryRuleSetInformation objects.
Type: String
Valid Values: `SMS | VOICE | MMS | RCS`

 ** [ProtectConfigurationArn](#API_GetProtectConfigurationCountryRuleSet_ResponseSyntax) **   <a name="pinpoint-GetProtectConfigurationCountryRuleSet-response-ProtectConfigurationArn"></a>
The Amazon Resource Name (ARN) of the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:\S+`

 ** [ProtectConfigurationId](#API_GetProtectConfigurationCountryRuleSet_ResponseSyntax) **   <a name="pinpoint-GetProtectConfigurationCountryRuleSet-response-ProtectConfigurationId"></a>
The unique identifier for the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

## Errors
<a name="API_GetProtectConfigurationCountryRuleSet_Errors"></a>

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
<a name="API_GetProtectConfigurationCountryRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/GetProtectConfigurationCountryRuleSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/GetProtectConfigurationCountryRuleSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/GetProtectConfigurationCountryRuleSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/GetProtectConfigurationCountryRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/GetProtectConfigurationCountryRuleSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/GetProtectConfigurationCountryRuleSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/GetProtectConfigurationCountryRuleSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/GetProtectConfigurationCountryRuleSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/GetProtectConfigurationCountryRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/GetProtectConfigurationCountryRuleSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
