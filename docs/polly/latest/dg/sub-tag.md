---
source_url: https://docs.aws.amazon.com/polly/latest/dg/sub-tag.html
---

# Pronouncing acronyms and abbreviations
<a name="sub-tag"></a>

*<sub>*

This tag is supported by generative, long-form, neural, and standard TTS formats.

Use the `<sub>` tag with the `alias` attribute to substitute a different word (or pronunciation) for selected text such as an acronym or abbreviation.

This uses the syntax:

```
<sub alias="{{new word}}">{{abbreviation}}</sub>
```

 In the following example, the name "Mercury" is substituted for the element's chemical symbol to make the audio content clearer.

```
<speak>
     My favorite chemical element is <sub alias="Mercury">Hg</sub>, because it looks so shiny.
</speak>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
