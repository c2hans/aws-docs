---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_ListDataLakeNamespaces.html
---

# ListDataLakeNamespaces
<a name="API_ListDataLakeNamespaces"></a>

Enables you to programmatically view the list of AWS Supply Chain data lake namespaces. Developers can view the namespaces and the corresponding information such as description for a given instance ID. Note that this API only return custom namespaces, instance pre-defined namespaces are not included.

## Request Syntax
<a name="API_ListDataLakeNamespaces_RequestSyntax"></a>

```
GET /api/datalake/instance/{{instanceId}}/namespaces?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataLakeNamespaces_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_ListDataLakeNamespaces_RequestSyntax) **   <a name="supplychain-ListDataLakeNamespaces-request-uri-instanceId"></a>
The AWS Supply Chain instance identifier.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [maxResults](#API_ListDataLakeNamespaces_RequestSyntax) **   <a name="supplychain-ListDataLakeNamespaces-request-uri-maxResults"></a>
The max number of namespaces to fetch in this paginated request.
Valid Range: Minimum value of 1. Maximum value of 20.

 ** [nextToken](#API_ListDataLakeNamespaces_RequestSyntax) **   <a name="supplychain-ListDataLakeNamespaces-request-uri-nextToken"></a>
The pagination token to fetch next page of namespaces.
Length Constraints: Minimum length of 1. Maximum length of 65535.

## Request Body
<a name="API_ListDataLakeNamespaces_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataLakeNamespaces_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "namespaces": [
      {
         "arn": "string",
         "createdTime": number,
         "description": "string",
         "instanceId": "string",
         "lastModifiedTime": number,
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataLakeNamespaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [namespaces](#API_ListDataLakeNamespaces_ResponseSyntax) **   <a name="supplychain-ListDataLakeNamespaces-response-namespaces"></a>
The list of fetched namespace details. Noted it only contains custom namespaces, pre-defined namespaces are not included.
Type: Array of [DataLakeNamespace](API_DataLakeNamespace.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.

 ** [nextToken](#API_ListDataLakeNamespaces_ResponseSyntax) **   <a name="supplychain-ListDataLakeNamespaces-response-nextToken"></a>
The pagination token to fetch next page of namespaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

## Errors
<a name="API_ListDataLakeNamespaces_Errors"></a>

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
<a name="API_ListDataLakeNamespaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/ListDataLakeNamespaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/ListDataLakeNamespaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/ListDataLakeNamespaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/ListDataLakeNamespaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/ListDataLakeNamespaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/ListDataLakeNamespaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/ListDataLakeNamespaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/ListDataLakeNamespaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/ListDataLakeNamespaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/ListDataLakeNamespaces)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
