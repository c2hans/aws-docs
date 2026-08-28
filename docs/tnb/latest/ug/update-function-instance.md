---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/update-function-instance.html
---

# Update a function instance in AWS TNB
<a name="update-function-instance"></a>

After a network instance is instantiated, you can update a function package in the network instance.

------
#### [ Console ]

**To update a function instance using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Networks**.

1. Select the network instance. You can update a network instance only if its state is `Instantiated`.

   The network instance page appears.

1. From the **Functions** tab, select the function instance to update.

1. Choose **Update**.

1. Enter your update overrides.

1. Choose **Update**.

------
#### [ AWS CLI ]

**Use the CLI to update a function instance**
Use the [update-sol-network-instance](https://docs.aws.amazon.com/cli/latest/reference/tnb/update-sol-network-instance.html) command with the `MODIFY_VNF_INFORMATION` update type to update a function instance in a network instance.

```
aws tnb update-sol-network-instance --ns-instance-id {{^ni-[a-f0-9]{17}$}} --update-type MODIFY_VNF_INFORMATION --modify-vnf-info ...
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
