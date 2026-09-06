---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/updating-template-parameters.html
---

# Updating template parameters
<a name="updating-template-parameters"></a>

Use the following instructions to update template parameters in such a way that there is no drift between your resources and your CloudFormation stack, and to ensure that all necessary changes are made to your resources:

1. Sign in to the AWS CloudFormation console, select your existing Dynamic Image Transformation for Amazon CloudFront CloudFormation stack, and select Update.

1. Leaving Use Current Template selected, choose Next

1. Modify the template parameters as needed

1. Continue through the rest of the workflow as you would when creating the stack.

**Note**
Modifications made to DIT which are not reflected in the CloudFormation template may be removed when updating template parameters in this fashion
