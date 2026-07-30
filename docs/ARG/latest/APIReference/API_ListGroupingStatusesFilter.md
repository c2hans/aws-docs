---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroupingStatusesFilter.html
---

# ListGroupingStatusesFilter
<a name="API_ListGroupingStatusesFilter"></a>

A filter name and value pair that is used to obtain more specific results from the list of grouping statuses.

## Contents
<a name="API_ListGroupingStatusesFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="ARG-Type-ListGroupingStatusesFilter-Name"></a>
The name of the filter. Filter names are case-sensitive.
Type: String
Valid Values: `status | resource-arn`
Required: Yes

 ** Values **   <a name="ARG-Type-ListGroupingStatusesFilter-Values"></a>
One or more filter values. Allowed filter values vary by resource filter name, and are case-sensitive.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `SUCCESS|FAILED|IN_PROGRESS|SKIPPED|arn:aws(-[a-z]+)*:[a-z0-9\-]*:([a-z]{2}(-[a-z]+)+-\d{1})?:([0-9]{12})?:.+`
Required: Yes

## See Also
<a name="API_ListGroupingStatusesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/ListGroupingStatusesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/ListGroupingStatusesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/ListGroupingStatusesFilter)
