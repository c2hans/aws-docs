---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GrokClassifier.html
---

# GrokClassifier
<a name="API_GrokClassifier"></a>

A classifier that uses `grok` patterns.

## Contents
<a name="API_GrokClassifier_Contents"></a>

 ** Classification **   <a name="Glue-Type-GrokClassifier-Classification"></a>
An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, and so on.
Type: String
Required: Yes

 ** GrokPattern **   <a name="Glue-Type-GrokClassifier-GrokPattern"></a>
The grok pattern applied to a data store by this classifier. For more information, see built-in patterns in [Writing Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\t]*`
Required: Yes

 ** Name **   <a name="Glue-Type-GrokClassifier-Name"></a>
The name of the classifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** CreationTime **   <a name="Glue-Type-GrokClassifier-CreationTime"></a>
The time that this classifier was registered.
Type: Timestamp
Required: No

 ** CustomPatterns **   <a name="Glue-Type-GrokClassifier-CustomPatterns"></a>
Optional custom grok patterns defined by this classifier. For more information, see custom patterns in [Writing Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16000.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LastUpdated **   <a name="Glue-Type-GrokClassifier-LastUpdated"></a>
The time that this classifier was last updated.
Type: Timestamp
Required: No

 ** Version **   <a name="Glue-Type-GrokClassifier-Version"></a>
The version of this classifier.
Type: Long
Required: No

## See Also
<a name="API_GrokClassifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GrokClassifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GrokClassifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GrokClassifier)
