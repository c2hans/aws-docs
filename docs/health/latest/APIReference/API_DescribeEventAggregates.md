---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventAggregates.html
---

# DescribeEventAggregates
<a name="API_DescribeEventAggregates"></a>

Returns the number of events of each event type (issue, scheduled change, and account notification). If no filter is specified, the counts of all events in each category are returned.

**Note**
This API operation uses pagination. Specify the `nextToken` parameter in the next request to return more results.

## Request Syntax
<a name="API_DescribeEventAggregates_RequestSyntax"></a>

```
{
   "aggregateField": "{{string}}",
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
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEventAggregates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [aggregateField](#API_DescribeEventAggregates_RequestSyntax) **   <a name="AWSHealth-DescribeEventAggregates-request-aggregateField"></a>
The only currently supported value is `eventTypeCategory`.
Type: String
Valid Values: `eventTypeCategory`
Required: Yes

 ** [filter](#API_DescribeEventAggregates_RequestSyntax) **   <a name="AWSHealth-DescribeEventAggregates-request-filter"></a>
Values to narrow the results returned.
Type: [EventFilter](API_EventFilter.md) object
Required: No

 ** [maxResults](#API_DescribeEventAggregates_RequestSyntax) **   <a name="AWSHealth-DescribeEventAggregates-request-maxResults"></a>
The maximum number of items to return in one batch, between 10 and 100, inclusive.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeEventAggregates_RequestSyntax) **   <a name="AWSHealth-DescribeEventAggregates-request-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`
Required: No

## Response Syntax
<a name="API_DescribeEventAggregates_ResponseSyntax"></a>

```
{
   "eventAggregates": [
      {
         "aggregateValue": "string",
         "count": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeEventAggregates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [eventAggregates](#API_DescribeEventAggregates_ResponseSyntax) **   <a name="AWSHealth-DescribeEventAggregates-response-eventAggregates"></a>
The number of events in each category that meet the optional filter criteria.
Type: Array of [EventAggregate](API_EventAggregate.md) objects

 ** [nextToken](#API_DescribeEventAggregates_ResponseSyntax) **   <a name="AWSHealth-DescribeEventAggregates-response-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`

## Errors
<a name="API_DescribeEventAggregates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidPaginationToken **
The specified pagination token (`nextToken`) is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEventAggregates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeEventAggregates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeEventAggregates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeEventAggregates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeEventAggregates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeEventAggregates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeEventAggregates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeEventAggregates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeEventAggregates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeEventAggregates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeEventAggregates)
