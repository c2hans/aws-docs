---
source_url: https://docs.aws.amazon.com/polly/latest/dg/emphasis-tag.html
---

# Emphasizing words
<a name="emphasis-tag"></a>

*<emphasis>*

This tag is supported only by the standard TTS format.

To emphasize words, use the <emphasis> tag. Emphasizing words changes the speaking rate and volume. More emphasis makes Amazon Polly speak the text louder and slower. Less emphasis makes it speak quieter and faster. To specify the degree of emphasis, use the `level` attribute.

`level` attribute values:
+ `Strong`: Increases the volume and slows the speaking rate so that the speech is louder and slower.
+ `Moderate`: Increases the volume and slows the speaking rate, but less than `strong`. `Moderate` is the default.
+ `Reduced`: Decreases the volume and speeds up the speaking rate. Speech is softer and faster.

**Note**
The normal speaking rate and volume for a voice falls between the `moderate` and `reduced` levels.

For example:

```
<speak>I already told you I <emphasis level="strong">really like</emphasis> that person.</speak>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
