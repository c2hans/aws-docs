---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/cost-attribution.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Cost attribution
<a name="cost-attribution"></a>

SageMaker AI Studio has built in capabilities to help administrators track the spend of their individual domains, shared spaces, and users.

## Automated tagging
<a name="automated-tagging"></a>

SageMaker AI Studio now automatically tags new SageMaker resources such as training jobs, processing jobs, and kernel apps with their respective `sagemaker:domain-arn`. At a more granular level, SageMaker AI also tags the resource with the `sagemaker:user-profile-arn` or `sagemaker:space-arn` to designate the the principal creator of the resource.

SageMaker AI domain EFS volumes are tagged with a key named `ManagedByAmazonSageMakerResource` with the value of the domain ARN. They do not have granular tags to understand the space usage on a per user level. Administrators can attach the EFS volume to an EC2 instance for bespoke monitoring though.

## Cost monitoring
<a name="cost-monitoring"></a>

Automated tags enable Administrators to track, report, and monitor your ML spend through out-of-the-box solutions such as [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/), as well as custom solutions built on the data from [AWS Cost and Usage Reports](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/) (CURs).

To use the attached tags for cost analysis, they must first be activated in the **[Cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)** section of the AWS Billing console. It can take up to 24 hours for tags to show up in the cost allocate tag panel, so you’ll need to create a SageMaker AI resource prior to enabling them.

![A diagram that shows a space ARN enabled as cost allocation tags on Cost Explorer.](https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/space-arn.png)

After you have enabled a cost allocation tag, AWS will begin tracking your tagged resources, and after 24-48 hours, the tags will show up as selectable filters in cost explorer.

![A diagram that shows costs grouped by shared space for a sample domain.](https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/costs-grouped-by-shared-space.png)

## Cost control
<a name="cost-control"></a>

When the first SageMaker AI Studio user is onboarded, SageMaker AI creates an EFS volume for the domain. Storage costs are incurred for this EFS volume as notebooks and data files are stored in the user’s home directory. When the user launches Studio notebooks, they are launched for the compute instances running the notebooks. Refer to [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker/pricing/) for detailed breakdown of costs.

Administrators can control compute costs by specifying the list of instances a user can spin up, using IAM policies as mentioned in the *[Common guardrails](permissions-management.md#common-guardrails) *section. In addition, we recommend that customers make use of the SageMaker AI [Studio auto shutdown extension](https://github.com/aws-samples/sagemaker-studio-auto-shutdown-extension) to save costs by automatically shutting down idle apps. This server extension periodically polls for running apps per user profile, and shuts down idle apps based on a timeout set by the administrator.

To set this extension for all users in your domain, you can use a lifecycle configuration as described in *[Customization](customization.md)* section. Additionally, you can also use the [extension checker](https://github.com/aws-samples/sagemaker-studio-auto-shutdown-extension/tree/main/extension-checker) to ensure all of your domain’s users have the extension installed.
