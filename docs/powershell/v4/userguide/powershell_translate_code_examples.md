---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/powershell_translate_code_examples.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# Amazon Translate examples using Tools for PowerShell V4
<a name="powershell_translate_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with Amazon Translate.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `ConvertTo-TRNTargetLanguage`
<a name="translate_TranslateText_powershell_topic"></a>

The following code example shows how to use `ConvertTo-TRNTargetLanguage`.

**Tools for PowerShell V4**
**Example 1: Converts the specified English text to French. The text to convert can also be passed as the -Text parameter.**

```
"Hello World" | ConvertTo-TRNTargetLanguage -SourceLanguageCode en -TargetLanguageCode fr
```
+  For API details, see [TranslateText](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
