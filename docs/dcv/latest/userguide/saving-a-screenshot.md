---
source_url: https://docs.aws.amazon.com/dcv/latest/userguide/saving-a-screenshot.html
---

# Saving a screenshot
<a name="saving-a-screenshot"></a>

You can use Amazon DCV to save a screenshot of the Amazon DCV session. This functionality is available on the Windows, web browser, Linux, and macOS clients. The steps for saving a screenshot are similar on all clients.

You must be authorized to use this feature. If you aren't authorized, the functionality isn't available in the client. For more information, see [ Configuring Amazon DCV Authorization](https://docs.aws.amazon.com/dcv/latest/adminguide/security-authorization.html) in the *Amazon DCV Administrator Guide*. If you aren't authorized to save screenshots, the client also avoids the external tools that are running on your client computer to capture a screenshot of the Amazon DCV client. Images that are obtained by these tools either show a black rectangle instead of the Amazon DCV client window or only show the background desktop. This functionality is available only on Windows and macOS clients.

**To save a screenshot**

1. Launch the client, and connect to the Amazon DCV session.

1. In the client, choose **Session**, **Save a Screenshot**.
![Save a screenshot option that's located on the native client toolbar.](http://docs.aws.amazon.com/dcv/latest/userguide/images/screenshot.png)

1. Choose a location and the name for the screenshot file.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
