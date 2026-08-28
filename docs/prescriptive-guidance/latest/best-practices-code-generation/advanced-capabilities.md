---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/advanced-capabilities.html
---

# Advanced capabilities of Amazon Q Developer
<a name="advanced-capabilities"></a>

Although this guide focuses on using Amazon Q Developer in hands-on programming tasks, it's important to be aware of its following advanced capabilities:
+ Amazon Q Developer code transformation
+ Amazon Q Developer customizations

## Amazon Q Developer code transformation
<a name="code-transformation"></a>

The Amazon Q Developer Agent for code transformation can upgrade the code language version of your files without the need for you to rewrite the code manually. It works by analyzing your existing code files and automatically rewriting them to use a newer version of the language. For example, Amazon Q transforms a single module if you're working in an IDE like Eclipse. If you're using Visual Studio Code, Amazon Q can transform an entire project or workspace.

Use Amazon Q when you want to perform common code upgrade tasks such as the following:
+ Update code to work with the new syntax of the language version.
+ Run unit tests to validate successful compilation and execution.
+ Check and resolve deployment issues.

Amazon Q can save developers from days to months of tedious and repetitive work to upgrade code bases.

As of June 2024, Amazon Q Developer supports upgrading Java code and can transform Java 8 code to newer versions such as Java 11 or 17.

## Amazon Q Developer customizations
<a name="code-customization"></a>

With its customizations capability, Amazon Q Developer can provide in-line suggestions based on a company's own codebase. The company provides their code repository either to Amazon Simple Storage Service (Amazon S3) or through AWS CodeConnections, formerly known as AWS CodeStar Connections. Then, Amazon Q uses the custom code repository with enabled security to recommend coding patterns that are relevant to developers in that organization.

When using Amazon Q Developer customizations, be aware of the following:
+ As of June 2024, the Amazon Q Developer Customizations feature is in preview mode. As a result, the feature might be limited in availability and support.
+ Custom in-line code suggestions will only be accurate given the quality of the code repositories that are provided. We recommend that you review an [evaluation score](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/customizations-admin-activate.html) for each customization that you create.
+ To optimize performance, we recommend that you include at least 20 data files containing the given language where all source files are greater than 10MB. Make sure that your repository consists of referable source code and not metadata files (for example, config files, property files, and readme files.)

By using Amazon Q Developer customizations, you can save time in the following ways:
+ Use recommendations that are based on your own company proprietary code.
+ Increase re-usability of existing code bases.
+ Create repeatable patterns that are generalized across your company.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
