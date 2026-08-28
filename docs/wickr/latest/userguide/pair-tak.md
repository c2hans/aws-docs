---
source_url: https://docs.aws.amazon.com/wickr/latest/userguide/pair-tak.html
---

This guide provides documentation for AWS Wickr. For Wickr Enterprise, which is the on-premises version of Wickr, see [Enterprise Administration Guide](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/what-is-wickr.html).

# Pair ATAK with Wickr
<a name="pair-tak"></a>

You can pair the ATAK application with Wickr after you successfully installed the Wickr plugin for ATAK.

Complete the following procedure to pair the ATAK application with Wickr after you successfully installed the Wickr plugin for ATAK.

1. In the ATAK application, choose the menu icon ![Menu icon](http://docs.aws.amazon.com/wickr/latest/userguide/images/icon-wickr-settings-hamburger.png) at the top-right of the screen, and choose **Wickr Plugin**.

1. Choose **Pair Wickr**.
![Pair the Wickr client.](http://docs.aws.amazon.com/wickr/latest/userguide/images/atak_pair_wickr.png)

   A notification prompt will appear asking you to review permissions for the Wickr plugin for ATAK. If the notification prompt doesn't appear, open the Wickr client and go to **Settings**, then **Connected Apps**. You should see the plugin under the **Pending** section of the screen as shown in the following example.
![Pending connected applications in the Wickr client.](http://docs.aws.amazon.com/wickr/latest/userguide/images/atak_connected_apps_pending.png)

1. Choose **Approve** to pair.
![Connected apps approval screen.](http://docs.aws.amazon.com/wickr/latest/userguide/images/atak_connected_apps_pending_approve.png)

1. Choose **Open Wickr ATAK Plugin** button to go back to the ATAK application.
![Connected apps success screen.](http://docs.aws.amazon.com/wickr/latest/userguide/images/atak_connected_apps_success.png)

   You have now successfully paired the ATAK plugin and Wickr, and can use the plugin to send messages and collaborate using Wickr without exiting the ATAK application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
