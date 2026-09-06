---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_MultiRegionConfiguration.html
---

# MultiRegionConfiguration
<a name="API_MultiRegionConfiguration"></a>

Describes the configuration of this multi-Region key. This field appears only when the KMS key is a primary or replica of a multi-Region key.

For more information about any listed KMS key, use the [DescribeKey](API_DescribeKey.md) operation.

## Contents
<a name="API_MultiRegionConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MultiRegionKeyType **   <a name="KMS-Type-MultiRegionConfiguration-MultiRegionKeyType"></a>
Indicates whether the KMS key is a `PRIMARY` or `REPLICA` key.
Type: String
Valid Values: `PRIMARY | REPLICA`
Required: No

 ** PrimaryKey **   <a name="KMS-Type-MultiRegionConfiguration-PrimaryKey"></a>
Displays the key ARN and Region of the primary key. This field includes the current KMS key if it is the primary key.
Type: [MultiRegionKey](API_MultiRegionKey.md) object
Required: No

 ** ReplicaKeys **   <a name="KMS-Type-MultiRegionConfiguration-ReplicaKeys"></a>
displays the key ARNs and Regions of all replica keys. This field includes the current KMS key if it is a replica key.
Type: Array of [MultiRegionKey](API_MultiRegionKey.md) objects
Required: No

## See Also
<a name="API_MultiRegionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/MultiRegionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/MultiRegionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/MultiRegionConfiguration)
