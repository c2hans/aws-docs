---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/go_2_cloudwatch-logs_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# CloudWatch Logs examples using SDK for Go V2
<a name="go_2_cloudwatch-logs_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with CloudWatch Logs.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `StartLiveTail`
<a name="cloudwatch-logs_StartLiveTail_go_2_topic"></a>

The following code example shows how to use `StartLiveTail`.

**SDK for Go V2**
Include the required files.

```
import (
	"context"
	"log"
	"time"

	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs"
	"github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs/types"
)
```
Handle the events from the Live Tail session.

```
func handleEventStreamAsync(stream *cloudwatchlogs.StartLiveTailEventStream) {
	eventsChan := stream.Events()
	for {
		event := <-eventsChan
		switch e := event.(type) {
		case *types.StartLiveTailResponseStreamMemberSessionStart:
			log.Println("Received SessionStart event")
		case *types.StartLiveTailResponseStreamMemberSessionUpdate:
			for _, logEvent := range e.Value.SessionResults {
				log.Println(*logEvent.Message)
			}
		default:
			// Handle on-stream exceptions
			if err := stream.Err(); err != nil {
				log.Fatalf("Error occured during streaming: %v", err)
			} else if event == nil {
				log.Println("Stream is Closed")
				return
			} else {
				log.Fatalf("Unknown event type: %T", e)
			}
		}
	}
}
```
Start the Live Tail session.

```
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		panic("configuration error, " + err.Error())
	}
	client := cloudwatchlogs.NewFromConfig(cfg)

	request := &cloudwatchlogs.StartLiveTailInput{
		LogGroupIdentifiers:   logGroupIdentifiers,
		LogStreamNames:        logStreamNames,
		LogEventFilterPattern: logEventFilterPattern,
	}

	response, err := client.StartLiveTail(context.TODO(), request)
	// Handle pre-stream Exceptions
	if err != nil {
		log.Fatalf("Failed to start streaming: %v", err)
	}

	// Start a Goroutine to handle events over stream
	stream := response.GetStream()
	go handleEventStreamAsync(stream)
```
Stop the Live Tail session after a period of time has elapsed.

```
	// Close the stream (which ends the session) after a timeout
	time.Sleep(10 * time.Second)
	stream.Close()
	log.Println("Event stream closed")
```
+  For API details, see [StartLiveTail](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs#Client.StartLiveTail) in *AWS SDK for Go API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
