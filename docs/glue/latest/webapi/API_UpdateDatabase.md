---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateDatabase.html
---

# UpdateDatabase
<a name="API_UpdateDatabase"></a>

Updates an existing database definition in a Data Catalog.

## Request Syntax
<a name="API_UpdateDatabase_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseInput": {
      "CreateTableDefaultPermissions": [
         {
            "Permissions": [ "{{string}}" ],
            "Principal": {
               "DataLakePrincipalIdentifier": "{{string}}"
            }
         }
      ],
      "Description": "{{string}}",
      "FederatedDatabase": {
         "ConnectionName": "{{string}}",
         "ConnectionType": "{{string}}",
         "Identifier": "{{string}}"
      },
      "LocationUri": "{{string}}",
      "Name": "{{string}}",
      "Parameters": {
         "{{string}}" : "{{string}}"
      },
      "TargetDatabase": {
         "CatalogId": "{{string}}",
         "DatabaseName": "{{string}}",
         "Region": "{{string}}"
      }
   },
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDatabase_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_UpdateDatabase_RequestSyntax) **   <a name="Glue-UpdateDatabase-request-CatalogId"></a>
The ID of the Data Catalog in which the metadata database resides. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseInput](#API_UpdateDatabase_RequestSyntax) **   <a name="Glue-UpdateDatabase-request-DatabaseInput"></a>
A `DatabaseInput` object specifying the new definition of the metadata database in the catalog.
Type: [DatabaseInput](API_DatabaseInput.md) object
Required: Yes

 ** [Name](#API_UpdateDatabase_RequestSyntax) **   <a name="Glue-UpdateDatabase-request-Name"></a>
The name of the database to update in the catalog. For Hive compatibility, this is folded to lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Elements
<a name="API_UpdateDatabase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDatabase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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
<a name="API_UpdateDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateDatabase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateDatabase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateDatabase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateDatabase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateDatabase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateDatabase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateDatabase)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateDatabase)
