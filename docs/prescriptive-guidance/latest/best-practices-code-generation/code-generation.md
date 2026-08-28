---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/code-generation.html
---

# Best practices for code generation with Amazon Q Developer
<a name="code-generation"></a>

Amazon Q Developer provides automatic code generation, auto-completion, and natural language code suggestions. Following are best practices for using Amazon Q Developer in-line coding assistance:
+ **Provide context to help improve accuracy of responses**

  Start with existing code, import libraries, create classes and functions, or establish code skeletons. This context will help to significantly improve code generation quality.
+ **Code naturally**

  Use Amazon Q Developer code generation like a robust auto-completion engine. Code as you normally do, and let Amazon Q provide suggestions as you type or pause. If code generation isn't available or you're stuck on a code issue, initiate Amazon Q by typing **Alt\+C** on a PC or **Option\+C** on MacOS. For more information about common actions that you can take while using in-line suggestions, see [Using shortcut keys](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/actions-and-shortcuts.html) in the *Amazon Q Developer User Guide*.
+ **Include import libraries that are relevant to your script's objectives**

  Include relevant import libraries to help Amazon Q understand the context and generate code accordingly. You can also ask Amazon Q to suggest relevant import statements.
+ **Maintain clear and focused context**

  Keep your script focused on specific objectives, and modularize distinct functionalities into separate scripts with relevant context. Avoid noisy or confusing context.
+ **Experiment with prompts**

  Explore different prompts to nudge Amazon Q to produce useful results in code generation. For example, try the following approaches:
  + Use standard comment blocks for natural language prompts.
  + Create skeletons with comments to fill in classes and functions.
  + Be specific in your prompts, providing details instead of generalization.
+ **Chat with Amazon Q Developer and ask for assistance**

  If Amazon Q Developerisn't providing accurate suggestions, chat with Amazon Q Developer in your IDE. It can provide code snippets or full classes and functions to kickstart your context. For more information, see [Chatting with Amazon Q Developer about code](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-chat.html) in the *Amazon Q Developer User Guide.*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
