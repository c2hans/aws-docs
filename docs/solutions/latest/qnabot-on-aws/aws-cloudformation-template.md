---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/aws-cloudformation-template.html
---

# AWS CloudFormation templates
<a name="aws-cloudformation-template"></a>

You can download the AWS CloudFormation templates for this guidance before deploying it.

## Deploy via main template
<a name="template1"></a>

 **View template**

 [![View Template](https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/qnabot-on-aws/latest/qnabot-on-aws-main.template)

 **qnabot-on-aws-main.template** - Use this template to launch the guidance and all associated components. The default configuration deploys the core and supporting services found in the [AWS services in this guidance](architecture-details.md#aws-services-in-this-solution) section but you can customize the template to meet your specific needs.

## Deploy via VPC template
<a name="template2"></a>

 **View template**

 [![View Template](https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/qnabot-on-aws/latest/qnabot-on-aws-vpc.template)

 **qnabot-on-aws-vpc.template** - Use this template to launch the guidance and all associated components. The default configuration deploys the core and supporting services found in the [AWS services in this guidance](architecture-details.md#aws-services-in-this-solution) section but you can customize the template to meet your specific needs.

This template is made available for use as a separate installation mechanism. It is not the default template utilized in the public distribution. Take care in deploying QnABot in VPC. The OpenSearch Cluster becomes private to the VPC. In addition, the QnABot Lambda functions installed by the stack will be attached to subnets in the VPC. The OpenSearch cluster is no longer available outside of the VPC. The Lambda functions attached to the VPC allow communication with the cluster.

Two additional parameters are required by this template.
+  **VPCSubnetIdList**

**Important**
You should specify two private subnets, spread over two Availability Zones.
+  **VPCSecurityGroupIdList**

More information on how to deploy can be read in the [VPC Support](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/VPC_support) section of the GitHub repository. Additionally, we recommend following the [best practices for securing the VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html).

**Note**
If you have previously deployed this guidance, see [Update the stack](update-the-solution.md) for update instructions.
