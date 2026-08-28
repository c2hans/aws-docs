---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContainerServiceECRImagePullerRole.html
---

# ContainerServiceECRImagePullerRole
<a name="API_ContainerServiceECRImagePullerRole"></a>

Describes the activation status of the role that you can use to grant an Amazon Lightsail container service access to Amazon Elastic Container Registry (Amazon ECR) private repositories.

When activated, Lightsail creates an AWS Identity and Access Management (IAM) role for the specified Lightsail container service. You can use the ARN of the role to create a trust relationship between your Lightsail container service and an Amazon ECR private repository in your AWS account. This allows your container service to pull images from Amazon ECR private repositories. For more information, see [Configuring access to an Amazon ECR private repository for an Amazon Lightsail container service](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-service-ecr-private-repo-access) in the *Amazon Lightsail Developer Guide*.

## Contents
<a name="API_ContainerServiceECRImagePullerRole_Contents"></a>

 ** isActive **   <a name="Lightsail-Type-ContainerServiceECRImagePullerRole-isActive"></a>
A Boolean value that indicates whether the role is activated.
Type: Boolean
Required: No

 ** principalArn **   <a name="Lightsail-Type-ContainerServiceECRImagePullerRole-principalArn"></a>
The Amazon Resource Name (ARN) of the role, if it is activated.
Type: String
Required: No

## See Also
<a name="API_ContainerServiceECRImagePullerRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/ContainerServiceECRImagePullerRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/ContainerServiceECRImagePullerRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/ContainerServiceECRImagePullerRole)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
