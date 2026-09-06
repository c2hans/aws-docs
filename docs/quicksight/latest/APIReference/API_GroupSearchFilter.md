---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GroupSearchFilter.html
---

# GroupSearchFilter
<a name="API_GroupSearchFilter"></a>

A `GroupSearchFilter` object that you want to apply to your search.

## Contents
<a name="API_GroupSearchFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="QS-Type-GroupSearchFilter-Name"></a>
The name of the value that you want to use as a filter, for example `"Name": "GROUP_NAME"`. Currently, the only supported name is `GROUP_NAME`.
Type: String
Valid Values: `GROUP_NAME`
Required: Yes

 ** Operator **   <a name="QS-Type-GroupSearchFilter-Operator"></a>
The comparison operator that you want to use as a filter, for example `"Operator": "StartsWith"`. Currently, the only supported operator is `StartsWith`.
Type: String
Valid Values: `StartsWith`
Required: Yes

 ** Value **   <a name="QS-Type-GroupSearchFilter-Value"></a>
The value of the named item, in this case `GROUP_NAME`, that you want to use as a filter.
Type: String
Required: Yes

## See Also
<a name="API_GroupSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GroupSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GroupSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GroupSearchFilter)
