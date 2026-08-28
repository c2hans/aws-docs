---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/determine-number-embedded-caption-selectors.html
---

# Determining the number of captions selectors needed
<a name="determine-number-embedded-caption-selectors"></a>

To determine the number of captions selectors you need to created in the event, follow these rules:
+ **Embedded Passthrough** – Create only one captions selector. With this scenario, all languages are automatically extracted and are automatically included in the output.
+ **Embedded In, Other Out** – If you are setting up embedded-to-other, create one captions selector for each language that you want to include in the output, to a maximum of four selectors.
+ **A combination of Embedded passthrough and Embedded conversion** – If you are setting up embedded passthrough in some outputs and embedded-to-other in other outputs, create one captions selector for each language that you want to include in the output, to a maximum of four selectors. Do not worry about a selector for the embedded passthrough output. Elemental Live will extract all the languages for that output, even though no selector exists to explicitly specify this action.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
