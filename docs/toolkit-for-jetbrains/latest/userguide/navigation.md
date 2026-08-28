---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/navigation.html
---

# Navigating the AWS Toolkit for JetBrains
<a name="navigation"></a>

The following topics describe the basic locations and components of the AWS Toolkit for JetBrains.

**Topics**
+ [Viewing the toolkit from JetBrains](#w2aac13c15b7)
+ [The AWS Explorer](#w2aac13c15b9)
+ [Connecting to AWS](#w2aac13c15c11)

## Viewing the toolkit from JetBrains
<a name="w2aac13c15b7"></a>

To view the toolkit in your JetBrains IDE, complete the following steps:

1. From the JetBrains IDE, expand the **Active Toolbar** using the **Active Toolbar** icon located in the bottom left-hand corner of the JetBrains IDE.

1. From the **Active Toolbar** choose **AWS Toolkit**.

1. The AWS Toolkit for JetBrains is now open in the **Active Toolbar** window.

![IDE welcome screen showing keyboard shortcuts for Search Everywhere, Project View, Go to File, Recent Files, and Navigation Bar.](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/viewtoolkit2024.gif)

## The AWS Explorer
<a name="w2aac13c15b9"></a>

Your AWS services and resources are available through the AWS Toolkit for JetBrains Explorer.

**Note**
Your AWS services and resources are only visible from the AWS Explorer after you've set up authentication and connected to your AWS account.
For additional information about authentication and the AWS Toolkit for JetBrains, see the [Authentication and access](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/auth-access.html) table of contents in this User Guide.
For additional information about connecting to your AWS account from the AWS Toolkit for JetBrains, see the [Connecting to AWS](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/account-connect.html) topic in this User Guide.

To view your AWS services and resources from the AWS Toolkit for JetBrains Explorer:

1. From the AWS Toolkit for JetBrains choose the **Explorer** tab to view the AWS services associated with your account and region.

1. Select a service to expand a list of your resources.

1. Open the context menu for (right-click) a resource to see a list of features for modifying your resource.

![IntelliJ IDEA interface showing navigation shortcuts including Search Everywhere and Go to File.](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/awsexplorer2024.gif)

## Connecting to AWS
<a name="w2aac13c15c11"></a>

Your connection and authentication settings can be added or updated from the **AWS Toolkit Sign In** panel. The following procedure describes how to access the **AWS Toolkit Sign In** panel.

**Note**
If this is the first time that you're using the Toolkit or no credentials are detected on start up, then the **AWS Toolkit Sign In** pane automatically opens in the JetBrains editor.
For detailed instructions on how to connect to your AWS account from the AWS Toolkit for JetBrains, see the [Connect to AWS](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/account-connect.html) topic in this User Guide.

1. From the Toolkit, open **AWS Connection Settings** by choosing the **ellipses** icon in the connection pane.

1. From **AWS Connection Settings**, choose **Setup Authentication...** to open the **AWS Toolkit Sign In** pane.

1. From the **AWS Toolkit Sign In** panel, select your authentication method and follow the on-screen prompts.

The following is an image of the AWS Sign In panel.

![AWS Toolkit sign-in panel with Workforce and IAM Credential options and Continue button.](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/awssigninpane2024.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
