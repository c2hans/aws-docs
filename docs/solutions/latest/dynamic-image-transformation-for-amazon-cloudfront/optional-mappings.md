---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/optional-mappings.html
---

# Optional Configurations
<a name="optional-mappings"></a>

The following sections provide information surrounding optional features and how to disable them. For each feature, use the following instructions.

1. Download the `dynamic-image-transformation-for-amazon-cloudfront.template` [AWS CloudFormation template](aws-cloudformation-template.md) to your local hard drive.

1. Open the CloudFormation template with a text editor.

1. Locate the AWS CloudFormation template mapping section. It is under the following location:

   ```
   Mappings:
       Solution:
           Config:
   ```

1. Follow the instructions in the section for the feature you would like to disable.

1. Save the template and launch or update your CloudFormation stack using this modified template.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
