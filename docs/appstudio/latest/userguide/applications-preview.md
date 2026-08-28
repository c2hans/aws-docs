---
source_url: https://docs.aws.amazon.com/appstudio/latest/userguide/applications-preview.html
---

# Previewing applications
<a name="applications-preview"></a>

You can preview applications in App Studio to see how they will appear to users and also test its functionality by using it and checking logs in a debug panel.

The application preview environment does not support displaying live data or the connection with external resources with connectors, such as data sources. To test functionality in the preview environment, you can use mocked output in automations and sample data in entities. To view your application with real-time data, you must publish your app. For more information, see [Publishing applications](applications-publish.md).

The preview or development environment does not update the application published in the other environments. If an application has not been published, users will not be able to access it until it is published and shared. If an application has already been published and shared, users will still access the version that has been published, and not the version used in a preview environment.

**To preview your application**

1. If necessary, navigate to the application studio of the application you want to preview:

   1. In the navigation pane, choose **My applications** in the **Build** section.

   1. Choose **Edit** for the application.

1. Choose **Preview** to open the preview environment for the application.

1. (Optional) Expand the debug panel by choosing its header near the bottom of the screen. You can filter the panel by type of message by choosing the type of message in the **Filter logs** section. You can clear the panel's logs by choosing **Clear console**.

1. While in the preview environment, you can test your application by navigating around its pages, using its components, and choosing its buttons to start automations that transfer data. Because the preview environment doesn't support live data or connections to external sources, you can view examples of the data being transferred in the debug panel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstudio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
