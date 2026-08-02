---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/choosing-the-deployment-account.html
---

# Choosing the deployment account
<a name="choosing-the-deployment-account"></a>

If you are deploying Workload Discovery on AWS to an AWS Organization, the solution must be installed in a delegated admin account where [StackSets](https://aws.amazon.com/blogs/mt/cloudformation-stacksets-delegated-administration/) and [multi-Region AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/aggregated-register-delegated-administrator.html) capabilities have been enabled.

If you are not using AWS Organizations, we recommend that you deploy Workload Discovery on AWS into a dedicated AWS account created specifically for this solution. This approach means Workload Discovery on AWS is isolated from your existing workloads and provides a single location for configuring the solution, such as adding users and importing new Regions. It is also easier to track the costs incurred while running the solution.

After Workload Discovery on AWS is deployed, you can then import Regions from any accounts you already provisioned.
