---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sns-example-publish.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Sending a Message to All Amazon SNS Topic Subscribers
<a name="sns-example-publish"></a>

The following example sends the message supplied on the command line to all subscribers to the Amazon SNS topic with the ARN specified on the command line.

```
package main

import (
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/sns"

    "flag"
    "fmt"
    "os"
)

func main() {
    msgPtr := flag.String("m", "", "The message to send to the subscribed users of the topic")
    topicPtr := flag.String("t", "", "The ARN of the topic to which the user subscribes")

    flag.Parse()

    if *msgPtr == "" || *topicPtr == "" {
        fmt.Println("You must supply a message and topic ARN")
        fmt.Println("Usage: go run SnsPublish.go -m MESSAGE -t TOPIC-ARN")
        os.Exit(1)
    }

    // Initialize a session that the SDK will use to load
    // credentials from the shared credentials file. (~/.aws/credentials).
    sess := session.Must(session.NewSessionWithOptions(session.Options{
        SharedConfigState: session.SharedConfigEnable,
    }))

    svc := sns.New(sess)

    result, err := svc.Publish(&sns.PublishInput{
        Message:  msgPtr,
        TopicArn: topicPtr,
    })
    if err != nil {
        fmt.Println(err.Error())
        os.Exit(1)
    }

    fmt.Println(*result.MessageId)
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/go/example_code/sns/SnsPublish.go) on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
