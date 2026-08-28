---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/setting-up-for-captions.html
---

# Setting up for captions
<a name="setting-up-for-captions"></a>

When you create an event, you must specify the format of the input captions. On the output side, you must specify the desired formats of the captions for each output. When you save the event, Elemental Live validates your choices in terms of whether the specified input format can produce the specified output format, and whether that output format is supported in the specified output type.

**Topics**
+ [Step 1: Identify the source captions that you want](identify-captions-in-the-input.md)
+ [Step 2: Create captions selectors](create-caption-selectors.md)
+ [Step 3: Plan captions for the outputs](planning-captions-in-the-outputs.md)
+ [Step 4: Match formats to categories](categories-captions.md)
+ [Step 5: Create captions encodes](create-captions-encodes.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
