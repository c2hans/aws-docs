---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventTypes.html
---

# DescribeEventTypes
<a name="API_DescribeEventTypes"></a>

Returns the event types that meet the specified filter criteria. You can use this API operation to find information about the AWS Health event, such as the category, AWS service, and event code. The metadata for each event appears in the [EventType](https://docs.aws.amazon.com/health/latest/APIReference/API_EventType.html) object.

If you don't specify a filter criteria, the API operation returns all event types, in no particular order.

**Note**
This API operation uses pagination. Specify the `nextToken` parameter in the next request to return more results.

## Request Syntax
<a name="API_DescribeEventTypes_RequestSyntax"></a>

```
{
   "filter": {
      "actionabilities": [ "{{string}}" ],
      "eventTypeCategories": [ "{{string}}" ],
      "eventTypeCodes": [ "{{string}}" ],
      "personas": [ "{{string}}" ],
      "services": [ "{{string}}" ]
   },
   "locale": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEventTypes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_DescribeEventTypes_RequestSyntax) **   <a name="AWSHealth-DescribeEventTypes-request-filter"></a>
Values to narrow the results returned.
Type: [EventTypeFilter](API_EventTypeFilter.md) object
Required: No

 ** [locale](#API_DescribeEventTypes_RequestSyntax) **   <a name="AWSHealth-DescribeEventTypes-request-locale"></a>
The locale (language) to return information in. English (en) is the default and the only supported value at this time.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `.{2,256}`
Required: No

 ** [maxResults](#API_DescribeEventTypes_RequestSyntax) **   <a name="AWSHealth-DescribeEventTypes-request-maxResults"></a>
The maximum number of items to return in one batch, between 10 and 100, inclusive.
If you don't specify the `maxResults` parameter, this operation returns a maximum of 30 items by default.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeEventTypes_RequestSyntax) **   <a name="AWSHealth-DescribeEventTypes-request-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`
Required: No

## Response Syntax
<a name="API_DescribeEventTypes_ResponseSyntax"></a>

```
{
   "eventTypes": [
      {
         "actionability": "string",
         "category": "string",
         "code": "string",
         "personas": [ "string" ],
         "service": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeEventTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [eventTypes](#API_DescribeEventTypes_ResponseSyntax) **   <a name="AWSHealth-DescribeEventTypes-response-eventTypes"></a>
A list of event types that match the filter criteria. Event types have a category (`issue`, `accountNotification`, or `scheduledChange`), a service (for example, `EC2`, `RDS`, `DATAPIPELINE`, `BILLING`), and a code (in the format `AWS_SERVICE_DESCRIPTION `; for example, `AWS_EC2_SYSTEM_MAINTENANCE_EVENT`).
Type: Array of [EventType](API_EventType.md) objects

 ** [nextToken](#API_DescribeEventTypes_ResponseSyntax) **   <a name="AWSHealth-DescribeEventTypes-response-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`

## Errors
<a name="API_DescribeEventTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidPaginationToken **
The specified pagination token (`nextToken`) is not valid.
HTTP Status Code: 400

 ** UnsupportedLocale **
The specified locale is not supported.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEventTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeEventTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeEventTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeEventTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeEventTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeEventTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeEventTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeEventTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeEventTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeEventTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeEventTypes)
