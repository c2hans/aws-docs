---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ReplicaSpecification.html
---

# ReplicaSpecification
<a name="API_ReplicaSpecification"></a>

The AWS Region specific settings of a multi-Region table.

For a multi-Region table, you can configure the table's read capacity differently per AWS Region. You can do this by configuring the following parameters.
+  `region`: The Region where these settings are applied. (Required)
+  `readCapacityUnits`: The provisioned read capacity units. (Optional)
+  `readCapacityAutoScaling`: The read capacity auto scaling settings for the table. (Optional)

## Contents
<a name="API_ReplicaSpecification_Contents"></a>

 ** region **   <a name="keyspaces-Type-ReplicaSpecification-region"></a>
The AWS Region.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.
Required: Yes

 ** readCapacityAutoScaling **   <a name="keyspaces-Type-ReplicaSpecification-readCapacityAutoScaling"></a>
The read capacity auto scaling settings for the multi-Region table in the specified AWS Region.
Type: [AutoScalingSettings](API_AutoScalingSettings.md) object
Required: No

 ** readCapacityUnits **   <a name="keyspaces-Type-ReplicaSpecification-readCapacityUnits"></a>
The provisioned read capacity units for the multi-Region table in the specified AWS Region.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ReplicaSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/ReplicaSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/ReplicaSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/ReplicaSpecification)
