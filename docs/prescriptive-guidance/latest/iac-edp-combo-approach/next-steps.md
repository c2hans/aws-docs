---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iac-edp-combo-approach/next-steps.html
---

# Next steps
<a name="next-steps"></a>

We recommend that you consider the following next steps:
+ **Use CloudFormation to manage all stack resources** – After you launch a CloudFormation stack, use the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home), [API](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/), or [AWS Command Line Interface (AWS CLI)](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html) to update resources in your stack. Avoid making changes to stack resources outside of CloudFormation. Doing so can create a mismatch between your stack's template and the current state of your stack resources, which can cause errors if you update or delete the stack. For more information, see [Walkthrough: Updating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/updating.stacks.walkthrough.html) in the AWS CloudFormation User Guide.
+ **Use AWS Systems Manager Parameter Store** **to create parameters** – Consider using Parameter Store to create parameters and then use the parameters in your CloudFormation template. You can use Parameter Store to better maintain your templates and reduce operational overhead. For more information, see [Working with Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-working-with.html) in the AWS Systems Manager User Guide.
