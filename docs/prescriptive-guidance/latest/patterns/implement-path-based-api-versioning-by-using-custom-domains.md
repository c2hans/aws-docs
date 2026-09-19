---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-path-based-api-versioning-by-using-custom-domains.html
---

# Implement path-based API versioning by using custom domains in Amazon API Gateway
<a name="implement-path-based-api-versioning-by-using-custom-domains"></a>

*Corey Schnedl, Marcelo Barbosa, Mario Lopez Martinez, Anbazhagan Ponnuswamy, Gaurav Samudra, and Abhilash Vinod, Amazon Web Services*

## Summary
<a name="implement-path-based-api-versioning-by-using-custom-domains-summary"></a>

This pattern demonstrates how you can use the [API mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mappings.html) feature of [custom domains](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html) to implement a path-based API versioning solution for Amazon API Gateway.

Amazon API Gateway is a fully managed service that you can use to create, publish, maintain, monitor, and secure APIs at any scale. By using the service’s custom domain feature, you can create custom domain names that are simpler with more intuitive URLs that you can provide to your API users. You can use API mappings to connect API stages to a custom domain name. After you create a domain name and configure DNS records, you use API mappings to send traffic to your APIs through your custom domain name.

After an API becomes publicly available, consumers use it. As a public API evolves, its service contract also evolves to reflect new features and capabilities. However, it’s unwise to change or remove existing features. Any breaking changes might impact the consumer’s applications and break them at runtime. API versioning is important to avoid breaking backward compatibility and breaking a contract.

You need a clear strategy for API versioning to help consumers adopt them. Versioning APIs by using path-based URLs is the most straightforward and commonly used approach. In this type of versioning, versions are explicitly defined as part of API URIs. The following example URLs show how a consumer can use the URI to specify an API version for their request:

`https://api.example.com/api/v1/orders `

`https://api.example.com/api/v2/orders `

`https://api.example.com/api/vX/orders`

This pattern uses the AWS Cloud Development Kit (AWS CDK) to build, deploy, and test a sample implementation of a scalable path-based versioning solution for your API. AWS CDK is an open source software development framework to model and provision your cloud application resources using familiar programming languages.

## Prerequisites and limitations
<a name="implement-path-based-api-versioning-by-using-custom-domains-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ Ownership of a domain is required to use this pattern’s sample repository and to use Amazon API Gateway custom domain functionality. You can use Amazon Route 53 to create and manage your domains for your organization. For information about how to register or transfer a domain with Route 53, see [Registering new domains](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register-update.html) in the Route 53 documentation.
+ Before setting up a custom domain name for an API, you must have an [SSL/TLS certificate](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-specify-certificate-for-custom-domain-name.html) ready in AWS Certificate Manager.
+ You must create or update your DNS provider's resource record to map to your API endpoint. Without such a mapping, API requests bound for the custom domain name can’t reach API Gateway.

**Limitations **
+ A custom domain name must be unique within an AWS Region across all AWS accounts.
+ To configure API mappings with multiple levels, you must use a Regional custom domain name and use the TLS 1.2 security policy.
+ In an API mapping, the custom domain name and mapped APIs must be in the same AWS account.
+ API mappings must contain only letters, numbers, and the following characters: `$-_.+!*'()/`
+ The maximum length for the path in an API mapping is 300 characters.
+ You can have 200 API mappings with multiple levels for each domain name.
+ You can only map HTTP APIs to a Regional custom domain name with the TLS 1.2 security policy.
+ You can't map WebSocket APIs to the same custom domain name as an HTTP API or REST API.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ This sample implementation uses [AWS CDK in TypeScript](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-typescript.html) version 2.149.0.

## Architecture
<a name="implement-path-based-api-versioning-by-using-custom-domains-architecture"></a>

The following diagram shows the architecture workflow.

![Workflow using API mappings and custom domains to implement a path-based API versioning solution.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e1b32d2b-410f-4ace-967e-f0b8aaf0304c/images/fa9f04f1-efa6-4fb1-a541-ae3da4076b00.png)

The diagram illustrates the following:

1. The API user sends a request to Amazon API Gateway with a custom domain name.

1. API Gateway dynamically routes the user’s request to an appropriate instance and stage of API Gateway, based on the path indicated in the URL of the request. The following table shows an example of how the different URL-based paths can be routed to specific stages for different instances of API Gateway.

<table>
<tbody>
</tbody>
</table>

1. The destination API Gateway instance processes the request and returns the result to the user.

**Automation and scale**

We recommend that you use separate AWS CloudFormation stacks for each version of your API. With this approach, you can have complete isolation between the backend APIs that can be routed to by the custom domain API mapping feature. An advantage of this approach is that different versions of your API can be deployed or removed independently without introducing the risk of modifying another API. This approach increases resilience through isolation of CloudFormation stacks. Also, it provides you with different back-end options for your API such as AWS Lambda, AWS Fargate, HTTP endpoints, and actions of AWS services.

