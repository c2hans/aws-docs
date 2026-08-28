---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetLFTag.html
---

# GetLFTag
<a name="API_GetLFTag"></a>

Returns an LF-tag definition.

## Request Syntax
<a name="API_GetLFTag_RequestSyntax"></a>

```
POST /GetLFTag HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "TagKey": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetLFTag_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetLFTag_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetLFTag_RequestSyntax) **   <a name="lakeformation-GetLFTag-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [TagKey](#API_GetLFTag_RequestSyntax) **   <a name="lakeformation-GetLFTag-request-TagKey"></a>
The key-name for the LF-tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@%]*)$`
Required: Yes

## Response Syntax
<a name="API_GetLFTag_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CatalogId": "string",
   "TagKey": "string",
   "TagValues": [ "string" ]
}
```

## Response Elements
<a name="API_GetLFTag_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CatalogId](#API_GetLFTag_ResponseSyntax) **   <a name="lakeformation-GetLFTag-response-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [TagKey](#API_GetLFTag_ResponseSyntax) **   <a name="lakeformation-GetLFTag-response-TagKey"></a>
The key-name for the LF-tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@%]*)$`

 ** [TagValues](#API_GetLFTag_ResponseSyntax) **   <a name="lakeformation-GetLFTag-response-TagValues"></a>
A list of possible values an attribute can take.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\*\/=+\-@%]*)$`

## Errors
<a name="API_GetLFTag_Errors"></a>

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
<a name="API_GetLFTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/GetLFTag)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/GetLFTag)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/GetLFTag)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/GetLFTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/GetLFTag)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/GetLFTag)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/GetLFTag)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/GetLFTag)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/GetLFTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/GetLFTag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
