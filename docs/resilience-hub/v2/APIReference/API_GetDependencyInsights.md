---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_GetDependencyInsights.html
---

# GetDependencyInsights
<a name="API_GetDependencyInsights"></a>

Retrieves the dependency insights generated for a service. The response reports the current generation status; insights are populated once generation has completed. If generation failed, the response includes an error code, whose possible values are listed under the response's errorCode field, and a message describing the cause. To use this operation, you must have the `resiliencehub:GetDependencyInsights` permission on the service.

## Request Syntax
<a name="API_GetDependencyInsights_RequestSyntax"></a>

```
GET /v2/get-dependency-insights?serviceArn={{serviceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDependencyInsights_RequestParameters"></a>

The request uses the following URI parameters.

 ** [serviceArn](#API_GetDependencyInsights_RequestSyntax) **   <a name="ngresiliencehub-GetDependencyInsights-request-uri-serviceArn"></a>
ARN identifier.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Request Body
<a name="API_GetDependencyInsights_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDependencyInsights_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "errorCode": "string",
   "errorMessage": "string",
   "insights": [
      {
         "category": "string",
         "description": "string"
      }
   ],
   "overview": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetDependencyInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetDependencyInsights_ResponseSyntax) **   <a name="ngresiliencehub-GetDependencyInsights-response-createdAt"></a>
The timestamp when the dependency insights were generated.
Type: Timestamp

 ** [errorCode](#API_GetDependencyInsights_ResponseSyntax) **   <a name="ngresiliencehub-GetDependencyInsights-response-errorCode"></a>
The error code returned when insights generation failed. Valid values:
+ INSUFFICIENT\_DATA - There was not enough dependency data to generate insights.
+ LLM\_GENERATION\_FAILED - The insights could not be generated.
+ INTERNAL\_ERROR - An internal error occurred while generating insights.
Type: String
Valid Values: `INSUFFICIENT_DATA | LLM_GENERATION_FAILED | INTERNAL_ERROR`

 ** [errorMessage](#API_GetDependencyInsights_ResponseSyntax) **   <a name="ngresiliencehub-GetDependencyInsights-response-errorMessage"></a>
A message describing why insights generation failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [insights](#API_GetDependencyInsights_ResponseSyntax) **   <a name="ngresiliencehub-GetDependencyInsights-response-insights"></a>
The list of dependency insights generated for the service. This field is not returned until the status is COMPLETED.
Type: Array of [DependencyInsight](API_DependencyInsight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [overview](#API_GetDependencyInsights_ResponseSyntax) **   <a name="ngresiliencehub-GetDependencyInsights-response-overview"></a>
A summary of the dependency insights for the service. This field is not returned until the status is COMPLETED.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [status](#API_GetDependencyInsights_ResponseSyntax) **   <a name="ngresiliencehub-GetDependencyInsights-response-status"></a>
The status of the dependency insights generation. Valid values:
+ IN\_PROGRESS - Insights generation is in progress.
+ COMPLETED - Insights generation completed successfully.
+ FAILED - Insights generation failed. See errorCode and errorMessage for details.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED`

## Errors
<a name="API_GetDependencyInsights_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied — caller lacks required permissions.
HTTP Status Code: 403

 ** InternalServerException **
Internal service error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource not found.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
Too many requests — rate limit exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
Validation error — invalid input parameters.
 ** fieldList **
The list of fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_GetDependencyInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/GetDependencyInsights)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/GetDependencyInsights)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/GetDependencyInsights)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/GetDependencyInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/GetDependencyInsights)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/GetDependencyInsights)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/GetDependencyInsights)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/GetDependencyInsights)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/GetDependencyInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/GetDependencyInsights)
