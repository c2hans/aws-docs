---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ProtectedResourceConditions.html
---

# ProtectedResourceConditions
<a name="API_ProtectedResourceConditions"></a>

The conditions that you define for resources in your restore testing plan using tags.

## Contents
<a name="API_ProtectedResourceConditions_Contents"></a>

 ** StringEquals **   <a name="Backup-Type-ProtectedResourceConditions-StringEquals"></a>
Filters the values of your tagged resources for only those resources that you tagged with the same value. Also called "exact matching."
Type: Array of [KeyValue](API_KeyValue.md) objects
Required: No

 ** StringNotEquals **   <a name="Backup-Type-ProtectedResourceConditions-StringNotEquals"></a>
Filters the values of your tagged resources for only those resources that you tagged that do not have the same value. Also called "negated matching."
Type: Array of [KeyValue](API_KeyValue.md) objects
Required: No

## See Also
<a name="API_ProtectedResourceConditions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ProtectedResourceConditions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ProtectedResourceConditions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ProtectedResourceConditions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
