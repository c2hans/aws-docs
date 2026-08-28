---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/as-delete-sensorposition.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Deleting a sensor position
<a name="as-delete-sensorposition"></a>

Deleting a sensor position removes that data collection point from the asset. If a sensor is still paired to this position, you need to remove it before you can delete the position.

**Topics**
+ [To delete a sensor position in the mobile app](#delete-sensorposition-mobile)
+ [To delete a sensor position in the web app](#delete-sensorposition-web)

## To delete a sensor position in the mobile app
<a name="delete-sensorposition-mobile"></a>

1. From the **Assets** list, choose the asset that has the sensor position that you want to delete.

1. Under **Sensors**, choose **Actions**.

1. Choose **Delete position**.

1. If the position has a sensor paired to it, delete the sensor by choosing **Delete sensor**. Otherwise, skip to the next step.
![Dialog box for deleting "Pump sensor 2" position with warning and Delete sensor button.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/position-sensor-delete.png)

1. Choose **Delete**.

## To delete a sensor position in the web app
<a name="delete-sensorposition-web"></a>

1. Select the position.

1. Choose the **Actions** button in the **Positions** table.

1. Choose **Delete position**.

1. If the position has a sensor paired to it, delete the sensor by choosing **Delete sensor**. Otherwise, skip to the next step.
![Dialog box for deleting "Pump sensor 2" position with warning and Delete sensor button.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/position-sensor-delete.png)

1. Choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
