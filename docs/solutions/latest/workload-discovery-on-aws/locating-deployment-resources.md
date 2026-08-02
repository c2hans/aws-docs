---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/locating-deployment-resources.html
---

# Locating deployment resources
<a name="locating-deployment-resources"></a>

Follow these steps to locate resources that deployed into your account.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Select the Region you deployed the solution in.

   Depending on the usage of this account, it may contain multiple stacks for different workloads. There will be a main stack with the name provided during deployment and multiple nested stacks beneath it.

1. Select each stack to access the resources deployed using that template.

1. Select the **Resources** tab and choose the **Physical ID** link for the relevant resource to view the resource in its respective service console.

   If you know the **Logical ID** of a resource, you can also search using the search bar above the table.
