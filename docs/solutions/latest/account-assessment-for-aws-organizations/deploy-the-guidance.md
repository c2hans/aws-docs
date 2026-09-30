---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/deploy-the-guidance.html
---

# Deploy the guidance
<a name="deploy-the-guidance"></a>

Guidance for Account Assessment for AWS Organizations uses the AWS Cloud Development Kit (AWS CDK) and AWS CloudFormation stacks to automate deployment. The AWS CDK code defines the AWS resources included in this guidance and their properties. AWS CDK synthesizes CloudFormation templates and deploys the stacks.

**Resource-based policy validation**
We designed this guidance to aggregate scan findings for customers. This guidance does not check the validity or correctness of your underlying resource-based policies. When changing policies that allow account migration to another AWS Organization, we recommend:
Verifying that your policies work as intended before making changes.
Using AWS Identity and Access Management (IAM) [Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to verify that your policies achieve your desired permissions.
Reviewing and updating the `Condition` policy element to meet your security requirements. Do not delete the `Condition` without reviewing the underlying impact.
Engaging with AWS Solutions Architects, Technical Account Managers, and AWS Professional Services to review your AWS Organizations-based dependencies identified by the guidance before initiating account migration.

**Dependencies outside this guidance’s scope**
Dependencies outside the scope of this guidance can impact account migration between AWS Organizations. Examples include [AWS Organizations quotas](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html), resources shared by [AWS Resource Access Manager (AWS RAM)](https://aws.amazon.com/ram/), and service-managed [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).

## Deployment process overview
<a name="deployment-process-overview"></a>

Deploy this guidance from the AWS CDK application in the [GitHub repository](https://github.com/aws-solutions-library-samples/account-assessment-for-aws-organizations). Before you deploy, review the [cost](cost.md), [architecture](architecture-overview.md), [security](security.md), and [other considerations](plan-your-deployment.md) discussed in this guide.

The guidance consists of three AWS CDK stacks:

1.  **Hub stack** – Deploys the web UI, API, assessment functions, workflows, and data stores in a member account.

1.  **Org-Management stack** – Deploys the IAM role that the Hub stack uses to read AWS Organizations data. Deploy this stack in the Organizations management account.

1.  **Spoke stack** – Deploys the IAM roles that the Hub stack uses to assess an account. Deploy this stack in each account that you want to assess.

Deploy the Hub stack first, followed by the Org-Management and Spoke stacks.

 **Time to deploy:** Approximately 30 to 45 minutes

**Anonymized operational metrics**
This guidance sends anonymized operational metrics to AWS by default. We use this data to better understand how customers use this guidance and related services and products. AWS owns the data gathered through this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).
To opt out, open `source/infra/lib/account-assessment-hub-stack.ts` before you build the guidance. In the `AnonymousData` mapping, change the `Data` value from `Yes` to `No`. For more information, see [Anonymized data collection](reference.md#operational-metrics).
