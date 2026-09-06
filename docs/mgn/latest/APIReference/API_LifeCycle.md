---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_LifeCycle.html
---

# LifeCycle
<a name="API_LifeCycle"></a>

Lifecycle.

## Contents
<a name="API_LifeCycle_Contents"></a>

 ** addedToServiceDateTime **   <a name="mgn-Type-LifeCycle-addedToServiceDateTime"></a>
Lifecycle added to service date and time.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** elapsedReplicationDuration **   <a name="mgn-Type-LifeCycle-elapsedReplicationDuration"></a>
Lifecycle elapsed time and duration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** firstByteDateTime **   <a name="mgn-Type-LifeCycle-firstByteDateTime"></a>
Lifecycle replication initiation date and time.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** lastCutover **   <a name="mgn-Type-LifeCycle-lastCutover"></a>
Lifecycle last Cutover.
Type: [LifeCycleLastCutover](API_LifeCycleLastCutover.md) object
Required: No

 ** lastSeenByServiceDateTime **   <a name="mgn-Type-LifeCycle-lastSeenByServiceDateTime"></a>
Lifecycle last seen date and time.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** lastTest **   <a name="mgn-Type-LifeCycle-lastTest"></a>
Lifecycle last Test.
Type: [LifeCycleLastTest](API_LifeCycleLastTest.md) object
Required: No

 ** state **   <a name="mgn-Type-LifeCycle-state"></a>
Lifecycle state.
Type: String
Valid Values: `STOPPED | NOT_READY | READY_FOR_TEST | TESTING | READY_FOR_CUTOVER | CUTTING_OVER | CUTOVER | DISCONNECTED | DISCOVERED | PENDING_INSTALLATION`
Required: No

## See Also
<a name="API_LifeCycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/LifeCycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/LifeCycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/LifeCycle)
