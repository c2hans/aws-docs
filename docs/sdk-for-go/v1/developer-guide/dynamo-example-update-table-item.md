---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/dynamo-example-update-table-item.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Updating an Amazon DynamoDB Table Item
<a name="dynamo-example-update-table-item"></a>

The following example uses the DynamoDB [UpdateItem](https://docs.aws.amazon.com/sdk-for-go/api/service/dynamodb/#DynamoDB.UpdateItem) operation to update the rating to **0.5** for the item with the `year` **2015** and `title` **The Big New Movie** in the `Movies` table in your default region.

Create the file *DynamoDBUpdateItem.go*. Add the following statements to import the Go and AWS SDK for Go packages used in the example.

```
import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/dynamodb"

    "fmt"
    "log"
)
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

Call **UpdateItem** to add the item to the table. If we encounter an error, print the error message. Otherwise, display a message that the item was updated.

```
// Update item in table Movies
tableName := "Movies"
movieName := "The Big New Movie"
movieYear := "2015"
movieRating := "0.5"

input := &dynamodb.UpdateItemInput{
    ExpressionAttributeValues: map[string]*dynamodb.AttributeValue{
        ":r": {
            N: aws.String(movieRating),
        },
    },
    TableName: aws.String(tableName),
    Key: map[string]*dynamodb.AttributeValue{
        "Year": {
            N: aws.String(movieYear),
        },
        "Title": {
            S: aws.String(movieName),
        },
    },
    ReturnValues:     aws.String("UPDATED_NEW"),
    UpdateExpression: aws.String("set Rating = :r"),
}

_, err := svc.UpdateItem(input)
if err != nil {
    log.Fatalf("Got error calling UpdateItem: %s", err)
}

fmt.Println("Successfully updated '" + movieName + "' (" + movieYear + ") rating to " + movieRating)
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/go/example_code/dynamodb/DynamoDBUpdateItem.go) on GitHub.
