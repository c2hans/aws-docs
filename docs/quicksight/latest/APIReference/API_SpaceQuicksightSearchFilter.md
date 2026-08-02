---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SpaceQuicksightSearchFilter.html
---

# SpaceQuicksightSearchFilter
<a name="API_SpaceQuicksightSearchFilter"></a>

A filter to use when searching for spaces.

## Contents
<a name="API_SpaceQuicksightSearchFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** name **   <a name="QS-Type-SpaceQuicksightSearchFilter-name"></a>
The name of the filter field to use.
Type: String
Valid Values: `SPACE_ID | SPACE_NAME | DIRECT_QUICKSIGHT_OWNER | DIRECT_QUICKSIGHT_VIEWER_OR_OWNER | DIRECT_QUICKSIGHT_SOLE_OWNER | CONTRIBUTED_BY | CONSUMED_SOURCE_SIZE | CREATED_BY`
Required: Yes

 ** operator **   <a name="QS-Type-SpaceQuicksightSearchFilter-operator"></a>
The comparison operator to use for the filter.
Type: String
Valid Values: `STRING_EQUALS | STRING_LIKE | NUMBER_RANGE`
Required: Yes

 ** value **   <a name="QS-Type-SpaceQuicksightSearchFilter-value"></a>
The value to use for the filter.
Type: String
Required: Yes

## See Also
<a name="API_SpaceQuicksightSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SpaceQuicksightSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SpaceQuicksightSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SpaceQuicksightSearchFilter)
