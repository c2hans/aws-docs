---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/code-recommendations.html
---

# Best practices for code recommendations with Amazon Q Developer
<a name="code-recommendations"></a>

Amazon Q Developer can take developer questions and evaluate code to offer recommendations which range from code generation and bug fixes to guidance using natural language. Following are best practices for using chat in Amazon Q:
+ **Generate code from scratch**

  For new projects or when you need a general function (for example, copying files from Amazon S3), ask Amazon Q Developer to generate code examples using natural language prompts. Amazon Q can provide related links to public resources for further validation and investigation.
+ **Seek coding knowledge and error explanations**

  When faced with coding problems or error messages, provide the code block (with error message, if applicable) and your question as a prompt to Amazon Q Developer. This context will help Amazon Q provide accurate and relevant responses.
+ **Improve existing code**

  To fix known errors or optimize code (for example, to reduce complexity), select the relevant code block and send it to Amazon Q Developer with your request. Be specific with your prompts for better results.
+ **Explain code functionality**

  When exploring new code repositories, select a code block or an entire script and send it to Amazon Q Developer for explanation. Reduce the selection size for more specific explanations.
+ **Generate unit tests**

  After sending a code block as a prompt, ask Amazon Q Developer to generate unit tests. This approach can save time and development costs related to code coverage and DevOps.
+ **Find **AWS **answers**

  Amazon Q Developer is a valuable resource for developers working with AWS services because it contains a vast amount of knowledge related to AWS. Whether you're facing challenges with a specific AWS service, encountering error messages that are specific to AWS, or trying to learn a new AWS service, Amazon Q often provides relevant and useful information.

  Always review the recommendations that Amazon Q Developer provides to you. Then, make necessary edits and execute tests to make sure that the code meets your intended functionality.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
