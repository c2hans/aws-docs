---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/user-input-steps.html
---

# User input steps
<a name="user-input-steps"></a>

User input steps collect information from users when they run a flow.

## Text
<a name="text-input-step"></a>

The text input step collects free-form text from users. You can set a placeholder, a default value, and allow users to override the default at runtime.

Use placeholder text to guide users on what to enter. For example, you can present a set of options like "Enter 1 for Sales, 2 for Marketing, 3 for Support" to help users provide structured input that your flow can act on.

For configuration instructions, see [Editing flows](editing-flows.md).

## Files
<a name="file-upload-step"></a>

The file upload step accepts a document, image, or video from users. You can upload a default file and allow users to override it at runtime. You can upload one file per step.

File uploads are subject to the same size and format restrictions as uploading files in chat. If your content exceeds these limits, consider using a space or knowledge base to process the request instead.

For configuration instructions, see [Editing flows](editing-flows.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
