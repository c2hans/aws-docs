---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_ListNodes.html
---

# ListNodes
<a name="API_ListNodes"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Returns a list of nodes.

## Request Syntax
<a name="API_ListNodes_RequestSyntax"></a>

```
GET /nodes?category={{Category}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&ownerAccount={{OwnerAccount}}&packageName={{PackageName}}&packageVersion={{PackageVersion}}&patchVersion={{PatchVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNodes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Category](#API_ListNodes_RequestSyntax) **   <a name="panorama-ListNodes-request-uri-Category"></a>
Search for nodes by category.
Valid Values: `BUSINESS_LOGIC | ML_MODEL | MEDIA_SOURCE | MEDIA_SINK`

 ** [MaxResults](#API_ListNodes_RequestSyntax) **   <a name="panorama-ListNodes-request-uri-MaxResults"></a>
The maximum number of nodes to return in one page of results.
Valid Range: Minimum value of 0. Maximum value of 25.

 ** [NextToken](#API_ListNodes_RequestSyntax) **   <a name="panorama-ListNodes-request-uri-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`

 ** [OwnerAccount](#API_ListNodes_RequestSyntax) **   <a name="panorama-ListNodes-request-uri-OwnerAccount"></a>
Search for nodes by the account ID of the nodes' owner.
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9a-z\_]+`

 ** [PackageName](#API_ListNodes_RequestSyntax) **   <a name="panorama-ListNodes-request-uri-PackageName"></a>
Search for nodes by name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [PackageVersion](#API_ListNodes_RequestSyntax) **   <a name="panorama-ListNodes-request-uri-PackageVersion"></a>
Search for nodes by version.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([0-9]+)\.([0-9]+)`

 ** [PatchVersion](#API_ListNodes_RequestSyntax) **   <a name="panorama-ListNodes-request-uri-PatchVersion"></a>
Search for nodes by patch version.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9]+`

## Request Body
<a name="API_ListNodes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNodes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Nodes": [
      {
         "Category": "string",
         "CreatedTime": number,
         "Description": "string",
         "Name": "string",
         "NodeId": "string",
         "OwnerAccount": "string",
         "PackageArn": "string",
         "PackageId": "string",
         "PackageName": "string",
         "PackageVersion": "string",
         "PatchVersion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNodes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListNodes_ResponseSyntax) **   <a name="panorama-ListNodes-response-NextToken"></a>
A pagination token that's included if more results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`

 ** [Nodes](#API_ListNodes_ResponseSyntax) **   <a name="panorama-ListNodes-response-Nodes"></a>
A list of nodes.
Type: Array of [Node](API_Node.md) objects

## Errors
<a name="API_ListNodes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The target resource is in use.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 409

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

 ** ValidationException **
The request contains an invalid parameter value.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** Fields **
A list of request parameters that failed validation.
 ** Reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_ListNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/ListNodes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/ListNodes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/ListNodes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/ListNodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/ListNodes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/ListNodes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/ListNodes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/ListNodes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/ListNodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/ListNodes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
