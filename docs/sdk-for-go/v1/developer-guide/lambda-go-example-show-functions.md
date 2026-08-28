---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/lambda-go-example-show-functions.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Displaying Information about All Lambda Functions
<a name="lambda-go-example-show-functions"></a>

First import the packages we use in this example.

```
import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/lambda"

    "fmt"
    "os"
)
```

Next, create the session and Lambda client.

```
sess := session.Must(session.NewSessionWithOptions(session.Options{
    SharedConfigState: session.SharedConfigEnable,
}))

svc := lambda.New(sess, &aws.Config{Region: aws.String("us-west-2")})
```

Next, call `ListFunctions` and exit if there is an error.

```
result, err := svc.ListFunctions(nil)
if err != nil {
    fmt.Println("Cannot list functions")
    os.Exit(0)
}
```

Finally, display the names and descriptions of the Lambda functions.

```
fmt.Println("Functions:")

for _, f := range result.Functions {
    fmt.Println("Name:        " + aws.StringValue(f.FunctionName))
    fmt.Println("Description: " + aws.StringValue(f.Description))
    fmt.Println("")
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/go/example_code/lambda/aws-go-sdk-lambda-example-show-functions.go) on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
