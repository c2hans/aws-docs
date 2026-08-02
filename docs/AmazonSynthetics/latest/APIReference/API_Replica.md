---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_Replica.html
---

# Replica
<a name="API_Replica"></a>

A structure that contains information about a canary replica in a specific location.

## Contents
<a name="API_Replica_Contents"></a>

 ** CanaryState **   <a name="synthetics-Type-Replica-CanaryState"></a>
The current state of the canary in this replica location.
Type: String
Valid Values: `CREATING | READY | STARTING | RUNNING | UPDATING | STOPPING | STOPPED | ERROR | DELETING`
Required: No

 ** LastModified **   <a name="synthetics-Type-Replica-LastModified"></a>
The date and time that the replica was last modified.
Type: Timestamp
Required: No

 ** Location **   <a name="synthetics-Type-Replica-Location"></a>
The Amazon Web Services Region where this replica is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-{0,1}[0-9]{0,1}$`
Required: No

 ** ReplicationStatus **   <a name="synthetics-Type-Replica-ReplicationStatus"></a>
A structure that contains information about the replication status of this replica.
Type: [ReplicationStatus](API_ReplicationStatus.md) object
Required: No

 ** VpcConfig **   <a name="synthetics-Type-Replica-VpcConfig"></a>
The VPC configuration for the canary replica in this location.
Type: [VpcConfigOutput](API_VpcConfigOutput.md) object
Required: No

## See Also
<a name="API_Replica_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/Replica)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/Replica)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/Replica)
