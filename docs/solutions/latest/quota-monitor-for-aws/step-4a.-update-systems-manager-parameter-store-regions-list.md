---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-4a.-update-systems-manager-parameter-store-regions-list.html
---

# Step 4a. Update Systems Manager Parameter Store (Regions List)
<a name="step-4a.-update-systems-manager-parameter-store-regions-list"></a>

Use the following procedure to update the Systems Manager Parameter Store with the list of AWS Regions where you want to deploy the spoke templates.

1. Open the [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Parameter Store**.

    **Parameter Store**
![parameterstore](https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/parameterstore.png)

--Or--

If the Systems Manager home page opens first, choose the menu icon (![Horizontal black and white striped pattern forming a simple geometric design.](https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/image4.png) ) to open the navigation pane, then choose **Parameter Store**.

 **My Parameters**

![myparameters](https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/myparameters.png)

1. On the **My parameters** tab, select the box next to the parameter to update.

1. Choose **Edit**. Update the **Value**. The value should be comma-separated with no spaces. For example, `/QuotaMonitor/RegionsToDeploy: us-east-1,us-east-2`. The default value is `ALL`.

1. Choose **Save changes**.
