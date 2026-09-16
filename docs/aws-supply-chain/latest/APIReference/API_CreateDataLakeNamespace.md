---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_CreateDataLakeNamespace.html
---

# CreateDataLakeNamespace
<a name="API_CreateDataLakeNamespace"></a>

Enables you to programmatically create an AWS Supply Chain data lake namespace. Developers can create the namespaces for a given instance ID.

## Request Syntax
<a name="API_CreateDataLakeNamespace_RequestSyntax"></a>

```
PUT /api/datalake/instance/{{instanceId}}/namespaces/{{name}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDataLakeNamespace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_CreateDataLakeNamespace_RequestSyntax) **   <a name="supplychain-CreateDataLakeNamespace-request-uri-instanceId"></a>
The AWS Supply Chain instance identifier.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [name](#API_CreateDataLakeNamespace_RequestSyntax) **   <a name="supplychain-CreateDataLakeNamespace-request-uri-name"></a>
The name of the namespace. Noted you cannot create namespace with name starting with **asc**, **default**, **scn**, **aws**, **amazon**, **amzn**
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-z0-9_]+`
Required: Yes

## Request Body
<a name="API_CreateDataLakeNamespace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateDataLakeNamespace_RequestSyntax) **   <a name="supplychain-CreateDataLakeNamespace-request-description"></a>
The description of the namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** [tags](#API_CreateDataLakeNamespace_RequestSyntax) **   <a name="supplychain-CreateDataLakeNamespace-request-tags"></a>
The tags of the namespace.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateDataLakeNamespace_ResponseSyntax"></a>

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
<a name="API_CreateDataLakeNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [namespace](#API_CreateDataLakeNamespace_ResponseSyntax) **   <a name="supplychain-CreateDataLakeNamespace-response-namespace"></a>
The detail of created namespace.
Type: [DataLakeNamespace](API_DataLakeNamespace.md) object

## Errors
<a name="API_CreateDataLakeNamespace_Errors"></a>

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
<a name="API_CreateDataLakeNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/CreateDataLakeNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/CreateDataLakeNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/CreateDataLakeNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/CreateDataLakeNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/CreateDataLakeNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/CreateDataLakeNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/CreateDataLakeNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/CreateDataLakeNamespace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/CreateDataLakeNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/CreateDataLakeNamespace)
