---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_GetDatabase.html
---

# GetDatabase
<a name="API_GetDatabase"></a>

Returns a database object for the specified database and data catalog.

## Request Syntax
<a name="API_GetDatabase_RequestSyntax"></a>

```
{
   "CatalogName": "{{string}}",
   "DatabaseName": "{{string}}",
   "WorkGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDatabase_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogName](#API_GetDatabase_RequestSyntax) **   <a name="athena-GetDatabase-request-CatalogName"></a>
The name of the data catalog that contains the database to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [DatabaseName](#API_GetDatabase_RequestSyntax) **   <a name="athena-GetDatabase-request-DatabaseName"></a>
The name of the database to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [WorkGroup](#API_GetDatabase_RequestSyntax) **   <a name="athena-GetDatabase-request-WorkGroup"></a>
The name of the workgroup for which the metadata is being fetched. Required if requesting an IAM Identity Center enabled AWS Glue Data Catalog.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: No

## Response Syntax
<a name="API_GetDatabase_ResponseSyntax"></a>

```
{
   "Database": {
      "Description": "string",
      "Name": "string",
      "Parameters": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_GetDatabase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Database](#API_GetDatabase_ResponseSyntax) **   <a name="athena-GetDatabase-response-Database"></a>
The database returned.
Type: [Database](API_Database.md) object

## Errors
<a name="API_GetDatabase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** MetadataException **
An exception that Athena received when it called a custom metastore. Occurs if the error is not caused by user input (`InvalidRequestException`) or from the Athena platform (`InternalServerException`). For example, if a user-created Lambda function is missing permissions, the Lambda `4XX` exception is returned in a `MetadataException`.
HTTP Status Code: 400

## See Also
<a name="API_GetDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/GetDatabase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/GetDatabase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/GetDatabase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/GetDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/GetDatabase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/GetDatabase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/GetDatabase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/GetDatabase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/GetDatabase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
