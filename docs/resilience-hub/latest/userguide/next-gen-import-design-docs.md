---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-import-design-docs.html
---

# Import design documents
<a name="next-gen-import-design-docs"></a>

Design documents provide additional architectural context that the next generation of Resilience Hub uses during failure mode assessments. You can upload design documents stored in Amazon S3 as input sources for your service.

**To import a design document (console)**

1. Open the Next generation Resilience Hub console and navigate to your service.

1. Choose the **Assessments** tab.

1. Choose **Failure mode guidance**.

1. Choose **Add more** from Architecture design files.

1. Enter the Amazon S3 URL of your design document.

1. Choose **Save design file**.

**To import a design document (AWS CLI)**
+ Run the following command:

  ```
  aws resiliencehubv2 create-input-source \
    --service-arn "{{service-arn}}" \
    --resource-configuration '{"designFileS3Url": "s3://{{bucket}}/{{path/to/design-doc.pdf}}"}'
  ```

Supported design document formats include PDF, Markdown, and plain text files. The AI assessment engine uses these documents to understand your intended architecture and identify gaps between design intent and actual implementation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
