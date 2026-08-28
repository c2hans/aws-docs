---
source_url: https://docs.aws.amazon.com/comprehend/latest/dg/training-recognizers.html
---

# Training custom entity recognizer models
<a name="training-recognizers"></a>

A custom entity recognizer identifies only the entity types that you include when you train the model. It does not automatically include the preset entity types. If you want to also identify the preset entity types,such as LOCATION, DATE, or PERSON, you need to provide additional training data for those entities.

When you create a custom entity recognizer using annotated PDF files, you can use the recognizer with a variety of input file formats: plaintext, image files (JPG, PNG, TIFF), PDF files, and Word documents, with no pre-processing or doc flattening required. Amazon Comprehend doesn't support annotation of image files or Word documents.

**Note**
A custom entity recognizer using annotated PDF files supports English documents only.

After you create a custom entity recognizer, you can monitor the progress of the request using the [DescribeEntityRecognizer](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeEntityRecognizer.html) operation. Once the `Status` field is `TRAINED`, the recognizer model is ready to use for custom entity recognition.

**Topics**
+ [Train custom recognizers (console)](realtime-analysis-cer.md)
+ [Train custom entity recognizers (API)](train-cer-model.md)
+ [Custom entity recognizer metrics](cer-metrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
