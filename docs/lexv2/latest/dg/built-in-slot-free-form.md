---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-free-form.html
---

# AMAZON.FreeFormInput
<a name="built-in-slot-free-form"></a>

`AMAZON.FreeFormInput` can be used to capture free form input from the end user. It recognizes strings that consist of words or characters. The resolved value is the entire input utterance.

Example:

Bot: Please provide feedback from your call experience.

User: I got the answers to all of my questions, and I was able to complete the transaction.

Note:
+ `AMAZON.FreeFormInput` can be used to capture free form input as-is from the end user.
+ `AMAZON.FreeFormInput` cannot be used in intent sample utterances.
+ `AMAZON.FreeFormInput` cannot have slot sample utterances.
+ `AMAZON.FreeFormInput` is only recognized when elicited for.
+ `AMAZON.FreeFormInput` does not support wait and continue.
+ `AMAZON.FreeFormInput` is currently not supported in the Connect Customer Chat channel.
+ When a `AMAZON.FreeFormInput` slot is elicited, `FallbackIntent` will not be triggered.
+ When a `AMAZON.FreeFormInput` slot is elicited, there will be no intent switch.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
