---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_AdapterVersionOverview.html
---

# AdapterVersionOverview
<a name="API_AdapterVersionOverview"></a>

Summary info for an adapter version. Contains information on the AdapterId, AdapterVersion, CreationTime, FeatureTypes, and Status.

## Contents
<a name="API_AdapterVersionOverview_Contents"></a>

 ** AdapterId **   <a name="Textract-Type-AdapterVersionOverview-AdapterId"></a>
A unique identifier for the adapter associated with a given adapter version.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1011.
Required: No

 ** AdapterVersion **   <a name="Textract-Type-AdapterVersionOverview-AdapterVersion"></a>
An identified for a given adapter version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** CreationTime **   <a name="Textract-Type-AdapterVersionOverview-CreationTime"></a>
The date and time that a given adapter version was created.
Type: Timestamp
Required: No

 ** FeatureTypes **   <a name="Textract-Type-AdapterVersionOverview-FeatureTypes"></a>
The feature types that the adapter version is operating on.
Type: Array of strings
Valid Values: `TABLES | FORMS | QUERIES | SIGNATURES | LAYOUT`
Required: No

 ** Status **   <a name="Textract-Type-AdapterVersionOverview-Status"></a>
Contains information on the status of a given adapter version.
Type: String
Valid Values: `ACTIVE | AT_RISK | DEPRECATED | CREATION_ERROR | CREATION_IN_PROGRESS`
Required: No

 ** StatusMessage **   <a name="Textract-Type-AdapterVersionOverview-StatusMessage"></a>
A message explaining the status of a given adapter vesion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><]+$`
Required: No

## See Also
<a name="API_AdapterVersionOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/AdapterVersionOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/AdapterVersionOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/AdapterVersionOverview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
