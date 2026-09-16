---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_CreateDataset.html
---

# CreateDataset
<a name="API_CreateDataset"></a>

Creates a new DataBrew dataset.

## Request Syntax
<a name="API_CreateDataset_RequestSyntax"></a>

```
POST /datasets HTTP/1.1
Content-type: application/json

{
   "Format": "{{string}}",
   "FormatOptions": {
      "Csv": {
         "Delimiter": "{{string}}",
         "HeaderRow": {{boolean}}
      },
      "Excel": {
         "HeaderRow": {{boolean}},
         "SheetIndexes": [ {{number}} ],
         "SheetNames": [ "{{string}}" ]
      },
      "Json": {
         "MultiLine": {{boolean}}
      }
   },
   "Input": {
      "DatabaseInputDefinition": {
         "DatabaseTableName": "{{string}}",
         "GlueConnectionName": "{{string}}",
         "QueryString": "{{string}}",
         "TempDirectory": {
            "Bucket": "{{string}}",
            "BucketOwner": "{{string}}",
            "Key": "{{string}}"
         }
      },
      "DataCatalogInputDefinition": {
         "CatalogId": "{{string}}",
         "DatabaseName": "{{string}}",
         "TableName": "{{string}}",
         "TempDirectory": {
            "Bucket": "{{string}}",
            "BucketOwner": "{{string}}",
            "Key": "{{string}}"
         }
      },
      "Metadata": {
         "SourceArn": "{{string}}"
      },
      "S3InputDefinition": {
         "Bucket": "{{string}}",
         "BucketOwner": "{{string}}",
         "Key": "{{string}}"
      }
   },
   "Name": "{{string}}",
   "PathOptions": {
      "FilesLimit": {
         "MaxFiles": {{number}},
         "Order": "{{string}}",
         "OrderedBy": "{{string}}"
      },
      "LastModifiedDateCondition": {
         "Expression": "{{string}}",
         "ValuesMap": {
            "{{string}}" : "{{string}}"
         }
      },
      "Parameters": {
         "{{string}}" : {
            "CreateColumn": {{boolean}},
            "DatetimeOptions": {
               "Format": "{{string}}",
               "LocaleCode": "{{string}}",
               "TimezoneOffset": "{{string}}"
            },
            "Filter": {
               "Expression": "{{string}}",
               "ValuesMap": {
                  "{{string}}" : "{{string}}"
               }
            },
            "Name": "{{string}}",
            "Type": "{{string}}"
         }
      }
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDataset_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDataset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Input](#API_CreateDataset_RequestSyntax) **   <a name="databrew-CreateDataset-request-Input"></a>
Represents information on how DataBrew can find data, in either the AWS Glue Data Catalog or Amazon S3.
Type: [Input](API_Input.md) object
Required: Yes

 ** [Name](#API_CreateDataset_RequestSyntax) **   <a name="databrew-CreateDataset-request-Name"></a>
The name of the dataset to be created. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Format](#API_CreateDataset_RequestSyntax) **   <a name="databrew-CreateDataset-request-Format"></a>
The file format of a dataset that is created from an Amazon S3 file or folder.
Type: String
Valid Values: `CSV | JSON | PARQUET | EXCEL | ORC`
Required: No

 ** [FormatOptions](#API_CreateDataset_RequestSyntax) **   <a name="databrew-CreateDataset-request-FormatOptions"></a>
Represents a set of options that define the structure of either comma-separated value (CSV), Excel, or JSON input.
Type: [FormatOptions](API_FormatOptions.md) object
Required: No

 ** [PathOptions](#API_CreateDataset_RequestSyntax) **   <a name="databrew-CreateDataset-request-PathOptions"></a>
A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.
Type: [PathOptions](API_PathOptions.md) object
Required: No

 ** [Tags](#API_CreateDataset_RequestSyntax) **   <a name="databrew-CreateDataset-request-Tags"></a>
Metadata tags to apply to this dataset.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_CreateDataset_ResponseSyntax) **   <a name="databrew-CreateDataset-response-Name"></a>
The name of the dataset that you created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_CreateDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the specified resource was denied.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
A service quota is exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/CreateDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/CreateDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/CreateDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/CreateDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/CreateDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/CreateDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/CreateDataset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/CreateDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/CreateDataset)
