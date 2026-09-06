---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/troubleshoot.html
---

# Troubleshooting the AWS Toolkit for JetBrains
<a name="troubleshoot"></a>

The following sections contain general troubleshooting information about the AWS Toolkit for JetBrains.

**Topics**
+ [Troubleshooting best practices](#general-troubleshoot-best-practice)
+ [Unable to sign out of AWS IAM Identity Center](#signout-error)
+ [Amazon Q Developer is unavailable for JetBrains 2023.2.0 releases](#qunavail-error)
+ [Amazon Q Developer Code Transformation fails to start at sign in](#qauthentication-error)

## Troubleshooting best practices
<a name="general-troubleshoot-best-practice"></a>

The following are recommended best practices when troubleshooting AWS Toolkit for JetBrains issues.
+ Attempt to recreate your issue or error prior to sending a report.
+ Take detailed notes of each step, setting, and error message during the recreation process.
+ Collect AWS Toolkit Logs. For a detailed description of how to locate your AWS Toolkit logs, see the [How to locate your AWS logs](#general-troubleshoot-procedure-logs) procedure, located in this guide topic.
+ Check for open requests, known solutions, or report your unresolved issue in the [AWS Toolkit for JetBrains Issues](https://github.com/aws/aws-toolkit-jetbrains/issues/new/choose) section of the AWS Toolkit for JetBrains GitHub repository.

**How to locate your AWS Toolkit logs**

1. From the JetBrains main menu, expand **Help**.

1. Choose **Show Log in Explorer** to view the location of the current log file on your hard drive.

1. Copy this log file and include it when creating a new AWS Toolkit for JetBrains issue or request.

## Unable to sign out of AWS IAM Identity Center
<a name="signout-error"></a>

If you're unable to sign out of your IAM Identity Center credentials after choosing **Sign Out** from the **AWS Connection Settings** menu, and the **expired or invalid** notification is still visible, completing the following steps.

**Clearing your IAM Identity Center cache file**

1. From your operating system, locate the IAM Identity Center cache file. The default location for the cache file is: `.aws/sso/cache`.

1. Delete the contents in your cache folder.

1. Restart your JetBrains IDE.

1. You're signed out of your IAM Identity Center credentials.

## Amazon Q Developer is unavailable for JetBrains 2023.2.0 releases
<a name="qunavail-error"></a>

Amazon Q Developer is unavailable for JetBrains 2023.2.0 releases. This is due to a specific issue with the 2023.2.0 release of JetBrains IDEs. For additional information about this issue, see [Issue JBR-5850](https://youtrack.jetbrains.com/issue/JBR-5850) in JetBrains issue tracking.

To address this issue, install a later release of JetBrains (2023.2.1 or newer).

## Amazon Q Developer Code Transformation fails to start at sign in
<a name="qauthentication-error"></a>

If Amazon Q Developer Code Transformation fails to start at sign in and you receive the following error message (see image below), you need to re-authenticate your credentials. Re-authenticate, then initiate Amazon Q Developer Code Transformation.

![Transform failed error message indicating user is not authorized to make this call.](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/amazonqtransformfail2023.png)
