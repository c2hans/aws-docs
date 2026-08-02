---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/sns-example-list-subscriptions.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs//developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# List Your Amazon SNS Subscriptions
<a name="sns-example-list-subscriptions"></a>

The following example lists the ARNs for your Amazon SNS topic subscriptions and the associated topic in your default region.

```
package main

import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/sns"

    "flag"
    "fmt"
    "os"
)

func main() {
    emailPtr := flag.String("e", "", "The email address of the user subscribing to the topic")
    topicPtr := flag.String("t", "", "The ARN of the topic to which the user subscribes")

    flag.Parse()

    if *emailPtr == "" || *topicPtr == "" {
        fmt.Println("You must supply an email address and topic ARN")
        fmt.Println("Usage: go run SnsSubscribe.go -e EMAIL -t TOPIC-ARN")
        os.Exit(1)
    }

    // Initialize a session that the SDK will use to load
    // credentials from the shared credentials file. (~/.aws/credentials).
    sess := session.Must(session.NewSessionWithOptions(session.Options{
        SharedConfigState: session.SharedConfigEnable,
    }))

    svc := sns.New(sess)

    result, err := svc.Subscribe(&sns.SubscribeInput{
        Endpoint:              emailPtr,
        Protocol:              aws.String("email"),
        ReturnSubscriptionArn: aws.Bool(true), // Return the ARN, even if user has yet to confirm
        TopicArn:              topicPtr,
    })
    if err != nil {
        fmt.Println(err.Error())
        os.Exit(1)
    }

    fmt.Println(*result.SubscriptionArn)
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/go/example_code/sns/SnsListSubscriptions.go) on GitHub.
