---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_GetExecution.html
---

# GetExecution
<a name="API_DataExports_GetExecution"></a>

Exports data based on the source data update.

## Request Syntax
<a name="API_DataExports_GetExecution_RequestSyntax"></a>

```
{
   "ExecutionId": "{{string}}",
   "ExportArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DataExports_GetExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExecutionId](#API_DataExports_GetExecution_RequestSyntax) **   <a name="awscostmanagement-DataExports_GetExecution-request-ExecutionId"></a>
The ID for this specific execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** [ExportArn](#API_DataExports_GetExecution_RequestSyntax) **   <a name="awscostmanagement-DataExports_GetExecution-request-ExportArn"></a>
The Amazon Resource Name (ARN) of the Export object that generated this specific execution.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:(bcm-data-exports):[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: Yes

## Response Syntax
<a name="API_DataExports_GetExecution_ResponseSyntax"></a>

```
{
   "ExecutionId": "string",
   "ExecutionStatus": {
      "CompletedAt": "string",
      "CreatedAt": "string",
      "LastUpdatedAt": "string",
      "StatusCode": "string",
      "StatusReason": "string"
   },
   "Export": {
      "DataQuery": {
         "QueryStatement": "string",
         "TableConfigurations": {
            "string" : {
               "string" : "string"
            }
         }
      },
      "Description": "string",
      "DestinationConfigurations": {
         "S3Destination": {
            "S3Bucket": "string",
            "S3BucketOwner": "string",
            "S3OutputConfigurations": {
               "Compression": "string",
               "Format": "string",
               "OutputType": "string",
               "Overwrite": "string"
            },
            "S3Prefix": "string",
            "S3Region": "string"
         }
      },
      "ExportArn": "string",
      "Name": "string",
      "RefreshCadence": {
         "Frequency": "string"
      }
   }
}
```

## Response Elements
<a name="API_DataExports_GetExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExecutionId](#API_DataExports_GetExecution_ResponseSyntax) **   <a name="awscostmanagement-DataExports_GetExecution-response-ExecutionId"></a>
The ID for this specific execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`

 ** [ExecutionStatus](#API_DataExports_GetExecution_ResponseSyntax) **   <a name="awscostmanagement-DataExports_GetExecution-response-ExecutionStatus"></a>
The status of this specific execution.
Type: [ExecutionStatus](API_DataExports_ExecutionStatus.md) object

 ** [Export](#API_DataExports_GetExecution_ResponseSyntax) **   <a name="awscostmanagement-DataExports_GetExecution-response-Export"></a>
The export data for this specific execution. This export data is a snapshot from when the execution was generated. The data could be different from the current export data if the export was updated since the execution was generated.
Type: [Export](API_DataExports_Export.md) object

## Errors
<a name="API_DataExports_GetExecution_Errors"></a>

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
<a name="API_DataExports_GetExecution_Examples"></a>

### The following is a sample request of the GetExecution operation.
<a name="API_DataExports_GetExecution_Example_1"></a>

This example illustrates one usage of GetExecution.

#### Sample Request
<a name="API_DataExports_GetExecution_Example_1_Request"></a>

```
{
 "ExportArn": "arn:aws:bcm-data-exports:::export:Example/837fcfce-f85b-4600-b333-b38a12c3a927",
 "ExecutionId": "8ae3fbeb-fbeb-4048-bb39-f7c6c7e80c21"
}
```

### The following is a sample response of the GetExecution operation.
<a name="API_DataExports_GetExecution_Example_2"></a>

This example illustrates one usage of GetExecution.

#### Sample Response
<a name="API_DataExports_GetExecution_Example_2_Response"></a>

```
{
    "ExecutionId": "f0cfeaf0-c552-47e7-82bc-0107fbfc7a8b",
    "ExecutionStatus": {
        "CreatedAt": "2023-11-14T18:14:12.813Z",
        "LastUpdatedAt": "2023-11-14T18:18:14.252556820Z",
        "StatusCode": "DELIVERY_SUCCESS"
    },
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

## See Also
<a name="API_DataExports_GetExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-data-exports-2023-11-26/GetExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-data-exports-2023-11-26/GetExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/GetExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-data-exports-2023-11-26/GetExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/GetExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-data-exports-2023-11-26/GetExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-data-exports-2023-11-26/GetExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-data-exports-2023-11-26/GetExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-data-exports-2023-11-26/GetExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/GetExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
