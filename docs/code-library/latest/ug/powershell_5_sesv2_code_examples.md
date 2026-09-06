---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_5_sesv2_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon SES API v2 examples using Tools for PowerShell V5
<a name="powershell_5_sesv2_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Amazon SES API v2.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Send-SES2Email`
<a name="sesv2_SendSES2Email_powershell_5_topic"></a>

The following code example shows how to use `Send-SES2Email`.

**Tools for PowerShell V5**
**Example 1: This example shows how to send a standard email message.**

```
Send-SES2Email -FromEmailAddress "sender@example.com" -Destination_ToAddress "recipient@example.com" -Subject_Data "Email Subject" -Text_Data "Email Body"
```
+  For API details, see [SendEmail](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
