---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResourceTag.html
---

# ResourceTag
<a name="API_ResourceTag"></a>

The tag structure that contains a tag key and value.

**Note**
Tagging is supported only for the following Cost Explorer resource types: [`AnomalyMonitor`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyMonitor.html), [`AnomalySubscription`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html), [`CostCategory`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategory.html).

## Contents
<a name="API_ResourceTag_Contents"></a>

 ** Key **   <a name="awscostmanagement-Type-ResourceTag-Key"></a>
The key that's associated with the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** Value **   <a name="awscostmanagement-Type-ResourceTag-Value"></a>
The value that's associated with the tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## See Also
<a name="API_ResourceTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ResourceTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ResourceTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ResourceTag)
