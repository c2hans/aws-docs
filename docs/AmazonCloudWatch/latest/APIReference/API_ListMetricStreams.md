---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetricStreams.html
---

# ListMetricStreams
<a name="API_ListMetricStreams"></a>

Returns a list of metric streams in this account.

## Request Syntax
<a name="API_ListMetricStreams_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMetricStreams_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListMetricStreams_RequestSyntax) **   <a name="ACW-ListMetricStreams-request-MaxResults"></a>
The maximum number of results to return in one operation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_ListMetricStreams_RequestSyntax) **   <a name="ACW-ListMetricStreams-request-NextToken"></a>
Include this value, if it was returned by the previous call, to get the next set of metric streams.
Type: String
Required: No

## Response Syntax
<a name="API_ListMetricStreams_ResponseSyntax"></a>

```
{
   "Entries": [
      {
         "Arn": "string",
         "CreationDate": number,
         "FirehoseArn": "string",
         "LastUpdateDate": number,
         "Name": "string",
         "OutputFormat": "string",
         "State": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMetricStreams_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entries](#API_ListMetricStreams_ResponseSyntax) **   <a name="ACW-ListMetricStreams-response-Entries"></a>
The array of metric stream information.
Type: Array of [MetricStreamEntry](API_MetricStreamEntry.md) objects

 ** [NextToken](#API_ListMetricStreams_ResponseSyntax) **   <a name="ACW-ListMetricStreams-response-NextToken"></a>
The token that marks the start of the next batch of returned results. You can use this token in a subsequent operation to get the next batch of results.
Type: String

## Errors
<a name="API_ListMetricStreams_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
Request processing has failed due to some unknown error, exception, or failure.
 ** Message **

HTTP Status Code: 500

 ** InvalidNextToken **
The next token specified is invalid.
 ** message **

HTTP Status Code: 400

 ** InvalidParameterValue **
The value of an input parameter is bad or out-of-range.
 ** message **

HTTP Status Code: 400

 ** MissingParameter **
An input parameter that is required is missing.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_ListMetricStreams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/ListMetricStreams)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListMetricStreams)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ListMetricStreams)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/ListMetricStreams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListMetricStreams)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/ListMetricStreams)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/ListMetricStreams)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/ListMetricStreams)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListMetricStreams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListMetricStreams)
