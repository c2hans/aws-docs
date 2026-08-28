---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_UpdateDataset.html
---

# UpdateDataset
<a name="API_UpdateDataset"></a>

Modifies the definition of an existing DataBrew dataset.

## Request Syntax
<a name="API_UpdateDataset_RequestSyntax"></a>

```
PUT /datasets/{{name}} HTTP/1.1
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
   }
}
```

## URI Request Parameters
<a name="API_UpdateDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateDataset_RequestSyntax) **   <a name="databrew-UpdateDataset-request-uri-Name"></a>
The name of the dataset to be updated.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_UpdateDataset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Input](#API_UpdateDataset_RequestSyntax) **   <a name="databrew-UpdateDataset-request-Input"></a>
Represents information on how DataBrew can find data, in either the AWS Glue Data Catalog or Amazon S3.
Type: [Input](API_Input.md) object
Required: Yes

 ** [Format](#API_UpdateDataset_RequestSyntax) **   <a name="databrew-UpdateDataset-request-Format"></a>
The file format of a dataset that is created from an Amazon S3 file or folder.
Type: String
Valid Values: `CSV | JSON | PARQUET | EXCEL | ORC`
Required: No

 ** [FormatOptions](#API_UpdateDataset_RequestSyntax) **   <a name="databrew-UpdateDataset-request-FormatOptions"></a>
Represents a set of options that define the structure of either comma-separated value (CSV), Excel, or JSON input.
Type: [FormatOptions](API_FormatOptions.md) object
Required: No

 ** [PathOptions](#API_UpdateDataset_RequestSyntax) **   <a name="databrew-UpdateDataset-request-PathOptions"></a>
A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.
Type: [PathOptions](API_PathOptions.md) object
Required: No

## Response Syntax
<a name="API_UpdateDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_UpdateDataset_ResponseSyntax) **   <a name="databrew-UpdateDataset-response-Name"></a>
The name of the dataset that you updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_UpdateDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the specified resource was denied.
HTTP Status Code: 403

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/UpdateDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/UpdateDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/UpdateDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/UpdateDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/UpdateDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/UpdateDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/UpdateDataset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/UpdateDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/UpdateDataset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
