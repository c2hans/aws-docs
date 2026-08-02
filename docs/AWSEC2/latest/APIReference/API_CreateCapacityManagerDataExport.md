---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCapacityManagerDataExport.html
---

# CreateCapacityManagerDataExport
<a name="API_CreateCapacityManagerDataExport"></a>

 Creates a new data export configuration for EC2 Capacity Manager. This allows you to automatically export capacity usage data to an S3 bucket on a scheduled basis. The exported data includes metrics for On-Demand, Spot, and Capacity Reservations usage across your organization.

## Request Parameters
<a name="API_CreateCapacityManagerDataExport_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
 Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see Ensure Idempotency.
Type: String
Required: No

 **DryRun**
 Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **OutputFormat**
 The file format for the exported data. Parquet format is recommended for large datasets and better compression.
Type: String
Valid Values: `csv | parquet`
Required: Yes

 **S3BucketName**
 The name of the S3 bucket where the capacity data export files will be delivered. The bucket must exist and you must have write permissions to it.
Type: String
Required: Yes

 **S3BucketPrefix**
 The S3 key prefix for the exported data files. This allows you to organize exports in a specific folder structure within your bucket. If not specified, files are placed at the bucket root.
Type: String
Required: No

 **Schedule**
 The frequency at which data exports are generated.
Type: String
Valid Values: `hourly`
Required: Yes

 **TagSpecification.N**
 The tags to apply to the data export configuration. You can tag the export for organization and cost tracking purposes.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateCapacityManagerDataExport_ResponseElements"></a>

The following elements are returned by the service.

 **capacityManagerDataExportId**
 The unique identifier for the created data export configuration. Use this ID to reference the export in other API calls.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateCapacityManagerDataExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateCapacityManagerDataExport_Examples"></a>

### Example
<a name="API_CreateCapacityManagerDataExport_Example_1"></a>

This example creates a data export configuration that delivers hourly Parquet files to an S3 bucket.

#### Sample Request
<a name="API_CreateCapacityManagerDataExport_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateCapacityManagerDataExport
&S3BucketName=my-capacity-exports-bucket
&S3BucketPrefix=capacity-data/
&Schedule=hourly
&OutputFormat=parquet
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateCapacityManagerDataExport_Example_1_Response"></a>

```
<CreateCapacityManagerDataExportResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <capacityManagerDataExportId>cmde-0abcd1234EXAMPLE</capacityManagerDataExportId>
</CreateCapacityManagerDataExportResponse>
```

## See Also
<a name="API_CreateCapacityManagerDataExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateCapacityManagerDataExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateCapacityManagerDataExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateCapacityManagerDataExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateCapacityManagerDataExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateCapacityManagerDataExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateCapacityManagerDataExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateCapacityManagerDataExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateCapacityManagerDataExport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateCapacityManagerDataExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateCapacityManagerDataExport)
