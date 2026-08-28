---
source_url: https://docs.aws.amazon.com/dcv/latest/userguide/client-mac.html
---

# macOS client
<a name="client-mac"></a>

The Amazon DCV macOS client is supported on Apple Mac computers only. The macOS client is a standalone application that runs on the macOS operating system.

The macOS client is installed using a `.dmg` software package.

For instructions on how to connect to a Amazon DCV session using the macOS client, see [Connecting to a Amazon DCV session using the macOS client](using-connecting-mac.md).

**To install the macOS client**

1. Download the correct macOS client installer depending on your client computer.
   + [macOS client for Intel processors](https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Clients/nice-dcv-viewer-2025.0.8846.x86_64.dmg)
   + [macOS clients for Apple M1 processors](https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Clients/nice-dcv-viewer-2025.0.8846.arm64.dmg)
**Tip**
The [latest packages](http://download.amazondcv.com/latest.html) page of the download website contains links that always point to the newest available version. You can use these links to automatically retrieve the newest Amazon DCV packages.

1. Run the downloaded `.dmg` file.

   If you get an error stating that the application can't be installed because it's from an unidentified developer, see the [Safely open apps on your Mac](https://support.apple.com/en-ie/HT202491) webpage.

1. Click and drag the `DCV.app` file to the **Applications** folder.

1. (Optional) For easy access, create a desktop shortcut or add the application to the dock.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
