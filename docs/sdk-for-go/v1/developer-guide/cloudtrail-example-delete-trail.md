---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cloudtrail-example-delete-trail.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Deleting a CloudTrail Trail
<a name="cloudtrail-example-delete-trail"></a>

This example uses the [DeleteTrail](https://docs.aws.amazon.com/sdk-for-go/api/service/cloudtrail/#CloudTrail.DeleteTrail) operation to delete a CloudTrail trail in the `us-west-2` region. It requires one input, the name of the trail.

Choose `Copy` to save the code locally.

Create the file *delete\_trail.go*. Add the following statements to import the Go and AWS SDK for Go packages used in the example.

```
import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/cloudtrail"

    "flag"
    "fmt"
)
```

Get the name of the trail. If the trail name is missing, display an error message and exit.

```
trailNamePtr := flag.String("n", "", "The name of the trail to delete")

flag.Parse()

if *trailNamePtr == "" {
    fmt.Println("You must supply a trail name")
    return
}
```

Initialize the session that the SDK uses to load credentials from the shared credentials file `.aws/credentials` in your home folder and create the client.

```
sess := session.Must(session.NewSessionWithOptions(session.Options{
    SharedConfigState: session.SharedConfigEnable,
}))
```

Create a CloudTrail client and call **DeleteTrail** with the trail name. If an error occurs, print the error and exit. If no error occurs, print a success message.

```
svc := cloudtrail.New(sess)

_, err := svc.DeleteTrail(&cloudtrail.DeleteTrailInput{Name: aws.String(*trailNamePtr)})
if err != nil {
    fmt.Println("Got error calling CreateTrail:")
    fmt.Println(err.Error())
    return
}

fmt.Println("Successfully deleted trail", *trailNamePtr)
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/go/example_code/cloudtrail/delete_trail.go) on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
