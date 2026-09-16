---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateAggregatorV2.html
---

# UpdateAggregatorV2
<a name="API_UpdateAggregatorV2"></a>

Udpates the configuration for the Aggregator V2.

## Request Syntax
<a name="API_UpdateAggregatorV2_RequestSyntax"></a>

```
PATCH /aggregatorv2/update/{{AggregatorV2Arn+}} HTTP/1.1
Content-type: application/json

{
   "LinkedRegions": [ "{{string}}" ],
   "RegionLinkingMode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAggregatorV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AggregatorV2Arn](#API_UpdateAggregatorV2_RequestSyntax) **   <a name="securityhub-UpdateAggregatorV2-request-uri-AggregatorV2Arn"></a>
The ARN of the Aggregator V2.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_UpdateAggregatorV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [LinkedRegions](#API_UpdateAggregatorV2_RequestSyntax) **   <a name="securityhub-UpdateAggregatorV2-request-LinkedRegions"></a>
A list of AWS Regions linked to the aggegation Region.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** [RegionLinkingMode](#API_UpdateAggregatorV2_RequestSyntax) **   <a name="securityhub-UpdateAggregatorV2-request-RegionLinkingMode"></a>
Determines how AWS Regions should be linked to the Aggregator V2.
Type: String
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_UpdateAggregatorV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AggregationRegion": "string",
   "AggregatorV2Arn": "string",
   "LinkedRegions": [ "string" ],
   "RegionLinkingMode": "string"
}
```

## Response Elements
<a name="API_UpdateAggregatorV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AggregationRegion](#API_UpdateAggregatorV2_ResponseSyntax) **   <a name="securityhub-UpdateAggregatorV2-response-AggregationRegion"></a>
The AWS Region where data is aggregated.
Type: String
Pattern: `.*\S.*`

 ** [AggregatorV2Arn](#API_UpdateAggregatorV2_ResponseSyntax) **   <a name="securityhub-UpdateAggregatorV2-response-AggregatorV2Arn"></a>
The ARN of the Aggregator V2.
Type: String
Pattern: `.*\S.*`

 ** [LinkedRegions](#API_UpdateAggregatorV2_ResponseSyntax) **   <a name="securityhub-UpdateAggregatorV2-response-LinkedRegions"></a>
A list of AWS Regions linked to the aggegation Region.
Type: Array of strings
Pattern: `.*\S.*`

 ** [RegionLinkingMode](#API_UpdateAggregatorV2_ResponseSyntax) **   <a name="securityhub-UpdateAggregatorV2-response-RegionLinkingMode"></a>
Determines how AWS Regions should be linked to the Aggregator V2.
Type: String
Pattern: `.*\S.*`

## Errors
<a name="API_UpdateAggregatorV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** ConflictException **
The request causes conflict with the current state of the service resource.
HTTP Status Code: 409

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAggregatorV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/UpdateAggregatorV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/UpdateAggregatorV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UpdateAggregatorV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/UpdateAggregatorV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UpdateAggregatorV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/UpdateAggregatorV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/UpdateAggregatorV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/UpdateAggregatorV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/UpdateAggregatorV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UpdateAggregatorV2)
