---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-alphanumeric.html
---

# AMAZON.AlphaNumeric
<a name="built-in-slot-alphanumeric"></a>

Recognizes strings made up of letters and numbers, such as **APQ123**.

You can use the `AMAZON.AlphaNumeric` slot type for strings that contain:
+ Alphabetical characters, such as **ABC**
+ Numeric characters, such as **123**
+ A combination of alphanumeric characters, such as **ABC123**

The `AMAZON.AlphaNumeric` slot type supports inputs using spelling styles. You can use the spell-by-letter and spell-by-word styles to help your customers enter letters. For more information, see [Capturing slot values with spelling styles during the conversation](spelling-styles.md).

You can add a regular expression to the `AMAZON.AlphaNumeric` slot type to validate values entered for the slot. For example, you can use a regular expression to validate:
+ Canadian postal codes
+ Driver's license numbers
+ Vehicle identification numbers

Use a standard regular expression. Amazon Lex V2 supports the following characters in the regular expression:
+ A-Z, a-z
+ 0-9

Amazon Lex V2 also supports Unicode characters in regular expressions. The form is `\u{{Unicode}}`. Use four digits to represent Unicode characters. For example, `[\u0041-\u005A]` is equivalent to [A-Z].

The following regular expression operators are not supported:
+ Infinite repeaters: \*, \+, or {x,} with no upper bound.
+ Wild card (.)

The maximum length of the regular expression is 300 characters. The maximum length of a string stored in an `AMAZON.AlphaNumeric` slot type that uses a regular expression is 30 characters.

The following are some example regular expressions.
+ Alphanumeric strings, such as **APQ123** or **APQ1**: `[A-Z]{3}[0-9]{1,3}` or a more constrained `[A-DP-T]{3} [1-5]{1,3}`
+ US Postal Service Priority Mail International format, such as **CP123456789US**: `CP[0-9]{9}US`
+ Bank routing numbers, such as **123456789**: `[0-9]{9}`

To set the regular expression for a slot type, use the console or the [CreateSlotType](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateSlotType.html) operation. The regular expression is validated when you save the slot type. If the expression isn't valid, Amazon Lex V2 returns an error message.

When you use a regular expression in a slot type, Amazon Lex V2 checks input to slots of that type against the regular expression. If the input matches the expression, the value is accepted for the slot. If the input does not match, Amazon Lex V2 prompts the user to repeat the input.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
