---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RowLevelPermissionConfiguration.html
---

# RowLevelPermissionConfiguration
<a name="API_RowLevelPermissionConfiguration"></a>

Configuration for row level security.

## Contents
<a name="API_RowLevelPermissionConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RowLevelPermissionDataSet **   <a name="QS-Type-RowLevelPermissionConfiguration-RowLevelPermissionDataSet"></a>
Information about a dataset that contains permissions for row-level security (RLS). The permissions dataset maps fields to users or groups. For more information, see [Using Row-Level Security (RLS) to Restrict Access to a Dataset](https://docs.aws.amazon.com/quicksight/latest/user/restrict-access-to-a-data-set-using-row-level-security.html) in the *Quick Sight User Guide*.
The option to deny permissions by setting `PermissionPolicy` to `DENY_ACCESS` is not supported for new RLS datasets.
Type: [RowLevelPermissionDataSet](API_RowLevelPermissionDataSet.md) object
Required: No

 ** TagConfiguration **   <a name="QS-Type-RowLevelPermissionConfiguration-TagConfiguration"></a>
The configuration of tags on a dataset to set row-level security.
Type: [RowLevelPermissionTagConfiguration](API_RowLevelPermissionTagConfiguration.md) object
Required: No

## See Also
<a name="API_RowLevelPermissionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RowLevelPermissionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RowLevelPermissionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RowLevelPermissionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
