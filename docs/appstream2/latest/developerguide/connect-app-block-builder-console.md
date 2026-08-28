---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/connect-app-block-builder-console.html
---

# Amazon WorkSpaces Applications Console (Browser Connection)
<a name="connect-app-block-builder-console"></a>

To use the WorkSpaces Applications console to connect to an app block builder through a browser, complete the following steps.

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home).

1. In the left navigation pane, choose **Applications Manager**, and then choose **App block builders**.

1. In the list of app block builders, choose the app block builder to which you want to connect. Verify that the status of the app block builder is **Running**, and choose **Connect**.

   For this step to work, you might need to configure your browser to allow pop-ups from https://stream.<aws-region>.amazonappstream.com/.

1. Start streaming the app block builder.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
