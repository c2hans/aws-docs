---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/consolidate-amazon-s3-presigned-url-generation-and-object-downloads-by-using-an-endpoint-associated-with-static-ip-addresses.html
---

# Consolidate Amazon S3 presigned URL generation and object downloads by using an endpoint associated with static IP addresses
<a name="consolidate-amazon-s3-presigned-url-generation-and-object-downloads-by-using-an-endpoint-associated-with-static-ip-addresses"></a>

*Song Jin, Eunhye Jo, and Jun Soung Lee, Amazon Web Services*

## Summary
<a name="consolidate-amazon-s3-presigned-url-generation-and-object-downloads-by-using-an-endpoint-associated-with-static-ip-addresses-summary"></a>

This pattern simplifies access to Amazon Simple Storage Service (Amazon S3) by creating secure, custom presigned URLs for object downloads. The solution provides a single endpoint with a unique domain and static IP addresses. It's tailored for customers who require consolidation of both API and Amazon S3 endpoints under a unified domain with static IP addresses. The use case involves users following an IP and domain allowlist firewall policy, limiting API access to specific domains and IP addresses.

The architecture employs key AWS services, including AWS Global Accelerator, Amazon API Gateway, AWS Lambda, Application Load Balancer, AWS PrivateLink, and Amazon S3. This design centralizes the API for generating presigned URLs and the Amazon S3 endpoint under a single domain, linked to an accelerator with two static IP addresses. Consequently, users can effortlessly request presigned URLs and download Amazon S3 objects through a unified domain endpoint with static IP addresses.

This architecture is especially beneficial for customers with strict policies or compliance requirements, such as those in the public, medical, and finance sectors.

## Prerequisites and limitations
<a name="consolidate-amazon-s3-presigned-url-generation-and-object-downloads-by-using-an-endpoint-associated-with-static-ip-addresses-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A public hosted zone for your custom domain name
+ A domain imported in AWS Certificate Manager (ACM) in the AWS Region of your choice

**Limitations**
+ The Amazon S3 bucket name must match the domain name of the endpoint. This requirement is to ensure that the Amazon S3 endpoint can be served through the single API endpoint.
+ The custom domain name used in API Gateway should align with the domain name of the single API endpoint.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="consolidate-amazon-s3-presigned-url-generation-and-object-downloads-by-using-an-endpoint-associated-with-static-ip-addresses-architecture"></a>

The following diagram shows the target architecture and workflow for this pattern.

![Components and workflow for presigned URL generation and object download.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e19ebcb5-2138-481e-952e-3cfee9ad9e97/images/effd197c-d4d7-4990-8b66-3eb1c64aab4c.png)

The diagram illustrates the following concept and workflow:

1. A user initiates a request to generate a presigned URL by using the custom endpoint served through AWS Global Accelerator, using the custom domain name and associated IP addresses.

1. A Lambda function generates the presigned URL, pointing to the custom endpoint. It responds with a 301 redirect that contains the generated presigned URL. Through the redirected presigned URL, the user downloads the object automatically by using the custom endpoint served through Global Accelerator.

The components of the overall architecture for presigned URL generation and object download workflow are as follows:
+ Provisioning of static IP addresses by Global Accelerator.
+ Registration of the accelerator’s alias as an A record into the Amazon Route 53 public hosted zone with the custom domain name.
+ Creation of an Amazon S3 bucket with a bucket name that matches the registered custom domain name.
+ Creation of VPC endpoints for API Gateway and the Amazon S3 service.
+ Configuration of an internal-facing Application Load Balancer to connect to Global Accelerator.
+ Assignment of a custom domain name for API Gateway with an ACM certificate attached.
+ Deployment of a private API Gateway integrated with a Lambda function.
+ The Lambda function is equipped with an AWS Identity and Access Management (IAM) role attached (with [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) permissions).

## Tools
<a name="consolidate-amazon-s3-presigned-url-generation-and-object-downloads-by-using-an-endpoint-associated-with-static-ip-addresses-tools"></a>

