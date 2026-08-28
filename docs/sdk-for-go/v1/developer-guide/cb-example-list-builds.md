---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cb-example-list-builds.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Listing Your AWS CodeBuild Project Builds
<a name="cb-example-list-builds"></a>

The following example displays information about your AWS CodeBuild project builds, including the name of the project, when the build started, and how long each phase of the build took, in seconds.

```
package main

import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/codebuild"
    "fmt"
    "os"
)

// Lists the CodeBuild builds for all projects in the region configured in the shared config
func main() {
    // Initialize a session in us-west-2 that the SDK will use to load
    // credentials from the shared credentials file ~/.aws/credentials.
    sess, err := session.NewSession(&aws.Config{
        Region: aws.String("us-west-2")},
    )

    // Create CodeBuild service client
    svc := codebuild.New(sess)

    // Get the list of builds
    names, err := svc.ListBuilds(&codebuild.ListBuildsInput{SortOrder: aws.String("ASCENDING")})

    if err != nil {
        fmt.Println("Got error listing builds: ", err)
        os.Exit(1)
    }

    // Get information about each build
    builds, err := svc.BatchGetBuilds(&codebuild.BatchGetBuildsInput{Ids: names.Ids})

    if err != nil {
        fmt.Println("Got error getting builds: ", err)
        os.Exit(1)
    }

    for _, build := range builds.Builds {
        fmt.Printf("Project: %s\n", aws.StringValue(build.ProjectName))
        fmt.Printf("Phase:   %s\n", aws.StringValue(build.CurrentPhase))
        fmt.Printf("Status:  %s\n", aws.StringValue(build.BuildStatus))
        fmt.Println("")
    }
}
```

Choose `Copy` to save the code locally. See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/go/example_code/codebuild/cb_list_builds.go) on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
