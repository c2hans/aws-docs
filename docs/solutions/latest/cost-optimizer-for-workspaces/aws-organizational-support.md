---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/aws-organizational-support.html
---

# AWS Organizations support
<a name="aws-organizational-support"></a>

The solution supports AWS Organizations through a hub-and-spoke architecture. To monitor WorkSpaces across multiple accounts in your organization, allow trusted access for[AWS Resource Access Manager](https://aws.amazon.com/ram/) (AWS RAM) in the management account of your Organization. For more information on how to allow trusted access for RAM, refer to [AWS Resource Access Manager and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ram.html).

You can deploy the hub template in the central account, and then deploy the spoke template in each account that manages WorkSpaces. The spoke stacks must be deployed in the same Region as the hub stack.

For a multi-account deployment, provide the value for the **Organization ID for multi account deployment** and **Account ID of the Management Account for the Organization** input parameters. For a single-account deployment, or to manage WorkSpaces only in the central account, deploy only the hub template and leave the default value for the input parameters **Organization ID for multi account deployment** and **Account ID of the Management Account for the Organization**.
