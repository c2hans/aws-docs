---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteCapacityManagerDataExport.html
---

# DeleteCapacityManagerDataExport
<a name="API_DeleteCapacityManagerDataExport"></a>

 Deletes an existing Capacity Manager data export configuration. This stops future scheduled exports but does not delete previously exported files from S3.

## Request Parameters
<a name="API_DeleteCapacityManagerDataExport_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CapacityManagerDataExportId**
 The unique identifier of the data export configuration to delete.
Type: String
Required: Yes

 **DryRun**
 Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DeleteCapacityManagerDataExport_ResponseElements"></a>

The following elements are returned by the service.

 **capacityManagerDataExportId**
 The unique identifier of the deleted data export configuration.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DeleteCapacityManagerDataExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteCapacityManagerDataExport_Examples"></a>

### Example
<a name="API_DeleteCapacityManagerDataExport_Example_1"></a>

This example deletes a data export configuration.

#### Sample Request
<a name="API_DeleteCapacityManagerDataExport_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteCapacityManagerDataExport
&CapacityManagerDataExportId=cmde-0abcd1234EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteCapacityManagerDataExport_Example_1_Response"></a>

```
<DeleteCapacityManagerDataExportResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <capacityManagerDataExportId>cmde-0abcd1234EXAMPLE</capacityManagerDataExportId>
</DeleteCapacityManagerDataExportResponse>
```

## See Also
<a name="API_DeleteCapacityManagerDataExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteCapacityManagerDataExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteCapacityManagerDataExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteCapacityManagerDataExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteCapacityManagerDataExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteCapacityManagerDataExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteCapacityManagerDataExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteCapacityManagerDataExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteCapacityManagerDataExport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteCapacityManagerDataExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteCapacityManagerDataExport)
