---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer.html
---

# Deploy an Amazon API Gateway API on an internal website using private endpoints and an Application Load Balancer
<a name="deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer"></a>

*Saurabh Kothari, Amazon Web Services*

## Summary
<a name="deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer-summary"></a>

This pattern shows you how to deploy an Amazon API Gateway API on an internal website that’s accessible from an on-premises network. You learn to create a custom domain name for a private API by using an architecture that’s designed with private endpoints, an Application Load Balancer, AWS PrivateLink, and Amazon Route 53. This architecture prevents the unintended consequences of using a custom domain name and proxy server to help with domain-based routing on an API. For example, if you deploy a virtual private cloud (VPC) endpoint in a non-routable subnet, your network can’t reach API Gateway. A common solution is to use a custom domain name and then deploy the API in a routable subnet, but this can break other internal sites when the proxy configuration passes traffic (`execute-api.{region}.vpce.amazonaws.com`) to AWS Direct Connect. Finally, this pattern can help you meet organizational requirements for using a private API that’s unreachable from the internet and a custom domain name.

## Prerequisites and limitations
<a name="deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A Server Name Indication (SNI) certificate for your website and API
+ A connection from an on-premises environment to an AWS account that’s set up by using AWS Direct Connect or AWS Site-to-Site VPN
+ A [private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) with a corresponding domain (for example, domain.com) that’s resolved from an on-premises network and forwards DNS queries to Route 53
+ A routable private subnet that’s reachable from an on-premises network

**Limitations**

For more information about quotas (formerly referred to as limits) for load balancers, rules, and other resources, see [Quotas for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html) in the Elastic Load Balancing documentation.

## Architecture
<a name="deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer-architecture"></a>

**Technology stack**
+ Amazon API Gateway
+ Amazon Route 53
+ Application Load Balancer
+ AWS Certificate Manager
+ AWS PrivateLink

**Target architecture**

The following diagram shows how an Application Load Balancer is deployed in a VPC that directs web traffic to a website target group or API Gateway target group based on Application Load Balancer listener rules. The API Gateway target group is a list of IP addresses for the VPC endpoint in API Gateway. API Gateway is configured to make the API private with its resource policy. The policy denies all calls that are not from a specific VPC endpoint. Custom domain names in API gateway are updated to use api.domain.com for the API and its stage. Application Load Balancer rules are added to route traffic based on the host name.

![Architecture that uses Application Load Balancer listener rules to direct web traffic.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/83145062-4535-4ad0-8947-4ea8950cd174/images/12715186-26ea-4123-b9ef-e3105a934ff3.png)

The diagram shows the following workflow:

1. A user from an on-premises network tries to access an internal website. The request is sent to ui.domain.com and api.domain.com. Then, the request is resolved to the internal Application Load Balancer of the routable private subnet. The SSL is terminated at the Application Load Balancer for ui.domain.com and api.domain.com.

1. Listener rules, configured on the Application Load Balancer, check for the host header.

   a. If the host header is api.domain.com, the request is forwarded to the API Gateway target group. The Application Load Balancer initiates a new connection to API Gateway over port 443.

   b. If the host header is ui.domain.com, the request is forwarded to the website target group.

1. When the request reaches API Gateway, the custom domain mapping configured in API Gateway determines the hostname and which API to run.

**Automation and scale**

The steps in this pattern can be automated by using AWS CloudFormation or the AWS Cloud Development Kit (AWS CDK). To configure the target group of the API Gateway calls, you must use a custom resource to retrieve the IP address of the VPC endpoint. API calls to [describe-vpc-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoints.html) and [describe-network-interfaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-interfaces.html) return the IP addresses and the security group, which can be used to create the API target group of IP addresses.

## Tools
<a name="deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer-tools"></a>
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) helps you create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) is a highly available and scalable DNS web service.
+ [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) helps you create, store, and renew public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications.
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) helps you create unidirectional, private connections from your VPCs to services outside of the VPC.

## Epics
<a name="deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer-epics"></a>

### Create an SNI certificate
<a name="create-an-sni-certificate"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an SNI certificate and import the certificate into ACM. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer.html) | Network administrator |

### Deploy a VPC endpoint in a non-routable private subnet
<a name="deploy-a-vpc-endpoint-in-a-non-routable-private-subnet"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an interface VPC endpoint in API Gateway. | To create an interface VPC endpoint, follow the instructions from [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the Amazon Virtual Private Cloud (Amazon VPC) documentation. | Cloud administrator |

### Configure the Application Load Balancer
<a name="configure-the-application-load-balancer"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a target group for your application. | [Create a target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-target-group.html) for the UI resources of your application. | Cloud administrator |
| Create a target group for the API Gateway endpoint. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer.html) | Cloud administrator |
| Create an Application Load Balancer. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer.html) | Cloud administrator |
| Create listeners rules. | Create [listener rules](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#listener-rules) to do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer.html) | Cloud administrator |

### Configure Route 53
<a name="configure-route-53"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a private hosted zone. | [Create a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html) for domain.com. | Cloud administrator |
| Create domain records. | [Create CNAME records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) for the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer.html) | Cloud administrator |

### Create a private API endpoint in API Gateway
<a name="create-a-private-api-endpoint-in-api-gateway"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create and configure a private API endpoint. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer.html) | App developer, Cloud administrator |
| Create a custom domain name. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer.html) | Cloud administrator |

## Related resources
<a name="deploy-an-amazon-api-gateway-api-on-an-internal-website-using-private-endpoints-and-an-application-load-balancer-resources"></a>
+ [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
+ [Amazon Route 53](https://aws.amazon.com/route53/)
+ [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/)
+ [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)
+ [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/)
