---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/dotnet-layers.html
---

# Working with layers for .NET Lambda functions
<a name="dotnet-layers"></a>

We don't recommend using [layers](chapter-layers.md) to manage dependencies for Lambda functions written in .NET. This is because .NET is a compiled language, and your functions still have to manually load any shared assemblies into memory during the [Init](lambda-runtime-environment.md#runtimes-lifecycle-ib) phase, which can increase cold start times. Using layers not only complicates the deployment process, but also prevents you from taking advantage of built-in compiler optimizations.

To use external dependencies with your .NET handlers, include them directly in your deployment package at compile time. By doing so, you simplify the deployment process and also take advantage of built-in .NET compiler optimizations. For an example of how to import and use dependencies like NuGet packages in your function, see [Define Lambda function handler in C\#](csharp-handler.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
