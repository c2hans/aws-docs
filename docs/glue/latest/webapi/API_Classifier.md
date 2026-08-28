---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Classifier.html
---

# Classifier
<a name="API_Classifier"></a>

Classifiers are triggered during a crawl task. A classifier checks whether a given file is in a format it can handle. If it is, the classifier creates a schema in the form of a `StructType` object that matches that data format.

You can use the standard classifiers that AWS Glue provides, or you can write your own classifiers to best categorize your data sources and specify the appropriate schemas to use for them. A classifier can be a `grok` classifier, an `XML` classifier, a `JSON` classifier, or a custom `CSV` classifier, as specified in one of the fields in the `Classifier` object.

## Contents
<a name="API_Classifier_Contents"></a>

 ** CsvClassifier **   <a name="Glue-Type-Classifier-CsvClassifier"></a>
A classifier for comma-separated values (CSV).
Type: [CsvClassifier](API_CsvClassifier.md) object
Required: No

 ** GrokClassifier **   <a name="Glue-Type-Classifier-GrokClassifier"></a>
A classifier that uses `grok`.
Type: [GrokClassifier](API_GrokClassifier.md) object
Required: No

 ** JsonClassifier **   <a name="Glue-Type-Classifier-JsonClassifier"></a>
A classifier for JSON content.
Type: [JsonClassifier](API_JsonClassifier.md) object
Required: No

 ** XMLClassifier **   <a name="Glue-Type-Classifier-XMLClassifier"></a>
A classifier for XML content.
Type: [XMLClassifier](API_XMLClassifier.md) object
Required: No

## See Also
<a name="API_Classifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Classifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Classifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Classifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
