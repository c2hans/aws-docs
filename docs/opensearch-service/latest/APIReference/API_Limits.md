---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_Limits.html
---

# Limits
<a name="API_Limits"></a>

Limits for a given instance type and for each of its roles.

## Contents
<a name="API_Limits_Contents"></a>

 ** AdditionalLimits **   <a name="opensearchservice-Type-Limits-AdditionalLimits"></a>
List of additional limits that are specific to a given instance type for each of its instance roles.
Type: Array of [AdditionalLimit](API_AdditionalLimit.md) objects
Required: No

 ** InstanceLimits **   <a name="opensearchservice-Type-Limits-InstanceLimits"></a>
The limits for a given instance type.
Type: [InstanceLimits](API_InstanceLimits.md) object
Required: No

 ** StorageTypes **   <a name="opensearchservice-Type-Limits-StorageTypes"></a>
Storage-related attributes that are available for a given instance type.
Type: Array of [StorageType](API_StorageType.md) objects
Required: No

## See Also
<a name="API_Limits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/Limits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/Limits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/Limits)
