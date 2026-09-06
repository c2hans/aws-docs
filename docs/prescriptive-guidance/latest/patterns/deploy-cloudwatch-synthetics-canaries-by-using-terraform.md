---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-cloudwatch-synthetics-canaries-by-using-terraform.html
---

# Deploy CloudWatch Synthetics canaries by using Terraform
<a name="deploy-cloudwatch-synthetics-canaries-by-using-terraform"></a>

*Dhrubajyoti Mukherjee and Jean-Francois Landreau, Amazon Web Services*

## Summary
<a name="deploy-cloudwatch-synthetics-canaries-by-using-terraform-summary"></a>

It’s important to validate the health of a system from a customer perspective and confirm that customers are able to connect. This is more difficult when the customers don’t constantly call the endpoint. [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) supports the creation of canaries, which can test both public and private endpoints. By using canaries, you can know the status of a system even if it isn’t in use. These canaries are either Node.js Puppeteer scripts or Python Selenium scripts.

This pattern describes how to use HashiCorp Terraform to deploy canaries that test private endpoints. It embeds a Puppeteer script that tests whether a URL returns `200-OK`. The Terraform script can then be integrated with the script that deploys the private endpoint. You can also modify the solution to monitor public endpoints.

## Prerequisites and limitations
<a name="deploy-cloudwatch-synthetics-canaries-by-using-terraform-prereqs"></a>

**Prerequisites **
+ An active Amazon Web Services (AWS) account with a virtual private cloud (VPC) and private subnets
+ The URL of the endpoint that can be reached from the private subnets
+ Terraform installed in the deployment environment

**Limitations **

The current solution works for the following CloudWatch Synthetics runtime versions:
+ syn-nodejs-puppeteer-3.4
+ syn-nodejs-puppeteer-3.5
+ syn-nodejs-puppeteer-3.6
+ syn-nodejs-puppeteer-3.7

As new runtime versions are released, you might need to update the current solution. You will also need to modify the solution to keep up with security updates.

**Product versions**
+ Terraform 1.3.0

## Architecture
<a name="deploy-cloudwatch-synthetics-canaries-by-using-terraform-architecture"></a>

Amazon CloudWatch Synthetics is based on CloudWatch, Lambda, and Amazon Simple Storage Service (Amazon S3). Amazon CloudWatch offers a wizard to create the canaries and a dashboard that displays the status of the canary runs. The Lambda function runs the script. Amazon S3 stores the logs and screenshots from the canary runs.

This pattern simulates a private endpoint through an Amazon Elastic Compute Cloud (Amazon EC2) instance deployed in the targeted subnets. The Lambda function requires elastic network interfaces in the VPC where the private endpoint is deployed.

![Description follows the diagram.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/73ed0103-ec45-4653-bb29-f402a88f0c64/images/39aaed0f-f259-4f2a-98fb-8e3a340d0b02.png)

The diagram shows the following:

1. The Synthetics canary initiates the canary Lambda function.

1. The canary Lambda function connects to the elastic network interface.

1. The canary Lambda function monitors the status of the endpoint.

1. The Synthetics canary pushes run data to the S3 bucket and CloudWatch metrics.

1. A CloudWatch alarm is initiated based on the metrics.

1. The CloudWatch alarm initiates the Amazon Simple Notification Service (Amazon SNS) topic.

## Tools
<a name="deploy-cloudwatch-synthetics-canaries-by-using-terraform-tools"></a>

**AWS services**
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS. This pattern uses VPC endpoints and elastic network interfaces.

