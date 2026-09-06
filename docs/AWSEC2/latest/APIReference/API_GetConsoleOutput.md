---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetConsoleOutput.html
---

# GetConsoleOutput
<a name="API_GetConsoleOutput"></a>

Gets the console output for the specified instance. For Linux instances, the instance console output displays the exact console output that would normally be displayed on a physical monitor attached to a computer. For Windows instances, the instance console output includes the last three system event log errors.

For more information, see [Instance console output](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-console.html#instance-console-console-output) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_GetConsoleOutput_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the instance.
Type: String
Required: Yes

 **Latest**
When enabled, retrieves the latest console output for the instance.
Default: disabled (`false`)
Type: Boolean
Required: No

## Response Elements
<a name="API_GetConsoleOutput_ResponseElements"></a>

The following elements are returned by the service.

 **instanceId**
The ID of the instance.
Type: String

 **output**
The console output, base64-encoded. If you are using a command line tool, the tool decodes the output for you.
Type: String

 **requestId**
The ID of the request.
Type: String

 **timestamp**
The time at which the output was last updated.
Type: Timestamp

## Errors
<a name="API_GetConsoleOutput_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetConsoleOutput_Examples"></a>

### Example 1
<a name="API_GetConsoleOutput_Example_1"></a>

This example retrieves the console output for the specified instance.

#### Sample Request
<a name="API_GetConsoleOutput_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetConsoleOutput
&InstanceId=i-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetConsoleOutput_Example_1_Response"></a>

```
<GetConsoleOutputResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <instanceId>i-1234567890abcdef0</instanceId>
  <timestamp>2022-10-14T01:12:41.000Z</timestamp>
  <output>TGludXggdmVyc2lvbiAyLjYuMTYteGVuVSAoYnVpbGRlckBwYXRjaGJhdC5hbWF6b25zYSkgKGdj
YyB2ZXJzaW9uIDQuMC4xIDIwMDUwNzI3IChSZWQgSGF0IDQuMC4xLTUpKSAjMSBTTVAgVGh1IE9j
dCAyNiAwODo0MToyNiBTQVNUIDIwMDYKQklPUy1wcm92aWRlZCBwaHlzaWNhbCBSQU0gbWFwOgpY
ZW46IDAwMDAwMDAwMDAwMDAwMDAgLSAwMDAwMDAwMDZhNDAwMDAwICh1c2FibGUpCjk4ME1CIEhJ
R0hNRU0gYXZhaWxhYmxlLgo3MjdNQiBMT1dNRU0gYXZhaWxhYmxlLgpOWCAoRXhlY3V0ZSBEaXNh
YmxlKSBwcm90ZWN0aW9uOiBhY3RpdmUKSVJRIGxvY2t1cCBkZXRlY3Rpb24gZGlzYWJsZWQKQnVp
bHQgMSB6b25lbGlzdHMKS2VybmVsIGNvbW1hbmQgbGluZTogcm9vdD0vZGV2L3NkYTEgcm8gNApF
bmFibGluZyBmYXN0IEZQVSBzYXZlIGFuZCByZXN0b3JlLi4uIGRvbmUuCg==</output>
</GetConsoleOutputResponse>
```

### Example 2
<a name="API_GetConsoleOutput_Example_2"></a>

This example retrieves the latest console output for the specified instance.

#### Sample Request
<a name="API_GetConsoleOutput_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetConsoleOutput
&InstanceId=i-1234567890abcdef0
&Latest=true
&AUTHPARAMS
```

## See Also
<a name="API_GetConsoleOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetConsoleOutput)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetConsoleOutput)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetConsoleOutput)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetConsoleOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetConsoleOutput)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetConsoleOutput)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetConsoleOutput)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetConsoleOutput)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetConsoleOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetConsoleOutput)
