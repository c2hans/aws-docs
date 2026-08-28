---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/channel-planning-audio-encodes.html
---

# Identify the audio encodes
<a name="channel-planning-audio-encodes"></a>

You must decide on the number of audio encodes. Follow this procedure for each output group.

1. Determine the maximum number of encodes that are allowed in the output group. The following rules apply for each type of output group.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/channel-planning-audio-encodes.html)

1. If the output group allows more than one audio encode, decide how many you want. These guidelines apply:
   + Each different combination of output codec, coding mode, and language is one encode.

     MediaLive can produce a specific coding mode only if the source contains that coding mode or a higher mode. For example, MediaLive can create 1.0 from a 1.0 or a 2.0 source. It can't create 5.1 from a 2.0 source.
   + MediaLive can produce a specific language only if the source contains that language.
   + MediaLive can produce more than one encode for a given language.

     For example, you could choose to include Spanish in Dolby 5.1 and in AAC 2.0.
   + There is no requirement for the count of encodes to be the same for all languages. For example, you could create two encodes for Spanish, and only one encode for the other languages.

1. Identify the bitrate for each audio encode. You might have obtained requirements or recommendations from your downstream system when you [identified the output encodes](#channel-planning-audio-encodes).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
