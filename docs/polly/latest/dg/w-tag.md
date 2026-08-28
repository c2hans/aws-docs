---
source_url: https://docs.aws.amazon.com/polly/latest/dg/w-tag.html
---

# Improving pronunciation by specifying parts of speech
<a name="w-tag"></a>

*<w>*

This tag is supported by generative, long-form, neural, and standard TTS formats.

You can use the <w> tag to customize the pronunciation of words by specifying the word’s part of speech or alternate meaning. This is done using the `role` attribute.

This tag uses the following syntax:

```
<w role="{{attribute}}">{{text}}</w>
```

The following values can be used for the `role` attribute:

To specify the part of speech:
+ `amazon:VB`: interprets the word as a verb (present simple).
+ `amazon:VBD`: interprets the word as past tense verb.
+ `amazon:DT`: interprets the word as a determiner.
+ `amazon:IN`: interprets the word as a preposition.
+ `amazon:JJ`: interprets the word as an adjective.
+ `amazon:NN`: interprets the word as a noun.

For example, depending on its part of speech, the US English pronunciation of the word "read" varies based on the tag:

```
<speak>
     The word <say-as interpret-as="characters">read</say-as> may be interpreted
     as either the present simple form <w role="amazon:VB">read</w>, or the past
     participle form <w role="amazon:VBD">read</w>.
</speak>
```

To specify a specific meaning:
+ `amazon:DEFAULT`: uses the default sense of the word.
+ `amazon:SENSE_1`: uses the non-default sense of the word when present. For example, the noun "bass" is pronounced differently depending on its meaning. The default meaning is the lowest part of the musical range. The alternate meaning is a species of freshwater fish, also called "bass" but pronounced differently. Using `<w role="amazon:SENSE_1">bass</w>` renders the non-default pronunciation (freshwater fish) for the audio text.

This difference in pronunciation and meaning can be heard if you synthesize the following:

```
<speak>
    Depending on your meaning, the word <say-as interpret-as="characters">bass</say-as>
    may be interpreted as either a musical element: bass, or as its alternative meaning,
    a freshwater fish <w role="amazon:SENSE_1">bass</w>.
</speak>
```

**Note**
 Some languages may have a different selection of supported parts of speech.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
