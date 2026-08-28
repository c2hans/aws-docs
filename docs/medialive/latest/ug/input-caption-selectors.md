---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-caption-selectors.html
---

# Input settings—Caption selectors
<a name="input-caption-selectors"></a>

If you want to extract captions from the input or to specify an external file as the source of the captions, this section is required. You create one or more captions selectors to identify the captions to extract. Typically, you identify different languages in each selector, but you could also identify different captions formats.

For each captions item that you want to extract or include, choose the **Add captions** selector.

**To identify the caption assets to extract**

1. Choose **Add caption selector** once for each captions asset that you want to extract from the input.

   If you are creating a channel with multiple inputs, then you must extract the same captions languages from every input. For example, you must extract English and Spanish captions from every input.

1. In **Caption selector name**, enter a name that describes the captions that you are extracting.

   If you are creating a channel with multiple inputs, then you must assign the identical name to the selector in every input. For example, create a selector called **captions-english** in every input, and a selector called **captions-spanish** in every input.

1. In **Selector Settings**, select the format of the captions asset to extract. Then complete the fields that apply to that format.

For more information about setting up an input for captions, see [Including captions in a channel](captions.md), specifically [Create captions selectors in the inputs](identify-captions-in-the-input.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
