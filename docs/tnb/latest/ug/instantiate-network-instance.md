---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/instantiate-network-instance.html
---

# Instantiate a network instance using AWS TNB
<a name="instantiate-network-instance"></a>

After you create a network instance, you must instantiate it. When you instantiate a network instance, AWS TNB provisions the necessary AWS infrastructure, deploys containerized network functions, and configures networking and access management to create a fully operational network service.

------
#### [ Console ]

**To instantiate a network instance using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Networks**.

1. Select the network instance that you want to instantiate.

1. Choose **Actions** and then **Instantiate**.

1. On the **Instantiate network** page, review details and optionally, update parameter values.

   Updates to the parameter values apply only to this network instance. The parameters in the NSD and VNFD packages do not change.

1. Choose **Instantiate network**.

   The **Deployment status** page appears.

1. Use the **Refresh** icon to track the deployment status of your network instance. You can also enable **Auto refresh** in the **Deployment tasks** section to track the progress of each task.

   When the deployment status changes to `Completed`, the network instance is instantiated.

------
#### [ AWS CLI ]

**To instantiate a network instance using the AWS CLI**

1. Use the [instantiate-sol-network-instance](https://docs.aws.amazon.com/cli/latest/reference/tnb/instantiate-sol-network-instance.html) command to instantiate the network instance.

   ```
   aws tnb instantiate-sol-network-instance --ns-instance-id {{^ni-[a-f0-9]{17}$}} --additional-params-for-ns "{\"{{param1}}\": \"{{value1}}\", \"{{param2}}\": \"{{value2}}\"}"
   ```

1. Next, view the network operation status.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