**Other services**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an open-source infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources. This pattern uses Terraform to deploy the infrastructure.
+ [Puppeteer](https://pptr.dev/) is a Node.js library. The CloudWatch Synthetics runtime uses the Puppeteer framework.

**Code**

The solution is available in the GitHub [cloud watch-synthetics-canary-terraform](https://github.com/aws-samples/cloudwatch-synthetics-canary-terraform) repository. For more information, see the *Additional information* section.

## Epics
<a name="deploy-cloudwatch-synthetics-canaries-by-using-terraform-epics"></a>

### Implement the solution for monitoring a private URL
<a name="implement-the-solution-for-monitoring-a-private-url"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Gather requirements for monitoring the private URL. | Gather the full URL definition: domain, parameters, and headers. To communicate privately to Amazon S3 and Amazon CloudWatch, use VPC endpoints. Note how the VPC and subnets are accessible to the endpoint. Consider the frequency of canary runs. | Cloud architect, Network administrator |
| Modify the existing solution to monitor the private URL. | Modify the `terraform.tfvars` file:+ `name` – The name of your canary.<br />+ `runtime_version` – The runtime version of the canary. We recommend using syn-nodejs-puppeteer-3.7.<br />+ `take_screenshot` – Whether a screenshot should be taken.<br />+ `api_hostname` – The hostname of the endpoint that is monitored.<br />+ `api_path` – The path of the endpoint that is monitored.<br />+ `vpc_id` – The VPC ID that is used by the canary Lambda function.<br />+ `subnet_ids` – The subnet IDs that are used by the canary Lambda function.<br />+ `frequency` – The run frequency of the canary in minutes.<br />+ `alert_sns_topic` –  The SNS topic to which the CloudWatch alarm notification is sent. | Cloud architect |
| Deploy and operate the solution. | To deploy the solution, do the following:1. From the `cloudwatch-synthetics-canary-terraform` directory in your development environment, initialize Terraform.<pre>terraform init</pre><br />2. Plan and review the changes.<pre>terraform plan</pre><br />3. Deploy the solution.<pre>terraform apply</pre> | Cloud architect, DevOps engineer |

## Troubleshooting
<a name="deploy-cloudwatch-synthetics-canaries-by-using-terraform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Deletion of the provisioned resources gets stuck. | Manually delete the canary Lambda function, corresponding elastic network interface, and security group, in that order. |

## Related resources
<a name="deploy-cloudwatch-synthetics-canaries-by-using-terraform-resources"></a>
+ [Using synthetic monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
+ [Monitor API Gateway endpoints with Amazon CloudWatch Synthetics](https://aws.amazon.com/blogs/mt/monitor-api-gateway-endpoints-with-amazon-cloudwatch-synthetics/) (blog post)

## Additional information
<a name="deploy-cloudwatch-synthetics-canaries-by-using-terraform-additional"></a>

**Repository artifacts**

The repository artifacts are in the following structure.

```
.
├── README.md
├── main.tf
├── modules
│   ├── canary
│   └── canary-infra
├── terraform.tfvars
├── tf.plan
└── variable.tf
```

The `main.tf` file contains the core module, and it deploys two submodules:
+ `canary-infra` deploys the infrastructure required for the canaries.
+ `canary` deploys the canaries.

The input parameters for the solution are located in the `terraform.tfvars` file. You can use the following code example to create one canary.

```
module "canary" {
    source = "./modules/canary"
    name   = var.name
    runtime_version = var.runtime_version
    take_screenshot = var.take_screenshot
    api_hostname = var.api_hostname
    api_path = var.api_path
    reports-bucket = module.canary_infra.reports-bucket
    role = module.canary_infra.role
    security_group_id = module.canary_infra.security_group_id
    subnet_ids = var.subnet_ids
    frequency = var.frequency
    alert_sns_topic = var.alert_sns_topic
}
```

The corresponding .var file follows.

```
name   = "my-canary"
runtime_version = "syn-nodejs-puppeteer-3.7"
take_screenshot = false
api_hostname = "mydomain.internal"
api_path = "/path?param=value"
vpc_id = "vpc_id"
subnet_ids = ["subnet_id1"]
frequency = 5
alert_sns_topic = "arn:aws:sns:eu-central-1:111111111111:yyyyy"
```

**Cleaning up the solution**

If you are testing this in a development environment, you can clean up the solution to avoid accruing costs.

1. On the AWS Management Console, navigate to the Amazon S3 console. Empty the Amazon S3 bucket that the solution created. Make sure to take a backup of the data, if required.

1. In your development environment, from the `cloudwatch-synthetics-canary-terraform` directory, run the `destroy` command.

   ```
   terraform destroy
   ```
