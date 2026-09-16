---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_CreateExport.html
---

# CreateExport
<a name="API_DataExports_CreateExport"></a>

Creates a data export and specifies the data query, the delivery preference, and any optional resource tags.

A `DataQuery` consists of both a `QueryStatement` and `TableConfigurations`.

The `QueryStatement` is an SQL statement. Data Exports only supports a limited subset of the SQL syntax. For more information on the SQL syntax that is supported, see [Data query](https://docs.aws.amazon.com/cur/latest/userguide/de-data-query.html). To view the available tables and columns, see the [Data Exports table dictionary](https://docs.aws.amazon.com/cur/latest/userguide/de-table-dictionary.html).

The `TableConfigurations` is a collection of specified `TableProperties` for the table being queried in the `QueryStatement`. TableProperties are additional configurations you can provide to change the data and schema of a table. Each table can have different TableProperties. However, tables are not required to have any TableProperties. Each table property has a default value that it assumes if not specified. For more information on table configurations, see [Data query](https://docs.aws.amazon.com/cur/latest/userguide/de-data-query.html). To view the table properties available for each table, see the [Data Exports table dictionary](https://docs.aws.amazon.com/cur/latest/userguide/de-table-dictionary.html) or use the `ListTables` API to get a response of all tables and their available properties.

## Request Syntax
<a name="API_DataExports_CreateExport_RequestSyntax"></a>

```
{
   "Export": {
      "DataQuery": {
         "QueryStatement": "{{string}}",
         "TableConfigurations": {
            "{{string}}" : {
               "{{string}}" : "{{string}}"
            }
         }
      },
      "Description": "{{string}}",
      "DestinationConfigurations": {
         "S3Destination": {
            "S3Bucket": "{{string}}",
            "S3BucketOwner": "{{string}}",
            "S3OutputConfigurations": {
               "Compression": "{{string}}",
               "Format": "{{string}}",
               "OutputType": "{{string}}",
               "Overwrite": "{{string}}"
            },
            "S3Prefix": "{{string}}",
            "S3Region": "{{string}}"
         }
      },
      "ExportArn": "{{string}}",
      "Name": "{{string}}",
      "RefreshCadence": {
         "Frequency": "{{string}}"
      }
   },
   "ResourceTags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_DataExports_CreateExport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Export](#API_DataExports_CreateExport_RequestSyntax) **   <a name="awscostmanagement-DataExports_CreateExport-request-Export"></a>
The details of the export, including data query, name, description, and destination configuration.
Type: [Export](API_DataExports_Export.md) object
Required: Yes

 ** [ResourceTags](#API_DataExports_CreateExport_RequestSyntax) **   <a name="awscostmanagement-DataExports_CreateExport-request-ResourceTags"></a>
An optional list of tags to associate with the specified export. Each tag consists of a key and a value, and each key must be unique for the resource.
Type: Array of [ResourceTag](API_DataExports_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_DataExports_CreateExport_ResponseSyntax"></a>

```
{
   "ExportArn": "string"
}
```

## Response Elements
<a name="API_DataExports_CreateExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExportArn](#API_DataExports_CreateExport_ResponseSyntax) **   <a name="awscostmanagement-DataExports_CreateExport-response-ExportArn"></a>
The Amazon Resource Name (ARN) for this export.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:(bcm-data-exports):[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`

## Errors
<a name="API_DataExports_CreateExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An error on the server occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You've reached the limit on the number of resources you can create, or exceeded the size of an individual resource.
 ** QuotaCode **
The quota code that was exceeded.
 ** ResourceId **
The identifier of the resource that exceeded quota.
 ** ResourceType **
The type of the resource that exceeded quota.
 ** ServiceCode **
The service code that exceeded quota. It will always be “AWSBillingAndCostManagementDataExports”.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** QuotaCode **
The quota code that exceeded the throttling limit.
 ** ServiceCode **
The service code that exceeded the throttling limit. It will always be “AWSBillingAndCostManagementDataExports”.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Fields **
The list of fields that are invalid.
 ** Reason **
The reason for the validation exception.
HTTP Status Code: 400

## Examples
<a name="API_DataExports_CreateExport_Examples"></a>

### The following is a sample request of the CreateExport operation.
<a name="API_DataExports_CreateExport_Example_1"></a>

This example illustrates one usage of CreateExport.

#### Sample Request
<a name="API_DataExports_CreateExport_Example_1_Request"></a>

```
{
    "Export": {
        "Name": "ExampleExportName",
        "Description": "Example Description",
        "DataQuery": {
            "QueryStatement": "SELECT identity_line_item_id, identity_time_interval, line_item_product_code,line_item_unblended_cost FROM COST_AND_USAGE_REPORT",
            "TableConfigurations": {
                "COST_AND_USAGE_REPORT": {
                    "TIME_GRANULARITY": "DAILY",
                    "INCLUDE_RESOURCES": "FALSE",
                    "INCLUDE_MANUAL_DISCOUNT_COMPATIBILITY": "FALSE",
                    "INCLUDE_SPLIT_COST_ALLOCATION_DATA": "FALSE"
                }
            }
        },
        "DestinationConfigurations": {
            "S3Destination": {
                "S3Bucket": "ExampleS3Bucket",
                "S3BucketOwner": "123456789012",
                "S3Prefix": "ExampleS3Prefix",
                "S3Region": "us-east-1",
                "S3OutputConfigurations": {
                    "Overwrite": "OVERWRITE_REPORT",
                    "Format": "TEXT_OR_CSV",
                    "Compression": "GZIP",
                    "OutputType": "CUSTOM"
                }
            }
        },
        "RefreshCadence": {
            "Frequency": "SYNCHRONOUS"
        }
    },
    "ResourceTags": [
        {
            "Key": "YourTagKey",
            "Value": "YourTagValue"
        }
    ]
}
```

### The following is a sample response of the CreateExport operation.
<a name="API_DataExports_CreateExport_Example_2"></a>

This example illustrates one usage of CreateExport.

#### Sample Response
<a name="API_DataExports_CreateExport_Example_2_Response"></a>

```
{
    "ExportArn": "arn:aws:bcm-data-exports:::export/Example-b9ac8e7c-6a49-468f-a43e-9ce6b5b051d1"
}
```

## See Also
<a name="API_DataExports_CreateExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-data-exports-2023-11-26/CreateExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-data-exports-2023-11-26/CreateExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/CreateExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-data-exports-2023-11-26/CreateExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/CreateExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-data-exports-2023-11-26/CreateExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-data-exports-2023-11-26/CreateExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-data-exports-2023-11-26/CreateExport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bcm-data-exports-2023-11-26/CreateExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/CreateExport)
