---
source_url: https://docs.aws.amazon.com/dcv/latest/extsdkguide/install-register-extension.html
---

# Installing and registering the extension
<a name="install-register-extension"></a>

Amazon DCV does not determine where extension executables should be located. However, to ensure that file system ACLs protect extensions from unauthorized modification, it is best to follow the guidelines for your specific operating system. On Windows, for instance, use the `Program Files` folder.

## Registering the extension on Windows
<a name="register-extension-windows"></a>

 On Windows, manifest files can be placed in any directory, including the same directory as extension executables. Add the string value to the registry key outlined below to register the extension. If the key does not exist, create it. If you remove the extension, do not delete the key, since this may break other third-party extensions. Value names must contain the name of the extension, and value data must contain the path to the manifest file.

 On the client side, extensions could be registered per user or per machine. On the server side, extensions are registered only per-machine.

The per-machine key is `HKEY_LOCAL_MACHINE\SOFTWARE\Amazon\DCV Extensions`

The per-user key is `HKEY_CURRENT_USER\SOFTWARE\Amazon\DCV Extensions`

![Registry Editor showing DCV Extensions key with three extension entries and their manifest file paths.](http://docs.aws.amazon.com/dcv/latest/extsdkguide/images/register-ext.jpg)

## Registering the extension on Linux
<a name="register-extension-linux"></a>

You can register the extension by placing the `.json` manifest in the folder outlined below. If the folder does not exist, create it. If you remove an extension, you should not remove the folder or any files in it, since that may break other extensions. The manifest file name must be unique to the extension.

On the client side, extensions could be registered per user or per machine. On the server side, extensions are registered only per-machine

The per-machine folder is: `/usr/share/dcvextensions/`

The per-user folder is: `~/.local/share/dcvextensions`

## Registering the extension on macOS
<a name="register-extenstion-macos"></a>

You can register the extension by placing the `.json` manifest in the folder outlined below. If the folder does not exist, create it. If you remove an extension, you should not remove the folder or any files in it, since that may break other extensions. The manifest file name must be unique to the extension.

On the client side, extensions could be registered per user or per machine. On the server side, extensions are registered only per-machine

The per-machine folder is: `/Library/DCV Extensions/`

The per-user folder is: `Library/DCV Extensions/`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
