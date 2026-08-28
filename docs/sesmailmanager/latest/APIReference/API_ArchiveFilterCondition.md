---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ArchiveFilterCondition.html
---

# ArchiveFilterCondition
<a name="API_ArchiveFilterCondition"></a>

A filter condition used to include or exclude emails when exporting from or searching an archive.

## Contents
<a name="API_ArchiveFilterCondition_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BooleanExpression **   <a name="sesmailmanager-Type-ArchiveFilterCondition-BooleanExpression"></a>
A boolean expression to evaluate against email attributes.
Type: [ArchiveBooleanExpression](API_ArchiveBooleanExpression.md) object
Required: No

 ** StringExpression **   <a name="sesmailmanager-Type-ArchiveFilterCondition-StringExpression"></a>
A string expression to evaluate against email attributes.
Type: [ArchiveStringExpression](API_ArchiveStringExpression.md) object
Required: No

## See Also
<a name="API_ArchiveFilterCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ArchiveFilterCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ArchiveFilterCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ArchiveFilterCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
