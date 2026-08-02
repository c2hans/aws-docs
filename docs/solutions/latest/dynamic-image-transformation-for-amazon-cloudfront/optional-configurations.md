---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/optional-configurations.html
---

# Optional Configurations
<a name="optional-configurations"></a>

The following sections provide information surrounding optional features and how to disable them. For each feature, use the following instructions.

1. Download the `dynamic-image-transformation-for-amazon-cloudfront.template` [AWS CloudFormation template](aws-cloudformation-template.md) to your local hard drive.

1. Open the CloudFormation template with a text editor.

1. Locate the AWS CloudFormation template mapping section. It will be under the following location:

   ```
   Mappings:
       Solution:
           Config:
   ```

1. Follow the instructions in the section for the feature you would like to disable.

1. Save the template and launch or update your CloudFormation stack using this modified template.
