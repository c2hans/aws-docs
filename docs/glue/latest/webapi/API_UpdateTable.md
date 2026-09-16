---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateTable.html
---

# UpdateTable
<a name="API_UpdateTable"></a>

Updates a metadata table in the Data Catalog.

## Request Syntax
<a name="API_UpdateTable_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "Force": {{boolean}},
   "Name": "{{string}}",
   "SkipArchive": {{boolean}},
   "TableInput": {
      "Description": "{{string}}",
      "LastAccessTime": {{number}},
      "LastAnalyzedTime": {{number}},
      "Name": "{{string}}",
      "Owner": "{{string}}",
      "Parameters": {
         "{{string}}" : "{{string}}"
      },
      "PartitionKeys": [
         {
            "Comment": "{{string}}",
            "Name": "{{string}}",
            "Parameters": {
               "{{string}}" : "{{string}}"
            },
            "Type": "{{string}}"
         }
      ],
      "Retention": {{number}},
      "StorageDescriptor": {
         "AdditionalLocations": [ "{{string}}" ],
         "BucketColumns": [ "{{string}}" ],
         "Columns": [
            {
               "Comment": "{{string}}",
               "Name": "{{string}}",
               "Parameters": {
                  "{{string}}" : "{{string}}"
               },
               "Type": "{{string}}"
            }
         ],
         "Compressed": {{boolean}},
         "InputFormat": "{{string}}",
         "Location": "{{string}}",
         "NumberOfBuckets": {{number}},
         "OutputFormat": "{{string}}",
         "Parameters": {
            "{{string}}" : "{{string}}"
         },
         "SchemaReference": {
            "SchemaId": {
               "RegistryName": "{{string}}",
               "SchemaArn": "{{string}}",
               "SchemaName": "{{string}}"
            },
            "SchemaVersionId": "{{string}}",
            "SchemaVersionNumber": {{number}}
         },
         "SerdeInfo": {
            "Name": "{{string}}",
            "Parameters": {
               "{{string}}" : "{{string}}"
            },
            "SerializationLibrary": "{{string}}"
         },
         "SkewedInfo": {
            "SkewedColumnNames": [ "{{string}}" ],
            "SkewedColumnValueLocationMaps": {
               "{{string}}" : "{{string}}"
            },
            "SkewedColumnValues": [ "{{string}}" ]
         },
         "SortColumns": [
            {
               "Column": "{{string}}",
               "SortOrder": {{number}}
            }
         ],
         "StoredAsSubDirectories": {{boolean}}
      },
      "TableType": "{{string}}",
      "TargetTable": {
         "CatalogId": "{{string}}",
         "DatabaseName": "{{string}}",
         "Name": "{{string}}",
         "Region": "{{string}}"
      },
      "ViewDefinition": {
         "Definer": "{{string}}",
         "IsProtected": {{boolean}},
         "LastRefreshType": "{{string}}",
         "RefreshSeconds": {{number}},
         "Representations": [
            {
               "Dialect": "{{string}}",
               "DialectVersion": "{{string}}",
               "ValidationConnection": "{{string}}",
               "ViewExpandedText": "{{string}}",
               "ViewOriginalText": "{{string}}"
            }
         ],
         "SubObjects": [ "{{string}}" ],
         "SubObjectVersionIds": [ {{number}} ],
         "ViewVersionId": {{number}},
         "ViewVersionToken": "{{string}}"
      },
      "ViewExpandedText": "{{string}}",
      "ViewOriginalText": "{{string}}"
   },
   "TransactionId": "{{string}}",
   "UpdateOpenTableFormatInput": {
      "UpdateIcebergInput": {
         "UpdateIcebergTableInput": {
            "Updates": [
               {
                  "Action": "{{string}}",
                  "EncryptionKey": {
                     "EncryptedById": "{{string}}",
                     "EncryptedKeyMetadata": "{{string}}",
                     "KeyId": "{{string}}",
                     "Properties": {
                        "{{string}}" : "{{string}}"
                     }
                  },
                  "KeyId": "{{string}}",
                  "Location": "{{string}}",
                  "PartitionSpec": {
                     "Fields": [
                        {
                           "FieldId": {{number}},
                           "Name": "{{string}}",
                           "SourceId": {{number}},
                           "Transform": "{{string}}"
                        }
                     ],
                     "SpecId": {{number}}
                  },
                  "Properties": {
                     "{{string}}" : "{{string}}"
                  },
                  "Schema": {
                     "Fields": [
                        {
                           "Doc": "{{string}}",
                           "Id": {{number}},
                           "InitialDefault": {{JSON value}},
                           "Name": "{{string}}",
                           "Required": {{boolean}},
                           "Type": {{JSON value}},
                           "WriteDefault": {{JSON value}}
                        }
                     ],
                     "IdentifierFieldIds": [ {{number}} ],
                     "SchemaId": {{number}},
                     "Type": "{{string}}"
                  },
                  "SortOrder": {
                     "Fields": [
                        {
                           "Direction": "{{string}}",
                           "NullOrder": "{{string}}",
                           "SourceId": {{number}},
                           "Transform": "{{string}}"
                        }
                     ],
                     "OrderId": {{number}}
                  }
               }
            ]
         }
      }
   },
   "VersionId": "{{string}}",
   "ViewUpdateAction": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateTable_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_UpdateTable_RequestSyntax) **   <a name="Glue-UpdateTable-request-CatalogId"></a>
