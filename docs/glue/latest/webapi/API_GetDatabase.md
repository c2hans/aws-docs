---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetDatabase.html
---

# GetDatabase
<a name="API_GetDatabase"></a>

Retrieves the definition of a specified database.

## Request Syntax
<a name="API_GetDatabase_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDatabase_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetDatabase_RequestSyntax) **   <a name="Glue-GetDatabase-request-CatalogId"></a>
The ID of the Data Catalog in which the database resides. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Name](#API_GetDatabase_RequestSyntax) **   <a name="Glue-GetDatabase-request-Name"></a>
The name of the database to retrieve. For Hive compatibility, this should be all lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetDatabase_ResponseSyntax"></a>

```
{
   "Database": {
      "CatalogId": "string",
      "CreateTableDefaultPermissions": [
         {
            "Permissions": [ "string" ],
            "Principal": {
               "DataLakePrincipalIdentifier": "string"
            }
         }
      ],
      "CreateTime": number,
      "Description": "string",
      "FederatedDatabase": {
         "ConnectionName": "string",
         "ConnectionType": "string",
         "Identifier": "string"
      },
      "LocationUri": "string",
      "Name": "string",
      "Parameters": {
         "string" : "string"
      },
      "TargetDatabase": {
         "CatalogId": "string",
         "DatabaseName": "string",
         "Region": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetDatabase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Database](#API_GetDatabase_ResponseSyntax) **   <a name="Glue-GetDatabase-response-Database"></a>
The definition of the specified database in the Data Catalog.
Type: [Database](API_Database.md) object

## Errors
<a name="API_GetDatabase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** FederationSourceException **
A federation source failed.
 ** FederationSourceErrorCode **
The error code of the problem.
 ** Message **
The message describing the problem.
HTTP Status Code: 400

 ** FederationSourceRetryableException **
A federation source failed, but the operation may be retried.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** GlueEncryptionException **
An encryption operation failed.
 ** Message **
The message describing the problem.
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
<a name="API_GetDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetDatabase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetDatabase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetDatabase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetDatabase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetDatabase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetDatabase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetDatabase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetDatabase)
