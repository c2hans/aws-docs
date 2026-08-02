---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/port-solution.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Port the solution
<a name="port-solution"></a>

Toolkit for .NET Refactoring provides the following features to help you port the solution.

## Guided assistance
<a name="guided-assistance"></a>

You can apply all the recommended code changes at once or you can view each incompatibility individually. When you port a project or solution, Toolkit for .NET Refactoring prompts you to choose whether you want to apply all the recommended code changes. If you do not select that option, Toolkit for .NET Refactoring prompts you to view each incompatibility. After you make a code change, save your updates to view the updated recommendations for your code after the modifications have been applied.

When you port your solution to .NET Core, the Toolkit for .NET Refactoring extension provides guided assistance in the source editor.

When you are ready to port a project, select one of the following options from the **Extensions** tab:
+ **Port solution to .NET Core** – Use this option to port all projects to .NET Core.
+ **Port project to .NET Core** – Use this option to port a single project to .NET Core.

When the source file is open with a source editor, porting options are provided to assist you, and to automate the porting of each source file. Automated porting involves running the source code through code translation assistant rules for porting. This can be performed at the solution level when you select **Port solution to .NET Core** and choose to apply recommended source code changes.

## View incompatibilities
<a name="incompatabilities"></a>

View the list of incompatibilities and suggestions from the **Error list** pane at the bottom of the window. Select an error in the list to view the code in the source editor. The source file is annotated with the error message, details about the compatibility issue, and a recommended solution.

If you used automated porting to apply all the recommended code changes, a light bulb icon appears next to each line of code that was modified, with a comment describing the change.

In the source file, each line of source code with compatibility issues is highlighted. This helps you to visualize the issues in the file as you address them. The highlighting is disappears when the compatibility issues are addressed.

## Suggestions
<a name="suggestions"></a>

The source editor provides a replacement suggestion for each incompatibility in the source file. If a direct replacement exists, you can choose to select and replace it. If there is no direct replacement, references or contextual help on how to proceed are provided.
