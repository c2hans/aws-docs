---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/security.html
---

# Security
<a name="security"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit the [AWS Cloud Security](https://aws.amazon.com/security/).

## API Gateway Security Policy
<a name="api-gateway-security-policy"></a>

If you choose to enable the solution’s Web User Interface, an API Gateway REST API is deployed alongside the Admin CloudFormation stack which serves as the backend for all operations in the Web UI. The REST API deployed by the solution uses the default TLS security policy for API Gateway, which is `TLS-1-2` for regional APIs.

However, after deploying the Admin CloudFormation stack you may choose to customize the solution’s REST API by adding a more restrictive TLS security policy. For example, you can choose the `TLS_1_2 security policy` to restrict for traffic using TLSv1.2 or TLSv1.3. You can find the solution’s REST API in the API Gateway console under the name **AutomatedSecurityResponseApi**.

In order to choose a security policy for the solution’s REST API, you must first configure a custom domain name. For more information, see [Custom domain name for public REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).

For more information on adding a security policy to your REST API, see [Choose a security policy for your REST API custom domain in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html) in the API Gateway guide.
