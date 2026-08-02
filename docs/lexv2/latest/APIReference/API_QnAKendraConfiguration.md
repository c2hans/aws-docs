---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_QnAKendraConfiguration.html
---

# QnAKendraConfiguration
<a name="API_QnAKendraConfiguration"></a>

Contains details about the configuration of the Amazon Kendra index used for the `AMAZON.QnAIntent`.

## Contents
<a name="API_QnAKendraConfiguration_Contents"></a>

 ** kendraIndex **   <a name="lexv2-Type-QnAKendraConfiguration-kendraIndex"></a>
The ARN of the Amazon Kendra index to use.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `^arn:aws:kendra:[a-z]+-[a-z]+-[0-9]:[0-9]{12}:index\/[a-zA-Z0-9][a-zA-Z0-9_-]*$`
Required: Yes

 ** exactResponse **   <a name="lexv2-Type-QnAKendraConfiguration-exactResponse"></a>
Specifies whether to return an exact response from the Amazon Kendra index or to let the Amazon Bedrock model you select generate a response based on the results. To use this feature, you must first add FAQ questions to your index by following the steps at [Adding frequently asked questions (FAQs) to an index](https://docs.aws.amazon.com/kendra/latest/dg/in-creating-faq.html).
Type: Boolean
Required: No

 ** queryFilterString **   <a name="lexv2-Type-QnAKendraConfiguration-queryFilterString"></a>
Contains the Amazon Kendra filter string to use if enabled. For more information on the Amazon Kendra search filter JSON format, see [Using document attributes to filter search results](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html#search-filtering).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.
Required: No

 ** queryFilterStringEnabled **   <a name="lexv2-Type-QnAKendraConfiguration-queryFilterStringEnabled"></a>
Specifies whether to enable an Amazon Kendra filter string or not.
Type: Boolean
Required: No

## See Also
<a name="API_QnAKendraConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/QnAKendraConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/QnAKendraConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/QnAKendraConfiguration)
