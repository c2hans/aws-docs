---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-dev-env.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Installing and configuring your toolchain for the AWS SDK for .NET
<a name="net-dg-dev-env"></a>

To use the AWS SDK for .NET, you must have certain development tools installed.

## Developing cross-platform applications
<a name="net-dg-dev-env-cross"></a>

The following are required for cross-platform .NET development on Windows, Linux, or macOS:
+ The Microsoft [.NET SDK](https://learn.microsoft.com/en-us/dotnet/fundamentals/) for a version of .NET that the AWS SDK for .NET supports (see [Supported platforms](net-dg-supported-platforms.md)). The .NET SDK includes the .NET command line interface (CLI) (**`dotnet`**) and the .NET runtime.
+ A code editor or integrated development environment (IDE) that is appropriate for your operating system and requirements. This is typically one that provides some support for .NET.

  Examples include [Microsoft Visual Studio Code (VS Code)](https://code.visualstudio.com/), [JetBrains Rider](https://www.jetbrains.com/rider/), and [Microsoft Visual Studio](https://visualstudio.microsoft.com/vs/).
+ (Optional) An AWS toolkit if one is available for the editor you chose and your operating system.

  Examples include the [AWS Toolkit for Visual Studio Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html), [AWS Toolkit for JetBrains](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html), and [AWS Toolkit for Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html).

## Developing on Windows with Visual Studio and .NET
<a name="net-dg-dev-env-windows"></a>

The following are required for development on Windows with Visual Studio and .NET:
+ [Microsoft Visual Studio](https://visualstudio.microsoft.com/vs/)
+ The Microsoft .NET SDK for a version of .NET that the AWS SDK for .NET supports (see [Supported platforms](net-dg-supported-platforms.md))

  This is typically included by default when installing a recent version of Visual Studio.
+ (Optional) The AWS Toolkit for Visual Studio, which is a plugin that provides a user interface for managing your AWS resources and local profiles from Visual Studio. To install the toolkit, see [Setting up the AWS Toolkit for Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/getting-set-up.html).

  For more information, see the [AWS Toolkit for Visual Studio User Guide](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/).

## Next step
<a name="net-dg-dev-env-next"></a>

[Authenticating the AWS SDK for .NET with AWS](creds-idc.md)
