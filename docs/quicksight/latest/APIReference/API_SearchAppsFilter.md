---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchAppsFilter.html
---

# SearchAppsFilter
<a name="API_SearchAppsFilter"></a>

A filter to apply when searching for apps.

## Contents
<a name="API_SearchAppsFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="QS-Type-SearchAppsFilter-Name"></a>
The name of the filter attribute.
Type: String
Valid Values: `APP_ID | APP_NAME | DIRECT_QUICKSIGHT_SOLE_OWNER | DIRECT_QUICKSIGHT_OWNER | DIRECT_QUICKSIGHT_VIEWER_OR_OWNER`
Required: Yes

 ** Operator **   <a name="QS-Type-SearchAppsFilter-Operator"></a>
The comparison operator for the filter.
Type: String
Valid Values: `StringEquals | StringLike`
Required: Yes

 ** Value **   <a name="QS-Type-SearchAppsFilter-Value"></a>
The value to filter on.
Type: String
Required: Yes

## See Also
<a name="API_SearchAppsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchAppsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchAppsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchAppsFilter)
