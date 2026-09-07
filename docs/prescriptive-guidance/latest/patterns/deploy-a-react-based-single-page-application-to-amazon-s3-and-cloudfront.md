---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront.html
---

# Deploy a React-based single-page application to Amazon S3 and CloudFront
<a name="deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront"></a>

*Jean-Baptiste Guillois, Amazon Web Services*

## Summary
<a name="deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront-summary"></a>

A single-page application (SPA) is a website or web application that dynamically updates the contents of a displayed webpage by using JavaScript APIs. This approach enhances the user experience and performance of a website because it updates only new data instead of reloading the entire webpage from the server.

This pattern provides a step-by-step approach to coding and hosting an SPA that’s written in React on Amazon Simple Storage Service (Amazon S3) and Amazon CloudFront. The SPA in this pattern uses a REST API that’s configured in Amazon API Gateway and exposed through an Amazon CloudFront distribution to simplify [cross-origin resource sharing (CORS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html) management.

## Prerequisites and limitations
<a name="deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ Node.js and `npm`, installed and configured. For more information, see the [Downloads](https://nodejs.org/en/download/) section of the Node.js documentation.
+ Yarn, installed and configured. For more information, see the [Yarn documentation](https://classic.yarnpkg.com/lang/en/docs/install/#windows-stable).
+ Git, installed and configured. For more information, see the [Git documentation](https://github.com/git-guides/install-git).

## Architecture
<a name="deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront-architecture"></a>

![Architecture for deploying a React-based SPA to Amazon S3 and CloudFront](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/970a9d13-e8a2-44ac-aca5-a066e4be60e8/images/96061e05-8ac8-446e-b1da-baa6fc1cc7b6.png)

This architecture is automatically deployed by using AWS CloudFormation (infrastructure as code). It uses Regional services such as Amazon S3 to store the static assets and Amazon CloudFront with Amazon API Gateway to expose Regional API (REST) endpoints. The application logs are collected by using Amazon CloudWatch. All AWS API calls are audited in AWS CloudTrail. All security configuration (for example, identities and permissions) is managed in AWS Identity and Access Management (IAM). Static content is delivered through the Amazon CloudFront content delivery network (CDN), and DNS queries are handled by Amazon Route 53.

## Tools
<a name="deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront-tools"></a>

**AWS services**
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) helps you create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) speeds up distribution of your web content by delivering it through a worldwide network of data centers, which lowers latency and improves performance.
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you audit the governance, compliance, and operational risk of your AWS account.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) is a highly available and scalable DNS web service.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Code**

This pattern's sample application code is available in the GitHub [React-based CORS single-page application](https://github.com/aws-samples/react-cors-spa) repository.

## Best practices
<a name="deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront-best-practices"></a>

By using Amazon S3 object storage, you can store your application’s static assets in a secure, highly resilient, performant, and cost-effective way. There is no need to use a dedicated container or an Amazon Elastic Compute Cloud (Amazon EC2) instance for this task.

By using the Amazon CloudFront content delivery network, you can reduce the latency your users might experience when they access your application. You can also attach a web application firewall ([AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/cloudfront-features.html)) to protect your assets from malicious attacks.

## Epics
<a name="deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront-epics"></a>

### Locally build and deploy your application
<a name="locally-build-and-deploy-your-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | Run the following command to clone the sample application's repository:<pre>git clone https://github.com/aws-samples/react-cors-spa react-cors-spa && cd react-cors-spa</pre> | App developer, AWS DevOps |
| Locally deploy the application. | 1. In the project directory, run the `npm install` command to initiate the application dependencies. <br />2. Run the `yarn dev` command to start the application locally.  | App developer, AWS DevOps |
|  Locally access the application. | Open a browser window and enter the `http://localhost:3000` URL to access the application. | App developer, AWS DevOps |

### Deploy the application
<a name="deploy-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the AWS CloudFormation template. | 1. Sign in to the AWS Management Console, and then open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation).<br />2. Choose **Create Stack**, and then choose **With new resources (standard)**.<br />3. Choose **Upload a template file**.<br />4. Choose **Choose file**, choose the `react-cors-spa-stack.yaml` file from the cloned repository, and then choose **Next**.<br />5. Enter a name for your stack, and then choose **Next**.<br />6. Keep all default options, and then choose **Next**.<br />7. Review the final settings for your stack, and then choose **Create stack**. | App developer, AWS DevOps |
| Customize your application source files. | 1. After your stack is deployed, open the **Output** tab and identify the `Bucket` name and `APIDomain` value.<br />2. Copy the CloudFront distribution domain for the REST API.<br />3. Navigate to `<project_root>/src/pages/index.tsx`, and then insert or paste this domain into the `APIEndPoint` variable value on line 13 of the `index.tsx` file. | App developer |
| Build the application package. | In your project directory, run the `yarn build` command to build the application package. | App developer |
| Deploy the application package. | 1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/).<br />2. Identify and choose the S3 bucket that was created earlier by the CloudFormation stack.<br />3. Choose **Upload**, and then choose **Add files**.<br />4. Choose the content of your `out` folder.<br />5. Choose **Add folder**, and then choose the `_next` directory.Choose the `_next` directory, not the contents.<br />6. Choose **Upload** to upload the files and directory to your S3 bucket. | App developer, AWS DevOps |

### Test the application
<a name="test-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Access and test the application. | Open a browser window, and then paste the CloudFront distribution domain (the `SPADomain` output from the CloudFormation stack that you deployed previously) to access the application. | App developer, AWS DevOps |

### Clean up the resources
<a name="clean-up-the-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the S3 bucket contents. | 1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/) and choose the bucket that was created earlier by the stack (the first bucket whose name starts with `react-cors-spa-`). <br />2. Choose **Empty** to delete the bucket’s contents.<br />3. Choose the second bucket that was created earlier by the stack (the second bucket whose name starts with `react-cors-spa-` and ends with `-logs`). <br />4. Choose **Empty** to delete the bucket’s contents. | AWS DevOps, App developer |
| Delete the CloudFormation stack. | 1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation) and choose the stack that you created earlier.<br />2. Choose **Delete** to delete the stack and all related resources. | AWS DevOps, App developer |

## Related resources
<a name="deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront-resources"></a>

To deploy and host your web application, you can also use [AWS Amplify Hosting](https://docs.aws.amazon.com/amplify/latest/userguide/getting-started.html), which provides a Git-based workflow for hosting full-stack, serverless web apps with continuous deployment. Amplify Hosting is part of [AWS Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html), which provides a set of purpose-built tools and features that enable frontend web and mobile developers to quickly and easily build full-stack applications on AWS.

## Additional information
<a name="deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront-additional"></a>

To handle invalid URLs requested by the user that might generate 403 errors, a custom error page that’s configured in the CloudFront distribution catches 403 errors and redirects them to the application entry point (`index.html`).

To simplify the management of CORS, the REST API is exposed through a CloudFront distribution.
