---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_TsvStoreOptions.html
---

# TsvStoreOptions
<a name="API_TsvStoreOptions"></a>

File settings for a TSV store.

## Contents
<a name="API_TsvStoreOptions_Contents"></a>

 ** annotationType **   <a name="omics-Type-TsvStoreOptions-annotationType"></a>
The store's annotation type.
Type: String
Valid Values: `GENERIC | CHR_POS | CHR_POS_REF_ALT | CHR_START_END_ONE_BASE | CHR_START_END_REF_ALT_ONE_BASE | CHR_START_END_ZERO_BASE | CHR_START_END_REF_ALT_ZERO_BASE`
Required: No

 ** formatToHeader **   <a name="omics-Type-TsvStoreOptions-formatToHeader"></a>
The store's header key to column name mapping.
Type: String to string map
Valid Keys: `CHR | START | END | REF | ALT | POS`
Value Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** schema **   <a name="omics-Type-TsvStoreOptions-schema"></a>
The store's schema.
Type: Array of string to string maps
Array Members: Minimum number of 1 item. Maximum number of 5000 items.
Map Entries: Maximum number of 1 item.
Key Pattern: `[a-z0-9_]{1,255}`
Valid Values: `LONG | INT | STRING | FLOAT | DOUBLE | BOOLEAN`
Required: No

## See Also
<a name="API_TsvStoreOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/TsvStoreOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/TsvStoreOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/TsvStoreOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
