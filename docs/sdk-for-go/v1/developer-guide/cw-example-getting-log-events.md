---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cw-example-getting-log-events.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Getting Log Events from CloudWatch
<a name="cw-example-getting-log-events"></a>

The following example lists up to 100 of the latest events for a log group’s log stream. Replace LOG-GROUP-NAME with the name of the CloudWatch log group and LOG-STREAM-NAME with the name of the log stream for the log group.

```
package main

import (
    "flag"
    "fmt"

    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/cloudwatchlogs"
)

// GetLogEvents retrieves CloudWatchLog events.
// Inputs:
//     sess is the current session, which provides configuration for the SDK's service clients
//     limit is the maximum number of log events to retrieve
//     logGroupName is the name of the log group
//     logStreamName is the name of the log stream
// Output:
//     If success, a GetLogEventsOutput object containing the events and nil
//     Otherwise, nil and an error from the call to GetLogEvents
func GetLogEvents(sess *session.Session, limit *int64, logGroupName *string, logStreamName *string) (*cloudwatchlogs.GetLogEventsOutput, error) {
    svc := cloudwatchlogs.New(sess)

    resp, err := svc.GetLogEvents(&cloudwatchlogs.GetLogEventsInput{
        Limit:         limit,
        LogGroupName:  logGroupName,
        LogStreamName: logStreamName,
    })
    if err != nil {
        return nil, err
    }

    return resp, nil
}

func main() {
    limit := flag.Int64("l", 100, "The maximum number of events to retrieve")
    logGroupName := flag.String("g", "", "The name of the log group")
    logStreamName := flag.String("s", "", "The name of the log stream")
    flag.Parse()

    if *logGroupName == "" || *logStreamName == "" {
        fmt.Println("You must supply a log group name (-g LOG-GROUP) and log stream name (-s LOG-STREAM)")
        return
    }

    sess := session.Must(session.NewSessionWithOptions(session.Options{
        SharedConfigState: session.SharedConfigEnable,
    }))

    resp, err := GetLogEvents(sess, limit, logGroupName, logStreamName)
    if err != nil {
        fmt.Println("Got error getting log events:")
        fmt.Println(err)
        return
    }

    fmt.Println("Event messages for stream " + *logStreamName + " in log group  " + *logGroupName)

    gotToken := ""
    nextToken := ""

    for _, event := range resp.Events {
        gotToken = nextToken
        nextToken = *resp.NextForwardToken

        if gotToken == nextToken {
            break
        }

        fmt.Println("  ", *event.Message)
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
