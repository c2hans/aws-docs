---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/presentation-tier.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Presentation tier
<a name="presentation-tier"></a>

 The presentation tier is responsible for interacting with the logic tier through the API Gateway REST endpoints exposed over the internet. Any HTTPS capable client or device can communicate with these endpoints, giving your presentation tier the flexibility to take many forms (desktop applications, mobile apps, webpages, IoT devices, and so forth). Depending on your requirements, your presentation tier can use the following AWS serverless offerings:
+  **Amazon Cognito** - A serverless user identity and data synchronization service that enables you to add user sign-up, sign-in, and access control to your web and mobile apps quickly and efficiently. Amazon Cognito scales to millions of users and supports sign-in with social identity providers, such as Facebook, Google, and Amazon, and enterprise identity providers through SAML 2.0.
+  ** Amazon S3 with CloudFront** - Enables you to serve static websites, such as single-page applications, directly from an S3 bucket without requiring provision of a web server. You can use CloudFront as a managed content delivery network (CDN) to improve performance and enable SSL/TL using managed or custom certificates.

 [AWS Amplify](https://aws.amazon.com/amplify) is a set of tools and services that can be used together or on their own, to help front-end web and mobile developers build scalable full stack applications, powered by AWS. Amplify offers a fully managed service for deploying and hosting static web applications globally, served by Amazon's reliable CDN with hundreds of points of presence globally and with built-in CI/CD workflows that accelerate your application release cycle. Amplify supports popular web frameworks including JavaScript, React, Angular, Vue, Next.js, and mobile platforms including Android, iOS, React Native, Ionic, and Flutter. Depending on your networking configurations and application requirements, you might need to enable your API Gateway APIs to be cross-origin resource sharing (CORS) – compliant. CORS compliance allows web browsers to directly invoke your APIs from within static webpages.

 When you deploy a website with CloudFront, you are provided a CloudFront domain name to reach your application (for example, `d2d47p2vcczkh2.cloudfront.net`). You can use [Amazon Route 53](https://aws.amazon.com/route53) to register domain names and direct them to your CloudFront distribution, or direct already-owned domain names to your CloudFront distribution. This enables users to access your site using a familiar domain name. Note that you can also assign a custom domain name using Route 53 to your API Gateway distribution, which enables users to invoke APIs using familiar domain names.
