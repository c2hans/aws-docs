---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/code-generation.html
---

# Best practices for code generation with Amazon Q Developer

Amazon Q Developer provides automatic code generation, auto-completion, and natural language code suggestions. The following are best practices for using Amazon Q Developer inline coding assistance:
+ **Provide context to help improve accuracy of responses**

  Start with existing code, import libraries, create classes and functions, or establish code skeletons. This context helps improve code generation quality.
+ **Code naturally**

  Use Amazon Q Developer code generation like an auto-completion engine. Code as you normally do, and let Amazon Q provide suggestions as you type or pause. If code generation isn't available or you encounter a code issue, start Amazon Q by typing **Alt\+C** on Windows or **Option\+C** on macOS. For more information about common actions that you can take while using inline suggestions, see [Using shortcut keys](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/actions-and-shortcuts.html) in the *Amazon Q Developer User Guide*.
+ **Include import libraries that are relevant to your script's objectives**

  Include relevant import libraries to help Amazon Q understand the context and generate code accordingly. You can also ask Amazon Q to suggest relevant import statements.
+ **Maintain clear and focused context**

  Keep your script focused on specific objectives, and modularize distinct functionalities into separate scripts with relevant context. Avoid irrelevant or confusing context.
+ **Experiment with prompts**

  Explore different prompts to guide Amazon Q toward useful results in code generation. For example, try the following approaches:
  + Use standard comment blocks for natural language prompts.
  + Create skeletons with comments to fill in classes and functions.
  + Be specific in your prompts, and provide details instead of generalities.
+ **Chat with Amazon Q Developer and ask for assistance**

  If Amazon Q Developer isn't providing accurate suggestions, chat with Amazon Q Developer in your IDE. It can provide code snippets or full classes and functions to help establish your context. For more information, see [Chatting with Amazon Q Developer about code](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-chat.html) in the *Amazon Q Developer User Guide.*
