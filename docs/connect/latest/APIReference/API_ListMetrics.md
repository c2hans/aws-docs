---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListMetrics.html
---

# ListMetrics
<a name="API_ListMetrics"></a>

Retrieves a paginated list of metric summaries for the specified Connect Customer instance. Use pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListMetrics_RequestSyntax"></a>

```
GET /metrics/definitions/{{InstanceId}}?maxResults={{MaxResults}}&nextToken={{NextToken}}&type={{Type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMetrics_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListMetrics_RequestSyntax) **   <a name="connect-ListMetrics-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListMetrics_RequestSyntax) **   <a name="connect-ListMetrics-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListMetrics_RequestSyntax) **   <a name="connect-ListMetrics-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

 ** [Type](#API_ListMetrics_RequestSyntax) **   <a name="connect-ListMetrics-request-uri-Type"></a>
The type of metrics to list. Valid values: `AWS_MANAGED` \| `CUSTOMER_MANAGED`.
Valid Values: `AWS_MANAGED | CUSTOMER_MANAGED`

## Request Body
<a name="API_ListMetrics_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMetrics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MetricSummaryList": [
      {
         "Arn": "string",
         "Id": "string",
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "Status": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MetricSummaryList](#API_ListMetrics_ResponseSyntax) **   <a name="connect-ListMetrics-response-MetricSummaryList"></a>
The list of metric summaries.
Type: Array of [MetricSummary](API_MetricSummary.md) objects

 ** [NextToken](#API_ListMetrics_ResponseSyntax) **   <a name="connect-ListMetrics-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListMetrics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_ListMetrics_Examples"></a>

### Example
<a name="API_ListMetrics_Example_1"></a>

The following example lists customer-managed metrics.

#### Sample Request
<a name="API_ListMetrics_Example_1_Request"></a>

```
GET /metrics/definitions/12345678-1234-1234-1234-123456789012?type=CUSTOMER_MANAGED&maxResults=10
```

## See Also
<a name="API_ListMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListMetrics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListMetrics)
