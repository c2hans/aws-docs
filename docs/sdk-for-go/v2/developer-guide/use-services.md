---
source_url: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/use-services.html
---

# Use the AWS SDK for Go v2 with AWS services
<a name="use-services"></a>

 To make calls to an AWS service, you must first construct a service client instance. A service client provides low-level access to every API action for that service. For example, you create an Amazon S3 service client to make calls to Amazon S3 APIs.

 When you call service operations, you pass in input parameters as a struct. A successful call will result in an output struct containing the service API response. For example, after you successfully call an Amazon S3 create bucket action, the action returns an output struct with the bucket's location.

 For the list of service clients, including their methods and parameters, see the [AWS SDK for Go API Reference](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2).
