---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/bda-how-it-works.html
---

# How Bedrock Data Automation works
<a name="bda-how-it-works"></a>

Bedrock Data Automation (BDA) lets you configure output based on your processing needs for a specific data type: documents, images, video or audio. BDA can generate standard output or custom output. Below are some key concepts for understanding how BDA works. If you're a new user, start with the information about standard output.
+ Standard output – Sending a file to BDA with no other information returns the default standard output, which consists of commonly required information that's based on the data type. Examples include audio transcriptions, scene summaries for video, and document summaries. These outputs can be tuned to your use case using projects to modify them. For more information, see [Standard output in Bedrock Data Automation](bda-standard-output.md).
+ Custom output – For documents, audio,and images only. Choose custom output to define exactly what information you want to extract using a blueprint. A blueprint consists of a list of expected fields that you want retrieved from a file. Each field represents a piece of information that needs to be extracted to meet your specific use case. You can create your own blueprints, or select predefined blueprints from the BDA blueprint catalog. For more information, see [Custom output and blueprints](bda-custom-output-idp.md).
+ Projects – A project is a BDA resource that allows you to modify and organize output configurations. Each project can contain standard output configurations for documents, images, video, and audio, as well as custom output blueprints for documents, audio, and images. Projects are referenced in the `InvokeDataAutomationAsync` API call to instruct BDA on how to process the files. For more information about projects and their use cases, see [Bedrock Data Automation projects](bda-projects.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
