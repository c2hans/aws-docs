---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/create-network-instance.html
---

# Create a network instance using AWS TNB
<a name="create-network-instance"></a>

You create a network instance after creating a network package. After you create a network instance, instantiate it.

------
#### [ Console ]

**To create a network instance using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Networks**.

1. Choose **Create network instance**.

1. Enter a name and description for the instance and then choose **Next**.

1. Select the network package, verify the details, and choose **Next**.

1. Choose **Create network instance**.

   The new network instance appears on the **Networks** page. Next, instantiate this network instance.

------
#### [ AWS CLI ]

**To create a network instance using the AWS CLI**
+ Use the [create-sol-network-instance](https://docs.aws.amazon.com/cli/latest/reference/tnb/create-sol-network-instance.html) command to create a network instance.

  ```
  aws tnb create-sol-network-instance --nsd-info-id {{^np-[a-f0-9]{17}$}} --ns-name "{{SampleNs}}" --ns-description "{{Sample}}"
  ```

Next, instantiate this network instance.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
