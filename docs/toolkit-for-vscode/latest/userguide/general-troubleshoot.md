---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/general-troubleshoot.html
---

# Troubleshooting the AWS Toolkit for Visual Studio Code
<a name="general-troubleshoot"></a>

The following sections contain general troubleshooting information about the AWS Toolkit for Visual Studio Code and working with AWS services from the toolkit. For issues specifically related to troubleshooting SAM issues in the AWS Toolkit, see the [Troubleshooting serverless applications](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/serverless-apps-troubleshooting.html) topic in this User Guide.

**Topics**
+ [Troubleshooting best practices](#general-troubleshoot-best-practice)
+ [Profile ... could not be found in the config file](#general-troubleshoot-profile-not-found)
+ [SAM json schema: cannot change schema in template.yaml file](#general-troubleshoot-sam-json-template-yaml)

## Troubleshooting best practices
<a name="general-troubleshoot-best-practice"></a>

The following are recommended best practices when troubleshooting AWS Toolkit for Visual Studio Code issues. For detailed information about how you can contribute to the AWS Toolkit for Visual Studio Code, see the [Contributing to AWS Toolkit for Visual Studio Code](https://github.com/aws/aws-toolkit-vscode/blob/master/CONTRIBUTING.md) topic in the AWS Toolkit for Visual Studio Code GitHub repository.
+ Attempt to recreate your issue or error prior to sending a report.
+ Take detailed notes of each step, setting, and error message during the recreation process.
+ Collect your AWS Toolkit Debug Logs. For a detailed description of how to locate your AWS Toolkit Debug logs, see the *How to locate your AWS logs* procedure, located in this user guide topic.
+ Check for open requests, known solutions, or report your unresolved issue in the [AWS Toolkit for Visual Studio Code Issues](https://github.com/aws/aws-toolkit-vscode/issues) section of the AWS Toolkit for Visual Studio Code GitHub repository.

**Note**
The following procedure describes how to view your AWS Toolkit Debug logs. The process to view your Amazon Q Debug logs is identical except you choose **Amazon Q: View Logs** from the VS Code Command Palette.

**How to locate your AWS Toolkit for Visual Studio Code Debug logs**

1. From the VS Code open the Command Palette by pressing **Cmd \+ Shift \+ P** or **Ctrl \+ Shift \+ P** (Windows) and enter **AWS View Logs** into the search field.

1. Choose **AWS View Logs** to open your AWS Toolkit logs in the **VS Code terminal output** window.

1. From the **VS Code terminal output** window, expand the **Gear** icon menu and choose **Debug**.

1. Expand the **Gear** icon menu again and choose **Set As Default**.

1. Re-open the Command Palette by pressing **Cmd \+ Shift \+ P** or **Ctrl \+ Shift \+ P** (Windows) and search for **Reload Window**, then choose **Developer: Reload Window**.

1. VS Code reloads and the **VS Code terminal output** window displays your updated AWS Toolkit Debug logs.

## Profile ... could not be found in the config file
<a name="general-troubleshoot-profile-not-found"></a>

**Issue**

**Note**
This issue only applies to the `~/.aws/config` file and not the `~/.aws/credentials` file. For detailed information about AWS config and AWS credentials files, see the [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) topic in the *AWS SDK and Tools* reference guide.

When choosing credentials AWS Toolkit logs display a message with this structure: `Profile name could not be found in shared credentials file`.

The following is an example of what this error looks like in your AWS Toolkit logs:

```
         2023-08-08 18:20:45 [ERROR]: _aws.auth.reauthenticate: Error: Unable to authenticate connection
         -> CredentialsProviderError: Profile vscode-prod-readonly could not be found in shared credentials file.
```

**Solution**

If your profile already exists in `~/.aws/config`, check that it starts with `[profile `. The following is an example of a user profile that is structured **correctly**:

```
         [profile example]
         region=us-west-2
         credential_process=...
```

The following is an example of a user profile that is structured **incorrectly**:

```
         [example]
         region=us-west-2
         credential_process=...
```

## SAM json schema: cannot change schema in template.yaml file
<a name="general-troubleshoot-sam-json-template-yaml"></a>

**Issue**

You are unable to manually select a different json schema in SAM template.yaml

**Solution**

After updating to vscode-yaml version 1.11\+, you can add a **yaml-language-server** modeline to the top of a YAML file to force the use of a schema by URI. For additional information about [Using inlined schema](https://github.com/redhat-developer/yaml-language-server#using-inlined-schema) section in the *yaml language server* topic of the *Redhat developer* GitHub repository. The following is an example of a **yaml-language-server** modeline.

```
         # yaml-language-server: $schema=https://raw.githubusercontent.com/aws/serverless-application-model/main/samtranslator/schema/schema.json
```
