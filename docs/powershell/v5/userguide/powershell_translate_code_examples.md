---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_translate_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Amazon Translate examples using Tools for PowerShell V5
<a name="powershell_translate_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Amazon Translate.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `ConvertTo-TRNTargetLanguage`
<a name="translate_TranslateText_powershell_topic"></a>

The following code example shows how to use `ConvertTo-TRNTargetLanguage`.

**Tools for PowerShell V5**
**Example 1: Converts the specified English text to French. The text to convert can also be passed as the -Text parameter.**

```
"Hello World" | ConvertTo-TRNTargetLanguage -SourceLanguageCode en -TargetLanguageCode fr
```
+  For API details, see [TranslateText](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
