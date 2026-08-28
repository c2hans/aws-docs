---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/prompting-image-masks.html
---

# Mask prompts
<a name="prompting-image-masks"></a>

Mask prompts are used in editing operations. A mask prompt allows you to use natural language to describe the elements within an image that you want to change (in the case of inpainting) or to remain untouched (in the case of outpainting). You pass a mask prompt as part of your request using the `maskPrompt` parameter. Below are some examples that visualize the result of a mask prompt. The masked area is colored in dark blue.

**Mask Prompt: "dog"**

![A dog](http://docs.aws.amazon.com/nova/latest/userguide/images/Screenshot1.png)

**maskPrompt: "dog"**

![A dog](http://docs.aws.amazon.com/nova/latest/userguide/images/Screenshot3.png)

**Mask Prompt: "dog in a bucket"**

![A dog in a bucket](http://docs.aws.amazon.com/nova/latest/userguide/images/Screenshot2.png)

**maskPrompt: "black dog"**

![A black dog](http://docs.aws.amazon.com/nova/latest/userguide/images/Screenshot4.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
