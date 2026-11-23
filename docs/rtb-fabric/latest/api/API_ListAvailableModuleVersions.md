---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListAvailableModuleVersions.html
---

# ListAvailableModuleVersions

Lists the ACTIVE and DEPRECATED versions of a module that you can attach, highest version first (numerically by MAJOR, then MINOR, then PATCH). If you can't attach the module, the operation returns ResourceNotFoundException, the same as for a missing one. If the module has no ACTIVE or DEPRECATED versions, the operation returns an empty list. The operation lists DEPRECATED versions so that you can inspect one that you've attached, but you can't attach them. Results are paginated. Use `nextToken` to get the next page.

## Request Syntax
<a name="API_ListAvailableModuleVersions_RequestSyntax"></a>

```
GET /available-modules/{{moduleId}}/versions?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAvailableModuleVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAvailableModuleVersions_RequestSyntax) **   <a name="rtbfabric-ListAvailableModuleVersions-request-uri-maxResults"></a>
The maximum number of results for each page, from 1 to 10. The default is 10.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [moduleId](#API_ListAvailableModuleVersions_RequestSyntax) **   <a name="rtbfabric-ListAvailableModuleVersions-request-uri-moduleId"></a>
The module's ID.
Pattern: `module-[a-zA-Z0-9]{1,25}`
Required: Yes

 ** [nextToken](#API_ListAvailableModuleVersions_RequestSyntax) **   <a name="rtbfabric-ListAvailableModuleVersions-request-uri-nextToken"></a>
If nextToken is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours; using an expired token fails with ValidationException.

 ** [status](#API_ListAvailableModuleVersions_RequestSyntax) **   <a name="rtbfabric-ListAvailableModuleVersions-request-uri-status"></a>
Lists only versions in this status. Only ACTIVE and DEPRECATED versions are listed, so another value returns an empty list.
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | DEPRECATED`

## Request Body
<a name="API_ListAvailableModuleVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAvailableModuleVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "moduleId": "string",
   "nextToken": "string",
   "versions": [
      {
         "createdAt": number,
         "moduleVersionArn": "string",
         "status": "string",
         "version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAvailableModuleVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [moduleId](#API_ListAvailableModuleVersions_ResponseSyntax) **   <a name="rtbfabric-ListAvailableModuleVersions-response-moduleId"></a>
The module's ID.
Type: String
Pattern: `module-[a-zA-Z0-9]{1,25}`

 ** [nextToken](#API_ListAvailableModuleVersions_ResponseSyntax) **   <a name="rtbfabric-ListAvailableModuleVersions-response-nextToken"></a>
If nextToken is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours; using an expired token fails with ValidationException.
Type: String

 ** [versions](#API_ListAvailableModuleVersions_ResponseSyntax) **   <a name="rtbfabric-ListAvailableModuleVersions-response-versions"></a>
The versions on this page, highest version first.
Type: Array of [AvailableModuleVersionSummary](API_AvailableModuleVersionSummary.md) objects

## Errors
<a name="API_ListAvailableModuleVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_ListAvailableModuleVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/ListAvailableModuleVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/ListAvailableModuleVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/ListAvailableModuleVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/ListAvailableModuleVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/ListAvailableModuleVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/ListAvailableModuleVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/ListAvailableModuleVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/ListAvailableModuleVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/ListAvailableModuleVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/ListAvailableModuleVersions)
