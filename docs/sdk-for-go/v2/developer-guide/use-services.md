---
source_url: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/use-services.html
---

# Use the AWS SDK for Go v2 with AWS services
<a name="use-services"></a>

 To make calls to an AWS service, you must first construct a service client instance. A service client provides low-level access to every API action for that service. For example, you create an Amazon S3 service client to make calls to Amazon S3 APIs.

 When you call service operations, you pass in input parameters as a struct. A successful call will result in an output struct containing the service API response. For example, after you successfully call an Amazon S3 create bucket action, the action returns an output struct with the bucket's location.

 For the list of service clients, including their methods and parameters, see the [AWS SDK for Go API Reference](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go v2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
