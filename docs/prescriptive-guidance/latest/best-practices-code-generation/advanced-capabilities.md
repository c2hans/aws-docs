---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/advanced-capabilities.html
---

# Advanced capabilities of Amazon Q Developer
<a name="advanced-capabilities"></a>

Although this guide focuses on using Amazon Q Developer in hands-on programming tasks, it also offers the following advanced capabilities:
+ Amazon Q Developer code transformation
+ Amazon Q Developer customizations

## Amazon Q Developer code transformation
<a name="code-transformation"></a>

The Amazon Q Developer Agent for code transformation can upgrade the language version of your code files without manual rewriting. It analyzes your existing code files and automatically rewrites them to use a newer version of the language. Code transformation is supported in JetBrains IDEs and Visual Studio Code for Java upgrades, and in Visual Studio for .NET applications.

Use Amazon Q when you want to perform common code upgrade tasks such as the following:
+ Update code to work with the new syntax of the language version.
+ Run unit tests to validate successful compilation and execution.
+ Check and resolve deployment issues.

Amazon Q can help reduce the time and effort that developers spend on repetitive code upgrade work.

Amazon Q Developer supports upgrading Java code and can transform Java applications from source versions 8, 11, 17, or 21 to target versions 17 or 21.

## Amazon Q Developer customizations
<a name="code-customization"></a>

With its customizations capability, Amazon Q Developer can provide in-line suggestions based on a company's own codebase. The company provides its code repository either to Amazon Simple Storage Service (Amazon S3) or through AWS CodeConnections, formerly known as AWS CodeStar Connections. Then, Amazon Q uses the custom code repository to recommend coding patterns that are relevant to developers in that organization.

When using Amazon Q Developer customizations, be aware of the following:
+ As of June 2024, the Amazon Q Developer Customizations feature is in preview mode. As a result, the feature might be limited in availability and support.
+ The accuracy of custom in-line code suggestions depends on the quality of the code repositories that you provide. We recommend that you review the [evaluation score](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/customizations-admin-activate.html) for each customization that you create.
+ To improve performance, we recommend that you include at least 20 data files that contain the given language, where the total size of all source files is greater than 10 MB. Make sure that your repository consists of reference source code and not metadata files (for example, configuration files, property files, and readme files).

By using Amazon Q Developer customizations, you can save time in the following ways:
+ Use recommendations that are based on your company's proprietary code.
+ Increase reusability of existing codebases.
+ Create repeatable patterns that are generalized across your company.
