---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UserIndexCapacityFilter.html
---

# UserIndexCapacityFilter
<a name="API_UserIndexCapacityFilter"></a>

A filter for user index capacity queries. Only one filter type can be specified per request.

## Contents
<a name="API_UserIndexCapacityFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** totalCapacityBytes **   <a name="QS-Type-UserIndexCapacityFilter-totalCapacityBytes"></a>
Filter users by total capacity range in bytes.
Type: [CapacityBytesRangeFilter](API_CapacityBytesRangeFilter.md) object
Required: No

 ** userNameOrEmail **   <a name="QS-Type-UserIndexCapacityFilter-userNameOrEmail"></a>
Filter users by username or email prefix.
Type: [UserNameOrEmailFilter](API_UserNameOrEmailFilter.md) object
Required: No

## See Also
<a name="API_UserIndexCapacityFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UserIndexCapacityFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UserIndexCapacityFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UserIndexCapacityFilter)
