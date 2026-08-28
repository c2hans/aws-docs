---
source_url: https://docs.aws.amazon.com/devicefarm/latest/developerguide/how-to-access-session-results.html
---

# Retrieving the results of a remote access session in AWS Device Farm
<a name="how-to-access-session-results"></a>

For information about sessions, see [Sessions](sessions.md).
+ [Prerequisites](#how-to-access-session-results-prerequisites)
+ [Viewing session details](#how-to-view-session-details)
+ [Downloading session video or logs](#how-to-access-session-files)

## Prerequisites
<a name="how-to-access-session-results-prerequisites"></a>
+ Complete a session. Follow the instructions in [Using a remote access session in AWS Device Farm](how-to-use-session.md), and then return to this page.

## Viewing session details
<a name="how-to-view-session-details"></a>

When a remote access session ends, the Device Farm console displays a table that contains details about activity during the session. For more information, see [Analyzing Log Information](how-to-use-reports.md#how-to-use-reports-console-log).

To return to the details of a session at a later time:

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. Choose the project containing the session.

1. Choose **Remote access**, and then choose the session you want to review from the list.

## Downloading session video or logs
<a name="how-to-access-session-files"></a>

When a remote access session ends, the Device Farm console provides access to a video capture of the session and activity logs. In the session results, choose the **Files** tab for a list of links to the session video and logs. You can view these files in the browser or save them locally.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
