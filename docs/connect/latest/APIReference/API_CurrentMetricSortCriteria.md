---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CurrentMetricSortCriteria.html
---

# CurrentMetricSortCriteria
<a name="API_CurrentMetricSortCriteria"></a>

The way to sort the resulting response based on metrics. By default resources are sorted based on `AGENTS_ONLINE`, `DESCENDING`. The metric collection is sorted based on the input metrics.

## Contents
<a name="API_CurrentMetricSortCriteria_Contents"></a>

 ** SortByMetric **   <a name="connect-Type-CurrentMetricSortCriteria-SortByMetric"></a>
The current metric names.
Type: String
Valid Values: `AGENTS_ONLINE | AGENTS_AVAILABLE | AGENTS_ON_CALL | AGENTS_NON_PRODUCTIVE | AGENTS_AFTER_CONTACT_WORK | AGENTS_ERROR | AGENTS_STAFFED | CONTACTS_IN_QUEUE | OLDEST_CONTACT_AGE | CONTACTS_SCHEDULED | AGENTS_ON_CONTACT | SLOTS_ACTIVE | SLOTS_AVAILABLE | ESTIMATED_WAIT_TIME`
Required: No

 ** SortOrder **   <a name="connect-Type-CurrentMetricSortCriteria-SortOrder"></a>
The way to sort.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## See Also
<a name="API_CurrentMetricSortCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CurrentMetricSortCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CurrentMetricSortCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CurrentMetricSortCriteria)
