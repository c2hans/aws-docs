---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/confirm-cost-tags-associated-with-the-solution.html
---

# Confirm cost tags associated with the solution
<a name="confirm-cost-tags-associated-with-the-solution"></a>

After you activate cost allocation tags associated with the solution, you must confirm the cost allocation tags to see the costs for this solution. To confirm cost allocation tags:

1. Sign in to the [Systems Manager console](https://console.aws.amazon.com/systems-manager).

1. In the navigation pane, choose **Application Manager**.

1. In **Applications**, choose the application name for this solution and select it.

   The application name will have **App Registry** in the **Application Source** column, and will have a combination of the solution name, Region, account ID, or stack name.

1. In the **Overview** tab, in **Cost**, select **Add user tag**.

    **Screenshot depicting the Application Cost add user tag screen**
![AppManager 1](http://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/images/AppManager_1.png)

1. On the **Add user tag** page, enter `confirm`, then select **Add user tag**.

The activation process can take up to 24 hours to complete and the tag data to appear.
