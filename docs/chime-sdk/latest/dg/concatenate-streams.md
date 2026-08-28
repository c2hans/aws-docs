---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/concatenate-streams.html
---

# Concatenating data streams for Amazon Chime SDK media capture pipelines
<a name="concatenate-streams"></a>

**Note**
To automate the process of concatenating media capture artifacts, refer to [Creating media concatenation pipelines for Amazon Chime SDK meetings](create-concat-pipe.md) in this guide.

This example uses ffmpeg to concatenate video or audio files into a single mp4 file. First, create a filelist.txt file that contains all the input files. Use this format:

```
file 'input1.mp4'
file 'input2.mp4'
file 'input3.mp4'
```

Next, use this command to concatenate the input file:

```
ffmpeg -f concat -i filelist.txt -c copy output.mp4
```

For more information about media concatenation pipelines, refer to [Creating media concatenation pipelines for Amazon Chime SDK meetings](create-concat-pipe.md) in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
