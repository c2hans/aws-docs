---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CategoryFilterConfiguration.html
---

# CategoryFilterConfiguration
<a name="API_CategoryFilterConfiguration"></a>

The configuration for a `CategoryFilter`.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_CategoryFilterConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomFilterConfiguration **   <a name="QS-Type-CategoryFilterConfiguration-CustomFilterConfiguration"></a>
A custom filter that filters based on a single value. This filter can be partially matched.
Type: [CustomFilterConfiguration](API_CustomFilterConfiguration.md) object
Required: No

 ** CustomFilterListConfiguration **   <a name="QS-Type-CategoryFilterConfiguration-CustomFilterListConfiguration"></a>
A list of custom filter values. In the Quick Sight console, this filter type is called a custom filter list.
Type: [CustomFilterListConfiguration](API_CustomFilterListConfiguration.md) object
Required: No

 ** FilterListConfiguration **   <a name="QS-Type-CategoryFilterConfiguration-FilterListConfiguration"></a>
A list of filter configurations. In the Quick Sight console, this filter type is called a filter list.
Type: [FilterListConfiguration](API_FilterListConfiguration.md) object
Required: No

## See Also
<a name="API_CategoryFilterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CategoryFilterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CategoryFilterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CategoryFilterConfiguration)
