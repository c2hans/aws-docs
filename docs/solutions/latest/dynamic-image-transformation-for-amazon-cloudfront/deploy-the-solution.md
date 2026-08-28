---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

AWS Launch Wizard is the recommended deployment method for this solution in commercial AWS Regions. It provides:
+ A guided configuration experience with detailed help panels at each step
+ A centralized page to monitor the health of all your deployments
+ Indication when there is a more recent version of the solution available for deployment or upgrade

For opt-in Regions, AWS Launch Wizard is not supported. Use the [AWS CloudFormation template](deploy-using-aws-cloudformation.md) to deploy in these Regions. For information about opt-in Regions, refer to [Managing AWS Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) in the *AWS General Reference guide*.

## Deployment process overview
<a name="deployment-process-overview"></a>

Before you deploy the solution, review the [cost](cost.md), [architecture](architecture-overview.md), [security](security.md), and other considerations discussed earlier in this guide. Additionally, review the [deployment architecture options](choosing-deployment-architecture.md) to determine which template best meets your requirements.

 **Time to deploy:** Approximately 20 minutes.

**Note**
This solution includes data collection metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered through this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

**Note**
You are responsible for the cost of the AWS services used while running this solution. For more details, visit the [Cost](https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/cost.html) section in this guide and refer to the pricing webpage for each AWS service used in this solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
