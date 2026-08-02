---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ProspectingFromEngagementTaskSort.html
---

# ProspectingFromEngagementTaskSort
<a name="API_ProspectingFromEngagementTaskSort"></a>

Specifies the sort configuration for `ListProspectingFromEngagementTasks`. Contains the field to sort by and the sort direction.

## Contents
<a name="API_ProspectingFromEngagementTaskSort_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SortBy **   <a name="AWSPartnerCentral-Type-ProspectingFromEngagementTaskSort-SortBy"></a>
The field by which to sort the returned tasks. Valid values: `StartTime` (task creation timestamp), `TaskName` (alphabetically by task name), and `FailedEngagementCount` (number of failed engagements).
Type: String
Valid Values: `StartTime | TaskName | FailedEngagementCount`
Required: Yes

 ** SortOrder **   <a name="AWSPartnerCentral-Type-ProspectingFromEngagementTaskSort-SortOrder"></a>
The direction in which to sort the results. Use `ASCENDING` to return the smallest or earliest values first, or `DESCENDING` to return the largest or most recent values first.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: Yes

## See Also
<a name="API_ProspectingFromEngagementTaskSort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ProspectingFromEngagementTaskSort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ProspectingFromEngagementTaskSort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ProspectingFromEngagementTaskSort)
