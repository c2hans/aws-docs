---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetGeneratedPolicy.html
---

# GetGeneratedPolicy
<a name="API_GetGeneratedPolicy"></a>

Retrieves the policy that was generated using `StartPolicyGeneration`.

## Request Syntax
<a name="API_GetGeneratedPolicy_RequestSyntax"></a>

```
GET /policy/generation/{{jobId}}?includeResourcePlaceholders={{includeResourcePlaceholders}}&includeServiceLevelTemplate={{includeServiceLevelTemplate}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetGeneratedPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [includeResourcePlaceholders](#API_GetGeneratedPolicy_RequestSyntax) **   <a name="accessanalyzer-GetGeneratedPolicy-request-uri-includeResourcePlaceholders"></a>
The level of detail that you want to generate. You can specify whether to generate policies with placeholders for resource ARNs for actions that support resource level granularity in policies.
For example, in the resource section of a policy, you can receive a placeholder such as `"Resource":"arn:aws:s3:::${BucketName}"` instead of `"*"`.

 ** [includeServiceLevelTemplate](#API_GetGeneratedPolicy_RequestSyntax) **   <a name="accessanalyzer-GetGeneratedPolicy-request-uri-includeServiceLevelTemplate"></a>
The level of detail that you want to generate. You can specify whether to generate service-level policies.
IAM Access Analyzer uses `iam:servicelastaccessed` to identify services that have been used recently to create this service-level template.

 ** [jobId](#API_GetGeneratedPolicy_RequestSyntax) **   <a name="accessanalyzer-GetGeneratedPolicy-request-uri-jobId"></a>
The `JobId` that is returned by the `StartPolicyGeneration` operation. The `JobId` can be used with `GetGeneratedPolicy` to retrieve the generated policies or used with `CancelPolicyGeneration` to cancel the policy generation request.
Required: Yes

## Request Body
<a name="API_GetGeneratedPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetGeneratedPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "generatedPolicyResult": {
      "generatedPolicies": [
         {
            "policy": "string"
         }
      ],
      "properties": {
         "cloudTrailProperties": {
            "endTime": "string",
            "startTime": "string",
            "trailProperties": [
               {
                  "allRegions": boolean,
                  "cloudTrailArn": "string",
                  "regions": [ "string" ]
               }
            ]
         },
         "isComplete": boolean,
         "principalArn": "string"
      }
   },
   "jobDetails": {
      "completedOn": "string",
      "jobError": {
         "code": "string",
         "message": "string"
      },
      "jobId": "string",
      "startedOn": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_GetGeneratedPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [generatedPolicyResult](#API_GetGeneratedPolicy_ResponseSyntax) **   <a name="accessanalyzer-GetGeneratedPolicy-response-generatedPolicyResult"></a>
A `GeneratedPolicyResult` object that contains the generated policies and associated details.
Type: [GeneratedPolicyResult](API_GeneratedPolicyResult.md) object

 ** [jobDetails](#API_GetGeneratedPolicy_ResponseSyntax) **   <a name="accessanalyzer-GetGeneratedPolicy-response-jobDetails"></a>
A `GeneratedPolicyDetails` object that contains details about the generated policy.
Type: [JobDetails](API_JobDetails.md) object

## Errors
<a name="API_GetGeneratedPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Internal server error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 500

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
<a name="API_GetGeneratedPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetGeneratedPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetGeneratedPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetGeneratedPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetGeneratedPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetGeneratedPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetGeneratedPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetGeneratedPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetGeneratedPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetGeneratedPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetGeneratedPolicy)
