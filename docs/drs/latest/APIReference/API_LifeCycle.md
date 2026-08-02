---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_LifeCycle.html
---

# LifeCycle
<a name="API_LifeCycle"></a>

An object representing the Source Server Lifecycle.

## Contents
<a name="API_LifeCycle_Contents"></a>

 ** addedToServiceDateTime **   <a name="drs-Type-LifeCycle-addedToServiceDateTime"></a>
The date and time of when the Source Server was added to the service.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** elapsedReplicationDuration **   <a name="drs-Type-LifeCycle-elapsedReplicationDuration"></a>
The amount of time that the Source Server has been replicating for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** firstByteDateTime **   <a name="drs-Type-LifeCycle-firstByteDateTime"></a>
The date and time of the first byte that was replicated from the Source Server.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** lastLaunch **   <a name="drs-Type-LifeCycle-lastLaunch"></a>
An object containing information regarding the last launch of the Source Server.
Type: [LifeCycleLastLaunch](API_LifeCycleLastLaunch.md) object
Required: No

 ** lastSeenByServiceDateTime **   <a name="drs-Type-LifeCycle-lastSeenByServiceDateTime"></a>
The date and time this Source Server was last seen by the service.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

## See Also
<a name="API_LifeCycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/LifeCycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/LifeCycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/LifeCycle)
