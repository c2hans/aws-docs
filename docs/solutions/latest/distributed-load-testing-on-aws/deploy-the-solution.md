---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

This solution offers three web console hosting options. The backend architecture and Amazon Cognito authentication model are identical across all options.

| Hosting option | Description | When to use |
| --- | --- | --- |
|  **CloudFront \+ S3 (default)**  | The web console is hosted in Amazon S3 and served through Amazon CloudFront. | Recommended for most deployments. Provides global edge caching and requires no additional infrastructure. |
|  **ALB \+ ECS Fargate**  | The web console runs on an ECS Fargate service behind an Application Load Balancer with a customer-provided ACM certificate and custom domain. An AWS WAF web ACL is deployed in front of the ALB to filter common web-based attacks. | Use when VPC Block Public Access (BPA) policies prevent traffic from public CloudFront distributions, when your organization requires zero public internet exposure, when you need a custom domain name for the web console, or when you need web application firewall protection with customizable rules. Common in regulated industries (finance, healthcare, government) and environments with strict compliance requirements. |
|  **Headless (bring your own web server)**  | The solution deploys the backend only and provides a downloadable zip of the web console static assets for hosting on your own web server. | Use when you want to host the web console on existing infrastructure outside of AWS, when corporate policies require hosting on managed web servers, or when your organization mandates complete network isolation with no public-facing endpoints regardless of authentication mechanisms. |

 [AWS Launch Wizard](deploy-using-aws-launch-wizard.md) is the recommended deployment method for this solution. It provides:
+ A guided configuration experience with detailed help panels at each step
+ A centralized page to monitor the health of all your deployments
+ Indication when there is a more recent version of the solution available for deployment or upgrade

Alternatively, you can deploy the solution directly using an [AWS CloudFormation template](deploy-using-aws-cloudformation.md).

## Deployment process overview
<a name="deployment-process-overview"></a>

Before you deploy the solution, review the [cost](cost.md), [architecture](architecture-overview.md), [security](security-1.md), and other considerations discussed earlier in this guide.

 **Time to deploy:** Approximately 15 minutes for the main stack, plus 5 minutes for each additional Region

**Note**
This solution includes data collection metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered through this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

**Note**
You are responsible for the cost of the AWS services used while running this solution. For more information about costs, see the [Cost](cost.md) section in this guide. Also refer to the pricing webpage for each AWS service used in this solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Distributed Load Testing on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
