---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint.html
---

# Set up private access to an Amazon S3 bucket through a VPC endpoint

*Martin Maritsch, Nicolas Jacob Baer, Gabriel Rodriguez Garcia, Shukhrat Khodjaev, Mohan Gowda Purushothama, and Joaquin Rinaudo, Amazon Web Services*

## Summary
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint-summary"></a>

In Amazon Simple Storage Service (Amazon S3), presigned URLs enable you to share files of arbitrary size with target users. By default, Amazon S3 presigned URLs are accessible from the internet within an expiration time window, which makes them convenient to use. However, corporate environments often require access to Amazon S3 presigned URLs to be limited to a private network only.

This pattern presents a serverless solution for securely interacting with Amazon S3 objects by using presigned URLs from a private network without internet traversal. In the architecture, users access an Application Load Balancer through an internal domain name. The architecture routes traffic internally through Amazon API Gateway and a virtual private cloud (VPC) endpoint for the Amazon S3 bucket. The AWS Lambda function generates presigned URLs for file downloads through the private VPC endpoint, which helps enhance security and privacy for sensitive data.

## Prerequisites and limitations
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An Amazon Virtual Private Cloud (Amazon VPC) with a subnet deployed in an AWS account that is connected to the corporate network (for example, through AWS Direct Connect).

**Limitations**
+ The Amazon S3 bucket must have the same name as the domain. Review the [Amazon S3 bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).
+ This sample architecture doesn't include monitoring features for the deployed infrastructure. If your use case requires monitoring, consider adding [AWS monitoring services](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/welcome.html).
+ This sample architecture doesn't include input validation. If your use case requires input validation and an increased level of security, consider [using AWS WAF to protect your API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html).
+ This sample architecture doesn't include access logging with the Application Load Balancer. If your use case requires access logging, consider enabling [load balancer access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html).

## Architecture
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint-architecture"></a>

**Target technology stack**

