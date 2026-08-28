---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/captions-in-input-switching.html
---

# Captions and input switching setups
<a name="captions-in-input-switching"></a>

Your input might include a backup input that is only switched to if the first input fails. (This feature is called Input Switching or Input Switching with “Hot Hot” backup.) Or your input might include multiple inputs, each with its own backup input – several “input pairs.” The same rules apply as for multiple inputs: the captions in all the inputs must be identical for captions to work smoothly in the output.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
