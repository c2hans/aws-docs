---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-relative-mouse-offset-user.html
---

# Relative Mouse Offset
<a name="client-application-windows-relative-mouse-offset-user"></a>

By default, during a streaming session, WorkSpaces Applications transmits information about mouse movements by using absolute coordinates and rendering the mouse movements locally. For graphics-intensive applications, such as computer-aided design (CAD)/computer-aided manufacturing (CAM) software or video games, mouse performance improves when relative mouse mode is enabled. Relative mouse mode uses relative coordinates, which represent how far the mouse moved since the last frame, rather than the absolute x-y coordinate values within a window or screen. When you enable relative mouse mode, WorkSpaces Applications renders the mouse movements remotely.

You can enable this feature during an WorkSpaces Applications streaming session in either of the following ways:
+ Pressing Ctrl\+Shift\+F8
+ Choosing **Relative Mouse Position [Ctrl\+Shift\+F8]** from the **Settings **menu on the WorkSpaces Applications toolbar in the top left area of your streaming session window. This method works when you use classic mode or **Desktop View**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
