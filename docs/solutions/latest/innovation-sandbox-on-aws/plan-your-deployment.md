---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/plan-your-deployment.html
---

# Plan your deployment

This section describes the [Regions](#supported-aws-regions), [cost](cost.md), [security](security-1.md), and other considerations prior to deploying the solution.

## Supported AWS Regions
<a name="supported-aws-regions"></a>

Innovation Sandbox on AWS is available in the following AWS Regions. [Learn more](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) about enabling regions.

| Region Name | Region Code |
| --- | --- |
| US East (Ohio) | us-east-2 |
| US East (N. Virginia) | us-east-1 |
| US West (Oregon) | us-west-2 |
| Asia Pacific (Tokyo) | ap-northeast-1 |
| Asia Pacific (Seoul) | ap-northeast-2 |
| Asia Pacific (Mumbai) | ap-south-1 |
| Asia Pacific (Singapore) | ap-southeast-1 |
| Asia Pacific (Sydney) | ap-southeast-2 |
| Canada (Central) | ca-central-1 |
| Europe (Frankfurt) | eu-central-1 |
| Europe (Stockholm) | eu-north-1 |
| Europe (Ireland) | eu-west-1 |
| Europe (London) | eu-west-2 |
| Europe (Paris) | eu-west-3 |
| South America (São Paulo) | sa-east-1 |

For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

**Important**
 **CloudFront Access Logging Limitation**
As of September 2025, CloudFront access logging is automatically disabled in the following regions due to lack of support for standard logging (legacy):
Africa (Cape Town) - `af-south-1`
Asia Pacific (Hong Kong) - `ap-east-1`
Asia Pacific (Hyderabad) - `ap-south-2`
Asia Pacific (Jakarta) - `ap-southeast-3`
Asia Pacific (Melbourne) - `ap-southeast-4`
Canada West (Calgary) - `ca-west-1`
Europe (Milan) - `eu-south-1`
Europe (Spain) - `eu-south-2`
Europe (Zurich) - `eu-central-2`
Israel (Tel Aviv) - `il-central-1`
Middle East (Bahrain) - `me-south-1`
Middle East (UAE) - `me-central-1`
If you deploy the solution in one of these regions, the CloudFront distribution will function normally but will not generate access logs. If access logging is required for your use case, you can manually configure CloudFront Standard Logging V2 after deployment. For more information, refer to the [CloudFront Standard Logging V2 documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/standard-logging.html).

<a name="managed-opt-in-regions"></a>**Managed opt-in Regions**

AWS sets the opt-in status for an opt-in Region to `DISABLED` by default.

In each managed Region, the Compute stack creates or joins a shared CloudWatch Observability Access Manager (OAM) sink in the hub account. The service-managed `Isb-<namespace>-ObservabilityLinks` StackSet creates an OAM link in every account under the account pool OU hierarchy. TokenPoll uses these links to read Bedrock token metrics for leases that use token monitoring.

**Important**
Before you add an opt-in Region to **ISB Managed Regions**, set its opt-in status to `ENABLED` in the hub account and every existing pool account. For each new sandbox account, set the opt-in status for every configured opt-in Region to `ENABLED` before moving the account to the **Entry** OU.

If the Region’s opt-in status in the hub account is not `ENABLED`, the Compute stack update fails and rolls back. The Account Pool stack keeps its updated managed Region list. Enable the Region in the hub account, and then update the Compute stack again with another new **Force configuration update (optional)** value. Until the Compute update succeeds, TokenPoll can report a `MissingSinkError` for the Region. If the Region’s opt-in status in a pool account is not `ENABLED`, only that account’s observability link in the Region fails. The Compute stack succeeds because the StackSet tolerates member-account failures.

Every change to **ISB Managed Regions**, including removal of a Region, requires two stack updates. First, update the Account Pool stack and wait for the update to complete. Then, update the Compute stack with the existing template and change **Force configuration update (optional)** to a value different from its current value. The Compute stack re-reads the managed Regions, reconciles this namespace’s regional sink policies, and updates the `Isb-<namespace>-ObservabilityLinks` StackSet. If you add a Region without updating the Compute stack, TokenPoll cannot find its sink and reports a `MissingSinkError`. For instructions, see [Update managed Regions](step1-deploy-accountpool-stack.md#update-managed-regions).
