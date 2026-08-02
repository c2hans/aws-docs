---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/serve-static-content-in-an-amazon-s3-bucket-through-a-vpc-by-using-amazon-cloudfront.html
---

# Serve static content in an Amazon S3 bucket through a VPC by using Amazon CloudFront
<a name="serve-static-content-in-an-amazon-s3-bucket-through-a-vpc-by-using-amazon-cloudfront"></a>

*Angel Emmanuel Hernandez Cebrian, Amazon Web Services*

## Summary
<a name="serve-static-content-in-an-amazon-s3-bucket-through-a-vpc-by-using-amazon-cloudfront-summary"></a>

When you serve static content that is hosted on Amazon Web Services (AWS), the recommended approach is to use an Amazon Simple Storage Service (S3) bucket as the origin and use Amazon CloudFront to distribute the content. This solution has two primary benefits: the convenience of caching static content at edge locations, and the ability to define [web access control lists](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html) (web ACLs) for the CloudFront distribution, which helps you secure requests to the content with minimal configuration and administrative overhead.

However, there is a common architectural limitation to the standard, recommended approach. In some environments, you want virtual firewall appliances deployed in a virtual private cloud (VPC) to inspect all content, including static content. The standard approach doesn’t route traffic through the VPC for inspection. This pattern provides an alternative architectural solution. You still use a CloudFront distribution to serve static content in an S3 bucket, but the traffic is routed through the VPC by using an Application Load Balancer. An AWS Lambda function then retrieves and returns the content from the S3 bucket.

## Prerequisites and limitations
<a name="serve-static-content-in-an-amazon-s3-bucket-through-a-vpc-by-using-amazon-cloudfront-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ Static website content hosted in an S3 bucket.

**Limitations**
+ The resources in this pattern must be in a single AWS Region, but they can be provisioned in different AWS accounts.
+ Limits apply to the maximum request and response size that the Lambda function can receive and send, respectively. For more information, see *Limits* in [Lambda functions as targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html) (Elastic Load Balancing documentation).
+ It's important to find a good balance between performance, scalability, security, and cost-effectiveness when using this approach. Despite the high scalability of Lambda, if the number of concurrent Lambda invocations exceeds the maximum quota, some requests are throttled. For more information, see Lambda quotas (Lambda documentation). You also need to consider pricing when using Lambda. To minimize Lambda invocations, make sure that you properly define the cache for the CloudFront distribution. For more information, see [Optimizing caching and availability](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html) (CloudFront documentation).

## Architecture
<a name="serve-static-content-in-an-amazon-s3-bucket-through-a-vpc-by-using-amazon-cloudfront-architecture"></a>

**Target technology stack  **
+ CloudFront
+ Amazon Virtual Private Cloud (Amazon VPC)
+ Application Load Balancer
+ Lambda
+ Amazon S3

**Target architecture**

The following image shows the suggested architecture when you need to use CloudFront to serve static content from an S3 bucket through a VPC.

![Traffic flow through Application Load Balancers in the VPC to the Lambda function.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e0dd6928-4fe0-47ab-954f-9de5563349d8/images/b42c7dd9-4a72-4998-bf88-195c8f90ed3e.png)

1. The client requests the URL of CloudFront distribution to get a particular website file in the S3 bucket.

1. CloudFront sends the request to AWS WAF. AWS WAF filters the request by using the web ACLs applied to the CloudFront distribution. If the request is determined to be valid, the flow continues. If the request is determined to be invalid, the client receives a 403 error.

1. CloudFront checks its internal cache. If there is a valid key matching the incoming request, the associated value is sent back to the client as a response. If not, the flow continues.

1. CloudFront forwards the request to the URL of the specified Application Load Balancer.

1. The Application Load Balancer has a listener associated with a target group based on a Lambda function. The Application Load Balancer invokes the Lambda function.

1. The Lambda function connects to the S3 bucket, perform a `GetObject` operation on it, and returns the content as a response.

**Automation and scale**

To automate the deployment of static content using this approach, create CI/CD pipelines to update the Amazon S3 buckets that host websites.

The Lambda function scales automatically to handle the concurrent requests, within the quotas and limitations of the service. For more information, see [Lambda function scaling](https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html) and [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) (Lambda documentation). For the other AWS services and features, such as CloudFront and the Application Load Balancer, AWS scales these automatically.

