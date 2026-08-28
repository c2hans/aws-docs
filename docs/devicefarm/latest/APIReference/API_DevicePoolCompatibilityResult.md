---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DevicePoolCompatibilityResult.html
---

# DevicePoolCompatibilityResult
<a name="API_DevicePoolCompatibilityResult"></a>

Represents a device pool compatibility result.

## Contents
<a name="API_DevicePoolCompatibilityResult_Contents"></a>

 ** compatible **   <a name="devicefarm-Type-DevicePoolCompatibilityResult-compatible"></a>
Whether the result was compatible with the device pool.
Type: Boolean
Required: No

 ** device **   <a name="devicefarm-Type-DevicePoolCompatibilityResult-device"></a>
The device (phone or tablet) to return information about.
Type: [Device](API_Device.md) object
Required: No

 ** incompatibilityMessages **   <a name="devicefarm-Type-DevicePoolCompatibilityResult-incompatibilityMessages"></a>
Information about the compatibility.
Type: Array of [IncompatibilityMessage](API_IncompatibilityMessage.md) objects
Required: No

## See Also
<a name="API_DevicePoolCompatibilityResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/DevicePoolCompatibilityResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/DevicePoolCompatibilityResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/DevicePoolCompatibilityResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
