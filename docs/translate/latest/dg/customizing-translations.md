---
source_url: https://docs.aws.amazon.com/translate/latest/dg/customizing-translations.html
---

# Customizing your translations with Amazon Translate
<a name="customizing-translations"></a>

You can use the following settings to customize the translations that you produce with Amazon Translate:
+ **Do-not-translate tags** – Use start and end tags to specify content that you don't want to translate (in HTML content).
+ **Custom terminology** – Define how you want Amazon Translate to translate specific terms, such as brand names.
+ **Brevity** – Reduces the length of the translation output for most translations (compared to the translation output without brevity). Use brevity with real-time text translations.
+ **Profanity** – Mask profane words and phrases in your translation output.
+ **Formality** – Set the level of language formality in your translation output.
+ **Parallel data** – Adapt the translation output to reflect the style, tone, and word choices in the example translation samples that you provide.

**Topics**
+ [Using do-not-translate in Amazon Translate](customizing-translations-tags.md)
+ [Customizing your translations with custom terminology](how-custom-terminology.md)
+ [Using brevity in Amazon Translate](customizing-translations-brevity.md)
+ [Masking profane words and phrases in Amazon Translate](customizing-translations-profanity.md)
+ [Setting formality in Amazon Translate](customizing-translations-formality.md)
+ [Customizing your translations with parallel data (Active Custom Translation)](customizing-translations-parallel-data.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
