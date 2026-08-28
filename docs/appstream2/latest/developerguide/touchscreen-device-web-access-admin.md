---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/touchscreen-device-web-access-admin.html
---

# Touchscreen Device Support
<a name="touchscreen-device-web-access-admin"></a>

WorkSpaces Applications supports gestures on touch-enabled iPads, Android tablets, and Windows devices. All touch events are passed through to the streaming session and handled according to Windows conventions. Examples of supported touch gestures include long-tap to right-click, swipe to scroll, pinch to zoom, and two-finger rotation for supporting applications.

**Note**
To enable support for gestures on touch-enabled devices, your WorkSpaces Applications image must use a version of the WorkSpaces Applications agent released on or after March 7, 2019. For more information, see [WorkSpaces Applications Agent Release Notes](agent-software-versions.md).

For guidance that you can provide your users to help them get started with touch-enabled devices during their WorkSpaces Applications streaming sessions, see [Touchscreen Devices](web-browser-using-touchscreen-devices-user.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
