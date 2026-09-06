---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/analyze-assessment.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Analyze the results
<a name="analyze-assessment"></a>

When the assessment is complete, you can view the results in the dashboard. The dashboard contains the following information:
+ **Status** – The status of the assessment. **Assessment complete** indicates that you can review the assessment in the **Assessment Overview** pane.
+ **Solution file** – The file that you selected to run the assessment on.
+ **Version** – The .NET Core version that your solution file was compared to during the assessment.
+ **Incompatible NuGet packages** – The number of .NET Framework NuGet packages that are incompatible with the .NET Core version that you selected for the assessment.
+ **Portable NuGet packages** – The number of .NET Framework NuGet packages that are compatible with the .NET Core version that you selected for the assessment.
+ **Ported projects** – The number of projects that have been ported to the .NET Core version that you selected for the assessment.
+ **Incompatible APIs** – The number of .NET Framework APIs that are incompatible with the .NET Core version that you selected for the assessment.
+ **Portable APIs** – The number of .NET Framework APIs that are compatible with the .NET Core version that you selected for the assessment.

You can click on the incompatible NuGet packages or incompatible APIs to view details about individual incompatibilities, view the project dependency graph, or export the results to a `.csv` file.
