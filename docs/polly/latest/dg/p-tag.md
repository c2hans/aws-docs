---
source_url: https://docs.aws.amazon.com/polly/latest/dg/p-tag.html
---

# Adding a pause between paragraphs
<a name="p-tag"></a>

*<p>*

This tag is supported by generative, long-form, neural, and standard TTS formats.

To add a pause between paragraphs in your text, use the <p> tag. Using this tag provides a longer pause than native speakers usually place at commas or the end of a sentence. Use the <p> tag to enclose the paragraph:

```
<speak>
     <p>This is the first paragraph. There should be a pause after this text is spoken.</p>
     <p>This is the second paragraph.</p>
</speak>
```

This is equivalent to specifying a pause using <break strength="x-strong"/>.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
