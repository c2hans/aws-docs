---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeSourceServersRequestFilters.html
---

# DescribeSourceServersRequestFilters
<a name="API_DescribeSourceServersRequestFilters"></a>

A set of filters by which to return Source Servers.

## Contents
<a name="API_DescribeSourceServersRequestFilters_Contents"></a>

 ** hardwareId **   <a name="drs-Type-DescribeSourceServersRequestFilters-hardwareId"></a>
An ID that describes the hardware of the Source Server. This is either an EC2 instance id, a VMware uuid or a mac address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** sourceServerIDs **   <a name="drs-Type-DescribeSourceServersRequestFilters-sourceServerIDs"></a>
An array of Source Servers IDs that should be returned. An empty array means all Source Servers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: No

 ** stagingAccountIDs **   <a name="drs-Type-DescribeSourceServersRequestFilters-stagingAccountIDs"></a>
An array of staging account IDs that extended source servers belong to. An empty array means all source servers will be shown.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

## See Also
<a name="API_DescribeSourceServersRequestFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DescribeSourceServersRequestFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DescribeSourceServersRequestFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DescribeSourceServersRequestFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
