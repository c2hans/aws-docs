---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_CreateBillOfMaterialsImportJob.html
---

# CreateBillOfMaterialsImportJob
<a name="API_CreateBillOfMaterialsImportJob"></a>

CreateBillOfMaterialsImportJob creates an import job for the Product Bill Of Materials (BOM) entity. For information on the product\_bom entity, see the AWS Supply Chain User Guide.

The CSV file must be located in an Amazon S3 location accessible to AWS Supply Chain. It is recommended to use the same Amazon S3 bucket created during your AWS Supply Chain instance creation.

## Request Syntax
<a name="API_CreateBillOfMaterialsImportJob_RequestSyntax"></a>

```
POST /api/configuration/instances/{{instanceId}}/bill-of-materials-import-jobs HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "s3uri": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateBillOfMaterialsImportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_CreateBillOfMaterialsImportJob_RequestSyntax) **   <a name="supplychain-CreateBillOfMaterialsImportJob-request-uri-instanceId"></a>
The AWS Supply Chain instance identifier.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_CreateBillOfMaterialsImportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateBillOfMaterialsImportJob_RequestSyntax) **   <a name="supplychain-CreateBillOfMaterialsImportJob-request-clientToken"></a>
An idempotency token ensures the API request is only completed no more than once. This way, retrying the request will not trigger the operation multiple times. A client token is a unique, case-sensitive string of 33 to 128 ASCII characters. To make an idempotent API request, specify a client token in the request. You should not reuse the same client token for other requests. If you retry a successful request with the same client token, the request will succeed with no further actions being taken, and you will receive the same API response as the original successful request.
Type: String
Length Constraints: Minimum length of 33. Maximum length of 126.
Required: No

 ** [s3uri](#API_CreateBillOfMaterialsImportJob_RequestSyntax) **   <a name="supplychain-CreateBillOfMaterialsImportJob-request-s3uri"></a>
The S3 URI of the CSV file to be imported. The bucket must grant permissions for AWS Supply Chain to read the file.
Type: String
Length Constraints: Minimum length of 10.
Pattern: `[sS]3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.+`
Required: Yes

## Response Syntax
<a name="API_CreateBillOfMaterialsImportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobId": "string"
}
```

## Response Elements
<a name="API_CreateBillOfMaterialsImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobId](#API_CreateBillOfMaterialsImportJob_ResponseSyntax) **   <a name="supplychain-CreateBillOfMaterialsImportJob-response-jobId"></a>
The new BillOfMaterialsImportJob identifier.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_CreateBillOfMaterialsImportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the required privileges to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateBillOfMaterialsImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/CreateBillOfMaterialsImportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/CreateBillOfMaterialsImportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/CreateBillOfMaterialsImportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/CreateBillOfMaterialsImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/CreateBillOfMaterialsImportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/CreateBillOfMaterialsImportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/CreateBillOfMaterialsImportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/CreateBillOfMaterialsImportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/CreateBillOfMaterialsImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/CreateBillOfMaterialsImportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
