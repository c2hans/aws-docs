---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/deploy-the-guidance.html
---

# Deploy the guidance
<a name="deploy-the-guidance"></a>

 This guidance uses [CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation template specifies the AWS resources included in this guidance and their properties. The CloudFormation stack provisions the resources that are described in the template.

## Deployment process overview
<a name="deployment-process-overview"></a>

 Follow the step-by-step instructions in this section to configure and deploy the guidance into your account.

 Before you launch the guidance, review the [cost](cost.md), [architecture](architecture-overview.md), [network security](security.md), and other considerations discussed earlier in this guide.

 **Time to deploy:** Approximately 7–10 minutes

 [Step 1: Build deployment assets](step-1-build-deployment-assets.md)
+  Create S3 bucket.
+  Build deployment assets.
+  Copy assets to S3 bucket.

 [Step 2: Launch the stack](step-2-launch-the-stack.md)
+  Launch the CloudFormation template into your AWS account.
+  Enter values for required parameters.
+  Review the other template parameters, and adjust if necessary.

 [Step 2: Modify AWS Network Firewall, firewall policies, rule groups](step-3-modify-the-network-firewall-firewall-policies-and-rule-groups.md)
+  After the stack is successfully created, CloudFormation initiates CodePipeline.
+  Modify the network firewall, firewall policies, and rule group. For details, refer to [Configuring resources for Network Firewall](configuring-resources-for-network-firewall.md).
**Important**
 This guidance includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this guidance and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).
 To opt out of this feature, download the template, modify the AWS CloudFormation mapping section, and then use the AWS CloudFormation console to upload your updated template and deploy the guidance. For more information, see the [Anonymized data collection](reference.md#anonymized-data-collection) section of this guide.
