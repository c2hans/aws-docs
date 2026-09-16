---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateCatalog.html
---

# CreateCatalog
<a name="API_CreateCatalog"></a>

Creates a new catalog in the AWS Glue Data Catalog.

## Request Syntax
<a name="API_CreateCatalog_RequestSyntax"></a>

```
{
   "CatalogInput": {
      "AllowFullTableExternalDataAccess": "{{string}}",
      "CatalogProperties": {
         "CustomProperties": {
            "{{string}}" : "{{string}}"
         },
         "DataLakeAccessProperties": {
            "CatalogType": "{{string}}",
            "DataLakeAccess": {{boolean}},
            "DataTransferRole": "{{string}}",
            "KmsKey": "{{string}}"
         },
         "IcebergOptimizationProperties": {
            "Compaction": {
               "{{string}}" : "{{string}}"
            },
            "OrphanFileDeletion": {
               "{{string}}" : "{{string}}"
            },
            "Retention": {
               "{{string}}" : "{{string}}"
            },
            "RoleArn": "{{string}}"
         }
      },
      "CreateDatabaseDefaultPermissions": [
         {
            "Permissions": [ "{{string}}" ],
            "Principal": {
               "DataLakePrincipalIdentifier": "{{string}}"
            }
         }
      ],
      "CreateTableDefaultPermissions": [
         {
            "Permissions": [ "{{string}}" ],
            "Principal": {
               "DataLakePrincipalIdentifier": "{{string}}"
            }
         }
      ],
      "Description": "{{string}}",
      "FederatedCatalog": {
         "ConnectionName": "{{string}}",
         "ConnectionType": "{{string}}",
         "Identifier": "{{string}}"
      },
      "Parameters": {
         "{{string}}" : "{{string}}"
      },
      "TargetRedshiftCatalog": {
         "CatalogArn": "{{string}}"
      }
   },
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateCatalog_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogInput](#API_CreateCatalog_RequestSyntax) **   <a name="Glue-CreateCatalog-request-CatalogInput"></a>
A `CatalogInput` object that defines the metadata for the catalog.
Type: [CatalogInput](API_CatalogInput.md) object
Required: Yes

 ** [Name](#API_CreateCatalog_RequestSyntax) **   <a name="Glue-CreateCatalog-request-Name"></a>
The name of the catalog to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!(.*[.\/\\]|aws:)).*$`
Required: Yes

 ** [Tags](#API_CreateCatalog_RequestSyntax) **   <a name="Glue-CreateCatalog-request-Tags"></a>
A map array of key-value pairs, not more than 50 pairs. Each key is a UTF-8 string, not less than 1 or more than 128 bytes long. Each value is a UTF-8 string, not more than 256 bytes long. The tags you assign to the catalog.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Elements
<a name="API_CreateCatalog_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateCatalog_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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

 ** FederatedResourceAlreadyExistsException **
A federated resource already exists.
 ** AssociatedGlueResource **
The associated Glue resource already exists.
 ** Message **
The message describing the problem.
HTTP Status Code: 400

 ** FederationSourceException **
A federation source failed.
 ** FederationSourceErrorCode **
The error code of the problem.
 ** Message **
The message describing the problem.
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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateCatalog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateCatalog)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateCatalog)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateCatalog)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateCatalog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateCatalog)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateCatalog)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateCatalog)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateCatalog)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateCatalog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateCatalog)
