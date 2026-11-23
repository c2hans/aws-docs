---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ListEventsByWebACL.html
---

# ListEventsByWebACL

Retrieves a paginated list of event summaries for the specified web ACL. Use this operation to monitor and investigate potential threats to the resources that the web ACL protects. Results are paginated. Use the `NextMarker` value from the response to retrieve the next batch of results. Currently, this operation supports API Security AWS Managed Rules.

You can filter the results by time window, event category, resource, and API pattern, and sort them by start time, end time, or confidence.

To retrieve the events for all of the web ACLs in your account, use [ListEvents](API_ListEvents.md). To retrieve the full details of a single event, use [GetEvent](API_GetEvent.md).

## Request Syntax
<a name="API_ListEventsByWebACL_RequestSyntax"></a>

```
{
   "ApiPatternFilters": [
      {
         "Domains": [ "{{string}}" ],
         "Method": "{{string}}",
         "PathPattern": "{{string}}",
         "Port": {{number}}
      }
   ],
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Include": [ "{{string}}" ],
   "Limit": {{number}},
   "NextMarker": "{{string}}",
   "Scope": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "TimeWindow": {
      "EndTime": {{number}},
      "StartTime": {{number}}
   },
   "WebAclArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEventsByWebACL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApiPatternFilters](#API_ListEventsByWebACL_RequestSyntax) **   <a name="WAF-ListEventsByWebACL-request-ApiPatternFilters"></a>
Filters that narrow the results to events that involve the specified API patterns. If you specify more than one API pattern filter, AWS WAF returns the events that match any of the filters. You can specify up to 20 API pattern filters.
Type: Array of [ApiPatternFilter](API_ApiPatternFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** [Filters](#API_ListEventsByWebACL_RequestSyntax) **   <a name="WAF-ListEventsByWebACL-request-Filters"></a>
Filters that narrow the results by event category or by the Amazon Resource Name (ARN) of the protected resource. You can specify up to 8 filters.
Type: Array of [EventFilter](API_EventFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Required: No

 ** [Include](#API_ListEventsByWebACL_RequestSyntax) **   <a name="WAF-ListEventsByWebACL-request-Include"></a>
Additional fields to return with each event summary. By default, the response includes only the default summary fields.
Specify `TIMELINE` to return the timeline of each event in `ApiSecurityEventDetail$Timeline`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `TIMELINE`
Required: No

 ** [Limit](#API_ListEventsByWebACL_RequestSyntax) **   <a name="WAF-ListEventsByWebACL-request-Limit"></a>
The maximum number of events that you want AWS WAF to return for this request. Valid values are 1 to 20. If more events are available, AWS WAF returns a `NextMarker` value in the response that you can use in a subsequent call to get the next batch of events.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [NextMarker](#API_ListEventsByWebACL_RequestSyntax) **   <a name="WAF-ListEventsByWebACL-request-NextMarker"></a>
When you request a list of objects with a `Limit` setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a `NextMarker` value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.
The marker is valid only for a request with the same `WebAclArn`, `TimeWindow`, `Filters`, `SortBy`, and `SortOrder` settings as the request that returned it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** [Scope](#API_ListEventsByWebACL_RequestSyntax) **   <a name="WAF-ListEventsByWebACL-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`.
+ API and SDKs - For all calls, use the Region endpoint us-east-1.
Type: String
Valid Values: `CLOUDFRONT | REGIONAL`
Required: Yes

 ** [SortBy](#API_ListEventsByWebACL_RequestSyntax) **   <a name="WAF-ListEventsByWebACL-request-SortBy"></a>
The field that AWS WAF sorts the events by. Valid values:
+  `CONFIDENCE` - Sort by the confidence level of the event detection.
+  `END_TIME` - Sort by the time that the event ended.
+  `START_TIME` - Sort by the time that the event started.
Type: String
Valid Values: `START_TIME | END_TIME | CONFIDENCE`
Required: No

 ** [SortOrder](#API_ListEventsByWebACL_RequestSyntax) **   <a name="WAF-ListEventsByWebACL-request-SortOrder"></a>
The order in which AWS WAF sorts the events. Valid values:
+  `ASC` - Sort in ascending order.
+  `DESC` - Sort in descending order. This is the default.
Type: String
Valid Values: `ASC | DESC`
Required: No

 ** [TimeWindow](#API_ListEventsByWebACL_RequestSyntax) **   <a name="WAF-ListEventsByWebACL-request-TimeWindow"></a>
The time range for the events to return. If you don't specify a time window, AWS WAF returns events from the past year. The time window can't be longer than one year.
Type: [TimeWindow](API_TimeWindow.md) object
Required: No

 ** [WebAclArn](#API_ListEventsByWebACL_RequestSyntax) **   <a name="WAF-ListEventsByWebACL-request-WebAclArn"></a>
The Amazon Resource Name (ARN) of the web ACL whose events you want to retrieve.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_ListEventsByWebACL_ResponseSyntax"></a>

```
{
   "Events": [
      {
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
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListEventsByWebACL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Events](#API_ListEventsByWebACL_ResponseSyntax) **   <a name="WAF-ListEventsByWebACL-response-Events"></a>
The list of event summaries.
Type: Array of [EventDetailSummary](API_EventDetailSummary.md) objects
Array Members: Maximum number of 100 items.

 ** [NextMarker](#API_ListEventsByWebACL_ResponseSyntax) **   <a name="WAF-ListEventsByWebACL-response-NextMarker"></a>
When you request a list of objects with a `Limit` setting, if the number of objects that are still available for retrieval exceeds the limit, AWS WAF returns a `NextMarker` value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

## Errors
<a name="API_ListEventsByWebACL_Errors"></a>

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
<a name="API_ListEventsByWebACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/ListEventsByWebACL)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/ListEventsByWebACL)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ListEventsByWebACL)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/ListEventsByWebACL)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ListEventsByWebACL)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/ListEventsByWebACL)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/ListEventsByWebACL)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/ListEventsByWebACL)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/ListEventsByWebACL)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ListEventsByWebACL)
