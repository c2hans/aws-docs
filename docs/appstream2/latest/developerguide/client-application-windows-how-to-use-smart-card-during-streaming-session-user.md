---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-how-to-use-smart-card-during-streaming-session-user.html
---

# How to Use a Smart Card During a Streaming Session
<a name="client-application-windows-how-to-use-smart-card-during-streaming-session-user"></a>

Depending on the authentication settings that your administrator has enabled, you might need to use a smart card for authentication during an WorkSpaces Applications streaming session. For example, if you open a browser during your streaming session and navigate to an internal organizational site that requires smart card authentication, you must enter your smart card credentials.

By default, smart card redirection is enabled for WorkSpaces Applications streaming sessions, which means that you can use the smart card reader that is attached to your local computer without sharing it with WorkSpaces Applications. During your streaming session, your smart card reader and smart card are available for you to use with local applications, as well as with streaming applications.

If your administrator has disabled smart card redirection, you must share your smart card reader with WorkSpaces Applications. For more information, see the next section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
