---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/go_2_kafka_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon MSK examples using SDK for Go V2
<a name="go_2_kafka_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Amazon MSK.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Serverless examples](#serverless_examples)

## Serverless examples
<a name="serverless_examples"></a>

### Invoke a Lambda function from an Amazon MSK trigger
<a name="serverless_MSK_Lambda_go_2_topic"></a>

The following code example shows how to implement a Lambda function that receives an event triggered by receiving records from an Amazon MSK cluster. The function retrieves the MSK payload and logs the record contents.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-msk-to-lambda) repository.
Consuming an Amazon MSK event with Lambda using Go.

```
package main

import (
	"encoding/base64"
	"fmt"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
)

func handler(event events.KafkaEvent) {
	for key, records := range event.Records {
		fmt.Println("Key:", key)

		for _, record := range records {
			fmt.Println("Record:", record)

			decodedValue, _ := base64.StdEncoding.DecodeString(record.Value)
			message := string(decodedValue)
			fmt.Println("Message:", message)
		}
	}
}

func main() {
	lambda.Start(handler)
}
```
