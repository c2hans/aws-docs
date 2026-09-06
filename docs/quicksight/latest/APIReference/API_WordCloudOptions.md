---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_WordCloudOptions.html
---

# WordCloudOptions
<a name="API_WordCloudOptions"></a>

The word cloud options for a word cloud visual.

## Contents
<a name="API_WordCloudOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CloudLayout **   <a name="QS-Type-WordCloudOptions-CloudLayout"></a>
The cloud layout options (fluid, normal) of a word cloud.
Type: String
Valid Values: `FLUID | NORMAL`
Required: No

 ** MaximumStringLength **   <a name="QS-Type-WordCloudOptions-MaximumStringLength"></a>
The length limit of each word from 1-100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** WordCasing **   <a name="QS-Type-WordCloudOptions-WordCasing"></a>
The word casing options (lower\_case, existing\_case) for the words in a word cloud.
Type: String
Valid Values: `LOWER_CASE | EXISTING_CASE`
Required: No

 ** WordOrientation **   <a name="QS-Type-WordCloudOptions-WordOrientation"></a>
The word orientation options (horizontal, horizontal\_and\_vertical) for the words in a word cloud.
Type: String
Valid Values: `HORIZONTAL | HORIZONTAL_AND_VERTICAL`
Required: No

 ** WordPadding **   <a name="QS-Type-WordCloudOptions-WordPadding"></a>
The word padding options (none, small, medium, large) for the words in a word cloud.
Type: String
Valid Values: `NONE | SMALL | MEDIUM | LARGE`
Required: No

 ** WordScaling **   <a name="QS-Type-WordCloudOptions-WordScaling"></a>
The word scaling options (emphasize, normal) for the words in a word cloud.
Type: String
Valid Values: `EMPHASIZE | NORMAL`
Required: No

## See Also
<a name="API_WordCloudOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/WordCloudOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/WordCloudOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/WordCloudOptions)
