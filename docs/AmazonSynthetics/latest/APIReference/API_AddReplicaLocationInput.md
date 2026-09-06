---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_AddReplicaLocationInput.html
---

# AddReplicaLocationInput
<a name="API_AddReplicaLocationInput"></a>

A structure that specifies a replica location for a canary, including the Region and optional VPC configuration.

## Contents
<a name="API_AddReplicaLocationInput_Contents"></a>

 ** Location **   <a name="synthetics-Type-AddReplicaLocationInput-Location"></a>
The Amazon Web Services Region where the canary replica should be created, for example `us-east-1`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-{0,1}[0-9]{0,1}$`
Required: Yes

 ** VpcConfig **   <a name="synthetics-Type-AddReplicaLocationInput-VpcConfig"></a>
The VPC configuration to use for the canary replica in this location. If not specified, the replica runs without VPC connectivity.
Type: [VpcConfigInput](API_VpcConfigInput.md) object
Required: No

## See Also
<a name="API_AddReplicaLocationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/AddReplicaLocationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/AddReplicaLocationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/AddReplicaLocationInput)
