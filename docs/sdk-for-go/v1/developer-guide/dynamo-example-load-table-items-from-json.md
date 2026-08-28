---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/dynamo-example-load-table-items-from-json.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Creating Amazon DynamoDB Table Items from a JSON File
<a name="dynamo-example-load-table-items-from-json"></a>

The following example uses the DynamoDB [PutItem](https://docs.aws.amazon.com/sdk-for-go/api/service/dynamodb/#DynamoDB.PutItem) operation in a loop to create the items defined in *movie\_data.json* file in the `Movies` table in your default region.

Create the file *DynamoDBLoadItems.go*. Add the following statements to import the Go and AWS SDK for Go packages used in the example.

```
import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/dynamodb"
    "github.com/aws/aws-sdk-go/service/dynamodb/dynamodbattribute"

    "encoding/json"
    "fmt"
    "log"
    "io/ioutil"
    "strconv"
)
```

Create the data structure we use to contain the information about the table item.

```
// Create struct to hold info about new item
type Item struct {
    Year   int
    Title  string
    Plot   string
    Rating float64
}
```

Create a function to get the table items from the JSON file.

```
// Get table items from JSON file
func getItems() []Item {
    raw, err := ioutil.ReadFile("./.movie_data.json")
    if err != nil {
        log.Fatalf("Got error reading file: %s", err)
    }

    var items []Item
    json.Unmarshal(raw, &items)
    return items
}
```

Initialize a session that the SDK will use to load credentials from the shared credentials file `~/.aws/credentials` and region from the shared configuration file `~/.aws/config` and create a new DynamoDB service client.

```
// Initialize a session that the SDK will use to load
// credentials from the shared credentials file ~/.aws/credentials
// and region from the shared configuration file ~/.aws/config.
sess := session.Must(session.NewSessionWithOptions(session.Options{
    SharedConfigState: session.SharedConfigEnable,
}))

// Create DynamoDB client
svc := dynamodb.New(sess)
```

Call **getItems** to get the items. Loop through each item, marshall that data into a map of **AttributeValue** objects, add the item to the `Movies` table, and print out the title and year of the movie added to the table.

```
// Get table items from .movie_data.json
items := getItems()

// Add each item to Movies table:
tableName := "Movies"

for _, item := range items {
    av, err := dynamodbattribute.MarshalMap(item)
    if err != nil {
        log.Fatalf("Got error marshalling map: %s", err)
    }

    // Create item in table Movies
    input := &dynamodb.PutItemInput{
        Item:      av,
        TableName: aws.String(tableName),
    }

    _, err = svc.PutItem(input)
    if err != nil {
        log.Fatalf("Got error calling PutItem: %s", err)
    }

    year := strconv.Itoa(item.Year)

    fmt.Println("Successfully added '" + item.Title + "' (" + year + ") to table " + tableName)
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/go/example_code/dynamodb/DynamoDBLoadItems.go) and a [sample JSON file](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/go/example_code/dynamodb/.movie_data.json) on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
