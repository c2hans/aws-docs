---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipRule.html
---

# UpdateSipRule
<a name="API_voice-chime_UpdateSipRule"></a>

Updates the details of the specified SIP rule.

## Request Syntax
<a name="API_voice-chime_UpdateSipRule_RequestSyntax"></a>

```
PUT /sip-rules/{{sipRuleId}} HTTP/1.1
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
   ]
}
```

## URI Request Parameters
<a name="API_voice-chime_UpdateSipRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sipRuleId](#API_voice-chime_UpdateSipRule_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateSipRule-request-uri-SipRuleId"></a>
The SIP rule ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_UpdateSipRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Disabled](#API_voice-chime_UpdateSipRule_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateSipRule-request-Disabled"></a>
The new value that indicates whether the rule is disabled.
Type: Boolean
Required: No

 ** [Name](#API_voice-chime_UpdateSipRule_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateSipRule-request-Name"></a>
The new name for the specified SIP rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: Yes

 ** [TargetApplications](#API_voice-chime_UpdateSipRule_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateSipRule-request-TargetApplications"></a>
The new list of target applications.
Type: Array of [SipRuleTargetApplication](API_voice-chime_SipRuleTargetApplication.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: No

## Response Syntax
<a name="API_voice-chime_UpdateSipRule_ResponseSyntax"></a>

```
HTTP/1.1 202
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
<a name="API_voice-chime_UpdateSipRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [SipRule](#API_voice-chime_UpdateSipRule_ResponseSyntax) **   <a name="chimesdk-voice-chime_UpdateSipRule-response-SipRule"></a>
The updated SIP rule details.
Type: [SipRule](API_voice-chime_SipRule.md) object

## Errors
<a name="API_voice-chime_UpdateSipRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ConflictException **
Multiple instances of the same request were made simultaneously.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
The requested resource couldn't be found.
HTTP Status Code: 404

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
<a name="API_voice-chime_UpdateSipRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/UpdateSipRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/UpdateSipRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/UpdateSipRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/UpdateSipRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/UpdateSipRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/UpdateSipRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/UpdateSipRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/UpdateSipRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/UpdateSipRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/UpdateSipRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
