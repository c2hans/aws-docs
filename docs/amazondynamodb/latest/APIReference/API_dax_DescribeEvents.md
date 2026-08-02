---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeEvents.html
---

# DescribeEvents
<a name="API_dax_DescribeEvents"></a>

Returns events related to DAX clusters and parameter groups. You can obtain events specific to a particular DAX cluster or parameter group by providing the name as a parameter.

By default, only the events occurring within the last 24 hours are returned; however, you can retrieve up to 14 days' worth of events if necessary.

## Request Syntax
<a name="API_dax_DescribeEvents_RequestSyntax"></a>

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
<a name="API_dax_DescribeEvents_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Duration](#API_dax_DescribeEvents_RequestSyntax) **   <a name="DDB-dax_DescribeEvents-request-Duration"></a>
The number of minutes' worth of events to retrieve.
Type: Integer
Required: No

 ** [EndTime](#API_dax_DescribeEvents_RequestSyntax) **   <a name="DDB-dax_DescribeEvents-request-EndTime"></a>
The end of the time interval for which to retrieve events, specified in ISO 8601 format.
Type: Timestamp
Required: No

 ** [MaxResults](#API_dax_DescribeEvents_RequestSyntax) **   <a name="DDB-dax_DescribeEvents-request-MaxResults"></a>
The maximum number of results to include in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that the remaining results can be retrieved.
The value for `MaxResults` must be between 20 and 100.
Type: Integer
Required: No

 ** [NextToken](#API_dax_DescribeEvents_RequestSyntax) **   <a name="DDB-dax_DescribeEvents-request-NextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by `MaxResults`.
Type: String
Required: No

 ** [SourceName](#API_dax_DescribeEvents_RequestSyntax) **   <a name="DDB-dax_DescribeEvents-request-SourceName"></a>
The identifier of the event source for which events will be returned. If not specified, then all sources are included in the response.
Type: String
Required: No

 ** [SourceType](#API_dax_DescribeEvents_RequestSyntax) **   <a name="DDB-dax_DescribeEvents-request-SourceType"></a>
The event source to retrieve events for. If no value is specified, all events are returned.
Type: String
Valid Values: `CLUSTER | PARAMETER_GROUP | SUBNET_GROUP`
Required: No

 ** [StartTime](#API_dax_DescribeEvents_RequestSyntax) **   <a name="DDB-dax_DescribeEvents-request-StartTime"></a>
The beginning of the time interval to retrieve events for, specified in ISO 8601 format.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_dax_DescribeEvents_ResponseSyntax"></a>

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
<a name="API_dax_DescribeEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Events](#API_dax_DescribeEvents_ResponseSyntax) **   <a name="DDB-dax_DescribeEvents-response-Events"></a>
An array of events. Each element in the array represents one event.
Type: Array of [Event](API_dax_Event.md) objects

 ** [NextToken](#API_dax_DescribeEvents_ResponseSyntax) **   <a name="DDB-dax_DescribeEvents-response-NextToken"></a>
Provides an identifier to allow retrieval of paginated results.
Type: String

## Errors
<a name="API_dax_DescribeEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **
Two or more incompatible parameters were specified.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value for a parameter is invalid.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

## See Also
<a name="API_dax_DescribeEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dax-2017-04-19/DescribeEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dax-2017-04-19/DescribeEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/DescribeEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dax-2017-04-19/DescribeEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/DescribeEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dax-2017-04-19/DescribeEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dax-2017-04-19/DescribeEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dax-2017-04-19/DescribeEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dax-2017-04-19/DescribeEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/DescribeEvents)
