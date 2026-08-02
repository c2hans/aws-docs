---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateIntegration.html
---

# UpdateIntegration
<a name="API_UpdateIntegration"></a>

Update integration features.

## Request Syntax
<a name="API_UpdateIntegration_RequestSyntax"></a>

```
POST /workloads/{{WorkloadId}}/updateIntegration HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "IntegratingService": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateIntegration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [WorkloadId](#API_UpdateIntegration_RequestSyntax) **   <a name="wellarchitected-UpdateIntegration-request-uri-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_UpdateIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_UpdateIntegration_RequestSyntax) **   <a name="wellarchitected-UpdateIntegration-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure that this request is idempotent (executes only once).
You should not reuse the same token for other requests. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.
This token is listed as required, however, if you do not specify it, the AWS SDKs automatically generate one for you. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the request will fail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\x00-\x7F]*$`
Required: Yes

 ** [IntegratingService](#API_UpdateIntegration_RequestSyntax) **   <a name="wellarchitected-UpdateIntegration-request-IntegratingService"></a>
Which integrated service to update.
Type: String
Valid Values: `JIRA`
Required: Yes

## Response Syntax
<a name="API_UpdateIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/UpdateIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/UpdateIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/UpdateIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/UpdateIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/UpdateIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/UpdateIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/UpdateIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/UpdateIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/UpdateIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/UpdateIntegration)
