---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_GetDataLakeNamespace.html
---

# GetDataLakeNamespace
<a name="API_GetDataLakeNamespace"></a>

Enables you to programmatically view an AWS Supply Chain data lake namespace. Developers can view the data lake namespace information such as description for a given instance ID and namespace name.

## Request Syntax
<a name="API_GetDataLakeNamespace_RequestSyntax"></a>

```
GET /api/datalake/instance/{{instanceId}}/namespaces/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataLakeNamespace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_GetDataLakeNamespace_RequestSyntax) **   <a name="supplychain-GetDataLakeNamespace-request-uri-instanceId"></a>
The AWS Supply Chain instance identifier.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [name](#API_GetDataLakeNamespace_RequestSyntax) **   <a name="supplychain-GetDataLakeNamespace-request-uri-name"></a>
The name of the namespace. Besides the namespaces user created, you can also specify the pre-defined namespaces:
+  **asc** - Pre-defined namespace containing AWS Supply Chain supported datasets, see [https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html).
+  **default** - Pre-defined namespace containing datasets with custom user-defined schemas.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-z0-9_]+`
Required: Yes

## Request Body
<a name="API_GetDataLakeNamespace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataLakeNamespace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "namespace": {
      "arn": "string",
      "createdTime": number,
      "description": "string",
      "instanceId": "string",
      "lastModifiedTime": number,
      "name": "string"
   }
}
```

## Response Elements
<a name="API_GetDataLakeNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [namespace](#API_GetDataLakeNamespace_ResponseSyntax) **   <a name="supplychain-GetDataLakeNamespace-response-namespace"></a>
The fetched namespace details.
Type: [DataLakeNamespace](API_DataLakeNamespace.md) object

## Errors
<a name="API_GetDataLakeNamespace_Errors"></a>

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
<a name="API_GetDataLakeNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/GetDataLakeNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/GetDataLakeNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/GetDataLakeNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/GetDataLakeNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/GetDataLakeNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/GetDataLakeNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/GetDataLakeNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/GetDataLakeNamespace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/GetDataLakeNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/GetDataLakeNamespace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
