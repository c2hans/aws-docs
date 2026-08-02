---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/step-2-create-the-cloudformation-template.html
---

# Step 2: Create the CloudFormation template
<a name="step-2-create-the-cloudformation-template"></a>

The CloudFormation template defines the infrastructure that makes up the module. When you register a new module, MCS uses [ValidateTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ValidateTemplate.html) to validate the template and extract parameters. The template must be accessible so that MCS can fetch the template.

MCS fetches the CloudFormation template and generates a checksum to store along with the registration metadata. When the module is enabled, MCS verifies that the template still matches the checksum to ensure that it didn’t get corrupted or modified since it was registered. If the checksum doesn’t match, MCS reports the mismatch as an error, and the module isn’t enabled.

For instructions on how to create CloudFormation templates, see [Working with CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in the *AWS CloudFormation User Guide*.
