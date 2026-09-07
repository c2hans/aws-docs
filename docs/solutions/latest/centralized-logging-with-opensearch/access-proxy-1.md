---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/access-proxy-1.html
---

# Access proxy
<a name="access-proxy-1"></a>

By default, an Amazon OpenSearch Service domain within VPC cannot be accessed from the internet. Centralized Logging with OpenSearch creates a highly available [NGINX cluster](https://aws.amazon.com/premiumsupport/knowledge-center/opensearch-outside-vpc-nginx/) that allows you to access the OpenSearch Dashboards from the internet. Alternatively, you can choose to access the Amazon OpenSearch Service domains using [SSH Tunnel](https://aws.amazon.com/premiumsupport/knowledge-center/opensearch-outside-vpc-ssh/). Refer to the [Access proxy architecture](access-proxy.md) for more implementation details.

This section covers the following:

1.  [Create a proxy](#create-a-proxy)

1.  [Create an associated DNS record](#create-an-associated-dns-record)

1.  [Access Amazon OpenSearch Service via proxy](#access-amazon-opensearch-service-via-proxy)

1.  [Delete a proxy](#delete-a-proxy)

## Create a proxy
<a name="create-a-proxy"></a>

You can create the NGINX-based proxy using the Centralized Logging with OpenSearch console or by deploying a standalone CloudFormation stack.

 **Prerequisites**
+ Make sure an Amazon OpenSearch Service **domain** within VPC is available.
+ The domain associated **SSL certificate** is created or uploaded in [AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager).
+ Make sure you have the EC2 private key (.pem) file.

### （Option 1）Using the Centralized Logging with OpenSearch console
<a name="option-1using-the-centralized-logging-with-opensearch-console"></a>

1. Log in to the Centralized Logging with OpenSearch console.

1. In the navigation pane, under **Domains**, choose **OpenSearch domains**.

1. Select the domain from the table.

1. Under **General configuration**, choose **Enable** at the **Access Proxy** label.
**Note**
Once the access proxy is enabled, a link to the access proxy will be available.

1. On the **Create access proxy** page, choose the **Proxy Instance Type** and **Proxy Instance Number**.

1. Under **Public access proxy**, select at least 2 subnets for **Public Subnets**. You can choose 2 public subnets named `CLVPC/DefaultVPC/publicSubnetX`, which are created by Centralized Logging with OpenSearch by default.

1. Choose a Security Group of the Application Load Balancer in **Public Security Group**. You can choose a security group named `ProxySecurityGroup`, which is created by Centralized Logging with OpenSearch default.

1. Choose the NGINX Instance Key Name.

1. Enter the **Domain Name**.

1. Choose **Load Balancer SSL Certificate** associated with the domain name.

1. Choose **Create**.

### (Option 2) Using the CloudFormation stack
<a name="option-2-using-the-cloudformation-stack"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - NGINX access proxy* solution in the AWS Cloud.

1. Log in to the AWS Management Console and select the button to launch the AWS CloudFormation template. [![Launch solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fcentralized-logging-with-opensearch%2Flatest%2FNginxForOpenSearch.template)

You can also [download the template](https://s3.amazonaws.com/solutions-reference/centralized-logging-with-opensearch/latest/NginxForOpenSearch.template) as a starting point for your own implementation. . To launch the stack in a different AWS Region, use the Region selector in the console navigation bar. . On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**. . On the **Specify stack details** page, assign a name to your stack. . Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.

\+

| Parameter | Default | Description |
| --- | --- | --- |
| VPCId |  {{<Requires input>}}  | The VPC to deploy the NGINX proxy resources, for example, `vpc-bef13dc7`. |
| PublicSubnetIds |  {{<Requires input>}}  | The public subnets where Elastic Load Balancing is deployed. You must select at least two public subnets, for example, `subnet-12345abc`, `subnet-54321cba`. |
| ELBSecurityGroupId |  {{<Requires input>}}  | The security group being associated with the Elastic Load Balancing, for example, `sg-123456`. |
| ELBDomain |  {{<Requires input>}}  | The custom domain name of the Elastic Load Balancing, for example, `dashboard.example.com`. |
| ELBDomainCertificateArn |  {{<Requires input>}}  | The SSL certificate ARN associated with the ELBDomain. The certificate must be created from ACM. |
| PrivateSubnetIds |  {{<Requires input>}}  | The private subnets where NGINX instances are deployed. You must select at least two private subnets, for example, `subnet-12345abc`, `subnet-54321cba`. |
| NginxSecurityGroupId |  {{<Requires input>}}  | The security group associated with the NGINX instances. The security group must allow access from Elastic Load Balancing security group. |
| KeyName |  {{<Requires input>}}  | The PEM key name of the NGINX instances. |
| EngineType |  `OpenSearch`  | The engine type of the OpenSearch. Select OpenSearch. |
| Endpoint |  {{<Requires input>}}  | The OpenSearch endpoint, for example, `vpc-your_opensearch_domain_name-xcvgw6uu2o6zafsiefxubwuohe.us-east-1.es.amazonaws.com`. |
| CognitoEndpoint |  *Optional input*  | The Amazon Cognito User Pool endpoint URL of the OpenSearch domain, for example, mydomain.auth.us-east-1.amazoncognito.com. Leave empty if your OpenSearch domain is not authenticated through Amazon Cognito User Pool. |

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 15 minutes.

### Recommended Proxy Configuration
<a name="recommended-proxy-configuration"></a>

The following table provides a list of recommended proxy configuration examples for different number of concurrent users. You can create a proxy according to your own use cases.

| Number of Concurrent Users | Proxy Instance Type | Number of Proxy Instances |
| --- | --- | --- |
| 4 | t3.nano | 1 |
| 6 | t3.micro | 1 |
| 8 | t3.nano | 2 |
| 10 | t3.small | 1 |
| 12 | t3.micro | 2 |
| 20 | t3.small | 2 |
| 25 | t3.large | 1 |
| 50\+ | t3.large | 2 |

## Create an associated DNS record
<a name="create-an-associated-dns-record"></a>

After provisioning the proxy infrastructure, you must create an associated DNS record in your DNS resolver. The following introduces how to find the Application Load Balancer domain, and then create a CNAME record pointing to this domain.

1. Log in to the Centralized Logging with OpenSearch console.

1. In the navigation pane, under **Domains**, choose **OpenSearch domains**.

1. Select the domain from the table.

1. Choose the **Access Proxy** tab. You can see the **Load Balancer Domain**, which is the Application Load Balancer domain.

1. Go to the DNS resolver, create a CNAME record pointing to this domain. If your domain is managed by [Amazon Route 53](https://aws.amazon.com/route53), refer to [Creating records by using the Amazon Route 53 console](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html).

## Access Amazon OpenSearch Service via proxy
<a name="access-amazon-opensearch-service-via-proxy"></a>

After the DNS record takes effect, you can access the Amazon OpenSearch Service built-in dashboard from anywhere via proxy. You can enter the domain of the proxy in your browser, or choose the **Link** button under **Access Proxy** in the **General Configuration** section.

 **Example General configuration screen.**

![image30](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image30.png)

## Delete a Proxy
<a name="delete-a-proxy"></a>

1. Log in to the Centralized Logging with OpenSearch console.

1. In the navigation pane, under **Domains**, choose **OpenSearch domains**.

1. Select the domain from the table.

1. Choose the **Access Proxy** tab.

1. Choose the **Delete**.

1. On the confirmation prompt, choose **Delete**.
