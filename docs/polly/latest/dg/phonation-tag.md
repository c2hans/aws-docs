---
source_url: https://docs.aws.amazon.com/polly/latest/dg/phonation-tag.html
---

# Speaking softly
<a name="phonation-tag"></a>

*<amazon:effect phonation="soft">*

This tag is currently supported only by the standard TTS format.

To specify that input text should be spoken in a softer-than-normal voice, use the <amazon:effect phonation="soft"> tag.

This uses the syntax:

```
<amazon:effect phonation="soft">{{text}}</amazon:effect>
```

For example, you might use this tag with the Matthew voice as follows:

```
<speak>
     This is Matthew speaking in my normal voice. <amazon:effect phonation="soft">This
     is Matthew speaking in my softer voice.</amazon:effect>
</speak>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
