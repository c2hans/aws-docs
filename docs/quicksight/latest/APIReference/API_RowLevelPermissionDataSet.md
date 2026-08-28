---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RowLevelPermissionDataSet.html
---

# RowLevelPermissionDataSet
<a name="API_RowLevelPermissionDataSet"></a>

Information about a dataset that contains permissions for row-level security (RLS). The permissions dataset maps fields to users or groups. For more information, see [Using Row-Level Security (RLS) to Restrict Access to a Dataset](https://docs.aws.amazon.com/quicksight/latest/user/restrict-access-to-a-data-set-using-row-level-security.html) in the *Quick Sight User Guide*.

The option to deny permissions by setting `PermissionPolicy` to `DENY_ACCESS` is not supported for new RLS datasets.

## Contents
<a name="API_RowLevelPermissionDataSet_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-RowLevelPermissionDataSet-Arn"></a>
The Amazon Resource Name (ARN) of the dataset that contains permissions for RLS.
Type: String
Required: Yes

 ** PermissionPolicy **   <a name="QS-Type-RowLevelPermissionDataSet-PermissionPolicy"></a>
The type of permissions to use when interpreting the permissions for RLS. `DENY_ACCESS` is included for backward compatibility only.
Type: String
Valid Values: `GRANT_ACCESS | DENY_ACCESS`
Required: Yes

 ** FormatVersion **   <a name="QS-Type-RowLevelPermissionDataSet-FormatVersion"></a>
The user or group rules associated with the dataset that contains permissions for RLS.
By default, `FormatVersion` is `VERSION_1`. When `FormatVersion` is `VERSION_1`, `UserName` and `GroupName` are required. When `FormatVersion` is `VERSION_2`, `UserARN` and `GroupARN` are required, and `Namespace` must not exist.
Type: String
Valid Values: `VERSION_1 | VERSION_2`
Required: No

 ** Namespace **   <a name="QS-Type-RowLevelPermissionDataSet-Namespace"></a>
The namespace associated with the dataset that contains permissions for RLS.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: No

 ** Status **   <a name="QS-Type-RowLevelPermissionDataSet-Status"></a>
The status of the row-level security permission dataset. If enabled, the status is `ENABLED`. If disabled, the status is `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_RowLevelPermissionDataSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RowLevelPermissionDataSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RowLevelPermissionDataSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RowLevelPermissionDataSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
