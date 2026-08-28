---
source_url: https://docs.aws.amazon.com/dcv/latest/extsdkguide/extension.executable.html
---

# Extension executable
<a name="extension.executable"></a>

Extension manifest files define the `executable` file spawned by Amazon DCV. Amazon DCV will exchange messages with the extension using the `stdin` and `stdout` of the extension process.
+ The Amazon DCV client starts the extension once a Amazon DCV connection is established. The executable runs in the context of the user who launched the client.
+ The Amazon DCV server starts the extension when a user logs in. The executable runs in the context of the logged-in user.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
