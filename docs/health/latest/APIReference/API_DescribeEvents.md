---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEvents.html
---

# DescribeEvents
<a name="API_DescribeEvents"></a>

 Returns information about events that meet the specified filter criteria. Events are returned in a summary form and do not include the detailed description, any additional metadata that depends on the event type, or any affected resources. To retrieve that information, use the [DescribeEventDetails](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html) and [DescribeAffectedEntities](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntities.html) operations.

If no filter criteria are specified, all events are returned. Results are sorted by `lastModifiedTime`, starting with the most recent event.

**Note**
When you call the `DescribeEvents` operation and specify an entity for the `entityValues` parameter, AWS Health might return public events that aren't specific to that resource. For example, if you call `DescribeEvents` and specify an ID for an Amazon Elastic Compute Cloud (Amazon EC2) instance, AWS Health might return events that aren't specific to that resource or service. To get events that are specific to a service, use the `services` parameter in the `filter` object. For more information, see [Event](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html).
This API operation uses pagination. Specify the `nextToken` parameter in the next request to return more results.

## Request Syntax
<a name="API_DescribeEvents_RequestSyntax"></a>

```
{
   "filter": {
      "actionabilities": [ "{{string}}" ],
      "availabilityZones": [ "{{string}}" ],
      "endTimes": [
         {
            "from": {{number}},
            "to": {{number}}
         }
      ],
      "entityArns": [ "{{string}}" ],
      "entityValues": [ "{{string}}" ],
      "eventArns": [ "{{string}}" ],
      "eventStatusCodes": [ "{{string}}" ],
      "eventTypeCategories": [ "{{string}}" ],
      "eventTypeCodes": [ "{{string}}" ],
      "lastUpdatedTimes": [
         {
            "from": {{number}},
            "to": {{number}}
         }
      ],
      "personas": [ "{{string}}" ],
      "regions": [ "{{string}}" ],
      "services": [ "{{string}}" ],
      "startTimes": [
         {
            "from": {{number}},
            "to": {{number}}
         }
      ],
      "tags": [
         {
            "{{string}}" : "{{string}}"
         }
      ]
   },
   "locale": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_DescribeEvents_RequestSyntax) **   <a name="AWSHealth-DescribeEvents-request-filter"></a>
Values to narrow the results returned.
Type: [EventFilter](API_EventFilter.md) object
Required: No

 ** [locale](#API_DescribeEvents_RequestSyntax) **   <a name="AWSHealth-DescribeEvents-request-locale"></a>
The locale (language) to return information in. English (en) is the default and the only supported value at this time.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `.{2,256}`
Required: No

 ** [maxResults](#API_DescribeEvents_RequestSyntax) **   <a name="AWSHealth-DescribeEvents-request-maxResults"></a>
The maximum number of items to return in one batch, between 1 and 100, inclusive.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeEvents_RequestSyntax) **   <a name="AWSHealth-DescribeEvents-request-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`
Required: No

## Response Syntax
<a name="API_DescribeEvents_ResponseSyntax"></a>

```
{
   "events": [
      {
         "actionability": "string",
         "arn": "string",
         "availabilityZone": "string",
         "endTime": number,
         "eventScopeCode": "string",
         "eventTypeCategory": "string",
         "eventTypeCode": "string",
         "lastUpdatedTime": number,
         "personas": [ "string" ],
         "region": "string",
         "service": "string",
         "startTime": number,
         "statusCode": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_DescribeEvents_ResponseSyntax) **   <a name="AWSHealth-DescribeEvents-response-events"></a>
The events that match the specified filter criteria.
Type: Array of [Event](API_Event.md) objects

 ** [nextToken](#API_DescribeEvents_ResponseSyntax) **   <a name="AWSHealth-DescribeEvents-response-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`

## Errors
<a name="API_DescribeEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidPaginationToken **
The specified pagination token (`nextToken`) is not valid.
HTTP Status Code: 400

 ** UnsupportedLocale **
The specified locale is not supported.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
