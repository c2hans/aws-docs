---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CommandExecutionResult.html
---

# CommandExecutionResult
<a name="API_CommandExecutionResult"></a>

The result value of the command execution. The device can use the result field to share additional details about the execution such as a return value of a remote function call.

**Note**
This field is not applicable if you use the `AWS-IoT-FleetWise` namespace.

## Contents
<a name="API_CommandExecutionResult_Contents"></a>

 ** B **   <a name="iot-Type-CommandExecutionResult-B"></a>
An attribute of type Boolean. For example:
 `"BOOL": true`
Type: Boolean
Required: No

 ** BIN **   <a name="iot-Type-CommandExecutionResult-BIN"></a>
An attribute of type Binary.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1.
Required: No

 ** S **   <a name="iot-Type-CommandExecutionResult-S"></a>
An attribute of type String. For example:
 `"S": "Hello"`
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_CommandExecutionResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CommandExecutionResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CommandExecutionResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CommandExecutionResult)
