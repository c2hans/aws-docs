---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageReference.html
---

# ImageReference
<a name="API_ImageReference"></a>

A resource that is referencing an image.

## Contents
<a name="API_ImageReference_Contents"></a>

 ** arn **
The Amazon Resource Name (ARN) of the resource referencing the image.
Type: String
Required: No

 ** imageId **
The ID of the referenced image.
Type: String
Required: No

 ** resourceType **
The type of resource referencing the image.
Type: String
Valid Values: `ec2:Instance | ec2:LaunchTemplate | ssm:Parameter | imagebuilder:ImageRecipe | imagebuilder:ContainerRecipe`
Required: No

## See Also
<a name="API_ImageReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
