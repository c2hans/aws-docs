---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-android-tracking-resources.html
---

# Tutorial: Create Amazon Location resources for your app
<a name="qs-android-tracking-resources"></a>

To begin you will need to create the required Amazon Location resources. These resources will be essential for the functionality of the application and executing the provided code snippets.

**Note**
If you haven't created an AWS account, follow the instructions in the [AWS account managment](https://docs.aws.amazon.com/accounts/latest/reference/welcome-first-time-user.html) user guide.

To begin you will need to create a Amazon Cognito Identity Pool Id, use the following procedure:

1. Open the [Amazon Cognito console](https://console.aws.amazon.com/cognito/v2/) and select **Identity pools** from the left side menu, then select **Create Identity pool**.

1. Make sure **Guest Access** is checked, and press **Next** to contiue.

1. Next create a new IAM role or Use an existing IAM role.

1. Enter an Identity pool name, and make sure Identity Pool has access to Amazon Location `(geo)`resources for the map and tracker you will be creating nin the next procedure.

Next you need to create and style a map in the AWS Amazon Location console, use the following procedure:

1. Navigate to the [Maps section](https://console.aws.amazon.com/location/maps/home) of the Amazon Location console and select **Create Map**.

1. Give the new map a **Name** and **Description**. Record the name you assign, as it is used later in the tutorial.

1. When choosing a map style, consider the map data provider. Refer to section 82 of the [AWS service terms](http://aws.amazon.com/service-terms) for more details.

1. Accept the [Amazon Location Terms and Conditions](https://aws.amazon.com/service-terms/#:~:text=82.%20Amazon%20Location%20Service), then select **Create Map**, to finish the map creation process.

Next you need to create a tracker in the Amazon Location console, use the following procedure:

1.  Open the [Maps section](https://console.aws.amazon.com/location/trackers) in the Amazon Location console.

1. Choose **Create tracker**.

1. Fill in the required fields. Make note of the tracker's **Name** as it will be refrenced throughout this tutoiral.

1. Under the **Position filtering** field, choose the option that best fits how you intend to use your tracker resource. If you do not set Position filtering, the default setting is `TimeBased`. For more information, see [Trackers](), and [PositionFiltering]() in the Amazon Location API Reference.

1.  Choose **Create tracker** to finish creating the tracker.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
