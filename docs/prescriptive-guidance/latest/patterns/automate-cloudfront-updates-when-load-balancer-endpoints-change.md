---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-cloudfront-updates-when-load-balancer-endpoints-change.html
---

# Automate CloudFront updates when load balancer endpoints change by using Terraform
<a name="automate-cloudfront-updates-when-load-balancer-endpoints-change"></a>

*Tamilselvan P, Mohan Annam, and Naveen Suthar, Amazon Web Services*

## Summary
<a name="automate-cloudfront-updates-when-load-balancer-endpoints-change-summary"></a>

When users of Amazon Elastic Kubernetes Service (Amazon EKS) delete and re-install their ingress configuration through Helm charts, a new Application Load Balancer (ALB) is created. This creates a problem because Amazon CloudFront continues to reference the old ALB’s DNS record. As a result, services destined to this endpoint will not be reachable. (For more details about this problematic workflow, see [Additional information](#automate-cloudfront-updates-when-load-balancer-endpoints-change-additional).)

To solve this issue, this pattern describes using a custom AWS Lambda function that was developed with Python. This Lambda function automatically detects when a new ALB is created through Amazon EventBridge rules. Using the AWS SDK for Python (Boto3), the function then updates the CloudFront configuration with the new ALB’s DNS address, ensuring that traffic is routed to the correct endpoint.

This automated solution maintains service continuity without additional routing or latency. The process helps to ensure that CloudFront always references the correct ALB DNS endpoint, even when the underlying infrastructure changes.

## Prerequisites and limitations
<a name="automate-cloudfront-updates-when-load-balancer-endpoints-change-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ A sample web application for testing and validation that is deployed on Amazon EKS by using Helm. For more information, see [Deploy applications with Helm on Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/helm.html) in the Amazon EKS documentation.
+ Configure CloudFront to route calls to an ALB that is created by a Helm [ingress controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/). For more information, see [Install AWS Load Balancer Controller with Helm](https://docs.aws.amazon.com/eks/latest/userguide/lbc-helm.html) in the Amazon EKS documentation and [Restrict access to Application Load Balancers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.html) in the CloudFront documentation.
+ Terraform [installed](https://developer.hashicorp.com/terraform/install?product_intent=terraform) and configured in a local workspace.

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ Terraform version 1.0.0 or later
+ Terraform [AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) version 4.20 or later

## Architecture
<a name="automate-cloudfront-updates-when-load-balancer-endpoints-change-architecture"></a>

The following diagram shows the workflow and architecture components for this pattern.

![Workflow to update CloudFront with new ALB DNS address detected through EventBridge rule.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/03c30b18-4dd7-4dd4-b960-5a5cc58cec63/images/28854767-0902-4398-80af-b19141dd94e4.png)

This solution performs the following steps:

1. The Amazon EKS ingress controller creates a new Application Load Balancer (ALB) whenever there is a Helm restart or deployment.

1. EventBridge looks for ALB creation events.

1. The ALB creation event triggers the Lambda function.

1. The Lambda function has been deployed based on python 3.9 and uses boto3 API to call AWS services. The Lambda function updates the CloudFront entry with the latest load balancer DNS name, which is received from create load balancer events.

## Tools
<a name="automate-cloudfront-updates-when-load-balancer-endpoints-change-tools"></a>

**AWS services**
+ [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) speeds up distribution of your web content by delivering it through a worldwide network of data centers, which lowers latency and improves performance.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) is a software development kit that helps you integrate your Python application, library, or script with AWS services.

**Other tools**
+ [Python](https://www.python.org/) is a general-purpose computer programming language.
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

**Code repository**

The code for this pattern is available in the GitHub [aws-cloudfront-automation-terraform-samples](https://github.com/aws-samples/aws-cloudfront-automation-terraform-samples) repository.

## Epics
<a name="automate-cloudfront-updates-when-load-balancer-endpoints-change-epics"></a>

### Set up local workstation
<a name="set-up-local-workstation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up and configure the Git CLI. | To install and configure the Git command line interface (CLI) in your local workstation, follow the [Getting Started – Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) instructions in the Git documentation. | DevOps engineer |
| Create the project folder and add the files. | 1. Go to the pattern’s [GitHub repository](https://github.com/aws-samples/aws-cloudfront-automation-terraform-samples), and choose the **Code** button.<br />2. On the **Clone** dialog, choose the **HTTPS** tab. In **Clone using the web URL**, copy the URL that’s shown.<br />3. Create a folder on your local machine. Name it with your project name.<br />4. Open a terminal on your local machine, and navigate to this folder.<br />5. To clone this pattern’s git repository, run the following command: `git clone https://github.com/aws-samples/aws-cloudfront-automation-terraform-samples`<br />6. After the repository has been cloned, use the following command to go to the cloned directory: `cd <directory name>/cloudfront-update`<br />Open this project in an Integrated Development Environment (IDE) of your choice. | DevOps engineer |

### Provision the target architecture using the Terraform configuration
<a name="provision-the-target-architecture-using-the-terraform-configuration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the solution. | To deploy resources in the target AWS account, use the following steps:1. Go to the `cloudfront-update` folder.<br />2. Update the `terraform.tfvars` file with the `cloudfront_distribution_id`.<br />3. To set the AWS Region for your AWS profile, run the following command:<pre>export AWS_REGION={{ REGION }}</pre><br />4. To initialize Terraform, run the following command:<pre>terraform init</pre><br />5. To validate Terraform, run the following command:<pre>terraform validate</pre><br />6. To create a Terraform execution plan, run the following command:<pre>terraform plan</pre><br />7. To apply the actions from `terraform plan`, run the following command:<pre>terraform apply</pre> | DevOps engineer |

### Verify the deployment
<a name="verify-the-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the deployment. | 1. Sign in to the AWS Management Console and open the Amazon CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).<br />2. In the left navigation pane, choose **Distributions** and then open the CloudFront distribution.<br />3. On the **Origins** tab, verify that the origin name and origin mapping have the updated ALB DNS record. | DevOps engineer |

### Clean up infrastructure
<a name="clean-up-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up the infrastructure. | To clean up the infrastructure that you created earlier, use the following steps:1. Run the following command: `terraform destroy`<br />2. To confirm the destroy command, enter `yes`. | DevOps engineer |

## Troubleshooting
<a name="automate-cloudfront-updates-when-load-balancer-endpoints-change-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Error validating provider credentials | When you run the Terraform `apply` or `destroy` commands from your local machine, you might encounter an error similar to the following:<pre>Error: configuring Terraform AWS Provider: error validating provider <br />credentials: error calling sts:GetCallerIdentity: operation error STS: <br />GetCallerIdentity, https response error StatusCode: 403, RequestID: <br />123456a9-fbc1-40ed-b8d8-513d0133ba7f, api error InvalidClientTokenId: <br />The security token included in the request is invalid.</pre><br />This error is caused by the expiration of the security token for the credentials used in your local machine’s configuration.<br />To resolve the error, see [Set and view configuration settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-methods) in the AWS Command Line Interface (AWS CLI) documentation. |

## Related resources
<a name="automate-cloudfront-updates-when-load-balancer-endpoints-change-resources"></a>

**AWS resources**
+ [Restrict access to Application Load Balancers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.html)
+ [Route internet traffic with AWS Load Balancer Controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)

**Terraform documentation**
+ [AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
+ [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
+ [Remote State](https://developer.hashicorp.com/terraform/language/state/remote)

## Additional information
<a name="automate-cloudfront-updates-when-load-balancer-endpoints-change-additional"></a>

**Problematic workflow**

![Workflow that produces out-of-date ALB DNS entry in CloudFront.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/03c30b18-4dd7-4dd4-b960-5a5cc58cec63/images/bb3c2c93-c749-435d-9b1d-2bbf6f0cf085.png)

The diagram shows the following workflow:

1. When the user accesses the application, the call goes to CloudFront.

1. CloudFront routes the calls to the respective Application Load Balancer (ALB).

1. The ALB includes the target IP addresses which are the application pod's IP addresses. From there, the ALB provides the expected results to the user.

However, this workflow demonstrates a problem. The application deployments are happening through Helm charts. Whenever there is a deployment or if someone restarts Helm, the respective ingress is also re-created. As a result, the external load balancer controller re-creates the ALB. Also, during each re-creation, the ALB is re-created with a different DNS name. Because of this, CloudFront will have a stale entry in the origin settings. Because of this stale entry, the application will not be reachable for the user. This issue results in downtime for users.

**Alternative solution**

Another possible solution is to create an [external DNS](https://github.com/kubernetes-sigs/external-dns) for the ALB and then point it to the Amazon Route 53 private hosted zone endpoint in CloudFront. However, this approach adds another hop in the application flow, which might cause application latency. This pattern’s Lambda function solution doesn’t disrupt current flow.
