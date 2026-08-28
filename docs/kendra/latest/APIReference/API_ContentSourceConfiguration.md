---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_ContentSourceConfiguration.html
---

# ContentSourceConfiguration
<a name="API_ContentSourceConfiguration"></a>

Provides the configuration information for your content sources, such as data sources, FAQs, and content indexed directly via [BatchPutDocument](https://docs.aws.amazon.com/kendra/latest/dg/API_BatchPutDocument.html).

## Contents
<a name="API_ContentSourceConfiguration_Contents"></a>

 ** DataSourceIds **   <a name="kendra-Type-ContentSourceConfiguration-DataSourceIds"></a>
The identifier of the data sources you want to use for your Amazon Kendra experience.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** DirectPutContent **   <a name="kendra-Type-ContentSourceConfiguration-DirectPutContent"></a>
 `TRUE` to use documents you indexed directly using the `BatchPutDocument` API.
Type: Boolean
Required: No

 ** FaqIds **   <a name="kendra-Type-ContentSourceConfiguration-FaqIds"></a>
The identifier of the FAQs that you want to use for your Amazon Kendra experience.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

## See Also
<a name="API_ContentSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/ContentSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/ContentSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/ContentSourceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
