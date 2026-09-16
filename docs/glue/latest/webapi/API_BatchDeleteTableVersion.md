---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchDeleteTableVersion.html
---

# BatchDeleteTableVersion
<a name="API_BatchDeleteTableVersion"></a>

Deletes a specified batch of versions of a table.

## Request Syntax
<a name="API_BatchDeleteTableVersion_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "TableName": "{{string}}",
   "VersionIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchDeleteTableVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_BatchDeleteTableVersion_RequestSyntax) **   <a name="Glue-BatchDeleteTableVersion-request-CatalogId"></a>
The ID of the Data Catalog where the tables reside. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_BatchDeleteTableVersion_RequestSyntax) **   <a name="Glue-BatchDeleteTableVersion-request-DatabaseName"></a>
The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TableName](#API_BatchDeleteTableVersion_RequestSyntax) **   <a name="Glue-BatchDeleteTableVersion-request-TableName"></a>
The name of the table. For Hive compatibility, this name is entirely lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [VersionIds](#API_BatchDeleteTableVersion_RequestSyntax) **   <a name="Glue-BatchDeleteTableVersion-request-VersionIds"></a>
A list of the IDs of versions to be deleted. A `VersionId` is a string representation of an integer. Each version is incremented by 1.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_BatchDeleteTableVersion_ResponseSyntax"></a>

```
{
   "Errors": [
      {
         "ErrorDetail": {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         },
         "TableName": "string",
         "VersionId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteTableVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchDeleteTableVersion_ResponseSyntax) **   <a name="Glue-BatchDeleteTableVersion-response-Errors"></a>
A list of errors encountered while trying to delete the specified table versions.
Type: Array of [TableVersionError](API_TableVersionError.md) objects

## Errors
<a name="API_BatchDeleteTableVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
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
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_BatchDeleteTableVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchDeleteTableVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchDeleteTableVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchDeleteTableVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchDeleteTableVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchDeleteTableVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchDeleteTableVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchDeleteTableVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchDeleteTableVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchDeleteTableVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchDeleteTableVersion)
