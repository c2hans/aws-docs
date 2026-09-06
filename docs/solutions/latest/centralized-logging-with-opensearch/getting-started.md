---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/getting-started.html
---

# Getting started
<a name="getting-started"></a>

After [deploying the solution](automated-deployment.md), refer to this section to quickly learn how to use Centralized Logging with OpenSearch for log ingestion (AWS CloudTrail logs as an example), and log visualization.

You can also choose to start with [Domain management](domain-management.md), then build [AWS Service Log Analytics Pipelines](aws-service-logs.md) and [Application Log Analytics Pipelines](application-logs.md).

 **Steps**
+  [Step 1: Import an Amazon OpenSearch Service domain](#step-1-import-an-amazon-opensearch-domain). Import an existing Amazon OpenSearch Service domain into the solution.
+  [Step 2: Create Access Proxy](#step-2-create-access-proxy). Create a public access proxy, which allows you to access the templated dashboard from anywhere.
+  [Step 3: Ingest CloudTrail Logs](#step-3-ingest-aws-cloudtrail-logs). Ingest CloudTrail logs into the specified Amazon OpenSearch Service domain.
+  [Step 4: Access built-in dashboard](#step-4-access-the-dashboard). View the dashboard of CloudTrail logs.

## Step 1: Import an Amazon OpenSearch Service domain
<a name="step-1-import-an-amazon-opensearch-domain"></a>

To use the Centralized Logging with OpenSearch solution for the first time, you must import Amazon OpenSearch Service domains first.

Centralized Logging with OpenSearch supports Amazon OpenSearch Service domain with [fine-grained access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html) enabled [within a VPC](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html) only.

**Important**
Currently, Centralized Logging with OpenSearch supports Amazon OpenSearch Service with OpenSearch 1.3 or later.

 **Prerequisites**

At least one Amazon OpenSearch Service domain within VPC. If you don’t have an Amazon OpenSearch Service domain yet, you can create an Amazon OpenSearch Service domain within VPC. See [Launching your Amazon OpenSearch Service domains within a VPC](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html).

 **Steps**

Use the following procedure to import an Amazon OpenSearch Service domain through the Centralized Logging with OpenSearch console.

1. Sign in to the Centralized Logging with OpenSearch console (see instructions for accessing the console using [Amazon Cognito user pool](launch-with-amazon-cognito-user-pool.md#step-2.-launch-the-web-console) or [OIDC](launch-with-openid-connect-oidc.md#step-4.-launch-the-web-console)).

1. In the navigation pane, under **Domains**, choose **Import OpenSearch Domain**.

1. On the **Step 1. Select domain** page, choose a domain from the dropdown list.

1. Choose **Next**.

1. On the **Step 2. Configure network** page, under **Network creation**, choose **Automatic**. If your Centralized Logging with OpenSearch and OpenSearch domains reside in two different VPCs, the *Automatic* mode will create a VPC Peering Connection between them, and update route tables. See details in [Set up VPC Peering](domain-operations.md#set-up-vpc-peering).

1. On the Step 3. Create tags page, choose Import.

## Step 2: Create Access Proxy
<a name="step-2-create-access-proxy"></a>

**Note**
Access proxy is optional and it incurs additional cost. If you can connect to Amazon OpenSearch Service’s VPC (such as through a VPN connection), you don’t need to activate an access proxy. You must use it only if you want to connect to the Amazon OpenSearch Service dashboard from the public internet.

You can create a NGINX proxy and create a DNS record pointing to the proxy, so that you can access the Amazon OpenSearch Service dashboard securely from a public network. For more information, refer to [Access Proxy](access-proxy-1.md).

 **Create a NGINX proxy**

1. Sign in to the Centralized Logging with OpenSearch console (see instructions for accessing the console using [Amazon Cognito user pool](launch-with-amazon-cognito-user-pool.md#step-2.-launch-the-web-console) or [OIDC](launch-with-openid-connect-oidc.md#step-4.-launch-the-web-console)).

1. In the navigation pane, under **Domains**, choose **OpenSearch domains**.

1. Select the domain from the table.

1. Under General configuration, choose **Enable** at the Access Proxy label.

1. On the **Create access proxy** page, under **Public access proxy**, select at least 2 subnets that contain `CLVpc/DefaultVPC/publicSubnetX` for the **Public Subnets**.

1. For **Public Security Group**, choose the Security Group that contains `ProxySecurityGroup`.

1. Choose the NGINX Instance Key Name.

1. Enter the **Domain Name**.

1. Choose the associated **Load Balancer SSL Certificate that** applies to the domain name.

    **NGINX Instance key name. Specify the EC2 key name of the NGINX proxy.**
![image26](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image26.png)

1. Choose **Create**.

After provisioning the proxy infrastructure, you must create an associated DNS record in your DNS resolver. The following introduces how to find the Application Load Balancer domain, and then create a CNAME record pointing to this domain.

 **Create a DNS record**

1. Sign in to the Centralized Logging with OpenSearch console (see instructions for accessing the console using [Amazon Cognito user pool](launch-with-amazon-cognito-user-pool.md#step-2.-launch-the-web-console) or [OIDC](launch-with-openid-connect-oidc.md#step-4.-launch-the-web-console)).

1. In the navigation pane, under **Domains**, choose **OpenSearch domains**.

1. Select the domain from the table.

1. Choose the **Access Proxy** tab. Find **Load Balancer Domain**, which is the Application Load Balancer domain.

1. Go to the DNS resolver, and create a CNAME record pointing to this domain. If your domain is managed by [Amazon Route 53](https://aws.amazon.com/route53), refer to [Creating records by using the Amazon Route 53 console](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html).

## Step 3: Ingest AWS CloudTrail Logs
<a name="step-3-ingest-aws-cloudtrail-logs"></a>

You can build a log analytics pipeline to ingest AWS CloudTrail logs.

**Important**
Make sure your CloudTrail and Centralized Logging with OpenSearch are in the same AWS Region.

1. Sign in to the Centralized Logging with OpenSearch Console (see instructions for accessing the console using [Amazon Cognito user pool](launch-with-amazon-cognito-user-pool.md#step-2.-launch-the-web-console) or [OIDC](launch-with-openid-connect-oidc.md#step-4.-launch-the-web-console)).

1. In the navigation pane, select **AWS Service Log Analytics Pipelines**.

1. Choose **Create a log ingestion**.

1. In the **AWS Services** section, choose `AWS CloudTrail`.

1. Choose **Next**.

1. Under **Specify settings**, for **Trail**, select one from the dropdown list.

1. Choose **Next**.

1. In the **Specify OpenSearch domain** section, select the imported domain for the **Amazon OpenSearch Service domain**.

1. Choose `Yes` for **Sample dashboard**.

1. Keep default values and choose **Next**.

1. Choose **Create**.

## Step 4: Access the dashboard
<a name="step-4-access-the-dashboard"></a>

After the [DNS record](access-proxy-1.md#create-an-associated-dns-record) takes effect, you can access the built-in dashboard from anywhere via proxy.

1. Enter the domain of the proxy in your browser. Alternatively, click the **Link** button under **Access Proxy** in the **General Configuration** section of the domain.

1. Enter your credentials to log in to the Amazon OpenSearch Service Dashboard.

1. Click the username icon of the Amazon OpenSearch Service dashboard from the top right corner.

1. Choose `Switch Tenants`.

1. On the **Select your tenant** page, choose **Global**, and click **Confirm**.

1. On the left navigation panel, choose **Dashboards**.

1. Choose the dashboard created automatically and start to explore your data.
