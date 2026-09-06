---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdatePackageScope.html
---

# UpdatePackageScope
<a name="API_UpdatePackageScope"></a>

Updates the scope of a package. Scope of the package defines users who can view and associate a package.

## Request Syntax
<a name="API_UpdatePackageScope_RequestSyntax"></a>

```
POST /2021-01-01/packages/updateScope HTTP/1.1
Content-type: application/json

{
   "Operation": "{{string}}",
   "PackageID": "{{string}}",
   "PackageUserList": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdatePackageScope_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdatePackageScope_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Operation](#API_UpdatePackageScope_RequestSyntax) **   <a name="opensearchservice-UpdatePackageScope-request-Operation"></a>
 The operation to perform on the package scope (e.g., add/remove/override users).
Type: String
Valid Values: `ADD | OVERRIDE | REMOVE`
Required: Yes

 ** [PackageID](#API_UpdatePackageScope_RequestSyntax) **   <a name="opensearchservice-UpdatePackageScope-request-PackageID"></a>
ID of the package whose scope is being updated.
Type: String
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: Yes

 ** [PackageUserList](#API_UpdatePackageScope_RequestSyntax) **   <a name="opensearchservice-UpdatePackageScope-request-PackageUserList"></a>
 List of users to be added or removed from the package scope.
Type: Array of strings
Length Constraints: Minimum length of 6. Maximum length of 12.
Pattern: `^[0-9]{12}$|^GLOBAL$`
Required: Yes

## Response Syntax
<a name="API_UpdatePackageScope_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Operation": "string",
   "PackageID": "string",
   "PackageUserList": [ "string" ]
}
```

## Response Elements
<a name="API_UpdatePackageScope_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Operation](#API_UpdatePackageScope_ResponseSyntax) **   <a name="opensearchservice-UpdatePackageScope-response-Operation"></a>
The operation that was performed on the package scope.
Type: String
Valid Values: `ADD | OVERRIDE | REMOVE`

 ** [PackageID](#API_UpdatePackageScope_ResponseSyntax) **   <a name="opensearchservice-UpdatePackageScope-response-PackageID"></a>
 ID of the package whose scope was updated.
Type: String
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`

 ** [PackageUserList](#API_UpdatePackageScope_ResponseSyntax) **   <a name="opensearchservice-UpdatePackageScope-response-PackageUserList"></a>
 List of users who have access to the package after the scope update.
Type: Array of strings
Length Constraints: Minimum length of 6. Maximum length of 12.
Pattern: `^[0-9]{12}$|^GLOBAL$`

## Errors
<a name="API_UpdatePackageScope_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePackageScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/UpdatePackageScope)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/UpdatePackageScope)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/UpdatePackageScope)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/UpdatePackageScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/UpdatePackageScope)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/UpdatePackageScope)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/UpdatePackageScope)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/UpdatePackageScope)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/UpdatePackageScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/UpdatePackageScope)
