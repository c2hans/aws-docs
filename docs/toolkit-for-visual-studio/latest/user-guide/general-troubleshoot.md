---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/general-troubleshoot.html
---

# Troubleshooting the AWS Toolkit for Visual Studio
<a name="general-troubleshoot"></a>

The following sections contain general troubleshooting information about the AWS Toolkit for Visual Studio and working with AWS services from the toolkit.

**Note**
Installation and set-up-specific troubleshooting information is available in the [Troubleshooting installation issues](https://docs.aws.amazon.com//toolkit-for-visual-studio/latest/user-guide/setup-troubleshoot.html) topic, located in this User Guide.

**Topics**
+ [Troubleshooting best practices](#general-troubleshoot-best-practice)
+ [Viewing and filtering Amazon Q security scans](#general-troubleshoot-Q-securityscan)
+ [The AWS Toolkit isn't properly installed](#general-troubleshoot-component-initilization)
+ [Firewall and proxy settings](#general-troubleshoot-firewall)

## Troubleshooting best practices
<a name="general-troubleshoot-best-practice"></a>

The following are recommended best practices when troubleshooting AWS Toolkit for Visual Studio issues.
+ Repair Visual Studio and restart your system
+ Attempt to recreate your issue or error prior to sending a report.
+ Take detailed notes of each step, setting, and error message during the recreation process.
+ Collect AWS Toolkit Logs. For a detailed description of how to locate your AWS Toolkit logs, see the [How to locate your AWS logs](#general-troubleshoot-procedure-logs) procedure, located in this guide topic.
+ Check for open requests, known solutions, or report your unresolved issue in the [AWS Toolkit for Visual Studio Issues](https://github.com/aws/aws-toolkit-visual-studio/issues) section of the AWS Toolkit for Visual Studio GitHub repository.

**Repair Visual Studio and Restart your system**

1. Close all running instances of Visual Studio.

1. From the Windows start menu, Launch **Visual Studio Installer**.

1. Run Repair on the affected installation(s) of Visual Studio. This allows Visual Studio to rebuild its index of installed extensions.

1. Restart Windows prior to re-launching Visual Studio.

**How to locate your AWS Toolkit logs**

1. From the Visual Studio main menu, expand **Extensions**.

1. Choose the **AWS Toolkit** to expand the AWS Toolkit menu, then choose **View Toolkit Logs**.

1. When the AWS Toolkit logs folder opens in your Operating System, sort the files by date and locate any log file that contains information relevant to your current issue.

## Viewing and filtering Amazon Q security scans
<a name="general-troubleshoot-Q-securityscan"></a>

To view your Amazon Q security scans in Visual Studio, open the Visual Studio **Error List** by expanding the **View** heading in the Visual Studio main menu and choosing **Error List**.

By default, the Visual Studio **Error List** displays all of the warnings and errors for your code base. To filter your Amazon Q security scan findings from the Visual Studio **Error List**, create a filter by completing the following procedure.

**Note**
Amazon Q security scan findings are only visible after security scan has run and detected issues.
Amazon Q security scan findings appear as warnings in Visual Studio. In order to view Amazon Q security scan findings from your **Error List**, the **Warnings** option in the **Error List** heading must be selected.

1. From the Visual Studio main menu, expand the **View** heading and choose **Error List** to open the **Error List** pane.

1. From the **Error List** pane, right-click the header row to open the context menu.

1. From the context menu, expand **Show Columns**, then select **Tool** in the expanded menu.

1. The **Tool** column is added to your **Error List**.

1. From the **Tool** column header, select the **Filter** icon and choose Amazon Q to filter for Amazon Q security scan findings.

## The AWS Toolkit isn't properly installed
<a name="general-troubleshoot-component-initilization"></a>

**Issue:**

Within one minute after starting Visual Studio, the AWS Toolkit for Visual Studio the following messages appear in the output pane and info bar, respectively:

`Some Toolkit components could not be initialized. Some functionality may not work during this IDE session.`

`The AWS Toolkit is not properly installed.`

**Solution:**

It's possible that updating or installing an extension caused some of Visual Studio's internal cache files to go out-of-sync. The following procedure describes how to have these files rebuilt the next time that you launch Visual Studio.

**Note**
It's possible that this solution may impact your Visual Studio customizations. After completing this procedure, the AWS Toolkit extension should be listed as installed and no longer report an error message. If you continue to experience this issue after completing the following steps, please see [Issue \#452](https://github.com/aws/aws-toolkit-visual-studio/issues/452) in the AWS Toolkit for Visual Studio GitHub repository for additional information.

1. Install the latest version of Visual Studio 2022.
**Note**
The minimum required version is 17.11.5.

1. Close all running instances of Visual Studio.

1. From Windows, open the **Developer Command Prompt** as an Administrator.

1. From the **Developer Command Prompt**, run the following command: `devenv /updateconfiguration /resetExtensions`, then wait for the command to finish.

1. After the command has finished, restart Visual Studio.

1. In Visual Studio the AWS extension is now listed as installed and no longer reports the error messages listed at the top of this issue.

## Firewall and proxy settings
<a name="general-troubleshoot-firewall"></a>

### Troubleshooting firewall and proxy settings
<a name="w2aac19c15b3"></a>

Security-scanning software can interfere with your ability to download files from AWS Toolkit language servers by removing files from downloads or preventing downloads altogether.

To check your firewall and proxy settings, navigate to [https://aws-toolkit-language-servers.amazonaws.com/codewhisperer/0/manifest.json](https://aws-toolkit-language-servers.amazonaws.com/codewhisperer/0/manifest.json) from an internet browser installed on the same system as your instance of Visual Studio. If you encounter an error or the page is unable to load, then there may be a firewall or proxy filter preventing you from reaching `aws-toolkit-language-servers.amazonaws.com`.

### Custom certificates
<a name="w2aac19c15b5"></a>

The AWS Toolkit for Visual Studio utilizes a language server that runs on the Node.js runtime. For detailed information about how to check if your network uses a custom certificate, see the [Configuration and credential file setting in the AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html#cli-config-ca_bundle) topic in the *AWS Command Line Interface* User Guide for Version 1.

To configure your proxy settings and define a certificate, you must configure your `HTTPS_PROXY` env variable and create Windows Environment Variables for the `NODE_OPTIONS` and `NODE_EXTRA_CA_CERTS` keys.

To configure your `HTTPS_PROXY` env variable, complete the following steps.

1. From the Visual Studio main menu, choose **Tools**, then choose **Options**.

1. From the **Options** menu, expand **AWS Toolkit**, then choose **Proxy**.

1. From the **Proxy** menu, define your **Host** and **Port**.

**Note**
For information about configuring the `HTTPS_PROXY` from the AWS CLI, see the [Using an HTTP proxy for the AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-proxy.html) topic in the *AWS Command Line Interface* User Guide.

Create Windows Environment Variables for the following keys.
+ `NODE_OPTIONS = --use-openssl-ca`
+ `NODE_EXTRA_CA_CERTS = Path/To/Corporate/Certs`

**Note**
For more information about extracting corporate root certificates, see the [Export a certificate with its private key](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/export-certificate-private-key) article at *learn.microsoft.com*. For detailed information about the Windows Environment Variable keys, see the [Node.js v23.3.0 documentation](https://nodejs.org/api/cli.html#cli_node_extra_ca_certs_file) at *nodejs.org*.

### Allow listing and additional steps
<a name="general-troubleshoot-errors"></a>

In addition to interfering with AWS Toolkit language servers, firewall settings can prevent Amazon Q from uploading to Amazon S3 and calling the service API. To minimize the potential of these errors, we recommend allowing outbound internet access on **port 443 (HTTPS)** for the following endpoints:
+ `https://codewhisperer.us-east-1.amazonaws.com/`
+ `https://amazonq-code-transformation-us-east-1-c6160f047e0.s3.amazonaws.com/`
+ `https://aws-toolkit-language-servers.amazonaws.com/`
+ `https://q.us-east-1.amazonaws.com`
+ `https://client-telemetry.us-east-1.amazonaws.com`
+ `https://cognito-identity.us-east-1.amazonaws.com`
+ `https://oidc.us-east-1.amazonaws.com`

For a detailed list of endpoints, see the [Updating firewalls and gateways to allow access](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/endpoints.html) topic in this User Guide. For detailed information about configuring a corporate proxy for Amazon Q, see the [Configuring a corporate proxy in Amazon Q](https://docs.aws.amazon.com//amazonq/latest/qdeveloper-ug/firewall.html#corp-proxy) topic in the *Amazon Q Developer User Guide*. If you continue to encounter firewall and proxy issues, then collect your AWS Toolkit Logs and reach out to the AWS Toolkit for Visual Studio team through the [AWS Toolkit for Visual Studio issues](https://github.com/aws/aws-toolkit-visual-studio/issues) section of the AWS Toolkit for Visual Studio GitHub repository. For details on collecting your AWS Toolkit Logs, review the information in the **Troubleshooting best practices** section of this User Guide topic.
