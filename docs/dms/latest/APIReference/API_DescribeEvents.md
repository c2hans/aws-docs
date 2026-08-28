---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEvents.html
---

# DescribeEvents
<a name="API_DescribeEvents"></a>

 Lists events for a given source identifier and source type. You can also specify a start and end time. For more information on AWS DMS events, see [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html) in the * AWS Database Migration Service User Guide.*

## Request Syntax
<a name="API_DescribeEvents_RequestSyntax"></a>

```
{
   "Duration": {{number}},
   "EndTime": {{number}},
   "EventCategories": [ "{{string}}" ],
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}},
   "SourceIdentifier": "{{string}}",
   "SourceType": "{{string}}",
   "StartTime": {{number}}
}
```

## Request Parameters
<a name="API_DescribeEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Duration](#API_DescribeEvents_RequestSyntax) **   <a name="DMS-DescribeEvents-request-Duration"></a>
The duration of the events to be listed.
Type: Integer
Required: No

 ** [EndTime](#API_DescribeEvents_RequestSyntax) **   <a name="DMS-DescribeEvents-request-EndTime"></a>
The end time for the events to be listed.
Type: Timestamp
Required: No

 ** [EventCategories](#API_DescribeEvents_RequestSyntax) **   <a name="DMS-DescribeEvents-request-EventCategories"></a>
A list of event categories for the source type that you've chosen.
Type: Array of strings
Required: No

 ** [Filters](#API_DescribeEvents_RequestSyntax) **   <a name="DMS-DescribeEvents-request-Filters"></a>
Filters applied to events. The only valid filter is `replication-instance-id`.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeEvents_RequestSyntax) **   <a name="DMS-DescribeEvents-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeEvents_RequestSyntax) **   <a name="DMS-DescribeEvents-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

 ** [SourceIdentifier](#API_DescribeEvents_RequestSyntax) **   <a name="DMS-DescribeEvents-request-SourceIdentifier"></a>
 The identifier of an event source.
Type: String
Required: No

 ** [SourceType](#API_DescribeEvents_RequestSyntax) **   <a name="DMS-DescribeEvents-request-SourceType"></a>
The type of AWS DMS resource that generates events.
Valid values: replication-instance \| replication-task
Type: String
Valid Values: `replication-instance`
Required: No

 ** [StartTime](#API_DescribeEvents_RequestSyntax) **   <a name="DMS-DescribeEvents-request-StartTime"></a>
The start time for the events to be listed.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_DescribeEvents_ResponseSyntax"></a>

```
{
   "Events": [
      {
         "Date": number,
         "EventCategories": [ "string" ],
         "Message": "string",
         "SourceIdentifier": "string",
         "SourceType": "string"
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_DescribeEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Events](#API_DescribeEvents_ResponseSyntax) **   <a name="DMS-DescribeEvents-response-Events"></a>
The events described.
Type: Array of [Event](API_Event.md) objects

 ** [Marker](#API_DescribeEvents_ResponseSyntax) **   <a name="DMS-DescribeEvents-response-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

## Errors
<a name="API_DescribeEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
