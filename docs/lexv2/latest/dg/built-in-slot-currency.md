---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-currency.html
---

# AMAZON.Currency
<a name="built-in-slot-currency"></a>

Converts words that represent a currency into a standard ISO 4217 alphabetic currency code and a number. Amazon Lex V2 recognizes currencies but does not convert from one currency to another.

For more information, see [Currency codes - ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) on the International Organization for Standardization (ISO) website.

The currency represented is structured as follows: `{Unit} {Amount}`
+ {Unit} refers to the specific currency unit (for example, USD).
+ {Amount} denotes the monetary value, formatted to two decimal places (for example, 300.00).

Examples (all examples below are using the en-US locale; different locales may yield different results):
+ "3USD": USD 3.00
+ "USD300": USD 300.00
+ "3 dimes" : USD 0.30
+ "$1.56": USD 1.56
+ "5c": USD 0.05
+ "1 dollar": USD 1.00
+ "five fifteen": USD 515.00
+ “five dollars fifteen cents”: USD 5.15
+ "5 usd and 1/2": USD 5.50

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
