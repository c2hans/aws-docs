---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/onboarding.html
---

# Best practices for onboarding Amazon Q Developer

Amazon Q Developer is a generative AI coding assistant that you can use in integrated development environments (IDEs) such as Visual Studio Code, JetBrains, Visual Studio, and Eclipse. This section describes recommended practices for accessing Amazon Q Developer and onboarding it to your development environment.

## Prerequisites for Amazon Q Developer
<a name="prerequisites"></a>

Amazon Q Developer is available as part of the AWS Toolkit for Visual Studio Code and the AWS Toolkit for JetBrains (for example, IntelliJ and PyCharm). For Visual Studio Code and JetBrains IDEs, Amazon Q Developer supports Python, Java, JavaScript, TypeScript, C\#, Go, Rust, PHP, Ruby, Kotlin, C, C\+\+, Shell scripting, SQL, and Scala.

For detailed instructions on installing the AWS Toolkit for both Visual Studio Code and a JetBrains IDE, see [Installing the Amazon Q Developer extension or plugin in your IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html) in the *Amazon Q Developer User Guide*.

## Best practices when using Amazon Q Developer
<a name="best-practices-onboarding"></a>

General best practices when using Amazon Q Developer include the following:
+ Provide relevant context to get more accurate responses, such as the programming languages, frameworks, and tools that you use. Break down complex problems into smaller components.
+ Experiment and iterate on your prompts and questions. Programming often involves trying different approaches.
+ Review code suggestions before you accept them, and edit them as needed so that they do what you intend.
+ Use the [customization capability](advanced-capabilities.md) to make Amazon Q Developer aware of your internal libraries, APIs, best practices, and architectural patterns for more relevant recommendations.

## Data privacy and content usage in Amazon Q Developer
<a name="data-privacy"></a>

When you decide to use Amazon Q Developer, understand how your data and content are used. The following are key points:
+ For Amazon Q Developer Pro users, your code content is not used for service improvement or model training.
+ For Amazon Q Developer Free Tier users, you can opt out of having your content used for service improvement through IDE settings or AWS Organizations policies.
+ Encryption in transit helps protect transmitted content, and encryption at rest and access controls help protect stored content. For more information, see [Data encryption in Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/data-encryption.html) in the *Amazon Q Developer User Guide*.