You can use Git branching strategies, such as [Gitflow](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/gitflow-branching-strategy.html), in combination with isolated CloudFormation stacks to manage the source code that’s deployed to different versions of the API. By using this option, you can maintain different versions of your API without the need to duplicate the source code for new versions. With Gitflow, you can add tags to commits within your git repository as releases are performed. As a result, you have a complete snapshot of the source code related to a specific release. As updates need to be performed, you can check out the code from a specific release, make updates, and then deploy the updated source code to the CloudFormation stack that aligns with the corresponding major version. This approach reduces the risk of breaking another API version because each version of the API has isolated source code and is deployed to separate CloudFormation stacks.

## Tools
<a name="implement-path-based-api-versioning-by-using-custom-domains-tools"></a>

**AWS services**
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) helps you create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale.
+ [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) helps you create, store, and renew public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications.
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is an open-source software development framework for defining your cloud infrastructure in code and provisioning it through CloudFormation. This pattern’s sample implementation uses the [AWS CDK in TypeScript](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-typescript.html). Working with the AWS CDK in TypeScript uses familiar tools, including the Microsoft TypeScript compiler (`tsc`), [Node.js](https://nodejs.org/), and the node package manager (`npm`). If you prefer, you can use [Yarn](https://yarnpkg.com/) although the examples in this pattern use `npm`. The modules that comprise the [AWS Construct Library](https://docs.aws.amazon.com/cdk/v2/guide/libraries.html#libraries-construct) are distributed through the `npm `repository, [npmjs.org](https://docs.npmjs.com/).
+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) is a highly available and scalable DNS web service.
+ [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) is a web application firewall that helps you monitor HTTP and HTTPS requests that are forwarded to your protected web application resources.

