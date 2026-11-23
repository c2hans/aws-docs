---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ListEventActors.html
---

# ListEventActors

Retrieves a paginated list of the event actors in your account that are associated with events in the specified time window. An event actor is a client that is associated with one or more events. The operation returns up to the top 100 event actors by event count. Results are paginated. Use the `NextMarker` value from the response to retrieve the next batch of results. Currently, this operation supports API Security AWS Managed Rules.

## Request Syntax
<a name="API_ListEventActors_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextMarker": "{{string}}",
   "Scope": "{{string}}",
   "SortBy": "{{string}}",
   "TimeWindow": {
      "EndTime": {{number}},
      "StartTime": {{number}}
   }
}
```

## Request Parameters
<a name="API_ListEventActors_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_ListEventActors_RequestSyntax) **   <a name="WAF-ListEventActors-request-Limit"></a>
The maximum number of event actors that you want AWS WAF to return for this request. Valid values are 1 to 100. If more event actors are available, AWS WAF returns a `NextMarker` value in the response that you can use in a subsequent call to get the next batch of event actors.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextMarker](#API_ListEventActors_RequestSyntax) **   <a name="WAF-ListEventActors-request-NextMarker"></a>
When you request a list of objects with a `Limit` setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a `NextMarker` value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** [Scope](#API_ListEventActors_RequestSyntax) **   <a name="WAF-ListEventActors-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`.
+ API and SDKs - For all calls, use the Region endpoint us-east-1.
Type: String
Valid Values: `CLOUDFRONT | REGIONAL`
Required: Yes

 ** [SortBy](#API_ListEventActors_RequestSyntax) **   <a name="WAF-ListEventActors-request-SortBy"></a>
The field to sort event actors by. The only supported value is `EVENT_COUNT`.
Type: String
Valid Values: `EVENT_COUNT`
Required: No

 ** [TimeWindow](#API_ListEventActors_RequestSyntax) **   <a name="WAF-ListEventActors-request-TimeWindow"></a>
The time range for the event actors to return. The time window can't be longer than one year.
Type: [TimeWindow](API_TimeWindow.md) object
Required: Yes

## Response Syntax
<a name="API_ListEventActors_ResponseSyntax"></a>

```
{
   "EventActors": [
      {
         "Asn": "string",
         "AsnOrganization": "string",
         "AuthFingerprint": "string",
         "ClientIp": "string",
         "Country": "string",
         "CreatedAt": number,
         "EventActorId": "string",
         "EventCount": number,
         "TlsFingerprint": "string"
      }
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListEventActors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventActors](#API_ListEventActors_ResponseSyntax) **   <a name="WAF-ListEventActors-response-EventActors"></a>
The list of event actor summaries.
Type: Array of [EventActorSummary](API_EventActorSummary.md) objects
Array Members: Maximum number of 100 items.

 ** [NextMarker](#API_ListEventActors_ResponseSyntax) **   <a name="WAF-ListEventActors-response-NextMarker"></a>
When you request a list of objects with a `Limit` setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a `NextMarker` value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

## Errors
<a name="API_ListEventActors_Errors"></a>

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

## See Also
<a name="API_ListEventActors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/ListEventActors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/ListEventActors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ListEventActors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/ListEventActors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ListEventActors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/ListEventActors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/ListEventActors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/ListEventActors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/ListEventActors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ListEventActors)
