---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ScheduledActionFilter.html
---

# ScheduledActionFilter
<a name="API_ScheduledActionFilter"></a>

A set of elements to filter the returned scheduled actions.

## Contents
<a name="API_ScheduledActionFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **
The type of element to filter.
Type: String
Valid Values: `cluster-identifier | iam-role`
Required: Yes

 ** Values.item.N **
List of values. Compare if the value (of type defined by `Name`) equals an item in the list of scheduled actions.
Type: Array of strings
Length Constraints: Maximum length of 2147483647.
Required: Yes

## See Also
<a name="API_ScheduledActionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ScheduledActionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ScheduledActionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ScheduledActionFilter)
