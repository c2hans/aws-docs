---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-console-export.html
---

# Export a model card
<a name="model-cards-console-export"></a>

Follow these steps to export a model card.

1. Go to the Amazon SageMaker Model Card console.

1. Choose the name of the model card you want to export.

1. In the model card overview, choose **Actions** and then **Export PDF**.

1. Enter an S3 URI or browse available S3 buckets for your model card PDF.

1. If your model card exports successfully, you can either choose **Download PDF** in the resulting banner or download your PDF directly from Amazon S3.

You can export a model card in the SageMaker Python SDK by specifying an S3 output path and export your model card PDF to it with the following commands:

```
s3_output_path = f"s3://{{{bucket}}}/{{{prefix}}}/export"
pdf_s3_url = {{my_card}}.export_pdf(s3_output_path=s3_output_path).delete()
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
