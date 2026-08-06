---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint.html
---

# Set up private access to an Amazon S3 bucket through a VPC endpoint
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint"></a>

*Martin Maritsch, Nicolas Jacob Baer, Gabriel Rodriguez Garcia, Shukhrat Khodjaev, Mohan Gowda Purushothama, and Joaquin Rinaudo, Amazon Web Services*

## Summary
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint-summary"></a>

In Amazon Simple Storage Service (Amazon S3), presigned URLs enable you to share files of arbitrary size with target users. By default, Amazon S3 presigned URLs are accessible from the internet within an expiration time window, which makes them convenient to use. However, corporate environments often require access to Amazon S3 presigned URLs to be limited to a private network only.

This pattern presents a serverless solution for securely interacting with S3 objects by using presigned URLs from a private network without internet traversal. In the architecture, users access an Application Load Balancer through an internal domain name. Traffic is routed internally through Amazon API Gateway and a virtual private cloud (VPC) endpoint for the S3 bucket. The AWS Lambda function generates presigned URLs for file downloads through the private VPC endpoint, which helps enhance security and privacy for sensitive data.

## Prerequisites and limitations
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint-prereqs"></a>

**Prerequisites**
+ A VPC that includes a subnet deployed in an AWS account that is connected to the corporate network (for example, through AWS Direct Connect).

**Limitations**
+ The S3 bucket must have the same name as the domain, so we recommend that you check [Amazon S3 bucket naming rules.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html)
+ This sample architecture doesn't include monitoring features for the deployed infrastructure. If your use case requires monitoring, consider adding [AWS monitoring services](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/welcome.html).
+ This sample architecture doesn't include input validation. If your use case requires input validation and an increased level of security, consider [using AWS WAF to protect your API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html).
+ This sample architecture doesn't include access logging with the Application Load Balancer. If your use case requires access logging, consider enabling [load balancer access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html).

**Versions**
+ Python version 3.11 or later
+ Terraform version 1.6 or later

## Architecture
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint-architecture"></a>

**Target technology stack**

The following AWS services are used in the target technology stack:
+ **Amazon S3** is the core storage service used for uploading, downloading, and storing files securely.
+ **Amazon API Gateway** exposes resources and endpoints for interacting with the S3 bucket. This service plays a role in generating presigned URLs for downloading or uploading data.
+ **AWS Lambda** generates presigned URLs for downloading files from Amazon S3. The Lambda function is called by API Gateway.
+ **Amazon VPC** deploys resources within a VPC to provide network isolation. The VPC includes subnets and routing tables to control traffic flow.
+ **Application Load Balancer** routes incoming traffic either to API Gateway or to the VPC endpoint of the S3 bucket. It allows users from the corporate network to access resources internally.
+ **VPC endpoint for Amazon S3** enables direct, private communication between resources in the VPC and Amazon S3 without traversing the public internet.
+ **AWS Identity and Access Management (IAM)** controls access to AWS resources. Permissions are set up to ensure secure interactions with the API and other services.

**Target architecture**

![Setting up private access to an S3 bucket through a VPC endpoing](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/683ca6a1-789c-4444-bcbf-e4e80d253df3/images/1ca7ee17-d346-4eb9-bf61-ccf42528a401.png)

The diagram illustrates the following:

1. Users from the corporate network can access the Application Load Balancer through an internal domain name. We assume that a connection exists between the corporate network and the intranet subnet in the AWS account (for example, through a Direct Connect connection).

1. The Application Load Balancer routes incoming traffic either to API Gateway to generate presigned URLs to download or upload data to Amazon S3, or to the VPC endpoint of the S3 bucket. In both scenarios, requests are routed internally and do not need to traverse the internet.

1. API Gateway exposes resources and endpoints to interact with the S3 bucket. In this example, we provide an endpoint to download files from the S3 bucket, but this could be extended to provide upload functionality as well.

1. The Lambda function generates the presigned URL to download a file from Amazon S3 by using the domain name of the Application Load Balancer instead of the public Amazon S3 domain.

1. The user receives the presigned URL and uses it to download the file from Amazon S3 by using the Application Load Balancer. The load balancer includes a default route to send traffic that's not intended for the API toward the VPC endpoint of the S3 bucket.

1. The VPC endpoint routes the presigned URL with the custom domain name to the S3 bucket. The S3 bucket must have the same name as the domain.

**Automation and scale**

This pattern uses Terraform to deploy the infrastructure from the code repository into an AWS account.

## Tools
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint-tools"></a>

**Tools**
+ [Python](https://www.python.org/) is a general-purpose computer programming language.
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command-line shell.

**Code repository**

The code for this pattern is available in a GitHub repository at [https://github.com/aws-samples/private-s3-vpce](https://github.com/aws-samples/private-s3-vpce).

## Best practices
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint-best-practices"></a>

The sample architecture for this pattern uses [IAM permissions](https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html) to control access to the API. Anyone who has valid IAM credentials can call the API. If your use case requires a more complex authorization model, you might want to [use a different access control mechanism](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html).

## Epics
<a name="set-up-private-access-to-an-amazon-s3-bucket-through-a-vpc-endpoint-epics"></a>

### Deploy the solution in an AWS account
<a name="deploy-the-solution-in-an-aws-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Obtain AWS credentials. | Review your AWS credentials and your access to your account. For instructions, see [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) in the AWS CLI documentation. | AWS DevOps, General AWS |
| Clone the repository. | Clone the GitHub repository provided with this pattern:<pre>git clone https://github.com/aws-samples/private-s3-vpce</pre> | AWS DevOps, General AWS |
| Configure variables. | 1. On your computer, in the GitHub repository, open the `terraform` folder:<pre>cd terraform</pre><br />2. Open the `example.tfvars` file and customize the parameters according to your needs. | AWS DevOps, General AWS |
| Deploy solution. | 1. In the `terraform` folder, run Terraform and pass in the variables that you customized:<pre>terraform apply -var-file="example.tfvars"</pre><br />2. Confirm that the resources shown in the architecture diagram were deployed successfully. | AWS DevOps, General AWS |

### Test the solution
<a name="test-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a test file. | Upload a file to Amazon S3 to create a test scenario for the file download. You can use the [Amazon S3 console](https://console.aws.amazon.com/s3/) or the following AWS CLI command:<pre>aws s3 cp /path/to/testfile s3://your-bucket-name/testfile</pre> | AWS DevOps, General AWS |
| Test presigned URL functionality. | 1. Send a request to the Application Load Balancer to create a presigned URL for the test file by using [awscurl](https://github.com/okigan/awscurl):<pre>awscurl https://your-domain-name/api/get_url?key=testfile</pre><br />This step creates a valid signature from your credentials, which will be validated by API Gateway.<br />2. Parse the link from the response you receive from the previous step, and open the presigned URL to download the file. | AWS DevOps, General AWS |
| Clean up. | Make sure to remove the resources when they are no longer required:<pre>terraform destroy</pre> | AWS DevOps, General AWS |

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
