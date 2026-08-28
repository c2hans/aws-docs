---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListIdNamespaces.html
---

# ListIdNamespaces
<a name="API_ListIdNamespaces"></a>

Returns a list of all ID namespaces.

## Request Syntax
<a name="API_ListIdNamespaces_RequestSyntax"></a>

```
GET /idnamespaces?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListIdNamespaces_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListIdNamespaces_RequestSyntax) **   <a name="API-ListIdNamespaces-request-uri-maxResults"></a>
The maximum number of `IdNamespace` objects returned per page.
Valid Range: Maximum value of 25.

 ** [nextToken](#API_ListIdNamespaces_RequestSyntax) **   <a name="API-ListIdNamespaces-request-uri-nextToken"></a>
The pagination token from the previous API call.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z_0-9-=+/]*`

## Request Body
<a name="API_ListIdNamespaces_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListIdNamespaces_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "idNamespaceSummaries": [
      {
         "createdAt": number,
         "description": "string",
         "idMappingWorkflowProperties": [
            {
               "idMappingType": "string"
            }
         ],
         "idNamespaceArn": "string",
         "idNamespaceName": "string",
         "type": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListIdNamespaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [idNamespaceSummaries](#API_ListIdNamespaces_ResponseSyntax) **   <a name="API-ListIdNamespaces-response-idNamespaceSummaries"></a>
A list of `IdNamespaceSummaries` objects.
Type: Array of [IdNamespaceSummary](API_IdNamespaceSummary.md) objects

 ** [nextToken](#API_ListIdNamespaces_ResponseSyntax) **   <a name="API-ListIdNamespaces-response-nextToken"></a>
The pagination token from the previous API call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z_0-9-=+/]*`

## Errors
<a name="API_ListIdNamespaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_ListIdNamespaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/ListIdNamespaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/ListIdNamespaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/ListIdNamespaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/ListIdNamespaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/ListIdNamespaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/ListIdNamespaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/ListIdNamespaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/ListIdNamespaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/ListIdNamespaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/ListIdNamespaces)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
