---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sns-example-create-topic.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Creating an Amazon SNS Topic
<a name="sns-example-create-topic"></a>

The following example creates a topic with the name from the command line, in your default region, and displays the resulting topic ARN.

```
package main

import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/sns"

    "fmt"
    "os"
)

func main() {
    if len(os.Args) < 2 {
        fmt.Println("You must supply a topic name")
        fmt.Println("Usage: go run SnsCreateTopic.go TOPIC")
        os.Exit(1)
    }

    // Initialize a session that the SDK will use to load
    // credentials from the shared credentials file. (~/.aws/credentials).
    sess := session.Must(session.NewSessionWithOptions(session.Options{
        SharedConfigState: session.SharedConfigEnable,
    }))

    svc := sns.New(sess)

    result, err := svc.CreateTopic(&sns.CreateTopicInput{
        Name: aws.String(os.Args[1]),
    })
    if err != nil {
        fmt.Println(err.Error())
        os.Exit(1)
    }

    fmt.Println(*result.TopicArn)
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/go/example_code/sns/SnsCreateTopic.go) on GitHub.
