---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_LaunchTemplateSpecification.html
---

# LaunchTemplateSpecification
<a name="API_LaunchTemplateSpecification"></a>

An object representing a node group launch template specification. The launch template can't include [`SubnetId`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html), [`IamInstanceProfile`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IamInstanceProfile.html), [`RequestSpotInstances`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html), [`HibernationOptions`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest.html), or [`TerminateInstances`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html), or the node group deployment or update will fail. For more information about launch templates, see [`CreateLaunchTemplate`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) in the Amazon EC2 API Reference. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.

You must specify either the launch template ID or the launch template name in the request, but not both.

## Contents
<a name="API_LaunchTemplateSpecification_Contents"></a>

 ** id **   <a name="AmazonEKS-Type-LaunchTemplateSpecification-id"></a>
The ID of the launch template.
You must specify either the launch template ID or the launch template name in the request, but not both. After node group creation, you cannot use a different ID.
Type: String
Required: No

 ** name **   <a name="AmazonEKS-Type-LaunchTemplateSpecification-name"></a>
The name of the launch template.
You must specify either the launch template name or the launch template ID in the request, but not both. After node group creation, you cannot use a different name.
Type: String
Required: No

 ** version **   <a name="AmazonEKS-Type-LaunchTemplateSpecification-version"></a>
The version number of the launch template to use. If no version is specified, then the template's default version is used. You can use a different version for node group updates.
Type: String
Required: No

## See Also
<a name="API_LaunchTemplateSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/LaunchTemplateSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/LaunchTemplateSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/LaunchTemplateSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
