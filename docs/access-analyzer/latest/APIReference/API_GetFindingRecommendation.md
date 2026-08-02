---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetFindingRecommendation.html
---

# GetFindingRecommendation
<a name="API_GetFindingRecommendation"></a>

Retrieves information about a finding recommendation for the specified analyzer.

## Request Syntax
<a name="API_GetFindingRecommendation_RequestSyntax"></a>

```
GET /recommendation/{{id}}?analyzerArn={{analyzerArn}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFindingRecommendation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analyzerArn](#API_GetFindingRecommendation_RequestSyntax) **   <a name="accessanalyzer-GetFindingRecommendation-request-uri-analyzerArn"></a>
The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) used to generate the finding recommendation.
Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`
Required: Yes

 ** [id](#API_GetFindingRecommendation_RequestSyntax) **   <a name="accessanalyzer-GetFindingRecommendation-request-uri-id"></a>
The unique ID for the finding recommendation.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [maxResults](#API_GetFindingRecommendation_RequestSyntax) **   <a name="accessanalyzer-GetFindingRecommendation-request-uri-maxResults"></a>
The maximum number of results to return in the response.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_GetFindingRecommendation_RequestSyntax) **   <a name="accessanalyzer-GetFindingRecommendation-request-uri-nextToken"></a>
A token used for pagination of results returned.

## Request Body
<a name="API_GetFindingRecommendation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFindingRecommendation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "completedAt": "string",
   "error": {
      "code": "string",
      "message": "string"
   },
   "nextToken": "string",
   "recommendationType": "string",
   "recommendedSteps": [
      { ... }
   ],
   "resourceArn": "string",
   "startedAt": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetFindingRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [completedAt](#API_GetFindingRecommendation_ResponseSyntax) **   <a name="accessanalyzer-GetFindingRecommendation-response-completedAt"></a>
The time at which the retrieval of the finding recommendation was completed.
Type: Timestamp

 ** [error](#API_GetFindingRecommendation_ResponseSyntax) **   <a name="accessanalyzer-GetFindingRecommendation-response-error"></a>
Detailed information about the reason that the retrieval of a recommendation for the finding failed.
Type: [RecommendationError](API_RecommendationError.md) object

 ** [nextToken](#API_GetFindingRecommendation_ResponseSyntax) **   <a name="accessanalyzer-GetFindingRecommendation-response-nextToken"></a>
A token used for pagination of results returned.
Type: String

 ** [recommendationType](#API_GetFindingRecommendation_ResponseSyntax) **   <a name="accessanalyzer-GetFindingRecommendation-response-recommendationType"></a>
The type of recommendation for the finding.
Type: String
Valid Values: `UnusedPermissionRecommendation`

 ** [recommendedSteps](#API_GetFindingRecommendation_ResponseSyntax) **   <a name="accessanalyzer-GetFindingRecommendation-response-recommendedSteps"></a>
A group of recommended steps for the finding.
Type: Array of [RecommendedStep](API_RecommendedStep.md) objects

 ** [resourceArn](#API_GetFindingRecommendation_ResponseSyntax) **   <a name="accessanalyzer-GetFindingRecommendation-response-resourceArn"></a>
The ARN of the resource of the finding.
Type: String
Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`

 ** [startedAt](#API_GetFindingRecommendation_ResponseSyntax) **   <a name="accessanalyzer-GetFindingRecommendation-response-startedAt"></a>
The time at which the retrieval of the finding recommendation was started.
Type: Timestamp

 ** [status](#API_GetFindingRecommendation_ResponseSyntax) **   <a name="accessanalyzer-GetFindingRecommendation-response-status"></a>
The status of the retrieval of the finding recommendation.
Type: String
Valid Values: `SUCCEEDED | FAILED | IN_PROGRESS`

## Errors
<a name="API_GetFindingRecommendation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Internal server error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
Throttling limit exceeded error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 429

 ** ValidationException **
Validation exception error.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetFindingRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetFindingRecommendation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetFindingRecommendation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetFindingRecommendation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetFindingRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetFindingRecommendation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetFindingRecommendation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetFindingRecommendation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetFindingRecommendation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetFindingRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetFindingRecommendation)
