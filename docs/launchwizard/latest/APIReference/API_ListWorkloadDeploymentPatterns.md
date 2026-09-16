---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html
---

# ListWorkloadDeploymentPatterns
<a name="API_ListWorkloadDeploymentPatterns"></a>

Lists the workload deployment patterns for a given workload name. You can use the [ListWorkloads](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html) operation to discover the available workload names.

## Request Syntax
<a name="API_ListWorkloadDeploymentPatterns_RequestSyntax"></a>

```
POST /listWorkloadDeploymentPatterns HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "workloadName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWorkloadDeploymentPatterns_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListWorkloadDeploymentPatterns_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListWorkloadDeploymentPatterns_RequestSyntax) **   <a name="launchwizard-ListWorkloadDeploymentPatterns-request-maxResults"></a>
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListWorkloadDeploymentPatterns_RequestSyntax) **   <a name="launchwizard-ListWorkloadDeploymentPatterns-request-nextToken"></a>
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [workloadName](#API_ListWorkloadDeploymentPatterns_RequestSyntax) **   <a name="launchwizard-ListWorkloadDeploymentPatterns-request-workloadName"></a>
The name of the workload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z][a-zA-Z0-9-_]*`
Required: Yes

## Response Syntax
<a name="API_ListWorkloadDeploymentPatterns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "workloadDeploymentPatterns": [
      {
         "deploymentPatternName": "string",
         "deploymentPatternVersionName": "string",
         "description": "string",
         "displayName": "string",
         "status": "string",
         "statusMessage": "string",
         "workloadName": "string",
         "workloadVersionName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkloadDeploymentPatterns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWorkloadDeploymentPatterns_ResponseSyntax) **   <a name="launchwizard-ListWorkloadDeploymentPatterns-response-nextToken"></a>
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [workloadDeploymentPatterns](#API_ListWorkloadDeploymentPatterns_ResponseSyntax) **   <a name="launchwizard-ListWorkloadDeploymentPatterns-response-workloadDeploymentPatterns"></a>
Describes the workload deployment patterns.
Type: Array of [WorkloadDeploymentPatternDataSummary](API_WorkloadDeploymentPatternDataSummary.md) objects

## Errors
<a name="API_ListWorkloadDeploymentPatterns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on [re:Post](https://repost.aws/).
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified workload or deployment resource can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListWorkloadDeploymentPatterns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/launch-wizard-2018-05-10/ListWorkloadDeploymentPatterns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/launch-wizard-2018-05-10/ListWorkloadDeploymentPatterns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/ListWorkloadDeploymentPatterns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/launch-wizard-2018-05-10/ListWorkloadDeploymentPatterns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/ListWorkloadDeploymentPatterns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/launch-wizard-2018-05-10/ListWorkloadDeploymentPatterns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/launch-wizard-2018-05-10/ListWorkloadDeploymentPatterns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/launch-wizard-2018-05-10/ListWorkloadDeploymentPatterns)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/launch-wizard-2018-05-10/ListWorkloadDeploymentPatterns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/ListWorkloadDeploymentPatterns)
