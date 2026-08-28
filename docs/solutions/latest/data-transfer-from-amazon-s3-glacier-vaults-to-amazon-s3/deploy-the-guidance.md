---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/deploy-the-guidance.html
---

# Deploy the Guidance
<a name="deploy-the-guidance"></a>

 This Guidance uses [AWS CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation template specifies the AWS resources included in this Guidance and their properties. The CloudFormation stack provisions the resources that are described in the template.

**Note**
 This Guidance doesn't delete the original archives or the source Amazon Glacier vault. You must manually delete the archives and vault. For more information, refer to [Deleting an Archive in Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive.html) in the *Amazon Glacier Developer Guide*.
 If your source Amazon Glacier vault has a [Vault Lock policy](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html) that prevents deletion, you must delete this policy before deleting the original archives. However, if your Vault Lock policy is in the `Locked` state, you can't delete it. See [Amazon Glacier Vault Lock](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html) and [Abort Vault Lock (DELETE lock-policy)](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-AbortVaultLock.html) in the Amazon Glacier Developer Guide for more information.

## Deployment process overview
<a name="deployment-process-overview"></a>

 Follow the step-by-step instructions in this section to configure and deploy the Guidance into your account.

 Before you launch the Guidance, review the [cost](cost.md), [architecture](architecture-overview.md), [security](security-1.md), and other considerations discussed earlier in this guide.

 **Time to deploy:** Approximately 5–10 minutes

**Note**
The archive transfer can take up to one day to complete. If you need to move your data faster, contact [AWS Support](https://aws.amazon.com/premiumsupport) (AWS Developer Support plan or above).

 [Step 1: Launch the stack](step-1-launch-the-stack.md)

 [Step 2: Launch the transfer workflow](step-2-launch-the-transfer-workflow.md)

 [Step 3: Resume the transfer workflow](step-3-resume-the-transfer-workflow.md)

**Important**
 This Guidance includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this Guidance and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).
 To opt out of this feature, download the template, modify the AWS CloudFormation mapping section, and then use the AWS CloudFormation console to upload your updated template and deploy the Guidance. For more information, see the [Anonymized data collection](reference.md#anonymized-data-collection) section of this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
