---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_MultiLocationConfig.html
---

# MultiLocationConfig
<a name="API_MultiLocationConfig"></a>

A structure that contains information about the multi-location configuration of a canary, including whether it is a primary or replica, the primary location, and the list of replicas.

## Contents
<a name="API_MultiLocationConfig_Contents"></a>

 ** LocationType **   <a name="synthetics-Type-MultiLocationConfig-LocationType"></a>
Indicates whether this canary is the `Primary` or a `Replica` in the multi-location configuration.
Type: String
Valid Values: `Primary | Replica`
Required: No

 ** PrimaryLocation **   <a name="synthetics-Type-MultiLocationConfig-PrimaryLocation"></a>
The Amazon Web Services Region where the primary canary is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-{0,1}[0-9]{0,1}$`
Required: No

 ** Replicas **   <a name="synthetics-Type-MultiLocationConfig-Replicas"></a>
A list of replicas for this canary. This field is present only for the primary location canary.
Type: Array of [Replica](API_Replica.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** ReplicationState **   <a name="synthetics-Type-MultiLocationConfig-ReplicationState"></a>
The overall replication state of the canary across all replica locations. This field is present only for the primary location canary. Valid values are `InProgress`, `InSync`, and `Inconsistent`.
Type: String
Valid Values: `InProgress | InSync | Inconsistent`
Required: No

## See Also
<a name="API_MultiLocationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/MultiLocationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/MultiLocationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/MultiLocationConfig)
