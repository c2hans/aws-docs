---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/threatcomposer-overview.html
---

# Working with Threat Composer from the Toolkit
<a name="threatcomposer-overview"></a>

With Threat Composer you can create, view, and edit Threat Composer threat models directly in VS Code. For detailed information about the Threat Composer tool, see the [Threat Composer GitHub repository](https://github.com/awslabs/threat-composer#readme).

The following sections describe how to access Threat Composer tools in the AWS Toolkit for Visual Studio Code.

## Accessing Threat Composer from the Toolkit
<a name="threatcomposer-overview-access"></a>

There are 3 main ways that you can access Threat Composer from the Toolkit.

**Accessing Threat Composer through an existing threat model**

To open Threat Composer, open an existing threat-model file (extension `.tc.json`) in VS Code. Threat Composer automatically opens and renders a visualization of your threat-model file in the VS Code editor window.

**Creating a new Threat Composer threat model**

1. From the VS Code main menu, expand **File**, then choose **New File**.

1. From the **New File** dialog, choose **Threat Composer File...**.

1. When prompted, enter a `file name`, then press the **enter** key to open Threat Composer and create a visualization of your empty threat-model file in a new VS Code editor window.

**Creating a new Threat Composer threat model from the Command Palette**

1. From VS Code, open the Command Palette by pressing **Cmd \+ Shift \+ P** or **Ctrl \+ Shift \+ P** (Windows).

1. In the search field, enter **Threat Composer** and choose **Create New Threat Composer File** when it populates in the results.

1. When prompted, enter a `file name`, then press the **enter** key to open Threat Composer and create a visualization of your empty threat-model file in a new VS Code editor window.
