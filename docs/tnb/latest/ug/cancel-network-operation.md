---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/cancel-network-operation.html
---

# Cancel a AWS TNB network operation
<a name="cancel-network-operation"></a>

Learn how to cancel a network operation.

------
#### [ Console ]

**To cancel a network operation using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Networks**.

1. Select the ID of the network to open its details page.

1. On the **Deployments** tab, choose the Network Operation.

1. Choose **Cancel operation**.

------
#### [ AWS CLI ]

**To cancel a network operation using the AWS CLI**
Use the [cancel-sol-network-operation](https://docs.aws.amazon.com/cli/latest/reference/tnb/cancel-sol-network-operation.html) command to cancel a network operation.

```
aws tnb cancel-sol-network-operation --ns-lcm-op-occ-id {{^no-[a-f0-9]{17}$}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
