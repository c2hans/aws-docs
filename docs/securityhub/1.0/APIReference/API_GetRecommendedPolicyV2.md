---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetRecommendedPolicyV2.html
---

# GetRecommendedPolicyV2
<a name="API_GetRecommendedPolicyV2"></a>

Retrieves the recommended policy to remediate a Security Hub finding. `GetRecommendedPolicyV2` only supports findings for unused permissions.

## Request Syntax
<a name="API_GetRecommendedPolicyV2_RequestSyntax"></a>

```
GET /recommendedPolicyV2/{{MetadataUid}}?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRecommendedPolicyV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_GetRecommendedPolicyV2_RequestSyntax) **   <a name="securityhub-GetRecommendedPolicyV2-request-uri-MaxResults"></a>
The maximum number of recommendation steps to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [MetadataUid](#API_GetRecommendedPolicyV2_RequestSyntax) **   <a name="securityhub-GetRecommendedPolicyV2-request-uri-MetadataUid"></a>
The unique identifier (ID) of Security Hub OCSF findings found under the `metadata.uid` field of the finding.
Pattern: `.*\S.*`
Required: Yes

 ** [NextToken](#API_GetRecommendedPolicyV2_RequestSyntax) **   <a name="securityhub-GetRecommendedPolicyV2-request-uri-NextToken"></a>
The token used to paginate the `RecommendationSteps` list returned. On your first call to `GetRecommendedPolicyV2`, omit this parameter or set it to `NULL`. For subsequent calls, use the `NextToken` value returned in the previous response to retrieve the next page of results.

## Request Body
<a name="API_GetRecommendedPolicyV2_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRecommendedPolicyV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Error": {
      "Code": "string",
      "Message": "string"
   },
   "NextToken": "string",
   "RecommendationSteps": [
      { ... }
   ],
   "RecommendationType": "string",
   "ResourceArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_GetRecommendedPolicyV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Error](#API_GetRecommendedPolicyV2_ResponseSyntax) **   <a name="securityhub-GetRecommendedPolicyV2-response-Error"></a>
Detailed information for a `FAILED` retrieval status.
Type: [RecommendationError](API_RecommendationError.md) object

 ** [NextToken](#API_GetRecommendedPolicyV2_ResponseSyntax) **   <a name="securityhub-GetRecommendedPolicyV2-response-NextToken"></a>
The pagination token to use to request the next page of results.
Type: String

 ** [RecommendationSteps](#API_GetRecommendedPolicyV2_ResponseSyntax) **   <a name="securityhub-GetRecommendedPolicyV2-response-RecommendationSteps"></a>
The recommended steps to take to resolve the finding.
Type: Array of [RecommendationStep](API_RecommendationStep.md) objects

 ** [RecommendationType](#API_GetRecommendedPolicyV2_ResponseSyntax) **   <a name="securityhub-GetRecommendedPolicyV2-response-RecommendationType"></a>
The type of recommendation for the finding.
Type: String
Valid Values: `UNUSED_PERMISSION_RECOMMENDATION`

 ** [ResourceArn](#API_GetRecommendedPolicyV2_ResponseSyntax) **   <a name="securityhub-GetRecommendedPolicyV2-response-ResourceArn"></a>
The ARN of the resource of the finding.
Type: String
Pattern: `.*\S.*`

 ** [Status](#API_GetRecommendedPolicyV2_ResponseSyntax) **   <a name="securityhub-GetRecommendedPolicyV2-response-Status"></a>
The current status of the recommended policy retrieval.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`

## Errors
<a name="API_GetRecommendedPolicyV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

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
<a name="API_GetRecommendedPolicyV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetRecommendedPolicyV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetRecommendedPolicyV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetRecommendedPolicyV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetRecommendedPolicyV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetRecommendedPolicyV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetRecommendedPolicyV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetRecommendedPolicyV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetRecommendedPolicyV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetRecommendedPolicyV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetRecommendedPolicyV2)
