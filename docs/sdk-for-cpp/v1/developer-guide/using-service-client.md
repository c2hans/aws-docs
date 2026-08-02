---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/using-service-client.html
---

# Making AWS service requests using the AWS SDK for C\+\+
<a name="using-service-client"></a>

 To programmatically access AWS services, SDKs use a client class for each AWS service. For example, if your application needs to access Amazon EC2, your application creates an Amazon EC2 client object to interface with that service. You then use the service client to make requests to that AWS service.

To make a request to an AWS service, you must first create and [configure](configuring.md) a service client. For each AWS service your code uses, it has its own library and its own dedicated type for interacting with it. The client exposes one method for each API operation exposed by the service.

The namespace for a client class follows the convention `Aws::Service::ServiceClient`. For example, the client class for AWS Identity and Access Management (IAM) is `Aws::IAM::IAMClient` and the Amazon S3 client class is `Aws::S3::S3Client`.

All client classes for all AWS services are thread-safe.

When instantiating a client class, AWS credentials must be supplied. Credentials can be supplied from your code, the environment, or the shared AWS `config` file and shared `credentials` file. For more information about credentials, see [instructions for setting up the recommended IAM Identity Center authentication](credentials.md) or use [another credential provider that is available](credproviders.md).
