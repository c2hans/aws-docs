---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_JsonClassifier.html
---

# JsonClassifier
<a name="API_JsonClassifier"></a>

A classifier for `JSON` content.

## Contents
<a name="API_JsonClassifier_Contents"></a>

 ** JsonPath **   <a name="Glue-Type-JsonClassifier-JsonPath"></a>
A `JsonPath` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of JsonPath, as described in [Writing JsonPath Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json).
Type: String
Required: Yes

 ** Name **   <a name="Glue-Type-JsonClassifier-Name"></a>
The name of the classifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** CreationTime **   <a name="Glue-Type-JsonClassifier-CreationTime"></a>
The time that this classifier was registered.
Type: Timestamp
Required: No

 ** LastUpdated **   <a name="Glue-Type-JsonClassifier-LastUpdated"></a>
The time that this classifier was last updated.
Type: Timestamp
Required: No

 ** Version **   <a name="Glue-Type-JsonClassifier-Version"></a>
The version of this classifier.
Type: Long
Required: No

## See Also
<a name="API_JsonClassifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/JsonClassifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/JsonClassifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/JsonClassifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
