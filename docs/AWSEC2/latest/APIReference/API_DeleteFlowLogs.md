---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFlowLogs.html
---

# DeleteFlowLogs
<a name="API_DeleteFlowLogs"></a>

Deletes one or more flow logs.

## Request Parameters
<a name="API_DeleteFlowLogs_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FlowLogId.N**
One or more flow log IDs.
Constraint: Maximum of 1000 flow log IDs.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_DeleteFlowLogs_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **unsuccessful**
Information about the flow logs that could not be deleted successfully.
Type: Array of [UnsuccessfulItem](API_UnsuccessfulItem.md) objects

## Errors
<a name="API_DeleteFlowLogs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteFlowLogs_Examples"></a>

### Example
<a name="API_DeleteFlowLogs_Example_1"></a>

This example deletes flow log fl-1a2b3c4d.

#### Sample Request
<a name="API_DeleteFlowLogs_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteFlowLogs
&FlowLogId.1=fl-1a2b3c4d
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteFlowLogs_Example_1_Response"></a>

```
<DeleteFlowLogsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>c5c4f51f-f4e9-42bc-8700-EXAMPLE</requestId>
    <unsuccessful/>
</DeleteFlowLogsResponse>
```

## See Also
<a name="API_DeleteFlowLogs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteFlowLogs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteFlowLogs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteFlowLogs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteFlowLogs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteFlowLogs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteFlowLogs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteFlowLogs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteFlowLogs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteFlowLogs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteFlowLogs)
