---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/developer-workflows.html
---

# Using Amazon Q Developer in developer workflows
<a name="developer-workflows"></a>

Developers follow a standard workflow encompassing the stages of requirement gathering, design and planning, coding, testing, code review, and deployment. This section focuses on how you can use Amazon Q Developer capabilities to optimize key development steps.

![Code development tasks that Amazon Q Developer can do include design, writing, testing, and review.](http://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/images/guide-img/f65a39c3-c47d-43b6-afa3-d8124e7bbe1f/images/469a246e-ba24-49d0-adea-a43d264ced44.png)

The previous diagram shows how Amazon Q Developer can accelerate and streamline the following common tasks in stages of code development:
+ Design and planning \| Environment setup \| Code organization
  + Generate relevant libraries
  + Generate outlines of classes and functions
  + Ask Amazon Q for well-architected advice
  + Use Amazon Q to refactor code
+ Code writing \| Debugging and profiling \| Unit testing \| Documentation
  + Generate popular algorithms
  + Receive in-line code recommendations
  + Ask Amazon Q to optimize and fix code
  + Generate debugging and profiling statements
  + Generate unit tests
  + Generate documentation and comments within scripts
+ Code review
  + Ask Amazon Q to explain code
  + Send code as prompt with questions to Amazon Q

## Design and planning
<a name="design-and-planning.f8ff66d4-d784-5d58-aa39-8b0df57c32cf"></a>

After gathering business and technical requirements, developers design new, or extend existing, codebases. During this phase, Amazon Q Developer can assist developers to do the following tasks:
+ Generate relevant libraries and class and function outlines for well-architected advice.
+ Provide guidance for engineering, compatibility, and architectural design queries.

## Coding
<a name="coding.d9f7ad6e-de15-5913-90ef-404cb523536f"></a>

The coding process uses Amazon Q Developer to accelerate development in the following ways:
+ **Environment setup** - Install the AWS Toolkit in your integrated development environment (IDE) (for example, VS Code or IntelliJ). Then, use Amazon Q to generate libraries or receive setup suggestions based on your project goals. For more details, see [Best practices for onboarding Amazon Q Developer](onboarding.md).
+ **Code organization** - Refactor code or obtain organization recommendations from Amazon Q that align with your project objectives.
+ **Code writing - **Use in-line suggestions to generate code while developing or ask Amazon Q to generate code by using the Amazon Q chat panel in your IDE. For more details, see [Best practices for code generation with Amazon Q Developer](code-generation.md).
+ **Debugging and profiling - **Generate profiling commands, or use Amazon Q options like **Fix** and **Explain **to debug issues.
+ **Unit testing** - Provide code as a prompt to Amazon Q during a chat session and request applicable unit test generation. For more information, see [Code examples with Amazon Q Developer](examples.md).
+ **Documentation** - Use in-line suggestions to create comments and docstrings, or use the **Explain** option to generate detailed summaries for code selections. For more information, see [Code examples with Amazon Q Developer](examples.md).

## Code review
<a name="code-review.bc6ecdfa-85d1-5270-9acd-bd1a1566558a"></a>

Reviewers need to comprehend development code before promoting it to production. To accelerate this process, use the Amazon Q **Explain **and **Optimize **options, or send code selections with custom prompt instructions to Amazon Q in a chat session. For more information, see [Chat examples](examples-chat.md).

## Integration and deployment
<a name="integration-and-deployment.a83a2ed4-934a-5ea8-bf9e-470c9dfbbcc3"></a>

Ask Amazon Q for guidance about continuous integration, delivery pipelines, and deployment best practices that are specific to your project's architecture.

Using these recommendations, you can learn to effectively harness Amazon Q Developer features, optimizing your workflows and increasing productivity across the entire development lifecycle.
