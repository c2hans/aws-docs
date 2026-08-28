---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/view-network-operation.html
---

# View a AWS TNB network operation
<a name="view-network-operation"></a>

View the details of a network operation, including the tasks involved in the network operation and the status of the tasks.

------
#### [ Console ]

**To view a network operation using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Network instances**.

1. Use the search box to find the network instance.

1. On the **Deployments** tab, choose the network operation.

------
#### [ AWS CLI ]

**To view a network operation using the AWS CLI**

1. Use the [list-sol-network-operations](https://docs.aws.amazon.com/cli/latest/reference/tnb/list-sol-network-operations.html) command to list all network operations.

   ```
   aws tnb list-sol-network-operations
   ```

1. Use the [get-sol-network-operation](https://docs.aws.amazon.com/cli/latest/reference/tnb/get-sol-network-operation.html) command to view details about a network operation.

   ```
   aws tnb get-sol-network-operation --ns-lcm-op-occ-id {{^no-[a-f0-9]{17}$}}
   ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
