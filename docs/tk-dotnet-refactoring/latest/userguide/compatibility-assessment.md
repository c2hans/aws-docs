---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/compatibility-assessment.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Run a compatibility assessment
<a name="compatibility-assessment"></a>

After the extension is installed, you can run a compatibility assessment with Toolkit for .NET Refactoring to find Microsoft Windows dependencies and incompatibilities between your application and newer .NET Core versions. Perform the following steps to run the assessment:

1. In Microsoft Visual Studio, open a solution file and open a `.cs` file within the solution that you want to run the assessment on.

1. From the Visual Studio menu, open **Extensions** and select **AWS Toolkit for .NET Refactoring** from the drop-down menu. Select **Get Started**.

1. The first time that you run an assessment, the **Start modernization journey** tab opens. In the **Start modernization journey** tab, configure the following options:
   +  **AWS profile** – Select a named profile from the drop-down menu.
   + **Use existing AWS CLI / SDK credentials** – Select this option if you have temporary credentials. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*.
   + **Share my usage data** – Select this option to allow Toolkit for .NET Refactoring to collect usage data. For more information, see [Data collected](data-protection.md#dotnet-data-collected) in this guide.

1. From the **Getting Started** screen, you can choose the **Target Framework** version that you want to port your application to.

1. Click **Save** to save your settings.

1. Click **Next** to open the Toolkit for .NET Refactoring dashboard.

1. In the dashboard, click **Start assessment** to begin the assessment. Toolkit for .NET Refactoring runs a one-time, full assessment for the compatibility solution that is loaded in Visual Studio.

There is an **Error list** pane at the bottom of the window that displays the incompatibilities that Toolkit for .NET Refactoring discovered during the assessment. Select an entry in the list to view the incompatibility in the source code. The incompatible code is highlighted.

You can change the settings you entered into the **Getting Started** screen by selecting the **Tools** tab and choosing **Options** from the drop-down menu. Under **AWS Toolkit for .NET Refactoring VS Extension**, select **Data usage sharing** to select a different **AWS Named Profile**, **Add a named profile**, or to change your usage data selection. Choose **General** under **AWS Toolkit for .NET Refactoring VS Extension** to update the **Target Framework**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for NET Refactoring. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tk-dotnet-refactoring` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
