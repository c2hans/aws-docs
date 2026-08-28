---
source_url: https://docs.aws.amazon.com/polly/latest/dg/SynthesizeSpeechSamplePython.html
---

# SynthesizeSpeech
<a name="SynthesizeSpeechSamplePython"></a>

The following Python code example uses the AWS SDK for Python (Boto) synthesize speech with shorter texts for near real-time processing. For more information, see the reference for the [SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/APIReference/API_SynthesizeSpeech.html) operation.

This example uses a short string of plain text. You can use SSML text for more control over the output. For more information, see [Generating speech from SSML documents](ssml.md).

```
import boto3

polly_client = boto3.Session(
                aws_access_key_id=,
    aws_secret_access_key=,
    region_name='us-west-2').client('polly')

response = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3',
                Text = 'This is a sample text to be synthesized.',
                Engine = 'neural')

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
