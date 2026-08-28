---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/fields-teletext-caption-selector.html
---

# Completing the fields in the Captions Selector Group
<a name="fields-teletext-caption-selector"></a>
+ **Source**: Choose **Teletext**.
+ **Page**: This field specifies the page of the desired language. Complete as follows:
  + If you are setting up teletext passthrough captions (you are creating only one captions selector for the input captions), leave blank: the value is ignored.
  + If you are converting teletext to another format (you are creating several captions selectors, one for each language), specify the page for the desired language. If you leave this field blank, you get a validation error when you save the event.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
