---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_SearchTablesByLFTags.html
---

# SearchTablesByLFTags
<a name="API_SearchTablesByLFTags"></a>

This operation allows a search on `TABLE` resources by `LFTag`s. This will be used by admins who want to grant user permissions on certain LF-tags. Before making a grant, the admin can use `SearchTablesByLFTags` to find all resources where the given `LFTag`s are valid to verify whether the returned resources can be shared.

## Request Syntax
<a name="API_SearchTablesByLFTags_RequestSyntax"></a>

```
POST /SearchTablesByLFTags HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "Expression": [
      {
         "TagKey": "{{string}}",
         "TagValues": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchTablesByLFTags_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchTablesByLFTags_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_SearchTablesByLFTags_RequestSyntax) **   <a name="lakeformation-SearchTablesByLFTags-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Expression](#API_SearchTablesByLFTags_RequestSyntax) **   <a name="lakeformation-SearchTablesByLFTags-request-Expression"></a>
A list of conditions (`LFTag` structures) to search for in table resources.
Type: Array of [LFTag](API_LFTag.md) objects
Required: Yes

 ** [MaxResults](#API_SearchTablesByLFTags_RequestSyntax) **   <a name="lakeformation-SearchTablesByLFTags-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchTablesByLFTags_RequestSyntax) **   <a name="lakeformation-SearchTablesByLFTags-request-NextToken"></a>
A continuation token, if this is not the first call to retrieve this list.
Type: String
Required: No

## Response Syntax
<a name="API_SearchTablesByLFTags_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "TableList": [
      {
         "LFTagOnDatabase": [
            {
               "CatalogId": "string",
               "TagKey": "string",
               "TagValues": [ "string" ]
            }
         ],
         "LFTagsOnColumns": [
            {
               "LFTags": [
                  {
                     "CatalogId": "string",
                     "TagKey": "string",
                     "TagValues": [ "string" ]
                  }
               ],
               "Name": "string"
            }
         ],
         "LFTagsOnTable": [
            {
               "CatalogId": "string",
               "TagKey": "string",
               "TagValues": [ "string" ]
            }
         ],
         "Table": {
            "CatalogId": "string",
            "DatabaseName": "string",
            "Name": "string",
            "TableWildcard": {
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_SearchTablesByLFTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SearchTablesByLFTags_ResponseSyntax) **   <a name="lakeformation-SearchTablesByLFTags-response-NextToken"></a>
A continuation token, present if the current list segment is not the last. On the first run, if you include a not null (a value) token you can get empty pages.
Type: String

 ** [TableList](#API_SearchTablesByLFTags_ResponseSyntax) **   <a name="lakeformation-SearchTablesByLFTags-response-TableList"></a>
A list of tables that meet the LF-tag conditions.
Type: Array of [TaggedTable](API_TaggedTable.md) objects

## Errors
<a name="API_SearchTablesByLFTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** EntityNotFoundException **
A specified entity does not exist.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** GlueEncryptionException **
An encryption operation failed.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_SearchTablesByLFTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/SearchTablesByLFTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/SearchTablesByLFTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/SearchTablesByLFTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/SearchTablesByLFTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/SearchTablesByLFTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/SearchTablesByLFTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/SearchTablesByLFTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/SearchTablesByLFTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/SearchTablesByLFTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/SearchTablesByLFTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
