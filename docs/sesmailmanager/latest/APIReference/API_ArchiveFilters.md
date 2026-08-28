---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ArchiveFilters.html
---

# ArchiveFilters
<a name="API_ArchiveFilters"></a>

A set of filter conditions to include and/or exclude emails.

## Contents
<a name="API_ArchiveFilters_Contents"></a>

 ** Include **   <a name="sesmailmanager-Type-ArchiveFilters-Include"></a>
The filter conditions for emails to include.
Type: Array of [ArchiveFilterCondition](API_ArchiveFilterCondition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** Unless **   <a name="sesmailmanager-Type-ArchiveFilters-Unless"></a>
The filter conditions for emails to exclude.
Type: Array of [ArchiveFilterCondition](API_ArchiveFilterCondition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_ArchiveFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ArchiveFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ArchiveFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ArchiveFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
