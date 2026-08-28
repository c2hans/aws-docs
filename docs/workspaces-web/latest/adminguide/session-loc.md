---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/session-loc.html
---

# Configuring in-session localization for Amazon WorkSpaces Secure Browser
<a name="session-loc"></a>

When a user starts a session, WorkSpaces Secure Browser detects the user’s local browser language and time zone settings and applies them to the session. This affects the display language during the session, and helps ensure that the displayed time matches the current time in the user's location.

The session language is determined in the following priority order:

1. The **ForcedLanguages** policy in the web portal’s browser settings. For more information, see [ForcedLanguages](https://chromeenterprise.google/policies/#ForcedLanguages).

1. The end user’s local browser language setting.

1. The default value, **English (en-US)**.

The time zone is determined by the local time zone settings specified in the end user's browser. If the time zone setting isn't valid, UTC is used.

The following components in WorkSpaces Secure Browser support localization:
+ WorkSpaces Secure Browser sign-in page
+ WorkSpaces Secure Browser portal status messages (including loading messages and errors)
+ Chrome browser
+ System **Context** menu and **Save as** window

**Topics**
+ [Supported language codes for Amazon WorkSpaces Secure Browser](language-codes.md)
+ [Selecting languages in user browser settings](local-browser-settings.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
