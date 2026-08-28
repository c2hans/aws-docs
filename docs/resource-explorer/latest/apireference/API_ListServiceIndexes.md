---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListServiceIndexes.html
---

# ListServiceIndexes
<a name="API_ListServiceIndexes"></a>

Lists all Resource Explorer indexes across the specified AWS Regions. This operation returns information about indexes including their ARNs, types, and Regions.

## Request Syntax
<a name="API_ListServiceIndexes_RequestSyntax"></a>

```
POST /ListServiceIndexes HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Regions": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListServiceIndexes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListServiceIndexes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListServiceIndexes_RequestSyntax) **   <a name="resourceexplorer-ListServiceIndexes-request-MaxResults"></a>
The maximum number of index results to return in a single response. Valid values are between `1` and `100`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListServiceIndexes_RequestSyntax) **   <a name="resourceexplorer-ListServiceIndexes-request-NextToken"></a>
The pagination token from a previous `ListServiceIndexes` response. Use this token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Regions](#API_ListServiceIndexes_RequestSyntax) **   <a name="resourceexplorer-ListServiceIndexes-request-Regions"></a>
A list of AWS Regions to include in the search for indexes. If not specified, indexes from all Regions are returned.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Pattern: `[a-z-]+-[a-z]+-[0-9]`
Required: No

## Response Syntax
<a name="API_ListServiceIndexes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Indexes": [
      {
         "Arn": "string",
         "Region": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListServiceIndexes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Indexes](#API_ListServiceIndexes_ResponseSyntax) **   <a name="resourceexplorer-ListServiceIndexes-response-Indexes"></a>
A list of `Index` objects that describe the Resource Explorer indexes found in the specified Regions.
Type: Array of [Index](API_Index.md) objects

 ** [NextToken](#API_ListServiceIndexes_ResponseSyntax) **   <a name="resourceexplorer-ListServiceIndexes-response-NextToken"></a>
The pagination token to use in a subsequent `ListServiceIndexes` request to retrieve the next set of results.
Type: String

## Errors
<a name="API_ListServiceIndexes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## See Also
<a name="API_ListServiceIndexes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/ListServiceIndexes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/ListServiceIndexes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/ListServiceIndexes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/ListServiceIndexes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/ListServiceIndexes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/ListServiceIndexes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/ListServiceIndexes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/ListServiceIndexes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/ListServiceIndexes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/ListServiceIndexes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