The ID of the Data Catalog where the table resides. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_UpdateTable_RequestSyntax) **   <a name="Glue-UpdateTable-request-DatabaseName"></a>
The name of the catalog database in which the table resides. For Hive compatibility, this name is entirely lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Force](#API_UpdateTable_RequestSyntax) **   <a name="Glue-UpdateTable-request-Force"></a>
A flag that can be set to true to ignore matching storage descriptor and subobject matching requirements.
Type: Boolean
Required: No

 ** [Name](#API_UpdateTable_RequestSyntax) **   <a name="Glue-UpdateTable-request-Name"></a>
The unique identifier for the table within the specified database that will be created in the AWS Glue Data Catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [SkipArchive](#API_UpdateTable_RequestSyntax) **   <a name="Glue-UpdateTable-request-SkipArchive"></a>
By default, `UpdateTable` always creates an archived version of the table before updating it. However, if `skipArchive` is set to true, `UpdateTable` does not create the archived version.
Type: Boolean
Required: No

 ** [TableInput](#API_UpdateTable_RequestSyntax) **   <a name="Glue-UpdateTable-request-TableInput"></a>
An updated `TableInput` object to define the metadata table in the catalog.
Type: [TableInput](API_TableInput.md) object
Required: No

 ** [TransactionId](#API_UpdateTable_RequestSyntax) **   <a name="Glue-UpdateTable-request-TransactionId"></a>
The transaction ID at which to update the table contents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: No

 ** [UpdateOpenTableFormatInput](#API_UpdateTable_RequestSyntax) **   <a name="Glue-UpdateTable-request-UpdateOpenTableFormatInput"></a>
Input parameters for updating open table format tables in AWS GlueData Catalog, serving as a wrapper for format-specific update operations such as Apache Iceberg.
Type: [UpdateOpenTableFormatInput](API_UpdateOpenTableFormatInput.md) object
Required: No

 ** [VersionId](#API_UpdateTable_RequestSyntax) **   <a name="Glue-UpdateTable-request-VersionId"></a>
The version ID at which to update the table contents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [ViewUpdateAction](#API_UpdateTable_RequestSyntax) **   <a name="Glue-UpdateTable-request-ViewUpdateAction"></a>
The operation to be performed when updating the view.
Type: String
Valid Values: `ADD | REPLACE | ADD_OR_REPLACE | DROP`
Required: No

## Response Elements
<a name="API_UpdateTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateTable_Errors"></a>

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

 ** ResourceNotReadyException **
A resource was not ready for a transaction.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateTable)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateTable)
