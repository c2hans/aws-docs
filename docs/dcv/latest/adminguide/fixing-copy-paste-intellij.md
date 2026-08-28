---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/fixing-copy-paste-intellij.html
---

# Fixing Copy and Paste to IntelliJ IDEA
<a name="fixing-copy-paste-intellij"></a>

When trying to copy text from the macOS Amazon DCV Client to IntelliJ IDEA, the text cannot be pasted. IntelliJ can't accept the cross-platform format that Amazon DCV uses by default. To disable cross-platform text on Amazon DCV so you can paste text into IntelliJ, modify the `disabled-targets` field on the Amazon DCV Server.

This change will prevent copy and paste from working with the Amazon DCV web client. Make sure that you want copy and paste for Intellij IDEA to work on only the Amazon DCV Client before making this change.

**To configure the server to paste text into IntelliJ IDEA**

1. Navigate to `/etc/dcv/` and open the `dcv.conf` with your preferred text editor.

1. Locate the `disabled-targets` parameter in the `[clipboard]` section. If there is no `disabled-targets` or `[clipboard]` section, add them manually.

1. Add the following content to define the value for `disabled-targets`.

   ```
   [clipboard]
   disabled-targets = ['dcv/text', 'JAVA_DATAFLAVOR:application/x-java-jvm-local-objectref; class=com.intellij.codeInsight.editorActions.FoldingData']
   ```

1. Save and close the file.

1. [Stop](managing-sessions-lifecycle-stop.md) and [restart](managing-sessions-start.md) the Amazon DCV session.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
