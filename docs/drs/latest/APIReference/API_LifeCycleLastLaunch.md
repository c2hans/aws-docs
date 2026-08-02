---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_LifeCycleLastLaunch.html
---

# LifeCycleLastLaunch
<a name="API_LifeCycleLastLaunch"></a>

An object containing information regarding the last launch of a Source Server.

## Contents
<a name="API_LifeCycleLastLaunch_Contents"></a>

 ** initiated **   <a name="drs-Type-LifeCycleLastLaunch-initiated"></a>
An object containing information regarding the initiation of the last launch of a Source Server.
Type: [LifeCycleLastLaunchInitiated](API_LifeCycleLastLaunchInitiated.md) object
Required: No

 ** status **   <a name="drs-Type-LifeCycleLastLaunch-status"></a>
Status of Source Server's last launch.
Type: String
Valid Values: `PENDING | IN_PROGRESS | LAUNCHED | FAILED | TERMINATED`
Required: No

## See Also
<a name="API_LifeCycleLastLaunch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/LifeCycleLastLaunch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/LifeCycleLastLaunch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/LifeCycleLastLaunch)
