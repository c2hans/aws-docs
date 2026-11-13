---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_AutoPidMapConfiguration.html
---

# AutoPidMapConfiguration
<a name="API_AutoPidMapConfiguration"></a>

The configuration settings for automatic Packet ID (PID) assignment. These settings apply to any PID mapping rule that uses the `mapAuto` action, including the default action. For more information, see [Rule actions](https://docs.aws.amazon.com/mediaconnect/latest/ug/pid-remapping-writing-rules.html#pid-remapping-actions) in the * AWS Elemental MediaConnect User Guide*.

## Contents
<a name="API_AutoPidMapConfiguration_Contents"></a>

 ** pidsPerProgram **   <a name="mediaconnect-Type-AutoPidMapConfiguration-pidsPerProgram"></a>
The number of PIDs in the range for automatic PID assignment.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 8158.
Required: Yes

 ** startPid **   <a name="mediaconnect-Type-AutoPidMapConfiguration-startPid"></a>
The first PID in the range for automatic PID assignment.
Type: Integer
Valid Range: Minimum value of 32. Maximum value of 8190.
Required: Yes

## See Also
<a name="API_AutoPidMapConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/AutoPidMapConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/AutoPidMapConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/AutoPidMapConfiguration)
