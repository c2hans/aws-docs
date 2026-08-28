---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_SearchDatabasesByLFTags.html
---

# SearchDatabasesByLFTags
<a name="API_SearchDatabasesByLFTags"></a>

This operation allows a search on `DATABASE` resources by `TagCondition`. This operation is used by admins who want to grant user permissions on certain `TagConditions`. Before making a grant, the admin can use `SearchDatabasesByTags` to find all resources where the given `TagConditions` are valid to verify whether the returned resources can be shared.

## Request Syntax
<a name="API_SearchDatabasesByLFTags_RequestSyntax"></a>

```
POST /SearchDatabasesByLFTags HTTP/1.1
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
<a name="API_SearchDatabasesByLFTags_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchDatabasesByLFTags_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_SearchDatabasesByLFTags_RequestSyntax) **   <a name="lakeformation-SearchDatabasesByLFTags-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Expression](#API_SearchDatabasesByLFTags_RequestSyntax) **   <a name="lakeformation-SearchDatabasesByLFTags-request-Expression"></a>
A list of conditions (`LFTag` structures) to search for in database resources.
Type: Array of [LFTag](API_LFTag.md) objects
Required: Yes

 ** [MaxResults](#API_SearchDatabasesByLFTags_RequestSyntax) **   <a name="lakeformation-SearchDatabasesByLFTags-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchDatabasesByLFTags_RequestSyntax) **   <a name="lakeformation-SearchDatabasesByLFTags-request-NextToken"></a>
A continuation token, if this is not the first call to retrieve this list.
Type: String
Required: No

## Response Syntax
<a name="API_SearchDatabasesByLFTags_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DatabaseList": [
      {
         "Database": {
            "CatalogId": "string",
            "Name": "string"
         },
         "LFTags": [
            {
               "CatalogId": "string",
               "TagKey": "string",
               "TagValues": [ "string" ]
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchDatabasesByLFTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatabaseList](#API_SearchDatabasesByLFTags_ResponseSyntax) **   <a name="lakeformation-SearchDatabasesByLFTags-response-DatabaseList"></a>
A list of databases that meet the LF-tag conditions.
Type: Array of [TaggedDatabase](API_TaggedDatabase.md) objects

 ** [NextToken](#API_SearchDatabasesByLFTags_ResponseSyntax) **   <a name="lakeformation-SearchDatabasesByLFTags-response-NextToken"></a>
A continuation token, present if the current list segment is not the last.
Type: String

## Errors
<a name="API_SearchDatabasesByLFTags_Errors"></a>

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
<a name="API_SearchDatabasesByLFTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/SearchDatabasesByLFTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/SearchDatabasesByLFTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/SearchDatabasesByLFTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/SearchDatabasesByLFTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/SearchDatabasesByLFTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/SearchDatabasesByLFTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/SearchDatabasesByLFTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/SearchDatabasesByLFTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/SearchDatabasesByLFTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/SearchDatabasesByLFTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