**AWS services**
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) helps you create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale.
+ [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/) distribute incoming application traffic across multiple targets, such as Amazon Elastic Compute Cloud (Amazon EC2) instances, in multiple Availability Zones.
+ [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) helps you create, store, and renew public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications.
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) is a global service that supports endpoints in multiple AWS Regions. You can create accelerators that direct traffic to optimal endpoints over the AWS global network. This improves the availability and performance of your internet applications that are used by a global audience.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) helps you create unidirectional, private connections from your virtual private clouds (VPCs) to services outside of the VPC.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) is a highly available and scalable DNS web service.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other tools**
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

**Code repository**

You can deploy this pattern by using either the AWS CDK or Terraform based on your preference. The [Epics](#consolidate-amazon-s3-presigned-url-generation-and-object-downloads-by-using-an-endpoint-associated-with-static-ip-addresses-epics) section contains instructions for both deployment methods. The code for this pattern is available in the following GitHub repositories:
+ **AWS CDK** – [s3-presignedurl-staticips-endpoint-with-cdk](https://github.com/aws-samples/s3-presignedurl-staticips-endpoint-with-cdk)
+ **Terraform** – [s3-presignedurl-staticips-endpoint-with-terraform](https://github.com/aws-samples/s3-presignedurl-staticips-endpoint-with-terraform)

## Best practices
<a name="consolidate-amazon-s3-presigned-url-generation-and-object-downloads-by-using-an-endpoint-associated-with-static-ip-addresses-best-practices"></a>
+ To enhance security in the production environment, it’s crucial to implement authorization mechanisms, such as [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html), to restrict access to the `PresignedUrl` generation API.
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics
<a name="consolidate-amazon-s3-presigned-url-generation-and-object-downloads-by-using-an-endpoint-associated-with-static-ip-addresses-epics"></a>

### Prepare the environment
<a name="prepare-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Decide on a domain name. | Decide on a public domain name for the unified Amazon S3 endpoint. The domain name is also used as the Amazon S3 bucket name. | AWS administrator, Network administrator |
| Create a public hosted zone. | [Create a public hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingHostedZone.html) in Amazon Route 53. Its domain name must match the domain name that’s used in API Gateway. | AWS administrator, Network administrator |
| Prepare an SSL certificate. | Use AWS Certificate Manager (ACM) to [request](https://docs.aws.amazon.com/acm/latest/userguide/acm-public-certificates.html) or [import](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) an SSL certificate for your web application domain. | AWS administrator, Network administrator |

### Deploy the pattern with Terraform
<a name="deploy-the-pattern-with-terraform"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the Terraform development environment. | To set up the development environment, do the following:1. [Install Terraform](https://developer.hashicorp.com/terraform/install) version 1.0 or later.<br />2. Clone the GitHub [s3-presignedurl-staticips-endpoint-with-terraform](https://github.com/aws-samples/s3-presignedurl-staticips-endpoint-with-terraform) repository by running the following command in a terminal window:<br />`git clone https://github.com/aws-samples/s3-presignedurl-staticips-endpoint-with-terraform.git` | AWS administrator, Cloud administrator |
| Modify the `.tfvars` and ** **`provider.tf` files. | 1. **Create the required **`.tfvars`** files – ** Create `apg.tfvars` files in both the `1.vpc_alb_ga` and `2.apigw_s3_lambda` directories. These files will contain your environment-specific variable values.For `1.vpc_alb_ga/apg.tfvars`, create a file with the following template:<pre>hcl <br /> environment_name = "test"<br /> domain           = "your-domain.com"<br /> s3_bucket_prefix = "your-bucket-prefix"<br /> aws_region       = "ap-northeast-2" # Change to your preferred region</pre>For `2.apigw_s3_lambda/apg.tfvars`, create a file with the following template (you'll need to update the `vpc_id` after completing step 1):<pre>hcl <br /> vpc_id           = "vpc-xxxxxxxxx"  # Update this with the VPC ID output from step 1<br /> environment_name = "test"<br /> domain           = "your-domain.com"<br /> s3_bucket_prefix = "your-bucket-prefix"<br /> aws_region       = "ap-northeast-2" # Change to your preferred region</pre><br />2. **Modify the **`provider.tf` **files** ** – ** In both the `1.vpc_alb_ga` and `2.apigw_s3_lambda` folders, edit the `provider.tf` files to match your local AWS configuration:<pre>hcl <br /> provider "aws" {<br />  region  = "ap-northeast-2"  # Change to your preferred region<br />  profile = "apg"             # Change to your AWS profile name  <br />}</pre>**Note the following:**+ Replace the placeholder values in the `.tfvars` files with your actual values.<br />+ After completing the first Terraform deployment (`1.vpc_alb_ga`), update the `vpc_id` value in `2.apigw_s3_lambda/apg.tfvars` with the VPC ID from the output.<br />+ Make sure that your AWS profile name in the `provider.tf` file matches an existing profile in your `~/.aws/credentials` file.<br />+ The domain value should match your Route 53 hosted zone domain.<br />+ The `s3_bucket_prefix` combined with domain will form your Amazon S3 bucket name (for example, `your-bucket-prefix.your-domain.com`).<br />+ If you change `aws_region`, you might also need to update the hardcoded availability zones in the `main.tf` files to match your chosen AWS Region. | AWS administrator, Cloud administrator |
| Provision network resources. | To provision network resources, run the following commands:<pre>cd ./2.vpc_alb_ga<br />terraform init<br />terraform plan --var-file=apg.tfvars<br />terraform apply --var-file=apg.tfvars</pre><br />During the `apply `command’s execution, type **yes** when prompted. | AWS administrator, Cloud administrator |
| Provision API Gateway, Amazon S3, and Lambda. | To provision network resources, use the following commands:<pre>cd ./2.apigw_s3_lambda<br />terraform init<br />terraform plan --var-file=apg.tfvars<br />terraform apply --var-file=apg.tfvars</pre> | AWS administrator, Cloud administrator |

### Deploy the pattern with AWS CDK
<a name="deploy-the-pattern-with-cdk"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the AWS CDK development environment. | To set up the development environment, do the following:1. [Install the AWS CDK.](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html)<br />2. Clone the GitHub [s3-presignedurl-staticips-endpoint-with-cdk](https://github.com/aws-samples/s3-presignedurl-staticips-endpoint-with-cdk) repository by running the following command in a terminal window:<br />`git clone https://github.com/aws-samples/s3-presignedurl-staticips-endpoint-with-cdk.git` | AWS administrator, Cloud administrator |
| Configure domain settings in the `config/index.ts` file. | To edit the options of the constant variable, use the following commands:<pre>export const options = {<br />    certificateArn: '{arn of the acm which created before}',<br />    dnsAttr: {<br />        zoneName: '{public hosted zone name}',<br />        hostedZoneId: 'hosted zone Id',<br />    },<br />    domainNamePrefix: '{Prefix for the domain}',<br />    presignPath: 'presign',<br />    objectsPath: 'objects',<br />};</pre><br />In the commands, replace each placeholder with your own information:+ Replace `'{arn of the acm which created before}'` with your ACM certificate Amazon Resource Name (ARN).<br />+ Replace `'{public hosted zone name}'` with your domain name.<br />+ Replace `'hosted zone Id'` with your Route 53 hosted zone ID.<br />+ Replace `'{Prefix for the domain}'` with the domain prefix that you want to use.<br />+ Optionally, modify `'presign'` and `'objects'` paths if needed for your specific use case. | AWS administrator, Cloud administrator |
| Deploy the stacks. | To deploy two stacks, one for the virtual private cloud (VPC) and another for the application, use the following command:<pre>$ npm install <br />$ cdk synth <br />$ cdk deploy --all</pre> | AWS administrator, Cloud administrator |

### Test the pattern
<a name="test-the-pattern"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify the IP addresses of the endpoint. | To verify that the domain for this pattern has static IP addresses, use the following command:<pre>nslookup ${s3-bucket-prefix}.${domain}</pre> | Network administrator |
| Upload a test file that you can later download. | Upload the test file to the `'/objects'` folder in the Amazon S3 bucket. | AWS administrator, Cloud administrator |
| Invoke the API to generate a presigned URL. | To generate a presigned URL, call the URL from a browser or API client (for example, [Postman](https://www.postman.com/product/what-is-postman/)) using the following format:<pre>https://${s3-bucket-prefix}.${domain}/presign/objects/${uploaded-filename}</pre><br />Replace the placeholder values in `${s3-bucket-prefix}` and `${domain}` with the values that you set in previous steps. | App owner |
| Check the result. | The expected result is that you should receive a 301 (Moved Permanently) redirect status code. This response will contain the presigned URL, which should automatically initiate the download of your test file. | Test engineer |

### Clean up with Terraform
<a name="clean-up-with-terraform"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Destroy API Gateway, Amazon S3, and Lambda resources. | To delete resources, use the following commands:<pre>cd ./2.apigw_s3_lambda<br />terraform init<br />terraform plan --destroy --var-file=apg.tfvars<br />terraform destroy --var-file=apg.tfvars<br /></pre> | AWS administrator, Cloud administrator |
| Destroy network resources. | To delete network resources, use the following commands:<pre>cd ./1.vpc_alb_ga<br />terraform init<br />terraform plan --destroy --var-file=apg.tfvars<br />terraform destroy --var-file=apg.tfvars<br /></pre> | AWS administrator, Cloud administrator |

### Clean up with AWS CDK
<a name="clean-up-with-cdk"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Destroy the stacks. | To destroy both the VPC and application stacks, use the following command:<pre>$ cdk destroy --all</pre> | AWS administrator, Cloud administrator |
| Empty and delete the Amazon S3 buckets. | [Empty](https://docs.aws.amazon.com/AmazonS3/latest/userguide/empty-bucket.html) and [delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html) the object Amazon S3 bucket and the logs Amazon S3 bucket that are not deleted by default.<br />The Amazon S3 bucket names are `${s3-bucket-prefix}.${domain}` and `${s3-bucket-prefix}.${domain}-logs`.<br />If you prefer to use the [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) for deleting the buckets, use the following commands:<pre>$ aws s3 rm s3://${s3-bucket-prefix}.${domain} --recursive<br />$ aws s3 rb s3://${s3-bucket-prefix}.${domain} --force<br />$ aws s3 rm s3://${s3-bucket-prefix}.${domain}-logs --recursive<br />$ aws s3 rb s3://${s3-bucket-prefix}.${domain}-logs --force</pre><br />Replace `${s3-bucket-prefix}` and `${domain}` with the values you set in previous steps.,/p> | AWS administrator, Cloud administrator |

## Related resources
<a name="consolidate-amazon-s3-presigned-url-generation-and-object-downloads-by-using-an-endpoint-associated-with-static-ip-addresses-resources"></a>

**AWS Blogs**
+ [Accessing an Amazon API Gateway via static IP addresses provided by AWS Global Accelerator](https://aws.amazon.com/blogs/networking-and-content-delivery/accessing-an-aws-api-gateway-via-static-ip-addresses-provided-by-aws-global-accelerator/)
+ [Generate a presigned URL in modular AWS CDK for JavaScript](https://aws.amazon.com/blogs/developer/generate-presigned-url-modular-aws-sdk-javascript/)
+ [Hosting Internal HTTPS Static Websites with ALB, S3, and PrivateLink](https://aws.amazon.com/blogs/networking-and-content-delivery/hosting-internal-https-static-websites-with-alb-s3-and-privatelink/)
