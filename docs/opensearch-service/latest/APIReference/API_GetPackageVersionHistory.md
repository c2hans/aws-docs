---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetPackageVersionHistory.html
---

# GetPackageVersionHistory
<a name="API_GetPackageVersionHistory"></a>

Returns a list of Amazon OpenSearch Service package versions, along with their creation time, commit message, and plugin properties (if the package is a zip plugin package). For more information, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html).

## Request Syntax
<a name="API_GetPackageVersionHistory_RequestSyntax"></a>

```
GET /2021-01-01/packages/{{PackageID}}/history?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPackageVersionHistory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_GetPackageVersionHistory_RequestSyntax) **   <a name="opensearchservice-GetPackageVersionHistory-request-uri-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.
Valid Range: Maximum value of 100.

 ** [NextToken](#API_GetPackageVersionHistory_RequestSyntax) **   <a name="opensearchservice-GetPackageVersionHistory-request-uri-NextToken"></a>
If your initial `GetPackageVersionHistory` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `GetPackageVersionHistory` operations, which returns results in the next page.

 ** [PackageID](#API_GetPackageVersionHistory_RequestSyntax) **   <a name="opensearchservice-GetPackageVersionHistory-request-uri-PackageID"></a>
The unique identifier of the package.
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: Yes

## Request Body
<a name="API_GetPackageVersionHistory_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPackageVersionHistory_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "PackageID": "string",
   "PackageVersionHistoryList": [
      {
         "CommitMessage": "string",
         "CreatedAt": number,
         "PackageConfiguration": {
            "ConfigurationRequirement": "string",
            "LicenseFilepath": "string",
            "LicenseRequirement": "string",
            "RequiresRestartForConfigurationUpdate": boolean
         },
         "PackageVersion": "string",
         "PluginProperties": {
            "ClassName": "string",
            "Description": "string",
            "Name": "string",
            "UncompressedSizeInBytes": number,
            "Version": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetPackageVersionHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetPackageVersionHistory_ResponseSyntax) **   <a name="opensearchservice-GetPackageVersionHistory-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

 ** [PackageID](#API_GetPackageVersionHistory_ResponseSyntax) **   <a name="opensearchservice-GetPackageVersionHistory-response-PackageID"></a>
The unique identifier of the package.
Type: String
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`

 ** [PackageVersionHistoryList](#API_GetPackageVersionHistory_ResponseSyntax) **   <a name="opensearchservice-GetPackageVersionHistory-response-PackageVersionHistoryList"></a>
A list of package versions, along with their creation time and commit message.
Type: Array of [PackageVersionHistory](API_PackageVersionHistory.md) objects

## Errors
<a name="API_GetPackageVersionHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

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
<a name="API_GetPackageVersionHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/GetPackageVersionHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/GetPackageVersionHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/GetPackageVersionHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/GetPackageVersionHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/GetPackageVersionHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/GetPackageVersionHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/GetPackageVersionHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/GetPackageVersionHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/GetPackageVersionHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/GetPackageVersionHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
