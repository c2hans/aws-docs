---
source_url: https://docs.aws.amazon.com/silk/latest/developerguide/version.html
---

# Determining the Amazon Silk build version
<a name="version"></a>

Each version of Amazon Silk includes a build version and a browser version. In some troubleshooting scenarios, you may need to know both the browser and build versions for a given Amazon Silk client. You can find these values from the Amazon Silk user agent string.

From the Silk browser, tap the menu icon. If you see this menu, you have the latest version of Silk. Use the following procedure to locate the build version and browser version. If your menu looks different, you may have an older version of Silk.

![Silk browser menu showing options such as Enter Private Browsing, Bookmarks, and Settings.](http://docs.aws.amazon.com/silk/latest/developerguide/images/Silk_shared-menu.png)

1. From the Silk menu, tap **Settings**, and then tap **About Silk**.

1. Locate the application number, which should look something like this: `44.1.54.2403.63.10`.

   In this example, the first set of numbers, `44.1.54`, is the browser version.

   The second set of numbers, `2403.63.10`, is the build version.

![About Silk screen showing Application version 44.1.54.2403.63.10.](http://docs.aws.amazon.com/silk/latest/developerguide/images/silk-shared-version.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Silk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query silk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
