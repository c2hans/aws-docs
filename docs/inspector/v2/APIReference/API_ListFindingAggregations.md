---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListFindingAggregations.html
---

# ListFindingAggregations
<a name="API_ListFindingAggregations"></a>

Lists aggregated finding data for your environment based on specific criteria.

## Request Syntax
<a name="API_ListFindingAggregations_RequestSyntax"></a>

```
POST /findings/aggregation/list HTTP/1.1
Content-type: application/json

{
   "accountIds": [
      {
         "comparison": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "aggregationRequest": { ... },
   "aggregationType": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListFindingAggregations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListFindingAggregations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_ListFindingAggregations_RequestSyntax) **   <a name="inspector2-ListFindingAggregations-request-accountIds"></a>
The AWS account IDs to retrieve finding aggregation data for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [aggregationRequest](#API_ListFindingAggregations_RequestSyntax) **   <a name="inspector2-ListFindingAggregations-request-aggregationRequest"></a>
Details of the aggregation request that is used to filter your aggregation results.
Type: [AggregationRequest](API_AggregationRequest.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [aggregationType](#API_ListFindingAggregations_RequestSyntax) **   <a name="inspector2-ListFindingAggregations-request-aggregationType"></a>
The type of the aggregation request.
Type: String
Valid Values: `FINDING_TYPE | PACKAGE | TITLE | REPOSITORY | AMI | AWS_EC2_INSTANCE | AWS_ECR_CONTAINER | IMAGE_LAYER | ACCOUNT | AWS_LAMBDA_FUNCTION | LAMBDA_LAYER | CODE_REPOSITORY | VM_INSTANCE | CONTAINER_IMAGE | SERVERLESS_FUNCTION`
Required: Yes

 ** [maxResults](#API_ListFindingAggregations_RequestSyntax) **   <a name="inspector2-ListFindingAggregations-request-maxResults"></a>
The maximum number of results the response can return. If your request would return more than the maximum the response will return a `nextToken` value, use this value when you call the action again to get the remaining results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListFindingAggregations_RequestSyntax) **   <a name="inspector2-ListFindingAggregations-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the `maxResults` maximum value it will also return a `nextToken` value. For subsequent calls, use the `nextToken` value returned from the previous request to continue listing results after the first page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.
Required: No

## Response Syntax
<a name="API_ListFindingAggregations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aggregationType": "string",
   "nextToken": "string",
   "responses": [
      { ... }
   ]
}
```

## Response Elements
<a name="API_ListFindingAggregations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aggregationType](#API_ListFindingAggregations_ResponseSyntax) **   <a name="inspector2-ListFindingAggregations-response-aggregationType"></a>
The type of aggregation to perform.
Type: String
Valid Values: `FINDING_TYPE | PACKAGE | TITLE | REPOSITORY | AMI | AWS_EC2_INSTANCE | AWS_ECR_CONTAINER | IMAGE_LAYER | ACCOUNT | AWS_LAMBDA_FUNCTION | LAMBDA_LAYER | CODE_REPOSITORY | VM_INSTANCE | CONTAINER_IMAGE | SERVERLESS_FUNCTION`

 ** [nextToken](#API_ListFindingAggregations_ResponseSyntax) **   <a name="inspector2-ListFindingAggregations-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.

 ** [responses](#API_ListFindingAggregations_ResponseSyntax) **   <a name="inspector2-ListFindingAggregations-response-responses"></a>
Objects that contain the results of an aggregation operation.
Type: Array of [AggregationResponse](API_AggregationResponse.md) objects

## Errors
<a name="API_ListFindingAggregations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListFindingAggregations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListFindingAggregations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListFindingAggregations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListFindingAggregations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListFindingAggregations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListFindingAggregations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListFindingAggregations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListFindingAggregations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListFindingAggregations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListFindingAggregations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListFindingAggregations)
