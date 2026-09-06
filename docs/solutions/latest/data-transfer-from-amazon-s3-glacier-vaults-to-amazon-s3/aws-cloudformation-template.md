---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/aws-cloudformation-template.html
---

# AWS CloudFormation template
<a name="aws-cloudformation-template"></a>

 You can download the CloudFormation template for this Guidance before deploying it.

[![View template button.](http://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/images/view-template-button.png)](https://solutions-reference.s3.amazonaws.com/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3.template) **data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3.template** – Use this template to launch the Guidance and all associated components. The default configuration deploys the core and supporting services found in the [AWS services in this Guidance](architecture-details.md#aws-services-in-this-guidance) section, but you can customize the template to meet your specific needs.

**Note**
 AWS CloudFormation resources are created from AWS Cloud Development Kit (AWS CDK) (AWS CDK) constructs.

 This AWS CloudFormation template deploys Data Transfer from Amazon Glacier Vaults to Amazon S3 in the AWS Cloud.

**Important**
 **Notifications** – The Amazon Glacier service sends one notification per archive to the vault Amazon SNS topic (if it exists). If you don't want subscribers to the Amazon SNS topic to receive these notifications, confirm that the Amazon Glacier vault being transferred doesn't have notifications enabled. For more information, see [Configuring Vault Notifications in Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html) in the *Amazon Glacier Developer Guide*.
 **Inventory** – This Guidance copies your Amazon Glacier vault archives once when you launch the stack. If you make changes to your vault after launching this Guidance, the Guidance doesn’t replicate those changes.
 **Simultaneous workflows** – Running multiple transfer workflows simultaneously can exceed Amazon Glacier quotas and induce throttling. We recommend that you only run one transfer workflow at a time.
