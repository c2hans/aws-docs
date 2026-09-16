---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListMetrics.html
---

# ListMetrics
<a name="API_ListMetrics"></a>

Lists the metrics that can be exported.

## Request Syntax
<a name="API_ListMetrics_RequestSyntax"></a>

```
POST /list-metrics HTTP/1.1
Content-type: application/json

{
   "conditions": [
      {
         "field": "{{string}}",
         "operator": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "dataSource": "{{string}}",
   "fields": [
      {
         "aggregation": "{{string}}",
         "name": "{{string}}"
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sorts": [
      {
         "ascending": {{boolean}},
         "field": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_ListMetrics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListMetrics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [conditions](#API_ListMetrics_RequestSyntax) **   <a name="resiliencehub-ListMetrics-request-conditions"></a>
Indicates the list of all the conditions that were applied on the metrics.
Type: Array of [Condition](API_Condition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [dataSource](#API_ListMetrics_RequestSyntax) **   <a name="resiliencehub-ListMetrics-request-dataSource"></a>
Indicates the data source of the metrics.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [fields](#API_ListMetrics_RequestSyntax) **   <a name="resiliencehub-ListMetrics-request-fields"></a>
Indicates the list of fields in the data source.
Type: Array of [Field](API_Field.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [maxResults](#API_ListMetrics_RequestSyntax) **   <a name="resiliencehub-ListMetrics-request-maxResults"></a>
Maximum number of results to include in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListMetrics_RequestSyntax) **   <a name="resiliencehub-ListMetrics-request-nextToken"></a>
Null, or the token from a previous call to get the next set of results.
Type: String
Pattern: `\S{1,2000}`
Required: No

 ** [sorts](#API_ListMetrics_RequestSyntax) **   <a name="resiliencehub-ListMetrics-request-sorts"></a>
(Optional) Indicates the order in which you want to sort the fields in the metrics. By default, the fields are sorted in the ascending order.
Type: Array of [Sort](API_Sort.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_ListMetrics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "rows": [
      [ "string" ]
   ]
}
```

## Response Elements
<a name="API_ListMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListMetrics_ResponseSyntax) **   <a name="resiliencehub-ListMetrics-response-nextToken"></a>
Token for the next set of results, or null if there are no more results.
Type: String
Pattern: `\S{1,2000}`

 ** [rows](#API_ListMetrics_ResponseSyntax) **   <a name="resiliencehub-ListMetrics-response-rows"></a>
Specifies all the list of metric values for each row of metrics.
Type: Array of arrays of strings
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_ListMetrics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Resilience Hub service.
HTTP Status Code: 500

 ** ThrottlingException **
This exception occurs when you have exceeded the limit on the number of requests per second.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **
This exception occurs when a request is not valid.
HTTP Status Code: 400

## Examples
<a name="API_ListMetrics_Examples"></a>

### Sample Request
<a name="API_ListMetrics_Example_1"></a>

The following is an example request payload.

#### Sample Request
<a name="API_ListMetrics_Example_1_Request"></a>

```
{
  "dataSource": "Applications",
  "fields": [
    {
      "name": "Application Arn"
    }
  ]
}
```

### Sample Response
<a name="API_ListMetrics_Example_2"></a>

The following is an example response payload.

#### Sample Response
<a name="API_ListMetrics_Example_2_Response"></a>

```
{
  "headers": [
    "Application Arn"
  ],
  "rows": [
    [
      "arn:aws:resiliencehub:us-west-2:444455556666:app/dd058443-7e2f-410d-bee6-c634cb3edb39"
    ]
  ]
}
```

## See Also
<a name="API_ListMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/ListMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/ListMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ListMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/ListMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ListMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/ListMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/ListMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/ListMetrics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/ListMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ListMetrics)
