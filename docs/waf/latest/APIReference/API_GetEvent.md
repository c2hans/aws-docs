---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_GetEvent.html
---

# GetEvent

Retrieves the details of the specified event for the specified web ACL, including the event actors that are associated with the event and the event timeline. Currently, this operation supports API Security AWS Managed Rules.

## Request Syntax
<a name="API_GetEvent_RequestSyntax"></a>

```
{
   "EventId": "{{string}}",
   "Scope": "{{string}}",
   "WebAclArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetEvent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventId](#API_GetEvent_RequestSyntax) **   <a name="WAF-GetEvent-request-EventId"></a>
The unique identifier of the event. AWS WAF returns the event ID in the responses to [ListEvents](API_ListEvents.md) and [ListEventsByWebACL](API_ListEventsByWebACL.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: Yes

 ** [Scope](#API_GetEvent_RequestSyntax) **   <a name="WAF-GetEvent-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`.
+ API and SDKs - For all calls, use the Region endpoint us-east-1.
Type: String
Valid Values: `CLOUDFRONT | REGIONAL`
Required: Yes

 ** [WebAclArn](#API_GetEvent_RequestSyntax) **   <a name="WAF-GetEvent-request-WebAclArn"></a>
The Amazon Resource Name (ARN) of the web ACL that the event is associated with.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_GetEvent_ResponseSyntax"></a>

```
{
   "Event": {
      "ApiSecurityEventDetail": {
         "ApiPatterns": [
            {
               "Domains": [ "string" ],
               "Method": "string",
               "PathPattern": "string",
               "Port": number
            }
         ],
         "Category": "string",
         "Confidence": "string",
         "EventActors": [
            {
               "EventActorId": "string",
               "EventActorValue": "string"
            }
         ],
         "Label": "string",
         "Timeline": [
            {
               "ApiPatterns": [
                  {
                     "Domains": [ "string" ],
                     "Method": "string",
                     "PathPattern": "string",
                     "Port": number
                  }
               ],
               "ChangeTime": number,
               "Confidence": "string",
               "Label": "string"
            }
         ]
      },
      "EndTime": number,
      "EventCategory": "string",
      "EventId": "string",
      "EventStatus": "string",
      "LastUpdatedTime": number,
      "ResourceArn": "string",
      "StartTime": number,
      "WebAclArn": "string"
   }
}
```

## Response Elements
<a name="API_GetEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Event](#API_GetEvent_ResponseSyntax) **   <a name="WAF-GetEvent-response-Event"></a>
The details of the event.
Type: [EventDetailSummary](API_EventDetailSummary.md) object

## Errors
<a name="API_GetEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFInternalErrorException **
Your request is valid, but AWS WAF couldn’t perform the operation because of a system problem. Retry your request.
HTTP Status Code: 500

 ** WAFInvalidOperationException **
The operation isn't valid.
HTTP Status Code: 400

 ** WAFInvalidParameterException **
The operation failed because AWS WAF didn't recognize a parameter in the request. For example:
+ You specified a parameter name or value that isn't valid.
+ Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested.
+ You tried to update a `WebACL` with a `DefaultAction` that isn't among the types available at [DefaultAction](API_DefaultAction.md).
+ Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.
 ** Field **
The settings where the invalid parameter was found.
 ** Parameter **
The invalid parameter that resulted in the exception.
 ** Reason **
Additional information about the exception.
HTTP Status Code: 400

 ** WAFNonexistentItemException **
 AWS WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate.
HTTP Status Code: 400

## See Also
<a name="API_GetEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/GetEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/GetEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/GetEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/GetEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/GetEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/GetEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/GetEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/GetEvent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/GetEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/GetEvent)
