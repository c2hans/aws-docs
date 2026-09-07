---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-4b.-update-systems-manager-parameter-store-ous.html
---

# Step 4b. Update Systems Manager Parameter Store (OUs)
<a name="step-4b.-update-systems-manager-parameter-store-ous"></a>

Follow these steps to update the Systems Manager Parameter Store for the AWS accounts (**Account-Ids**) and OUs (**OU-ids**) you want to monitor.

1. Open the [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Parameter Store**.

    **Parameter Store**
![parameterstore](https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/parameterstore.png)

--Or--

If the Systems Manager home page opens first, choose the menu icon (![Horizontal black and white striped pattern forming a simple geometric design.](https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/image4.png)) to open the navigation pane, then choose **Parameter Store**.

 **My Parameters**

![myparameters](https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/myparameters.png)

1. On the **My parameters** tab, select the box next to the parameter to update.

1. Choose **Edit**. Update the **Value**. The value should be comma-separated with no spaces For example, `/QuotaMonitor/OUs: ou-a1bc-d2efghij,ou-k1lm-n2opqrst`.

1. Choose **Save changes**.

1. Once you update the parameter, StackSets should start deploying solution templates in the targeted OUs or accounts. [Review StackSets operation and instances.](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stacksets-concepts-ops)
