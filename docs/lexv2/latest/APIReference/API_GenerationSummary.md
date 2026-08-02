---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_GenerationSummary.html
---

# GenerationSummary
<a name="API_GenerationSummary"></a>

Contains information about a generation request made for the bot locale.

## Contents
<a name="API_GenerationSummary_Contents"></a>

 ** creationDateTime **   <a name="lexv2-Type-GenerationSummary-creationDateTime"></a>
The date and time at which the generation request was made.
Type: Timestamp
Required: No

 ** generationId **   <a name="lexv2-Type-GenerationSummary-generationId"></a>
The unique identifier of the generation request.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: No

 ** generationStatus **   <a name="lexv2-Type-GenerationSummary-generationStatus"></a>
The status of the generation request.
Type: String
Valid Values: `Failed | Complete | InProgress`
Required: No

 ** lastUpdatedDateTime **   <a name="lexv2-Type-GenerationSummary-lastUpdatedDateTime"></a>
The date and time at which the generation request was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_GenerationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/GenerationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/GenerationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/GenerationSummary)
