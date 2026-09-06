---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/go_2_docdb_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon DocumentDB examples using SDK for Go V2
<a name="go_2_docdb_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Amazon DocumentDB.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Serverless examples](#serverless_examples)

## Serverless examples
<a name="serverless_examples"></a>

### Invoke a Lambda function from a Amazon DocumentDB trigger
<a name="serverless_DocumentDB_Lambda_go_2_topic"></a>

The following code example shows how to implement a Lambda function that receives an event triggered by receiving records from a DocumentDB change stream. The function retrieves the DocumentDB payload and logs the record contents.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-docdb-to-lambda) repository.
Consuming a Amazon DocumentDB event with Lambda using Go.

```
package main

import (
	"context"
	"encoding/json"
	"fmt"

	"github.com/aws/aws-lambda-go/lambda"
)

type Event struct {
	Events []Record `json:"events"`
}

type Record struct {
	Event struct {
		OperationType string `json:"operationType"`
		NS            struct {
			DB   string `json:"db"`
			Coll string `json:"coll"`
		} `json:"ns"`
		FullDocument interface{} `json:"fullDocument"`
	} `json:"event"`
}

func main() {
	lambda.Start(handler)
}

func handler(ctx context.Context, event Event) (string, error) {
	fmt.Println("Loading function")
	for _, record := range event.Events {
		logDocumentDBEvent(record)
	}

	return "OK", nil
}

func logDocumentDBEvent(record Record) {
	fmt.Printf("Operation type: %s\n", record.Event.OperationType)
	fmt.Printf("db: %s\n", record.Event.NS.DB)
	fmt.Printf("collection: %s\n", record.Event.NS.Coll)
	docBytes, _ := json.MarshalIndent(record.Event.FullDocument, "", "  ")
	fmt.Printf("Full document: %s\n", string(docBytes))
}
```
