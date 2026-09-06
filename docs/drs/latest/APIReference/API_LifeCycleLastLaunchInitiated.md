---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_LifeCycleLastLaunchInitiated.html
---

# LifeCycleLastLaunchInitiated
<a name="API_LifeCycleLastLaunchInitiated"></a>

An object containing information regarding the initiation of the last launch of a Source Server.

## Contents
<a name="API_LifeCycleLastLaunchInitiated_Contents"></a>

 ** apiCallDateTime **   <a name="drs-Type-LifeCycleLastLaunchInitiated-apiCallDateTime"></a>
The date and time the last Source Server launch was initiated.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** jobID **   <a name="drs-Type-LifeCycleLastLaunchInitiated-jobID"></a>
The ID of the Job that was used to last launch the Source Server.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `drsjob-[0-9a-zA-Z]{17}`
Required: No

 ** type **   <a name="drs-Type-LifeCycleLastLaunchInitiated-type"></a>
The Job type that was used to last launch the Source Server.
Type: String
Valid Values: `RECOVERY | DRILL`
Required: No

## See Also
<a name="API_LifeCycleLastLaunchInitiated_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/LifeCycleLastLaunchInitiated)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/LifeCycleLastLaunchInitiated)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/LifeCycleLastLaunchInitiated)
