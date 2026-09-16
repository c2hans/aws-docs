---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_UpdateExport.html
---

# UpdateExport
<a name="API_DataExports_UpdateExport"></a>

Updates an existing data export by overwriting all export parameters. All export parameters must be provided in the UpdateExport request.

## Request Syntax
<a name="API_DataExports_UpdateExport_RequestSyntax"></a>

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
   "ExportArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DataExports_UpdateExport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Export](#API_DataExports_UpdateExport_RequestSyntax) **   <a name="awscostmanagement-DataExports_UpdateExport-request-Export"></a>
The name and query details for the export.
Type: [Export](API_DataExports_Export.md) object
Required: Yes

 ** [ExportArn](#API_DataExports_UpdateExport_RequestSyntax) **   <a name="awscostmanagement-DataExports_UpdateExport-request-ExportArn"></a>
The Amazon Resource Name (ARN) for this export.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:(bcm-data-exports):[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: Yes

## Response Syntax
<a name="API_DataExports_UpdateExport_ResponseSyntax"></a>

```
{
   "ExportArn": "string"
}
```

## Response Elements
<a name="API_DataExports_UpdateExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExportArn](#API_DataExports_UpdateExport_ResponseSyntax) **   <a name="awscostmanagement-DataExports_UpdateExport-response-ExportArn"></a>
The Amazon Resource Name (ARN) for this export.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:(bcm-data-exports):[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`

## Errors
<a name="API_DataExports_UpdateExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An error on the server occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified Amazon Resource Name (ARN) in the request doesn't exist.
 ** ResourceId **
The identifier of the resource that was not found.
 ** ResourceType **
The type of the resource that was not found.
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
<a name="API_DataExports_UpdateExport_Examples"></a>

### The following is a sample request of the UpdateExport operation.
<a name="API_DataExports_UpdateExport_Example_1"></a>

This example illustrates one usage of UpdateExport.

#### Sample Request
<a name="API_DataExports_UpdateExport_Example_1_Request"></a>

```
{
    "ExportArn": "arn:aws:bcm-data-exports:::export:Example/837fcfce-f85b-4600-b333-b38a12c3a927",
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
    }
}
```

### The following is a sample response of the UpdateExport operation.
<a name="API_DataExports_UpdateExport_Example_2"></a>

This example illustrates one usage of UpdateExport.

#### Sample Response
<a name="API_DataExports_UpdateExport_Example_2_Response"></a>

```
{
    "ExportArn": "arn:aws:bcm-data-exports:::export:Example/837fcfce-f85b-4600-b333-b38a12c3a927"
}
```

## See Also
<a name="API_DataExports_UpdateExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-data-exports-2023-11-26/UpdateExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-data-exports-2023-11-26/UpdateExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/UpdateExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-data-exports-2023-11-26/UpdateExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/UpdateExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-data-exports-2023-11-26/UpdateExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-data-exports-2023-11-26/UpdateExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-data-exports-2023-11-26/UpdateExport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bcm-data-exports-2023-11-26/UpdateExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/UpdateExport)
