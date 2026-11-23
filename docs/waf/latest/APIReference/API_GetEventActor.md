---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_GetEventActor.html
---

# GetEventActor

Retrieves the details of the specified event actor. An event actor is a client that is associated with one or more events. The details include the latest observed attributes of the event actor, the events that it's associated with, and the history of changes to its attributes. Currently, this operation supports API Security AWS Managed Rules.

## Request Syntax
<a name="API_GetEventActor_RequestSyntax"></a>

```
{
   "EventActorId": "{{string}}",
   "Scope": "{{string}}"
}
```

## Request Parameters
<a name="API_GetEventActor_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventActorId](#API_GetEventActor_RequestSyntax) **   <a name="WAF-GetEventActor-request-EventActorId"></a>
The unique identifier of the event actor. AWS WAF returns the event actor ID in the event details of [ListEvents](API_ListEvents.md), [ListEventsByWebACL](API_ListEventsByWebACL.md), and [GetEvent](API_GetEvent.md), and in the response to [ListEventActors](API_ListEventActors.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: Yes

 ** [Scope](#API_GetEventActor_RequestSyntax) **   <a name="WAF-GetEventActor-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`.
+ API and SDKs - For all calls, use the Region endpoint us-east-1.
Type: String
Valid Values: `CLOUDFRONT | REGIONAL`
Required: Yes

## Response Syntax
<a name="API_GetEventActor_ResponseSyntax"></a>

```
{
   "EventActor": {
      "Changes": [
         {
            "Asn": "string",
            "AsnOrganization": "string",
            "ChangeTime": number,
            "ClientIp": "string",
            "Country": "string",
            "TlsFingerprint": "string"
         }
      ],
      "Events": [
         {
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
            "EventId": "string",
            "Label": "string",
            "StartTime": number
         }
      ],
      "Summary": {
         "Asn": "string",
         "AsnOrganization": "string",
         "AuthFingerprint": "string",
         "ClientIp": "string",
         "Country": "string",
         "CreatedAt": number,
         "EventActorId": "string",
         "TlsFingerprint": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetEventActor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventActor](#API_GetEventActor_ResponseSyntax) **   <a name="WAF-GetEventActor-response-EventActor"></a>
The details of the event actor.
Type: [EventActorDetail](API_EventActorDetail.md) object

## Errors
<a name="API_GetEventActor_Errors"></a>

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
<a name="API_GetEventActor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/GetEventActor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/GetEventActor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/GetEventActor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/GetEventActor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/GetEventActor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/GetEventActor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/GetEventActor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/GetEventActor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/GetEventActor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/GetEventActor)
