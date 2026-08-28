---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/connection-methods.html
---

# Connection methods
<a name="connection-methods"></a>

 When streaming sessions in WorkSpaces Applications, users have two connection methods available:
+  **Web Browser Access** — Any HTML5-capable browser is supported. No plug- ins or downloads are required.
+  **WorkSpaces Applications Windows Client**

 As a best practice, consider the feature and device requirements for your user’s use case to align which browser, or device, best supports their requirements.

**Note**
 WorkSpaces Applications is not supported on devices that have screen resolutions smaller than 1024 x 768 pixels.

## Summary feature and device support
<a name="summary-feature-and-device-support"></a>

 *Table 3 — Summary feature and device support*

|   |   **Web browser access**   |   **WorkSpaces Applications Windows Client**   |
| --- | --- | --- |
|  Multiple monitor (up to 2k resolution)  |  Supported  |  Supported  |
|  Multiple monitor (up to 4k resolution)  |  N/A  |  Supported  |
|  Drawing tablet support  |  Supported \*  |  Supported  |
|  Touchscreen device support  |  Supported  |  N/A  |
|  USB passthrough device support  |  N/A  |  Supported  |
|  Keyboard shortcuts  |  Supported  |  Supported  |
|  Relative mouse offset  |  Supported  |  Supported  |
|  File transfer  |  Supported  |  Supported  |
|  Local printer redirection  |  N/A  |  Supported  |
|  Local drive redirection  |  N/A  |  Supported  |
|  Web-cam support  |  Supported  |  Supported  |

 \*Google Chrome and Mozilla Firefox only

## Web browser access
<a name="web-browser-access"></a>

 WorkSpaces Applications [*web browser access*](https://docs.aws.amazon.com/appstream2/latest/developerguide/access-through-web-browser-admin.html) allows access to applications without the need to install a dedicated client. Users can connect using a supported HTML5-capable browser. There is no requirement for any browser plugin or extension.

 Web browser access provides for a wide choice of end device operating systems and types.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
