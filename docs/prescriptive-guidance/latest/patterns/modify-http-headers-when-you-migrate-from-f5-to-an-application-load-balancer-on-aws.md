---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modify-http-headers-when-you-migrate-from-f5-to-an-application-load-balancer-on-aws.html
---

# Modify HTTP headers when you migrate from F5 to an Application Load Balancer on AWS
<a name="modify-http-headers-when-you-migrate-from-f5-to-an-application-load-balancer-on-aws"></a>

*Sachin Trivedi, Amazon Web Services*

## Summary
<a name="modify-http-headers-when-you-migrate-from-f5-to-an-application-load-balancer-on-aws-summary"></a>

When you migrate an application that uses an F5 Load balancer to Amazon Web Services (AWS) and want to use an Application Load Balancer on AWS, migrating F5 rules for header modifications is a common problem. An Application Load Balancer doesn’t support header modifications, but you can use Amazon CloudFront as a content delivery network (CDN) and Lambda@Edge to modify headers.

This pattern describes the required integrations and provides sample code for header modification by using AWS CloudFront and Lambda@Edge.

## Prerequisites and limitations
<a name="modify-http-headers-when-you-migrate-from-f5-to-an-application-load-balancer-on-aws-prereqs"></a>

**Prerequisites **
+ An on-premises application that uses an F5 load balancer with a configuration that replaces the  HTTP header value by using `if, else`. For more information about this configuration, see [HTTP::header](https://clouddocs.f5.com/api/irules/HTTP__header.html) in the F5 product documentation.

**Limitations **
+ This pattern applies to F5 load balancer header customization. For other third-party load balancers, please check the load balancer documentation for support information.
+ The Lambda functions that you use for Lambda@Edge must be in the US East (N. Virginia) Region.

## Architecture
<a name="modify-http-headers-when-you-migrate-from-f5-to-an-application-load-balancer-on-aws-architecture"></a>

The following diagram shows the architecture on AWS, including the integration flow between the CDN and other AWS components.

![Architecture for header modification by using Amazon CloudFront and Lambda@Edge](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/00abbe3c-2453-4291-9b24-b488dced4868/images/4ee9a19e-6da2-4c5a-a8bc-19d3918a166e.png)

## Tools
<a name="modify-http-headers-when-you-migrate-from-f5-to-an-application-load-balancer-on-aws-tools"></a>

**AWS services**
+ [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) ─  An Application Load Balancer is an AWS fully managed load balancing service that functions at the seventh layer of the Open Systems Interconnection (OSI) model. It balances traffic across multiple targets and supports advanced routing requests based on HTTP headers and methods, query strings, and host-based or path-based routing.
+ [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) – Amazon CloudFront is a web service that speeds up the distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations for lower latency and improved performance.
+ [Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html) ─ Lambda@Edge is an extension of AWS Lambda that lets you run functions to customize the content that CloudFront delivers. You can author functions in the US East (N. Virginia) Region, and then associate the function with a CloudFront distribution to automatically replicate your code around the world, without provisioning or managing servers. This reduces latency and improves the user experience.

**Code**

The following sample code provides a blueprint for modifying CloudFront response headers. Follow the instructions in the *Epics* section to deploy the code.

```
exports.handler = async (event, context) => {
    const response = event.Records[0].cf.response;
    const headers = response.headers;

    const headerNameSrc = 'content-security-policy';
    const headerNameValue = '*.xyz.com';

    if (headers[headerNameSrc.toLowerCase()]) {
        headers[headerNameSrc.toLowerCase()] = [{
            key: headerNameSrc,
            value: headerNameValue,
        }];
        console.log(`Response header "${headerNameSrc}" was set to ` +
                    `"${headers[headerNameSrc.toLowerCase()][0].value}"`);
    }
    else {
            headers[headerNameSrc.toLowerCase()] = [{
            key: headerNameSrc,
            value: headerNameValue,
            }];
    }
    return response;
};
```

## Epics
<a name="modify-http-headers-when-you-migrate-from-f5-to-an-application-load-balancer-on-aws-epics"></a>

### Create a CDN distribution
<a name="create-a-cdn-distribution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a CloudFront web distribution.  | In this step, you create a CloudFront distribution to tell CloudFront where you want content to be delivered from, and the details about how to track and manage content delivery.<br />To create a distribution by using the console, sign in to the AWS Management Console, open the [CloudFront console](https://console.aws.amazon.com/cloudfront/v3/home), and then follow the steps in the [CloudFront documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.html). | Cloud administrator |

### Create and deploy the Lambda@Edge function
<a name="create-and-deploy-the-lambda-edge-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create and deploy a Lambda@Edge function. | You can create a Lambda@Edge function by using a blueprint for modifying CloudFront response headers. (Other bluePrints are available for different use cases; for more information, see [Lambda@Edge example functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html) in the CloudFront documentation.) <br />To create a Lambda@Edge function:1. Sign in to the AWS Management Console and open the AWS Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/).<br />2. Make sure that you’re in the US East (N. Virginia) Region. CloudFront blueprints are available only in this Region.<br />3. Choose **Create function**.<br />4. Choose **Use a blueprint**, and then enter **cloudfront **in the **Blueprints** search field. <br />5. Choose the **cloudfront-modify-response-header** blueprint, and then choose **Configure**.<br />6. On the **Basic information **page, enter the following information:Enter a function name.For **Execution role**, choose **Create a new role from AWS policy templates**.Associate the required AWS Identity and Access Management (IAM) role name.<br />7. Choose **Create function**.<br />8. In the **Designer** section of the page, choose your function name.<br />9. In the **Function code** section, replace the template code with the sample code provided previously in this pattern, in the *Code *section.<br />10. In the sample code, replace `xyz.com` with your domain name.  <br />11. Choose **Save**. | AWS administrator |
| Deploy the Lambda@Edge function. | Follow the instructions in [step 4](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works-tutorial.html#lambda-edge-how-it-works-tutorial-add-trigger) of the *Tutorial: Creating a simple Lambda@Edge function* in the Amazon CloudFront documentation to configure the CloudFront trigger and deploy the function. | AWS administrator |

## Related resources
<a name="modify-http-headers-when-you-migrate-from-f5-to-an-application-load-balancer-on-aws-resources"></a>

**CloudFront documentation**
+ [Request and response behavior for custom origins](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html)
+ [Working with distributions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.html)
+ [Lambda@Edge example functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html)
+ [Customizing at the edge with Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html)
+ [Tutorial: Creating a simple Lambda@Edge function](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-how-it-works-tutorial.html)
