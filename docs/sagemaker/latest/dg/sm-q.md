---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sm-q.html
---

# Use Amazon Q Developer with Amazon SageMaker Studio Classic
<a name="sm-q"></a>

**Note**
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md).
Studio Classic is still maintained for existing workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md).

Amazon SageMaker Studio Classic is an integrated machine learning environment where you can build, train, deploy, and analyze your models all in the same application. You can generate code recommendations and suggest improvements related to code issues by using Amazon Q Developer with Amazon SageMaker AI.

Amazon Q Developer is a generative artificial intelligence (AI) powered conversational assistant that can help you understand, build, extend, and operate AWS applications. In the context of an integrated AWS coding environment, Amazon Q can generate code recommendations based on developers' code, as well as their comments in natural language.

Amazon Q has the most support for Java, Python, JavaScript, TypeScript, C\#, Go, PHP, Rust, Kotlin, and SQL, as well as the Infrastructure as Code (IaC) languages JSON (CloudFormation), YAML (CloudFormation), HCL (Terraform), and CDK (Typescript, Python). It also supports code generation for Ruby, C\+\+, C, Shell, and Scala. For examples of how Amazon Q integrates with Amazon SageMaker AI and displays code suggestions in the Amazon SageMaker Studio Classic IDE, see [Code Examples](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/inline-suggestions-code-examples.html) in the *Amazon Q Developer User Guide*.

For more information on using Amazon Q with Amazon SageMaker Studio Classic, see the [Amazon Q Developer User Guide](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/sagemaker-setup.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