**Other tools**
+ [Bruno](https://www.usebruno.com/) is an open source, git-friendly API testing client.
+ [cdk-nag](https://github.com/cdklabs/cdk-nag) is an open source utility that checks AWS CDK applications for best practices by using rule packs.

**Code repository**

The code for this pattern is available in the GitHub [path-based-versioning-with-api-gateway](https://github.com/aws-samples/path-based-versioning-with-api-gateway) repository.

## Best practices
<a name="implement-path-based-api-versioning-by-using-custom-domains-best-practices"></a>
+ Use a robust continuous integration and continuous delivery (CI/CD) pipeline to automate the testing and deployment of your CloudFormation stacks that are built with the AWS CDK. For more information related to this recommendation, see the [AWS Well-Architected DevOps Guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html).
+ AWS WAF is a managed firewall that easily integrates with services like Amazon API Gateway. Although AWS WAF isn’t a necessary component for this versioning pattern to work, we recommend as a security best practice to include AWS WAF with API Gateway.
+ Encourage API consumers to upgrade regularly to the latest version of your API so that older versions of your API can be deprecated and removed efficiently.
+ Before using this approach in a production setting, implement a firewall and authorization strategy for your API.
+ Implement access to the management of AWS resources of your AWS account by using the [least-privilege access model](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege).
+ To enforce best practices and security recommendations for applications built with the AWS CDK, we recommend that you use the [cdk-nag utility](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/check-aws-cdk-applications-or-cloudformation-templates-for-best-practices-by-using-cdk-nag-rule-packs.html).

## Epics
<a name="implement-path-based-api-versioning-by-using-custom-domains-epics"></a>

### Prepare your local environment
<a name="prepare-your-local-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | To clone the sample application repository, run the following command:<pre>git clone https://github.com/aws-samples/path-based-versioning-with-api-gateway</pre> | App developer |
| Navigate to the cloned repository. | To navigate to the cloned repository folder location, run the following command: <pre>cd api-gateway-custom-domain-versioning</pre> | App developer |
| Install the required dependencies. | To install the required dependencies, run the following command:<pre>npm install </pre> | App developer |

### Deploy the CloudFormation routing stack
<a name="deploy-the-cfnshort-routing-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Initiate deployment of the routing stack. | To initiate the deployment of the CloudFormation routing stack `CustomDomainRouterStack`, run the following command, replacing `example.com` with the name of the domain that you own:<pre>npx cdk deploy CustomDomainRouterStack --parameters PrerequisiteDomainName=example.com</pre>The stack deployment will not succeed until the following domain DNS validation task is performed successfully. | App developer |

### Verify domain ownership
<a name="verify-domain-ownership"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify ownership of your domain. | The certificate will remain in a **Pending validation** status until you prove ownership of the associated domain. <br />To prove ownership, add CNAME records to the hosted zone that is associated with the domain. For more information, see [DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html) in the AWS Certificate Manager documentation. <br />Adding the appropriate records enables the `CustomDomainRouterStack` deployment to succeed. | App developer, AWS systems administrator, Network administrator |
| Create an alias record to point to your API Gateway custom domain. | After the certificate is issued and validated successfully, [create a DNS record](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html#apigateway-regional-api-custom-domain-dns-record) that points to your Amazon API Gateway custom domain URL. <br />The custom domain URL is uniquely generated by the provisioning of the custom domain and is specified as a CloudFormation output parameter. Following is an [example of the record](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-basic.html): <br />**Routing policy**: Simple routing<br />**Record name**: `demo.api-gateway-custom-domain-versioning.example.com`<br />**Alias**: Yes<br />**Record type**: A DNS record of type "A" that points to an AWS resource<br />**Value**: `d-xxxxxxxxxx.execute-api.xx-xxxx-x.amazonaws.com`<br />**TTL (seconds)**: 300 | App developer, AWS systems administrator, Network administrator |

### Deploy CloudFormation stacks and invoke the API
<a name="deploy-cfnshort-stacks-and-invoke-the-api"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the `ApiStackV1` stack. | To deploy the `ApiStackV1` stack, use the following command:<pre>npm run deploy-v1</pre><br />The following CDK code adds API mapping:<pre>var apiMapping = new CfnApiMapping(this, "ApiMapping", {<br />      apiId: this.lambdaRestApi.restApiId,<br />      domainName: props.customDomainName.domainName,<br />      stage: "api",<br />      apiMappingKey: "api/v1",<br />    });</pre> | App developer |
| Deploy the `ApiStackV2` stack. | To deploy the `ApiStackV2` stack, use the following command:<pre>npm run deploy-v2</pre> | App developer |
| Invoke the API. | To invoke the API and test the API endpoints by using Bruno, see the instructions in [Additional information](#implement-path-based-api-versioning-by-using-custom-domains-additional). | App developer |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up resources. | To destroy the resources associated with this sample application, use the following command:<pre>npx cdk destroy --all</pre>Make sure that you clean up any Route 53 DNS records that were added manually for the domain ownership verification process. | App developer |

## Troubleshooting
<a name="implement-path-based-api-versioning-by-using-custom-domains-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The deployment of `CustomDomainRouterStack` times out because the certificate can’t be validated. | Make sure that you added the proper DNS validation CNAME records as described in the earlier task. Your new certificate might continue to display a status of **Pending validation** for up to 30 minutes after adding the DNS validation records. For more information, see [DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html) in the AWS Certificate Manager documentation. |

## Related resources
<a name="implement-path-based-api-versioning-by-using-custom-domains-resources"></a>
+ [Implementing header-based API Gateway versioning with Amazon CloudFront](https://aws.amazon.com/blogs/compute/implementing-header-based-api-gateway-versioning-with-amazon-cloudfront/) – This AWS Compute Blog post offers a header-based versioning strategy as an alternative to the path-based versioning strategy outlined in this pattern.
+ [AWS CDK Workshop](https://cdkworkshop.com/20-typescript.html) – This introductory workshop focuses on building and deploying applications on AWS by using the AWS Cloud Development Kit (AWS CDK). This workshop supports Go, Python, and TypeScript.

## Additional information
<a name="implement-path-based-api-versioning-by-using-custom-domains-additional"></a>

**Testing your API with Bruno**

We recommend that you use [Bruno](https://www.usebruno.com/), an open source API testing tool, to verify that the path-based routing is working properly for the sample application. This pattern provides a sample collection to facilitate testing your sample API.

To invoke and test your API, use the following steps:

1. [Install Bruno.](https://www.usebruno.com/downloads)

1. Open Bruno.

1. In this pattern’s [code repository](https://github.com/aws-samples/path-based-versioning-with-api-gateway), select **Bruno/Sample-API-Gateway-Custom-Domain-Versioning **and open the collection.

1. To see the **Environments** dropdown in the top right of the user interface (UI), select any request in the collection.

1. In the **Environments** dropdown, select **Configure**.

1. Replace the `REPLACE_ME_WITH_YOUR_DOMAIN` value with your custom domain.

1. Choose **Save**, and then close the **Configuration** section.

1. For **Sandbox Environment**,** **verify that the **Active** option is selected.

1. Invoke your API by using the **->** button for the selected request.

1. Take note on how validation (passing in non-number values) is handled in V1 compared to V2.

To see screenshots of example API invocation and comparison of V1 and V2 validation, see **Testing your sample API** in the `README.md` file in this pattern’s [code repository](https://github.com/aws-samples/path-based-versioning-with-api-gateway).
