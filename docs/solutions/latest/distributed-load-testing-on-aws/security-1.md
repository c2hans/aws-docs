---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/security-1.html
---

# Security
<a name="security-1"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

AWS Identity and Access Management (IAM) roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud. This solution creates IAM roles that grant the solution’s AWS Lambda functions access to create Regional resources.

## Amazon CloudFront
<a name="amazon-cloudfront"></a>

This solution deploys a web UI  [hosted](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)  in an Amazon S3 bucket, which is distributed by Amazon CloudFront. To help reduce latency and improve security, this solution includes a CloudFront distribution with an origin access identity, which is a CloudFront user that provides public access to the solution website’s bucket contents. By default, the CloudFront distribution supports connections up to TLS 1.3, using the highest protocol version that the viewer supports. For more information, refer to [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the *Amazon CloudFront Developer Guide*.

CloudFront activates additional security mitigations to append HTTP security headers to each viewer response. For more information, refer to [Adding or removing HTTP headers in CloudFront responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/adding-response-headers.html).

This solution uses the default CloudFront certificate, which has a minimum supported security protocol of TLS v1.0. To enforce the use of TLS v1.2 or TLS v1.3, you must use a custom SSL certificate instead of the default CloudFront certificate. For more information, refer to [How do I configure my CloudFront distribution to use an SSL/TLS certificate](https://aws.amazon.com/premiumsupport/knowledge-center/install-ssl-cloudfront/).

## Amazon API Gateway
<a name="amazon-api-gateway"></a>

This solution deploys edge-optimized Amazon API Gateway endpoints to provide RESTful APIs for the load testing functionality using the default API Gateway endpoint rather than a custom domain. For edge-optimized APIs using the default endpoint, API Gateway uses the TLS-1-0 security policy. For more information, refer to [Working with REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api.html) in the *Amazon API Gateway Developer Guide*.

This solution uses the default API Gateway certificate, which has a minimum supported security protocol of TLS v1.0. To enforce the use of TLS v1.2 or TLS v1.3, you must use a custom domain with a custom SSL certificate instead of the default API Gateway certificate. For more information, refer to [Setting up custom domain names for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).

## AWS Fargate security group
<a name="aws-fargate"></a>

By default, this solution opens the outbound rule of the AWS Fargate security group to the public. If you want to block AWS Fargate from sending traffic everywhere, change the outbound rule to a specific Classless Inter-Domain Routing (CIDR).

This security group also includes an inbound rule that allows local traffic on port 50,000 to any source that belongs to the same security group. This is used to allow the containers to communicate with one another.

## Amazon VPC
<a name="amazon-vpc"></a>

 **VPC**: A virtual private cloud (VPC) based on the Amazon VPC service gives you a private, logically isolated network in the AWS Cloud.

You can specify your own VPC in [AWS CloudFormation parameters](launch-the-stack.md) during deployment. The VPC is used exclusively by the ECS tasks that generate load; the web console and API are not deployed within this VPC. If you do not specify an existing VPC, the solution creates a new VPC with the required networking configuration. If you choose to use an existing VPC, it must meet the following requirements to run load testing tasks successfully.

### VPC requirements
<a name="vpc-requirements"></a>

The minimum requirements for a VPC to be used with Distributed Load Testing on AWS are listed below.
+ The VPC must contain at least two AZs
+ The VPC must contain at least two subnets, each in a separate AZ
+ VPC subnets can be either public or private, but they must use the same configuration (both public OR both private)
+ The VPC must provide access to endpoints for ECR, CloudWatch Logs, S3, and AWS IoT Core.
+ The VPC must provide access to the service(s) being targeted by load tests.

**Note**
If you don’t have a VPC that meets these criteria, you can create a VPC with the VPC wizard quickly. For more information, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html).

Public subnets may meet these requirements by including the following:
+ An internet gateway attached to the VPC
+ A route to the internet gateway (0.0.0.0/0)

Private subnets may meet these requirements through the use of NAT Gateways or VPC endpoints, as described below.

 **Option 1: NAT Gateway**
+ Deploy a NAT Gateway in each AZ with private subnets
+ Configure route tables to route internet-bound traffic (0.0.0.0/0) through the NAT Gateway

 **Option 2: VPC Endpoints**

Create the following VPC endpoints in your VPC:
+ Amazon ECR API Endpoint: `com.amazonaws.<region>.ecr.api`
+ Amazon ECR DKR Endpoint: `com.amazonaws.<region>.ecr.dkr`
+ Amazon CloudWatch Logs endpoint: `com.amazonaws.<region>.logs`
+ Amazon S3 Gateway endpoint: `com.amazonaws.<region>.s3`
+ AWS IoT Core endpoint (required if using the live data charts) `com.amazonaws.<region>.iot.data`

Other VPC configurations may also work.

**Important**
The security group attached to each VPC endpoint interface must allow inbound TCP traffic on port 443 from the ECS task security group.

 **Security Group Configuration**

During deployment, the solution will create a security group within your VPC to permit the following traffic with tasks in the ECS cluster:
+ All outbound traffic
+ Inbound traffic on port 50000 from other tasks in the same security group, to facilitate coordination between worker and leader tasks.

## Network stress test
<a name="network-stress-test"></a>

You are responsible for using this solution under the [Amazon EC2 Testing Policy](https://aws.amazon.com/ec2/testing/). The policy covers high-volume network tests run from Amazon EC2 instances to other Amazon EC2 instances, AWS services, or external endpoints. These tests are sometimes called stress tests, load tests, or gameday tests. Review the policy to understand the distinction between network stress tests and DDoS simulations (which are prohibited on EC2 and covered separately by the [DDoS Simulation Testing policy](https://aws.amazon.com/security/ddos-simulation-testing/)), and note that AWS may employ traffic engineering or shaping at high traffic volumes. Refer to the policy page for current thresholds and guidance before running high-volume tests.

## Restricting access to the public user interface
<a name="restricting-access-to-the-public-user-interface"></a>

The approach for restricting access to the web console depends on the deployment option you choose.

 **Default (CloudFront \+ S3) deployment** — To restrict access to the public-facing user interface beyond the authentication and authorization mechanisms provided by IAM and Amazon Cognito, you can associate an AWS WAF web ACL with the CloudFront distribution. Consider using the [AWS WAF Security Automations solution](https://aws.amazon.com/solutions/implementations/aws-waf-security-automations/), which deploys a set of preconfigured AWS WAF rules that filter common web-based attacks. The default CloudFront \+ S3 template does not deploy WAF resources automatically.

 **ALB \+ ECS Fargate deployment** — The solution automatically deploys an AWS WAF web ACL in front of the ALB with managed rules that provide baseline protection against common web-based attacks. You can customize the WAF rules to meet your specific security requirements, including adding IP-based allow or block lists, geographic restrictions, rate limiting, or additional AWS managed rule groups. For instructions on modifying the WAF configuration, refer to the [WAF integration](deploy-alb-ecs-fargate.md#alb-ecs-waf-integration) section in the deployment instructions.

## MCP Server security (Optional)
<a name="mcp-server-security"></a>

If you deploy the optional MCP Server integration, the solution uses Amazon Bedrock AgentCore Gateway to provide secure access to load testing data for AI agents. AgentCore Gateway validates Amazon Cognito authentication tokens for each request, so that only authorized users can access the MCP Server. All MCP Server interactions use the same permission boundaries and access controls as the web console.

The **MCP Server Access Mode** parameter controls what AI agents can do. In the default `ReadOnly` mode, the MCP Server exposes read tools only. The AWS Identity and Access Management (IAM) policy on the MCP Server Lambda function permits only `GET` requests to the solution’s API, so agents cannot modify test configurations or results. In `ReadWrite` mode, agents can additionally create, modify, delete, and start test scenarios. Choose `ReadWrite` only if your use case requires agents to change tests.

 **Credential rotation** — If you connect an MCP client using service-based (machine-to-machine) authentication, the solution creates an Amazon Cognito app client with a long-lived client secret. You are responsible for rotating that secret and for storing it securely. We recommend rotating it at least every 90 days. For procedures, refer to [Rotate the MCP Server client secret](mcp-server-integration.md#rotate-mcp-client-secret) in *Use the solution*.

## ALB \+ ECS Fargate hosted web console security (Optional)
<a name="alb-ecs-security"></a>

If you choose the ALB \+ ECS Fargate deployment option, the following security considerations apply:
+  **VPC Block Public Access compatibility** — The ALB \+ ECS Fargate option is designed for environments where VPC Block Public Access (BPA) policies block traffic from public CloudFront distributions. The ALB can be deployed as an internal load balancer within your VPC, accessible only through your corporate network, VPN, or AWS PrivateLink, meeting zero public internet exposure requirements.
+  **ACM certificate management** — The ALB uses an ACM certificate for HTTPS termination. You are responsible for ensuring the certificate remains valid and is renewed before expiration. ACM automatically renews certificates that it manages, but imported certificates must be renewed manually. For more information, refer to [Managed certificate renewal](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html) in the AWS Certificate Manager User Guide.
+  **AWS WAF protection** — WAF is deployed by default with the ALB \+ ECS Fargate template. For details, refer to [Restricting access to the public user interface](#restricting-access-to-the-public-user-interface).

## Headless (bring your own web server) security (Optional)
<a name="self-hosted-security"></a>

If you choose the headless deployment option and host the web console on your own web server, you are responsible for the following security considerations:
+  **HTTPS configuration** — We strongly recommend configuring HTTPS on your web server.
+  **Access controls** — You are responsible for implementing access controls, firewall rules, and network security on your web server.
+  **Security hardening** — Apply your organization’s security hardening standards to the web server, including patching, monitoring, and intrusion detection.

## Third-party testing frameworks
<a name="third-party-testing-frameworks"></a>

Distributed Load Testing on AWS bundles three third-party testing frameworks — Apache JMeter, Grafana k6, and Locust. Under the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), you are responsible for evaluating whether these frameworks and their bundled versions meet your organization’s security requirements before running load tests. The solution distributes each framework without modification and verifies the bundled binaries using SHA512 checksums at build time and runtime.

For details on when each framework is installed and how it’s provisioned, see [Testing framework provisioning](back-end.md#framework-provisioning).

### Apache JMeter
<a name="jmeter-security"></a>

The bundled version of Apache JMeter has known security vulnerabilities that cannot be fully patched externally without breaking compatibility with the Taurus test automation framework and the JMeter plugin ecosystem that the solution depends on. Before running load tests, review the [Apache JMeter security advisories](https://jmeter.apache.org/security.html) and evaluate if they may cause security vulnerabilities for you.

**Note**
Apache JMeter also runs under the hood for the **Simple HTTP Endpoint** test type. When you configure a URL, method, headers, and body payload in the web console, the solution generates a JMeter test plan and executes it with the bundled JMeter binary. The JMeter security considerations described in this section therefore apply to Simple HTTP Endpoint tests as well.

If you need a patched version of JMeter, you have two options. Both options require a test archive and are available only for the **JMeter** test type:
+  **Supply a patched JMeter binary** — Include a patched JMeter binary in your test archive. The solution uses your binary in place of the bundled version.
+  **Override individual plugin JARs** — Use the plugin override mechanism to replace specific vulnerable plugin JARs with patched versions. For more information, refer to [JMeter tests](design-considerations.md#jmeter-script-support).

The **Simple HTTP Endpoint** test type does not accept a test archive and therefore cannot override the bundled JMeter binary or plugins. If you need to run HTTP endpoint tests with a patched JMeter, use the **JMeter** test type and supply a JMeter script (.jmx) or a .zip archive that includes your patched JMeter binary or plugin JARs.

### Grafana k6
<a name="k6-security"></a>

k6 is released under the [AGPL-3.0 license](https://github.com/grafana/k6/blob/master/LICENSE.md). The web console displays a license acknowledgment message when you create a new k6 test. No known security vulnerabilities were identified in the bundled version of k6 at the time of this solution’s release. The solution does not monitor k6 for new vulnerabilities on an ongoing basis; you are responsible for evaluating k6 against your security requirements throughout its use.

### Locust
<a name="locust-security"></a>

No known security vulnerabilities were identified in the bundled version of Locust at the time of this solution’s release. The solution does not monitor Locust for new vulnerabilities on an ongoing basis; you are responsible for evaluating Locust against your security requirements throughout its use.
