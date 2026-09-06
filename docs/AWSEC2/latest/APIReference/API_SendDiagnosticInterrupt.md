---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SendDiagnosticInterrupt.html
---

# SendDiagnosticInterrupt
<a name="API_SendDiagnosticInterrupt"></a>

Sends a diagnostic interrupt to the specified Amazon EC2 instance to trigger a *kernel panic* (on Linux instances), or a *blue screen*/*stop error* (on Windows instances). For instances based on Intel and AMD processors, the interrupt is received as a *non-maskable interrupt* (NMI).

In general, the operating system crashes and reboots when a kernel panic or stop error is triggered. The operating system can also be configured to perform diagnostic tasks, such as generating a memory dump file, loading a secondary kernel, or obtaining a call trace.

Before sending a diagnostic interrupt to your instance, ensure that its operating system is configured to perform the required diagnostic tasks.

For more information about configuring your operating system to generate a crash dump when a kernel panic or stop error occurs, see [Send a diagnostic interrupt (for advanced users)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/diagnostic-interrupt.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_SendDiagnosticInterrupt_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the instance.
Type: String
Required: Yes

## Response Elements
<a name="API_SendDiagnosticInterrupt_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_SendDiagnosticInterrupt_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_SendDiagnosticInterrupt_Examples"></a>

### Example
<a name="API_SendDiagnosticInterrupt_Example_1"></a>

This example sends a diagnostic interrupt to the specified instance.

#### Sample Request
<a name="API_SendDiagnosticInterrupt_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=SendDiagnosticInterrupt
&InstanceId=i-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_SendDiagnosticInterrupt_Example_1_Response"></a>

```
<SendDiagnosticInterruptResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <return>true</return>
</SendDiagnosticInterruptResponse>
```

## See Also
<a name="API_SendDiagnosticInterrupt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/SendDiagnosticInterrupt)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/SendDiagnosticInterrupt)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SendDiagnosticInterrupt)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/SendDiagnosticInterrupt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SendDiagnosticInterrupt)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/SendDiagnosticInterrupt)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/SendDiagnosticInterrupt)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/SendDiagnosticInterrupt)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/SendDiagnosticInterrupt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SendDiagnosticInterrupt)
