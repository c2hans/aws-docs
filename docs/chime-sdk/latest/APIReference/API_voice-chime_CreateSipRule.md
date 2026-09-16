---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipRule.html
---

# CreateSipRule
<a name="API_voice-chime_CreateSipRule"></a>

Creates a SIP rule, which can be used to run a SIP media application as a target for a specific trigger type. For more information about SIP rules, see [Managing SIP media applications and rules](https://docs.aws.amazon.com/chime-sdk/latest/ag/manage-sip-applications.html) in the *Amazon Chime SDK Administrator Guide*.

## Request Syntax
<a name="API_voice-chime_CreateSipRule_RequestSyntax"></a>

```
POST /sip-rules HTTP/1.1
Content-type: application/json

{
   "Disabled": {{boolean}},
   "Name": "{{string}}",
   "TargetApplications": [
      {
         "AwsRegion": "{{string}}",
         "Priority": {{number}},
         "SipMediaApplicationId": "{{string}}"
      }
   ],
   "TriggerType": "{{string}}",
   "TriggerValue": "{{string}}"
}
```

## URI Request Parameters
<a name="API_voice-chime_CreateSipRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_voice-chime_CreateSipRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Disabled](#API_voice-chime_CreateSipRule_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipRule-request-Disabled"></a>
Disables or enables a SIP rule. You must disable SIP rules before you can delete them.
Type: Boolean
Required: No

 ** [Name](#API_voice-chime_CreateSipRule_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipRule-request-Name"></a>
The name of the SIP rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: Yes

 ** [TargetApplications](#API_voice-chime_CreateSipRule_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipRule-request-TargetApplications"></a>
List of SIP media applications, with priority and AWS Region. Only one SIP application per AWS Region can be used.
Type: Array of [SipRuleTargetApplication](API_voice-chime_SipRuleTargetApplication.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: No

 ** [TriggerType](#API_voice-chime_CreateSipRule_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipRule-request-TriggerType"></a>
The type of trigger assigned to the SIP rule in `TriggerValue`, currently `RequestUriHostname` or `ToPhoneNumber`.
Type: String
Valid Values: `ToPhoneNumber | RequestUriHostname`
Required: Yes

 ** [TriggerValue](#API_voice-chime_CreateSipRule_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipRule-request-TriggerValue"></a>
If `TriggerType` is `RequestUriHostname`, the value can be the outbound host name of a Voice Connector. If `TriggerType` is `ToPhoneNumber`, the value can be a customer-owned phone number in the E164 format. The `SipMediaApplication` specified in the `SipRule` is triggered if the request URI in an incoming SIP request matches the `RequestUriHostname`, or if the `To` header in the incoming SIP request matches the `ToPhoneNumber` value.
Type: String
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_voice-chime_CreateSipRule_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "SipRule": {
      "CreatedTimestamp": "string",
      "Disabled": boolean,
      "Name": "string",
      "SipRuleId": "string",
      "TargetApplications": [
         {
            "AwsRegion": "string",
            "Priority": number,
            "SipMediaApplicationId": "string"
         }
      ],
      "TriggerType": "string",
      "TriggerValue": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_voice-chime_CreateSipRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [SipRule](#API_voice-chime_CreateSipRule_ResponseSyntax) **   <a name="chimesdk-voice-chime_CreateSipRule-response-SipRule"></a>
The SIP rule information, including the rule ID, triggers, and target applications.
Type: [SipRule](API_voice-chime_SipRule.md) object

## Errors
<a name="API_voice-chime_CreateSipRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** AccessDeniedException **
You don't have the permissions needed to run this action.
HTTP Status Code: 403

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ConflictException **
Multiple instances of the same request were made simultaneously.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The number of customer requests exceeds the request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client isn't authorized to request a resource.
HTTP Status Code: 401

## See Also
<a name="API_voice-chime_CreateSipRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/CreateSipRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/CreateSipRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/CreateSipRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/CreateSipRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/CreateSipRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/CreateSipRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/CreateSipRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/CreateSipRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/CreateSipRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/CreateSipRule)
