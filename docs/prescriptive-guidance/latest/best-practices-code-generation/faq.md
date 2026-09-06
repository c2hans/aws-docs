---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/faq.html
---

# FAQs about Amazon Q Developer
<a name="faq"></a>

This section provides answers to frequently asked questions about using Amazon Q Developer for code development.

## What is Amazon Q Developer?
<a name="what-is-9999999999999999qdevlong--.8b87ca58-1189-5647-803e-9cfaa3372a07"></a>

Amazon Q Developer is a powerful generative AI-powered service designed to accelerate code development tasks by providing intelligent code generation and recommendations. On April 30, 2024, Amazon CodeWhisperer became a part of Amazon Q Developer.

## How do I access Amazon Q Developer?
<a name="how-do-i-access-9999999999999999qdevlong--.08b0eb54-be82-5c40-82bb-1f2e984e6316"></a>

Amazon Q Developer is available as part of the AWS Toolkits for Visual Studio Code and JetBrains IDEs, such as IntelliJ and PyCharm. To get started, [install the latest AWS Toolkit version](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html).

## What programming languages does Amazon Q Developer support?
<a name="what-programming-languages-does-9999999999999999qdevlong--support-.a9800b0e-fac4-5d17-b357-465613febb2d"></a>

For Visual Studio Code and JetBrains IDEs, Amazon Q Developer supports Python, Java, JavaScript, TypeScript, C\#, Go, Rust, PHP, Ruby, Kotlin, C, C\+\+, Shell scripting, SQL, and Scala. Although this guide focuses on Python and Java for example purposes, the concepts are applicable to any supported programming language.

## How can I provide context to Amazon Q Developer for better code generation?
<a name="how-can-i-provide-context-to-9999999999999999qdevlong--for-better-code-generation-.ba733f4b-c703-5af5-a808-6bff7728bc95"></a>

Start with existing code, import relevant libraries, create classes and functions, or establish code skeletons. Use standard comment blocks for natural language prompts. Keep your script focused on specific objectives, and modularize distinct functionalities into separate scripts with relevant context. For more information, see [Best coding practices with Amazon Q Developer](best-practices-coding.md).

## What should I do if in-line code generation with Amazon Q Developer isn't accurate?
<a name="what-should-i-do-if-in-line-code-generation-with-9999999999999999qdevlong--isn-t-accurate-.7f270220-0ecc-5ed2-b92f-2e62dad54d2f"></a>

Review the context of the script, ensure libraries are present, and make sure that classes and functions relate to the new code. Modularize your code, and separate different classes and functions by their objective. Write clear and specific prompts or comments. If you're still uncertain about the code's accuracy and you can't proceed with it, start a chat with Amazon Q and send it the code snippet with instructions. For more information, see [Troubleshooting code generation scenarios in Amazon Q Developer](troubleshooting.md).

## How can I use the Amazon Q Developer chat capability for code generation and troubleshooting?
<a name="how-can-i-use-the-9999999999999999qdevlong--chat-capability-for-code-generation-and-troubleshooting-.bae28b11-416c-5d43-83c0-a1628c694bc0"></a>

Chat with Amazon Q to generate common functions, ask for recommendations, or explain code. If the initial response isn't satisfactory, experiment with different prompts and follow the provided URLs. Also, provide feedback to Amazon Q to help improve its future chat performance. Use the thumbs-up and thumbs-down icons to provide your feedback. For more information, see [Chat examples](examples-chat.md).

## What are some best practices for using Amazon Q Developer?
<a name="what-are-some-best-practices-for-using-9999999999999999qdevlong--.5b1f93d6-99e1-5172-9c47-d680961ddd30"></a>

Provide relevant context, experiment, and iterate on prompts, review code suggestions before accepting them, use customization capabilities, and understand data privacy and content usage policies. For more information, see [Best practices for code generation with Amazon Q Developer](code-generation.md) and [Best practices for code recommendations with Amazon Q Developer](code-recommendations.md).

## Can I customize Amazon Q Developer to generate recommendations based on my own code?
<a name="can-i-customize-9999999999999999qdevlong--to-generate-recommendations-based-on-my-own-code-.766f6d0a-fa79-5a5f-b7a0-6559236178dc"></a>

Yes, use customizations, which is an advanced capability of Amazon Q Developer. With customizations, businesses can provide their own code repositories to enable Amazon Q Developer to recommend in-line code suggestions. For more information, see [Advanced capabilities of Amazon Q Developer](advanced-capabilities.md) and [Resources](resources.md).
