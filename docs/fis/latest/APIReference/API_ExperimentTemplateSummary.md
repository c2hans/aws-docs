---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateSummary.html
---

# ExperimentTemplateSummary
<a name="API_ExperimentTemplateSummary"></a>

Provides a summary of an experiment template.

## Contents
<a name="API_ExperimentTemplateSummary_Contents"></a>

 ** arn **   <a name="fis-Type-ExperimentTemplateSummary-arn"></a>
The Amazon Resource Name (ARN) of the experiment template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** creationTime **   <a name="fis-Type-ExperimentTemplateSummary-creationTime"></a>
The time that the experiment template was created.
Type: Timestamp
Required: No

 ** description **   <a name="fis-Type-ExperimentTemplateSummary-description"></a>
The description of the experiment template.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]+`
Required: No

 ** id **   <a name="fis-Type-ExperimentTemplateSummary-id"></a>
The ID of the experiment template.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

 ** lastUpdateTime **   <a name="fis-Type-ExperimentTemplateSummary-lastUpdateTime"></a>
The time that the experiment template was last updated.
Type: Timestamp
Required: No

 ** tags **   <a name="fis-Type-ExperimentTemplateSummary-tags"></a>
The tags for the experiment template.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]+`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_ExperimentTemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentTemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentTemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentTemplateSummary)