The target technology stack uses the following AWS services:
+ [**Amazon S3**](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is the core storage service used for uploading, downloading, and storing files.
+ [**Amazon API Gateway**](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) exposes resources and endpoints for interacting with the S3 bucket. This service helps generate presigned URLs for downloading or uploading data.
+ [**AWS Lambda**](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) generates presigned URLs for downloading files from Amazon S3. API Gateway calls the Lambda function.
+ **Amazon VPC** provides network isolation for the deployed resources. The VPC includes subnets and route tables to control traffic flow.
+ **Application Load Balancer** routes incoming traffic either to API Gateway or to the VPC endpoint of the S3 bucket. It allows users from the corporate network to access resources internally.
+ **VPC endpoint for Amazon S3** enables direct, private communication between resources in the VPC and Amazon S3 without traversing the public internet.
+ [**AWS Identity and Access Management**](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)** (IAM)** controls access to AWS resources. You configure permissions to help secure interactions with the API and other services.

**Target architecture**

![Setting up private access to an S3 bucket through a VPC endpoing](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/683ca6a1-789c-4444-bcbf-e4e80d253df3/images/1ca7ee17-d346-4eb9-bf61-ccf42528a401.png)

The diagram illustrates the following:

1. Users from the corporate network can access the Application Load Balancer through an internal domain name. This pattern assumes that a connection exists between the corporate network and the intranet subnet in the AWS account (for example, through an [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) connection).

1. The Application Load Balancer routes incoming traffic either to API Gateway to generate presigned URLs to download or upload data to Amazon S3, or to the VPC endpoint of the S3 bucket. In both scenarios, the Application Load Balancer routes requests internally, so they don't traverse the internet.

1. API Gateway exposes resources and endpoints to interact with the S3 bucket. This example provides an endpoint to download files from the S3 bucket, but you can extend it to provide upload functionality as well.

1. The Lambda function generates the presigned URL to download a file from Amazon S3 by using the domain name of the Application Load Balancer instead of the public Amazon S3 domain.

1. The user receives the presigned URL and uses it to download the file from Amazon S3 by using the Application Load Balancer. The load balancer includes a default route to send traffic that's not intended for the API toward the VPC endpoint of the S3 bucket.

1. The VPC endpoint routes the presigned URL with the custom domain name to the S3 bucket. The S3 bucket must have the same name as the domain.

## Best practices
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint-best-practices"></a>

The sample architecture for this pattern uses [IAM permissions](https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html) to control access to the API. Any user with valid IAM credentials and a policy that allows the API invoke action can call the API. If your use case requires a more complex authorization model, consider [using a different access control mechanism](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html).

## Epics
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint-epics"></a>

### Prepare the network, DNS, and certificate
<a name="prepare-the-network-dns-and-certificate"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Choose the internal domain name | Choose a fully qualified domain name for the internal entry point (for example, `files.example.internal`). The [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket name must exactly match this name, so make sure that it follows the bucket naming rules. | Cloud architect |
| Request a certificate | In [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html), request or import a certificate for the domain name. The [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/) uses the certificate to serve HTTPS. | Cloud architect |
| Create the interface VPC endpoints | In the private subnets, create an interface VPC endpoint for Amazon S3 and one for [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) (execute-api). Attach a security group that allows HTTPS (port 443) only from the Application Load Balancer security group. Note the private IP addresses of both endpoints. | Network administrator |
| Create the DNS record | In an Amazon Route 53 private hosted zone that is associated with the VPC (or in your corporate DNS), create a record that points the domain name to the Application Load Balancer that you create in a later epic. | Network administrator |

### Create and secure the S3 bucket
<a name="create-and-secure-the-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the bucket | Create an Amazon S3 bucket with exactly the same name as the domain name. Keep all Block Public Access settings turned on, and turn on default encryption. | Cloud architect |
| Restrict access to the VPC endpoint | Add a bucket policy that denies all access unless the request comes through the S3 interface endpoint (aws:SourceVpce condition) and uses TLS (aws:SecureTransport). | Cloud architect |
| Upload a test file | Upload a test object to the bucket so that you can verify the download flow later. | Cloud architect |

### Create the presigned URL function and the private API
<a name="create-the-presigned-url-function-and-the-private-api"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Lambda execution role | Create an AWS Identity and Access Management (IAM) role for the [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function that allows only s3:GetObject on the bucket objects, plus the permissions to write logs to Amazon CloudWatch Logs (logs:CreateLogGroup, logs:CreateLogStream, and logs:PutLogEvents) for the function's log group. Don't use wildcard actions or resources. | Cloud architect |
| Create the Lambda function | Create a Lambda function that accepts an object key and returns a presigned GET URL. Configure the Amazon S3 client in your SDK to use the internal domain name (https://<domain-name>) as its endpoint instead of the public Amazon S3 endpoint. Keep Transport Layer Security (TLS) certificate verification turned on, and use a short expiration (for example, 5 minutes). Validate and URL-encode the object key. | App developer |
| Create the private REST API | In Amazon API Gateway, create a private REST API with a GET method (for example, /api/get\_url) that is integrated with the Lambda function. Use IAM authorization (AWS\_IAM). | App developer |
| Restrict the API to the VPC endpoint | Add a resource policy to the API that allows execute-api:Invoke only through the execute-api VPC endpoint. Deploy the API to a stage. | Cloud architect |
| Turn on logging and tracing | Turn on access logging and [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) tracing for the API stage. | Cloud architect |
| Map the domain name to the API | Create a private custom domain name in API Gateway that uses the internal domain name and the ACM certificate, and map it to the API stage. This mapping allows API Gateway to accept requests that arrive through the Application Load Balancer with that host name. | Cloud architect |

### Configure the internal Application Load Balancer
<a name="configure-the-internal-application-load-balancer"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the target groups | Create two IP-type target groups that use HTTPS on port 443. Register the private IP addresses of the execute-api endpoint in one target group and those of the Amazon S3 endpoint in the other. Set the health check success codes to the codes that the endpoints return (for example, 403 for API Gateway and 307 or 405 for Amazon S3). | Network administrator |
| Create the load balancer | Create an internal Application Load Balancer in the intranet subnets. Attach a security group that allows HTTPS only from the corporate network IP ranges. | Network administrator |
| Configure the HTTPS listener and rules | Add an HTTPS listener that uses the ACM certificate. Add a rule that forwards /api/\* to the API Gateway target group, and set the default action to forward to the S3 target group. | Network administrator |
| Turn on access logs | Turn on Application Load Balancer access logs and deliver them to a separate logging bucket. | Network administrator |

### Test the solution and clean up
<a name="test-the-solution-and-clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Request a presigned URL | From the corporate network, send a request that is signed with Signature Version 4 (SigV4) and valid IAM credentials to https://<domain-name>/api/get\_url?key=<test-file>. The response contains a presigned URL that starts with the internal domain name. | Cloud architect |
| Download the file | Open the presigned URL from the corporate network. The file downloads through the Application Load Balancer and the Amazon S3 interface VPC endpoint without traversing the internet. Verify that the same URL doesn't work from outside the corporate network. | Cloud architect |
| Clean up | When you no longer need the resources, delete the Application Load Balancer, target groups, API, Lambda function, VPC endpoints, DNS records, ACM certificate, and Amazon S3 buckets (including the logging bucket). | Cloud architect |

## Troubleshooting
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| S3 object key names with special characters such as number signs (\#) break URL parameters and lead to errors. | Encode URL parameters properly, and make sure that the S3 object key name follows [Amazon S3 guidelines](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html). |

## Related resources
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint-resources"></a>

Amazon S3:
+ [Sharing objects with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html)
+ [Controlling access from VPC endpoints with bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.html)

Amazon API Gateway:
+ [Use VPC endpoint policies for private APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-vpc-endpoint-policies.html)

Application Load Balancer:
+ [Hosting Internal HTTPS Static Websites with ALB, S3, and PrivateLink](https://aws.amazon.com/blogs/networking-and-content-delivery/hosting-internal-https-static-websites-with-alb-s3-and-privatelink/) (AWS blog post)
