---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceDataReplicationInitiation.html
---

# RecoveryInstanceDataReplicationInitiation
<a name="API_RecoveryInstanceDataReplicationInitiation"></a>

Data replication initiation.

## Contents
<a name="API_RecoveryInstanceDataReplicationInitiation_Contents"></a>

 ** startDateTime **   <a name="drs-Type-RecoveryInstanceDataReplicationInitiation-startDateTime"></a>
The date and time of the current attempt to initiate data replication.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** steps **   <a name="drs-Type-RecoveryInstanceDataReplicationInitiation-steps"></a>
The steps of the current attempt to initiate data replication.
Type: Array of [RecoveryInstanceDataReplicationInitiationStep](API_RecoveryInstanceDataReplicationInitiationStep.md) objects
Required: No

## See Also
<a name="API_RecoveryInstanceDataReplicationInitiation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryInstanceDataReplicationInitiation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryInstanceDataReplicationInitiation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryInstanceDataReplicationInitiation)
