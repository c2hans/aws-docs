---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_DescribeDataset.html
---

# DescribeDataset
<a name="API_DescribeDataset"></a>

Returns the definition of a specific DataBrew dataset.

## Request Syntax
<a name="API_DescribeDataset_RequestSyntax"></a>

```
GET /datasets/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DescribeDataset_RequestSyntax) **   <a name="databrew-DescribeDataset-request-uri-Name"></a>
The name of the dataset to be described.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_DescribeDataset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateDate": number,
   "CreatedBy": "string",
   "Format": "string",
   "FormatOptions": {
      "Csv": {
         "Delimiter": "string",
         "HeaderRow": boolean
      },
      "Excel": {
         "HeaderRow": boolean,
         "SheetIndexes": [ number ],
         "SheetNames": [ "string" ]
      },
      "Json": {
         "MultiLine": boolean
      }
   },
   "Input": {
      "DatabaseInputDefinition": {
         "DatabaseTableName": "string",
         "GlueConnectionName": "string",
         "QueryString": "string",
         "TempDirectory": {
            "Bucket": "string",
            "BucketOwner": "string",
            "Key": "string"
         }
      },
      "DataCatalogInputDefinition": {
         "CatalogId": "string",
         "DatabaseName": "string",
         "TableName": "string",
         "TempDirectory": {
            "Bucket": "string",
            "BucketOwner": "string",
            "Key": "string"
         }
      },
      "Metadata": {
         "SourceArn": "string"
      },
      "S3InputDefinition": {
         "Bucket": "string",
         "BucketOwner": "string",
         "Key": "string"
      }
   },
   "LastModifiedBy": "string",
   "LastModifiedDate": number,
   "Name": "string",
   "PathOptions": {
      "FilesLimit": {
         "MaxFiles": number,
         "Order": "string",
         "OrderedBy": "string"
      },
      "LastModifiedDateCondition": {
         "Expression": "string",
         "ValuesMap": {
            "string" : "string"
         }
      },
      "Parameters": {
         "string" : {
            "CreateColumn": boolean,
            "DatetimeOptions": {
               "Format": "string",
               "LocaleCode": "string",
               "TimezoneOffset": "string"
            },
            "Filter": {
               "Expression": "string",
               "ValuesMap": {
                  "string" : "string"
               }
            },
            "Name": "string",
            "Type": "string"
         }
      }
   },
   "ResourceArn": "string",
   "Source": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_DescribeDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Input](#API_DescribeDataset_ResponseSyntax) **   <a name="databrew-DescribeDataset-response-Input"></a>
Represents information on how DataBrew can find data, in either the AWS Glue Data Catalog or Amazon S3.
Type: [Input](API_Input.md) object

 ** [Name](#API_DescribeDataset_ResponseSyntax) **   <a name="databrew-DescribeDataset-response-Name"></a>
The name of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [CreateDate](#API_DescribeDataset_ResponseSyntax) **   <a name="databrew-DescribeDataset-response-CreateDate"></a>
The date and time that the dataset was created.
Type: Timestamp

 ** [CreatedBy](#API_DescribeDataset_ResponseSyntax) **   <a name="databrew-DescribeDataset-response-CreatedBy"></a>
The identifier (user name) of the user who created the dataset.
Type: String

 ** [Format](#API_DescribeDataset_ResponseSyntax) **   <a name="databrew-DescribeDataset-response-Format"></a>
The file format of a dataset that is created from an Amazon S3 file or folder.
Type: String
Valid Values: `CSV | JSON | PARQUET | EXCEL | ORC`

 ** [FormatOptions](#API_DescribeDataset_ResponseSyntax) **   <a name="databrew-DescribeDataset-response-FormatOptions"></a>
Represents a set of options that define the structure of either comma-separated value (CSV), Excel, or JSON input.
Type: [FormatOptions](API_FormatOptions.md) object

 ** [LastModifiedBy](#API_DescribeDataset_ResponseSyntax) **   <a name="databrew-DescribeDataset-response-LastModifiedBy"></a>
The identifier (user name) of the user who last modified the dataset.
Type: String

 ** [LastModifiedDate](#API_DescribeDataset_ResponseSyntax) **   <a name="databrew-DescribeDataset-response-LastModifiedDate"></a>
The date and time that the dataset was last modified.
Type: Timestamp

 ** [PathOptions](#API_DescribeDataset_ResponseSyntax) **   <a name="databrew-DescribeDataset-response-PathOptions"></a>
A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.
Type: [PathOptions](API_PathOptions.md) object

 ** [ResourceArn](#API_DescribeDataset_ResponseSyntax) **   <a name="databrew-DescribeDataset-response-ResourceArn"></a>
The Amazon Resource Name (ARN) of the dataset.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [Source](#API_DescribeDataset_ResponseSyntax) **   <a name="databrew-DescribeDataset-response-Source"></a>
The location of the data for this dataset, Amazon S3 or the AWS Glue Data Catalog.
Type: String
Valid Values: `S3 | DATA-CATALOG | DATABASE`

 ** [Tags](#API_DescribeDataset_ResponseSyntax) **   <a name="databrew-DescribeDataset-response-Tags"></a>
Metadata tags associated with this dataset.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_DescribeDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/DescribeDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/DescribeDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/DescribeDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/DescribeDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/DescribeDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/DescribeDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/DescribeDataset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/DescribeDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/DescribeDataset)
