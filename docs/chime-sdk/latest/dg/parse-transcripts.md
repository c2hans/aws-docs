---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/parse-transcripts.html
---

# Parsing Amazon Chime SDK transcripts
<a name="parse-transcripts"></a>

Use the following command to parse transcription content from a transcription message. The command parses complete sentences from the transcript-message.txt files.

```
with open('transcript-message.txt') as f:
        for line in f:
            result_json = json.loads(line)["transcript"]["results"][0]
            if result_json['isPartial'] == False:
                print(result_json["alternatives"][0]["transcript"])
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
