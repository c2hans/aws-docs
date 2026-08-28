---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/view-network-instance.html
---

# View a network instance in AWS TNB
<a name="view-network-instance"></a>

Learn how to view a network instance.

------
#### [ Console ]

**To view a network instance using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Network instances**.

1. Use the search box to find the network instance.

------
#### [ AWS CLI ]

**To view a network instance using the AWS CLI**

1. Use the [list-sol-network-instances](https://docs.aws.amazon.com/cli/latest/reference/tnb/list-sol-network-instances.html) command to list your network instances.

   ```
   aws tnb list-sol-network-instances
   ```

1. Use the [get-sol-network-instance](https://docs.aws.amazon.com/cli/latest/reference/tnb/get-sol-network-instance.html) command to view details about a specific network instance.

   ```
   aws tnb get-sol-network-instance --ns-instance-id {{^ni-[a-f0-9]{17}$}}
   ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
