---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_DeleteDataCatalog.html
---

# DeleteDataCatalog
<a name="API_DeleteDataCatalog"></a>

Deletes a data catalog.

## Request Syntax
<a name="API_DeleteDataCatalog_RequestSyntax"></a>

```
{
   "DeleteCatalogOnly": {{boolean}},
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDataCatalog_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeleteCatalogOnly](#API_DeleteDataCatalog_RequestSyntax) **   <a name="athena-DeleteDataCatalog-request-DeleteCatalogOnly"></a>
Deletes the Athena Data Catalog. You can only use this with the `FEDERATED` catalogs. You usually perform this before registering the connector with Glue Data Catalog. After deletion, you will have to manage the Glue Connection and Lambda function.
Type: Boolean
Required: No

 ** [Name](#API_DeleteDataCatalog_RequestSyntax) **   <a name="athena-DeleteDataCatalog-request-Name"></a>
The name of the data catalog to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_DeleteDataCatalog_ResponseSyntax"></a>

```
{
   "DataCatalog": {
      "ConnectionType": "string",
      "Description": "string",
      "Error": "string",
      "Name": "string",
      "Parameters": {
         "string" : "string"
      },
      "Status": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_DeleteDataCatalog_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataCatalog](#API_DeleteDataCatalog_ResponseSyntax) **   <a name="athena-DeleteDataCatalog-response-DataCatalog"></a>
Contains information about a data catalog in an AWS account.
In the Athena console, data catalogs are listed as "data sources" on the **Data sources** page under the **Data source name** column.
Type: [DataCatalog](API_DataCatalog.md) object

## Errors
<a name="API_DeleteDataCatalog_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDataCatalog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/DeleteDataCatalog)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/DeleteDataCatalog)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/DeleteDataCatalog)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/DeleteDataCatalog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/DeleteDataCatalog)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/DeleteDataCatalog)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/DeleteDataCatalog)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/DeleteDataCatalog)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/DeleteDataCatalog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/DeleteDataCatalog)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