## Tools
<a name="serve-static-content-in-an-amazon-s3-bucket-through-a-vpc-by-using-amazon-cloudfront-tools"></a>
+ [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) speeds up distribution of your web content by delivering it through a worldwide network of data centers, which lowers latency and improves performance.
+ [Elastic Load Balancing (ELB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) distributes incoming application or network traffic across multiple targets. In this pattern, you use an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) provisioned through Elastic Load Balancing to direct traffic to the Lambda function.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

## Epics
<a name="serve-static-content-in-an-amazon-s3-bucket-through-a-vpc-by-using-amazon-cloudfront-epics"></a>

### Use CloudFront to serve static content from Amazon S3 through a VPC
<a name="use-cloudfront-to-serve-static-content-from-amazon-s3-through-a-vpc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC. | Create a VPC for hosting the resources deployed in this pattern, such as the Application Load Balancer and the Lambda function.  For instructions, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#Create-VPC) (Amazon VPC documentation). | Cloud architect |
| Create an AWS WAF web ACL. | Create an AWS WAF web ACL. Later in this pattern, you apply this web ACL to the CloudFront distribution. For instructions, see [Creating a web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-creating.html) (AWS WAF documentation). | Cloud architect |
| Create the Lambda function. | Create the Lambda function that serves the static content hosted in the S3 bucket as a website. Use the code provided in the [Additional information](#serve-static-content-in-an-amazon-s3-bucket-through-a-vpc-by-using-amazon-cloudfront-additional) section of this pattern. Customize the code to identify your target S3 bucket. | General AWS |
| Upload the Lambda function. | Enter the following command to upload the Lambda function code to a .zip file archive in Lambda.<pre>aws lambda update-function-code \<br />--function-name  \ <br />--zip-file fileb://lambda-alb-s3-website.zip</pre> | General AWS |
| Create an Application Load Balancer. | Create an internet-facing Application Load Balancer that points to the Lambda function. For instructions, see [Create a target group for the Lambda function](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html#register-lambda-function) (Elastic Load Balancing documentation). For a high-availability configuration, create the Application Load Balancer and attach it to private subnets in different Availability Zones. | Cloud architect |
| Create a CloudFront distribution. | Create a CloudFront distribution that points to the Application Load Balancer you created.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/serve-static-content-in-an-amazon-s3-bucket-through-a-vpc-by-using-amazon-cloudfront.html) | Cloud architect |

## Related resources
<a name="serve-static-content-in-an-amazon-s3-bucket-through-a-vpc-by-using-amazon-cloudfront-resources"></a>

**AWS documentation**
+ [Optimizing caching and availability](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html) (CloudFront documentation)
+ [Lambda functions as targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html) (Elastic Load Balancing documentation)
+ [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) (Lambda documentation)

**AWS service websites**
+ [Application Load Balancer](https://aws.amazon.com/es/elasticloadbalancing/application-load-balancer/)
+ [Lambda](https://aws.amazon.com/en/lambda/)
+ [CloudFront](https://aws.amazon.com/en/cloudfront/)
+ [Amazon S3](https://aws.amazon.com/en/s3/)
+ [AWS WAF](https://aws.amazon.com/en/waf/)
+ [Amazon VPC](https://aws.amazon.com/en/vpc/)

## Additional information
<a name="serve-static-content-in-an-amazon-s3-bucket-through-a-vpc-by-using-amazon-cloudfront-additional"></a>

**Code**

The following example Lambda function is written in Node.js. This Lambda function acts as a web server that performs a `GetObject` operation to an S3 bucket that contains the website resources.

```
/**

 * This is an AWS Lambda function created for demonstration purposes.

 * It retrieves static assets from a defined Amazon S3 bucket.

 * To make the content available through a URL, use an Application Load Balancer with a Lambda integration.
 *
 * Set the S3_BUCKET environment variable in the Lambda function definition.
 */

var AWS = require('aws-sdk');

exports.handler = function(event, context, callback) {

    var bucket = process.env.S3_BUCKET;
    var key = event.path.replace('/', '');

    if (key == '') {
        key = 'index.html';
    }

    // Fetch from S3
    var s3 = new AWS.S3();
    return s3.getObject({Bucket: bucket, Key: key},
       function(err, data) {

            if (err) {
                return err;
            }

            var isBase64Encoded = false;
            var encoding = 'utf8';

            if (data.ContentType.indexOf('image/') > -1) {
                isBase64Encoded = true;
                encoding = 'base64'
            }

            var resp = {
                statusCode: 200,
                headers: {
                    'Content-Type': data.ContentType,
                },
                body: new Buffer(data.Body).toString(encoding),
                isBase64Encoded: isBase64Encoded
            };

            callback(null, resp);
        }
    );
};
```
