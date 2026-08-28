---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

## AWS Snowball Edge
<a name="Welcome_Amazon_Import_Export_Snowball"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

The job management API for AWS Snowball Edge is a network protocol based on HTTP (RFC 2616). For more information on this RFC, see [HTTP (RFC 2616)](https://www.ietf.org/rfc/rfc2616.txt) on the IETF website. For each call to the job management API, you make an HTTP request to the region-specific job management API endpoint for the AWS Region where you want to manage jobs. The API uses JSON (RFC 4627) documents for HTTP request/response bodies.

**Note**
API calls made within the US regions for listing jobs or describing addresses return all jobs or addresses within the US for that account.

The job management API for Snowball Edge is an RPC model. In this model, there is a fixed set of operations and the syntax for each operation is known to clients without any previous interaction. Following, you can find a description of each API operation using an abstract RPC notation, with an operation name that does not appear on the wire. For each operation, the topic specifies the mapping to HTTP request elements.

The specific job management operation to which a given request maps is determined by a combination of the request's method (GET, PUT, POST, or DELETE) and which of the various patterns its Request-URI matches. If the operation is PUT or POST, Snowball Edge extracts call arguments from the Request-URI path segment, query parameters, and the JSON object in the request body.

Although the operation name, such as `CreateJob`, doesn't appear on the wire, these operation names are meaningful in AWS Identity and Access Management (IAM) policies. The operation name is also used to name commands in command-line tools and elements of the AWS SDK APIs. For example, the AWS Command Line Interface (AWS CLI) command `create-job` maps to the `CreateJob` operation. The operation name also appears in CloudTrail logs for Snowball Edge API calls.

For more information about using the job management API, including API endpoints, API version, and permission policies, see [Using the Job Management API](https://docs.aws.amazon.com/snowball/latest/developer-guide/api-using.html) in the * AWS Snowball Edge Developer Guide*.

For information on installing and setting up the AWS CLI, including specifying what regions you want to make AWS CLI calls against, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).

**Note**
The job management API provides a programmatic interface to the same functionality available in the AWS Snow Family Management Console, that is to create and manage jobs for Snowball Edge. To transfer data locally with a Snowball appliance, use the Snowball Edge Client or the S3 SDK Adapter for Snowball Edge. For more information, see [Transferring Data with a Snowball](https://docs.aws.amazon.com/snowball/latest/ug/snowball-data-transfer.html) in the * AWS Snowball Edge User Guide*.
If you use a Snowball Edge, use the Snowball Edge Client to unlock the appliance. For more information, see [Using the Snowball Client](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-client.html) in the * AWS Snowball Edge Developer Guide*.

## AWS Snowball Edge Device Management
<a name="Welcome_AWS_Snow_Device_Management"></a>

 AWS Snowball Edge Device Management allows you to manage your AWS Snowball Edge devices and local AWS services remotely. You can use AWS Snowball Edge Device Management to create and manage tasks such as unlocking or rebooting a device, check device and task status, and manage Amazon EC2-compatible instances and resources on your device. For more information, see [Using AWS Snowball Edge Device Management to manage Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html) in the * AWS Snowball Edge Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
