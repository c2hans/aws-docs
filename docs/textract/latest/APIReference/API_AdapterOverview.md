---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_AdapterOverview.html
---

# AdapterOverview
<a name="API_AdapterOverview"></a>

Contains information on the adapter, including the adapter ID, Name, Creation time, and feature types.

## Contents
<a name="API_AdapterOverview_Contents"></a>

 ** AdapterId **   <a name="Textract-Type-AdapterOverview-AdapterId"></a>
A unique identifier for the adapter resource.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1011.
Required: No

 ** AdapterName **   <a name="Textract-Type-AdapterOverview-AdapterName"></a>
A string naming the adapter resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** CreationTime **   <a name="Textract-Type-AdapterOverview-CreationTime"></a>
The date and time that the adapter was created.
Type: Timestamp
Required: No

 ** FeatureTypes **   <a name="Textract-Type-AdapterOverview-FeatureTypes"></a>
The feature types that the adapter is operating on.
Type: Array of strings
Valid Values: `TABLES | FORMS | QUERIES | SIGNATURES | LAYOUT`
Required: No

## See Also
<a name="API_AdapterOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/AdapterOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/AdapterOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/AdapterOverview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
