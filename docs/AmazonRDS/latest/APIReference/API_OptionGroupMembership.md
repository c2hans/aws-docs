---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_OptionGroupMembership.html
---

# OptionGroupMembership
<a name="API_OptionGroupMembership"></a>

Provides information on the option groups the DB instance is a member of.

## Contents
<a name="API_OptionGroupMembership_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** OptionGroupName **
The name of the option group that the instance belongs to.
Type: String
Required: No

 ** Status **
The status of the DB instance's option group membership. Valid values are: `in-sync`, `pending-apply`, `pending-removal`, `pending-maintenance-apply`, `pending-maintenance-removal`, `applying`, `removing`, and `failed`.
Type: String
Required: No

## See Also
<a name="API_OptionGroupMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/OptionGroupMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/OptionGroupMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/OptionGroupMembership)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
