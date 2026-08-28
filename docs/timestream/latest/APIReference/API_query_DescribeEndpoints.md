---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_DescribeEndpoints.html
---

# DescribeEndpoints
<a name="API_query_DescribeEndpoints"></a>

DescribeEndpoints returns a list of available endpoints to make Timestream API calls against. This API is available through both Write and Query.

Because the Timestream SDKs are designed to transparently work with the service’s architecture, including the management and mapping of the service endpoints, *it is not recommended that you use this API unless*:
+ You are using [VPC endpoints (AWS PrivateLink) with Timestream ](https://docs.aws.amazon.com/timestream/latest/developerguide/VPCEndpoints)
+ Your application uses a programming language that does not yet have SDK support
+ You require better control over the client-side implementation

For detailed information on how and when to use and implement DescribeEndpoints, see [The Endpoint Discovery Pattern](https://docs.aws.amazon.com/timestream/latest/developerguide/Using.API.html#Using-API.endpoint-discovery).

## Response Syntax
<a name="API_query_DescribeEndpoints_ResponseSyntax"></a>

```
{
   "Endpoints": [
      {
         "Address": "string",
         "CachePeriodInMinutes": number
      }
   ]
}
```

## Response Elements
<a name="API_query_DescribeEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Endpoints](#API_query_DescribeEndpoints_ResponseSyntax) **   <a name="timestream-query_DescribeEndpoints-response-Endpoints"></a>
An `Endpoints` object is returned when a `DescribeEndpoints` request is made.
Type: Array of [Endpoint](API_query_Endpoint.md) objects

## Errors
<a name="API_query_DescribeEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal server error occurred while processing the request.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to excessive requests.
HTTP Status Code: 400

 ** ValidationException **
 Invalid or malformed request.
HTTP Status Code: 400

## See Also
<a name="API_query_DescribeEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-query-2018-11-01/DescribeEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-query-2018-11-01/DescribeEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/DescribeEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-query-2018-11-01/DescribeEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/DescribeEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-query-2018-11-01/DescribeEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-query-2018-11-01/DescribeEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-query-2018-11-01/DescribeEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-query-2018-11-01/DescribeEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/DescribeEndpoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
