---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdateDataCatalog.html
---

# UpdateDataCatalog
<a name="API_UpdateDataCatalog"></a>

Updates the data catalog that has the specified name.

## Request Syntax
<a name="API_UpdateDataCatalog_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Parameters": {
      "{{string}}" : "{{string}}"
   },
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDataCatalog_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateDataCatalog_RequestSyntax) **   <a name="athena-UpdateDataCatalog-request-Description"></a>
New or modified text that describes the data catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [Name](#API_UpdateDataCatalog_RequestSyntax) **   <a name="athena-UpdateDataCatalog-request-Name"></a>
The name of the data catalog to update. The catalog name must be unique for the AWS account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters. The remainder of the length constraint of 256 is reserved for use by Athena.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Parameters](#API_UpdateDataCatalog_RequestSyntax) **   <a name="athena-UpdateDataCatalog-request-Parameters"></a>
Specifies the Lambda function or functions to use for updating the data catalog. This is a mapping whose values depend on the catalog type.
+ For the `HIVE` data catalog type, use the following syntax. The `metadata-function` parameter is required. `The sdk-version` parameter is optional and defaults to the currently supported version.

   `metadata-function=lambda_arn, sdk-version=version_number `
+ For the `LAMBDA` data catalog type, use one of the following sets of required parameters, but not both.
  + If you have one Lambda function that processes metadata and another for reading the actual data, use the following syntax. Both parameters are required.

     `metadata-function=lambda_arn, record-function=lambda_arn `
  +  If you have a composite Lambda function that processes both metadata and data, use the following syntax to specify your Lambda function.

     `function=lambda_arn `
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 51200.
Required: No

 ** [Type](#API_UpdateDataCatalog_RequestSyntax) **   <a name="athena-UpdateDataCatalog-request-Type"></a>
Specifies the type of data catalog to update. Specify `LAMBDA` for a federated catalog, `HIVE` for an external hive metastore, or `GLUE` for an AWS Glue Data Catalog.
Type: String
Valid Values: `LAMBDA | GLUE | HIVE | FEDERATED`
Required: Yes

## Response Elements
<a name="API_UpdateDataCatalog_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDataCatalog_Errors"></a>

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
<a name="API_UpdateDataCatalog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/UpdateDataCatalog)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/UpdateDataCatalog)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/UpdateDataCatalog)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/UpdateDataCatalog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/UpdateDataCatalog)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/UpdateDataCatalog)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/UpdateDataCatalog)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/UpdateDataCatalog)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/UpdateDataCatalog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/UpdateDataCatalog)
