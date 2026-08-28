---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/determine-number-teletext-caption-selectors.html
---

# Determining the number of captions selectors needed
<a name="determine-number-teletext-caption-selectors"></a>
+ If you are setting up teletext passthrough captions, create only one captions selector, even if you want to include multiple languages in the output. With this scenario, all languages are automatically extracted and are automatically included in the output.
+ If you are setting up teletext-to-other, create one captions selector for each language that you want to include in the output. For example, one selector to extract English teletext, and one selector to extract Swedish teletext.
+ If you are setting up teletext passthrough in some outputs and teletext-to-other in other outputs, create individual selectors for the teletext-to-other, one for each language being converted. Do not worry about a selector for the teletext passthrough output. Elemental Live will extract all the data in the teletext, even though there is not a selector to explicitly specify this action.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
