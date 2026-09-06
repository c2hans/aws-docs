---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicyDetailFilter.html
---

# LifecyclePolicyDetailFilter
<a name="API_LifecyclePolicyDetailFilter"></a>

Defines filters that the lifecycle policy uses to determine impacted resource.

## Contents
<a name="API_LifecyclePolicyDetailFilter_Contents"></a>

 ** type **   <a name="imagebuilder-Type-LifecyclePolicyDetailFilter-type"></a>
Filter resources based on either `age` or `count`.
Type: String
Valid Values: `AGE | COUNT`
Required: Yes

 ** value **   <a name="imagebuilder-Type-LifecyclePolicyDetailFilter-value"></a>
The number of units for the time period or for the count. For example, a value of `6` might refer to six months or six AMIs.
For count-based filters, this value represents the minimum number of resources to keep on hand. If you have fewer resources than this number, the resource is excluded from lifecycle actions.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** retainAtLeast **   <a name="imagebuilder-Type-LifecyclePolicyDetailFilter-retainAtLeast"></a>
For age-based filters, this is the number of resources to keep on hand after the lifecycle `DELETE` action is applied. Impacted resources are only deleted if you have more than this number of resources. If you have fewer resources than this number, the impacted resource is not deleted.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** unit **   <a name="imagebuilder-Type-LifecyclePolicyDetailFilter-unit"></a>
Defines the unit of time that the lifecycle policy uses to determine impacted resources. This is required for age-based rules.
Type: String
Valid Values: `DAYS | WEEKS | MONTHS | YEARS`
Required: No

## See Also
<a name="API_LifecyclePolicyDetailFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecyclePolicyDetailFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecyclePolicyDetailFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecyclePolicyDetailFilter)
