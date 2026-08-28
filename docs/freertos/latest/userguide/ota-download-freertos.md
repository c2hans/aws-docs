---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/ota-download-freertos.html
---

# Download FreeRTOS with the OTA library
<a name="ota-download-freertos"></a>

You can clone or download FreeRTOS from [GitHub](https://github.com/freertos/freertos). See the [README.md](https://github.com/freertos/freertos/blob/main/README.md) file for instructions.

For information about setting up and running the OTA demo application, see [Over-the-air updates demo application](ota-demo.md).

**Important**
In this topic, the path to the FreeRTOS download directory is referred to as `{{freertos}}`.
Space characters in the `{{freertos}}` path can cause build failures. When you clone or copy the repository, make sure the path you that create doesn't contain space characters.
The maximum length of a file path on Microsoft Windows is 260 characters. Long FreeRTOS download directory paths can cause build failures.
Because the source code may contain symbolic links, if you're using Windows to extract the archive, you may have to:
Enable [ Developer Mode](https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development) or,
Use a console that is elevated as administrator.
In this way, Windows can properly create symbolic links when it extracts the archive. Otherwise, symbolic links will be written as normal files that contain the paths of the symbolic links as text or are empty. For more information, see the blog entry [ Symlinks in Windows 10\!](https://blogs.windows.com/windowsdeveloper/2016/12/02/symlinks-windows-10/).
If you use Git under Windows, you must enable Developer Mode or you must:
Set `core.symlinks` to true with the following command:

    ```
    git config --global core.symlinks true
    ```
Use a console that is elevated as administrator whenever you use a git command that writes to the system (for example, **git pull**, **git clone**, and **git submodule update --init --recursive**).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
