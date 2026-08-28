---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DeleteDataLakeNamespace.html
---

# DeleteDataLakeNamespace
<a name="API_DeleteDataLakeNamespace"></a>

Enables you to programmatically delete an AWS Supply Chain data lake namespace and its underling datasets. Developers can delete the existing namespaces for a given instance ID and namespace name.

## Request Syntax
<a name="API_DeleteDataLakeNamespace_RequestSyntax"></a>

```
DELETE /api/datalake/instance/{{instanceId}}/namespaces/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDataLakeNamespace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_DeleteDataLakeNamespace_RequestSyntax) **   <a name="supplychain-DeleteDataLakeNamespace-request-uri-instanceId"></a>
The AWS Supply Chain instance identifier.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [name](#API_DeleteDataLakeNamespace_RequestSyntax) **   <a name="supplychain-DeleteDataLakeNamespace-request-uri-name"></a>
The name of the namespace. Noted you cannot delete pre-defined namespace like **asc**, **default** which are only deleted through instance deletion.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-z0-9_]+`
Required: Yes

## Request Body
<a name="API_DeleteDataLakeNamespace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDataLakeNamespace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "instanceId": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_DeleteDataLakeNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instanceId](#API_DeleteDataLakeNamespace_ResponseSyntax) **   <a name="supplychain-DeleteDataLakeNamespace-response-instanceId"></a>
The AWS Supply Chain instance identifier.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_DeleteDataLakeNamespace_ResponseSyntax) **   <a name="supplychain-DeleteDataLakeNamespace-response-name"></a>
The name of deleted namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-z0-9_]+`

## Errors
<a name="API_DeleteDataLakeNamespace_Errors"></a>

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
<a name="API_DeleteDataLakeNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/DeleteDataLakeNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/DeleteDataLakeNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DeleteDataLakeNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/DeleteDataLakeNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DeleteDataLakeNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/DeleteDataLakeNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/DeleteDataLakeNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/DeleteDataLakeNamespace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/DeleteDataLakeNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DeleteDataLakeNamespace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
