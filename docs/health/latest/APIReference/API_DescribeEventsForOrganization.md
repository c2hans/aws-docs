---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventsForOrganization.html
---

# DescribeEventsForOrganization
<a name="API_DescribeEventsForOrganization"></a>

Returns information about events across your organization in AWS Organizations. You can use the`filters` parameter to specify the events that you want to return. Events are returned in a summary form and don't include the affected accounts, detailed description, any additional metadata that depends on the event type, or any affected resources. To retrieve that information, use the following operations:
+  [DescribeAffectedAccountsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedAccountsForOrganization.html)
+  [DescribeEventDetailsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html)
+  [DescribeAffectedEntitiesForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntitiesForOrganization.html)

If you don't specify a `filter`, the `DescribeEventsForOrganizations` returns all events across your organization. Results are sorted by `lastModifiedTime`, starting with the most recent event.

For more information about the different types of AWS Health events, see [Event](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html).

Before you can call this operation, you must first enable AWS Health to work with AWS Organizations. To do this, call the [EnableHealthServiceAccessForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html) operation from your organization's management account.

**Note**
This API operation uses pagination. Specify the `nextToken` parameter in the next request to return more results.

## Request Syntax
<a name="API_DescribeEventsForOrganization_RequestSyntax"></a>

```
{
   "filter": {
      "actionabilities": [ "{{string}}" ],
      "awsAccountIds": [ "{{string}}" ],
      "endTime": {
         "from": {{number}},
         "to": {{number}}
      },
      "entityArns": [ "{{string}}" ],
      "entityValues": [ "{{string}}" ],
      "eventStatusCodes": [ "{{string}}" ],
      "eventTypeCategories": [ "{{string}}" ],
      "eventTypeCodes": [ "{{string}}" ],
      "lastUpdatedTime": {
         "from": {{number}},
         "to": {{number}}
      },
      "personas": [ "{{string}}" ],
      "regions": [ "{{string}}" ],
      "services": [ "{{string}}" ],
      "startTime": {
         "from": {{number}},
         "to": {{number}}
      }
   },
   "locale": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEventsForOrganization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_DescribeEventsForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeEventsForOrganization-request-filter"></a>
Values to narrow the results returned.
Type: [OrganizationEventFilter](API_OrganizationEventFilter.md) object
Required: No

 ** [locale](#API_DescribeEventsForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeEventsForOrganization-request-locale"></a>
The locale (language) to return information in. English (en) is the default and the only supported value at this time.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `.{2,256}`
Required: No

 ** [maxResults](#API_DescribeEventsForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeEventsForOrganization-request-maxResults"></a>
The maximum number of items to return in one batch, between 1 and 100, inclusive.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeEventsForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeEventsForOrganization-request-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`
Required: No

## Response Syntax
<a name="API_DescribeEventsForOrganization_ResponseSyntax"></a>

```
{
   "events": [
      {
         "actionability": "string",
         "arn": "string",
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
<a name="API_DescribeEventsForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_DescribeEventsForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeEventsForOrganization-response-events"></a>
The events that match the specified filter criteria.
Type: Array of [OrganizationEvent](API_OrganizationEvent.md) objects

 ** [nextToken](#API_DescribeEventsForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeEventsForOrganization-response-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`

## Errors
<a name="API_DescribeEventsForOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidPaginationToken **
The specified pagination token (`nextToken`) is not valid.
HTTP Status Code: 400

 ** UnsupportedLocale **
The specified locale is not supported.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEventsForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeEventsForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeEventsForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeEventsForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeEventsForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeEventsForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeEventsForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeEventsForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeEventsForOrganization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeEventsForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeEventsForOrganization)
