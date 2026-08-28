---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/polly-example-synthesize-speech.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Synthesizing Speech
<a name="polly-example-synthesize-speech"></a>

This example uses the [SynthesizeSpeech](https://docs.aws.amazon.com/sdk-for-go/api/service/polly/#Polly.SynthesizeSpeech) operation to get the text from a file and produce an MP3 file containing the synthesized speech.

Choose `Copy` to save the code locally.

Create the file *pollySynthesizeSpeech.go*. Import the packages used in the example.

```
import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/polly"

    "fmt"
    "os"
    "strings"
    "io"
    "io/ioutil"
)
```

Get the name of the text file from the command line.

```
if len(os.Args) != 2 {
    fmt.Println("You must supply an alarm name")
    os.Exit(1)
}

fileName := os.Args[1]
```

Open the text file and read the contents as a string.

```
contents, err := ioutil.ReadFile(fileName)
s := string(contents[:])
```

Initialize a session that the SDK will use to load credentials from the shared credentials file `~/.aws/credentials`, load your configuration from the shared configuration file `~/.aws/config`, and create an Amazon Polly client.

```
sess := session.Must(session.NewSessionWithOptions(session.Options{
    SharedConfigState: session.SharedConfigEnable,
}))

svc := polly.New(sess)
```

Create the input for and call `SynthesizeSpeech`.

```
input := &polly.SynthesizeSpeechInput{OutputFormat: aws.String("mp3"), Text: aws.String(s), VoiceId: aws.String("Joanna")}

output, err := svc.SynthesizeSpeech(input)
```

Save the resulting synthesized speech as an MP3 file.

```
names := strings.Split(fileName, ".")
name := names[0]
mp3File := name + ".mp3"

outFile, err := os.Create(mp3File)
defer outFile.Close()
```

**Note**
The resulting MP3 file is in the MPEG-2 format.

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/go/example_code/polly/pollySynthesizeSpeech.go) on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
