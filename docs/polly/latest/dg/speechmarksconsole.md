---
source_url: https://docs.aws.amazon.com/polly/latest/dg/speechmarksconsole.html
---

# Requesting speech marks
<a name="speechmarksconsole"></a>

You can use the console or the `synthesize-speech` command to request speech marks from Amazon Polly. You can then view the metadata or save it to a file.

------
#### [ Console ]

**To generate speech marks on the console**

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/).

1. Choose the **Text-to-Speech** tab.

1. Turn on **SSML** to use SSML.

1. Type or paste your text into the input box.

1. For **Language**, choose the language of your text.

1. For **Voice**, choose the voice you want to use.

1. To change text pronunciation, expand **Additional settings**, turn on **Customize pronunciation**, and for **Apply lexicon**, choose the desired lexicon.

1. To verify the speech, choose **Listen**.

1. Turn on **Speech file format settings**.
**Note**
Downloading MP3, OGG, PCM, Mu-law, or A-law formats will not generate speech marks.

1. For **File Format**, choose **Speech marks**.

1. For **Speech mark types**, choose the types of speech marks to generate. The option to choose **SSML** metadata is only available when **SSML** is on. For more information on using SSML with Amazon Polly see [Generating speech from SSML documents](ssml.md).

1. Choose **Download**.

------
#### [ AWS CLI ]

In addition to the input text, the following elements are required to return this metadata:
+ `output-format`

  Amazon Polly supports only the JSON format when returning speech marks.

  ```
  --output-format json
  ```

  If you use an unsupported output format, Amazon Polly throws an exception.
+ `voice-id`

  To ensure that the metadata matches the associated audio stream, specify the same voice that is used to generate the synthesized speech audio stream. The available voices don't have identical speech rates. If you use a voice other than the one used to generate the speech, the metadata will not match the audio stream.

  ```
  --voice-id Joanna
  ```
+ `speech-mark-types`

  Specify the type or types of speech marks you want. You can request any or all of the speech mark types, but must specify at least one type.

  ```
  --speech-mark-types='["sentence", "word", "viseme", "ssml"]'
  ```
+ `text-type`

  Plain text is the default input text for Amazon Polly, so you must use `text-type ssml` if you want to return SSML speech marks.
+ `outfile`

  Specify the output file to which the metadata is written.

  ```
  MaryLamb.txt
  ```

The following AWS CLI example is formatted for Unix, Linux, and macOS. For Windows, replace the backslash (\\) Unix continuation character at the end of each line with a caret (^) and use full quotation marks (") around the input text with single quotes (') for interior tags.

```
aws polly synthesize-speech \
  --output-format json \
  --voice-id {{Voice ID}} \
  --text '{{Input text}}' \
  --speech-mark-types='["sentence", "word", "viseme"]' \
  {{outfile}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
