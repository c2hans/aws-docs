---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeEvents.html
---

# DescribeEvents
<a name="API_DescribeEvents"></a>

Returns events related to clusters, security groups, and parameter groups. You can obtain events specific to a particular cluster, security group, or parameter group by providing the name as a parameter. By default, only the events occurring within the last hour are returned; however, you can retrieve up to 14 days' worth of events if necessary.

## Request Syntax
<a name="API_DescribeEvents_RequestSyntax"></a>

```
{
   "Duration": {{number}},
   "EndTime": {{number}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SourceName": "{{string}}",
   "SourceType": "{{string}}",
   "StartTime": {{number}}
}
```

## Request Parameters
<a name="API_DescribeEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Duration](#API_DescribeEvents_RequestSyntax) **   <a name="MemoryDB-DescribeEvents-request-Duration"></a>
The number of minutes worth of events to retrieve.
Type: Integer
Required: No

 ** [EndTime](#API_DescribeEvents_RequestSyntax) **   <a name="MemoryDB-DescribeEvents-request-EndTime"></a>
The end of the time interval for which to retrieve events, specified in ISO 8601 format. Example: 2017-03-30T07:03:49.555Z
Type: Timestamp
Required: No

 ** [MaxResults](#API_DescribeEvents_RequestSyntax) **   <a name="MemoryDB-DescribeEvents-request-MaxResults"></a>
The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeEvents_RequestSyntax) **   <a name="MemoryDB-DescribeEvents-request-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

 ** [SourceName](#API_DescribeEvents_RequestSyntax) **   <a name="MemoryDB-DescribeEvents-request-SourceName"></a>
The identifier of the event source for which events are returned. If not specified, all sources are included in the response.
Type: String
Required: No

 ** [SourceType](#API_DescribeEvents_RequestSyntax) **   <a name="MemoryDB-DescribeEvents-request-SourceType"></a>
The event source to retrieve events for. If no value is specified, all events are returned.
Type: String
Valid Values: `node | parameter-group | subnet-group | cluster | user | acl`
Required: No

 ** [StartTime](#API_DescribeEvents_RequestSyntax) **   <a name="MemoryDB-DescribeEvents-request-StartTime"></a>
The beginning of the time interval to retrieve events for, specified in ISO 8601 format. Example: 2017-03-30T07:03:49.555Z
Type: Timestamp
Required: No

## Response Syntax
<a name="API_DescribeEvents_ResponseSyntax"></a>

```
{
   "Events": [
      {
         "Date": number,
         "Message": "string",
         "SourceName": "string",
         "SourceType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Events](#API_DescribeEvents_ResponseSyntax) **   <a name="MemoryDB-DescribeEvents-response-Events"></a>
A list of events. Each element in the list contains detailed information about one event.
Type: Array of [Event](API_Event.md) objects

 ** [NextToken](#API_DescribeEvents_ResponseSyntax) **   <a name="MemoryDB-DescribeEvents-response-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

## Errors
<a name="API_DescribeEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_DescribeEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DescribeEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DescribeEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DescribeEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DescribeEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DescribeEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DescribeEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DescribeEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DescribeEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DescribeEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DescribeEvents)
