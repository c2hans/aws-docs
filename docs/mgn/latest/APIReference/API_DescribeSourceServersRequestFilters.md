---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeSourceServersRequestFilters.html
---

# DescribeSourceServersRequestFilters
<a name="API_DescribeSourceServersRequestFilters"></a>

Request to filter Source Servers list.

## Contents
<a name="API_DescribeSourceServersRequestFilters_Contents"></a>

 ** applicationIDs **   <a name="mgn-Type-DescribeSourceServersRequestFilters-applicationIDs"></a>
Request to filter Source Servers list by application IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Fixed length of 21.
Pattern: `app-[0-9a-zA-Z]{17}`
Required: No

 ** isArchived **   <a name="mgn-Type-DescribeSourceServersRequestFilters-isArchived"></a>
Request to filter Source Servers list by archived.
Type: Boolean
Required: No

 ** lifeCycleStates **   <a name="mgn-Type-DescribeSourceServersRequestFilters-lifeCycleStates"></a>
Request to filter Source Servers list by life cycle states.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `STOPPED | NOT_READY | READY_FOR_TEST | TESTING | READY_FOR_CUTOVER | CUTTING_OVER | CUTOVER | DISCONNECTED | DISCOVERED | PENDING_INSTALLATION`
Required: No

 ** replicationTypes **   <a name="mgn-Type-DescribeSourceServersRequestFilters-replicationTypes"></a>
Request to filter Source Servers list by replication type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `AGENT_BASED | SNAPSHOT_SHIPPING`
Required: No

 ** sourceServerIDs **   <a name="mgn-Type-DescribeSourceServersRequestFilters-sourceServerIDs"></a>
Request to filter Source Servers list by Source Server ID.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: No

## See Also
<a name="API_DescribeSourceServersRequestFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DescribeSourceServersRequestFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DescribeSourceServersRequestFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DescribeSourceServersRequestFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
