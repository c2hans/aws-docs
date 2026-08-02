---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsItemRelatedItemsFilter.html
---

# OpsItemRelatedItemsFilter
<a name="API_OpsItemRelatedItemsFilter"></a>

Describes a filter for a specific list of related-item resources.

## Contents
<a name="API_OpsItemRelatedItemsFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-OpsItemRelatedItemsFilter-Key"></a>
The name of the filter key. Supported values include `ResourceUri`, `ResourceType`, or `AssociationId`.
Type: String
Valid Values: `ResourceType | AssociationId | ResourceUri`
Required: Yes

 ** Operator **   <a name="systemsmanager-Type-OpsItemRelatedItemsFilter-Operator"></a>
The operator used by the filter call. The only supported operator is `EQUAL`.
Type: String
Valid Values: `Equal`
Required: Yes

 ** Values **   <a name="systemsmanager-Type-OpsItemRelatedItemsFilter-Values"></a>
The values for the filter.
Type: Array of strings
Required: Yes

## See Also
<a name="API_OpsItemRelatedItemsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsItemRelatedItemsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsItemRelatedItemsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsItemRelatedItemsFilter)
