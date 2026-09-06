---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledControlResourceDrift.html
---

# EnabledControlResourceDrift
<a name="API_EnabledControlResourceDrift"></a>

Represents drift information related to the underlying AWS resources managed by the control.

## Contents
<a name="API_EnabledControlResourceDrift_Contents"></a>

 ** status **   <a name="controltower-Type-EnabledControlResourceDrift-status"></a>
The status of resource drift for the enabled control, indicating whether the underlying resources match the expected configuration.
Type: String
Valid Values: `DRIFTED | IN_SYNC | NOT_CHECKING | UNKNOWN`
Required: No

## See Also
<a name="API_EnabledControlResourceDrift_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/EnabledControlResourceDrift)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/EnabledControlResourceDrift)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/EnabledControlResourceDrift)
