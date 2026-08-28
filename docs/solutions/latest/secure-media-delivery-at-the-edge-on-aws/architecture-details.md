---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

 This section describes the components and AWS services that make up this solution and the architecture details on how these components work together.

## Base module
<a name="base-module"></a>

![Secure Media Delivery at the Edge on AWS: Base module architecture diagram.](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/image3.png)

 The base module includes solution components that are central to the solution, while the rest of the modules further expands on it. From a functional standpoint, it encompasses some of the key elements for providing the most fundamental outcomes for this solution, which are:
+  A validator function implemented as a CloudFront Function code that you attach to your CloudFront distribution. This function inspects requests’ attached token and validates conditions.
+  AWS Secrets Manager stores the secrets holding signing keys that are used when the token is generated and validated. This part of the solution does not require any user maintenance when keys are created, updated new keys are distributed to CloudFront Function validator, and when keys are supplied to the service generating tokens through the provided solution library.
+  AWS WAF rule group, Lambda function, and DynamoDB connect together to create a session revocation pipeline. The session revocation pipeline allows blocking playback sessions that are determined as compromised. The details of the compromised sessions can be either sent manually through the method that can be found in the solution library, or in an automated way by the means of automatic session revocation. Automatic session revocation automatically runs a log processing pipeline to detect suspicious sessions and push them towards that AWS WAF rule group.

 The `Validator` CloudFront function is the same, static code which doesn’t change across implementations and use cases. As such, it can be associated with multiple CloudFront distributions delivering different types of video streaming content, as long as it is acceptable to use the same set of signing keys in all cases. Function logic takes the token (subject to validation) from the beginning of the URL path and removes it, before moving the request forward upon successfully token validation. Because CloudFront Function is attached to viewer request trigger, using an individual token does not affect the cache hit rate, as the function code removes the token from the URL path before the cache key is computed. This means that viewers requesting the same video object but using different, individual tokens, will still share the same object from the cache. With regards to scalability, CloudFront Functions have been designed to follow CloudFront scale, and no additional considerations are required in terms of adjusting the service limits for this component. When token validation process is invoked, the input string retrieved from the URL path for further processing has the following format:

 `[SessionID].JWTHeader.JWTPayload.JWTSignagure `

 **SessionId** parameter is optional. You can generate your token without Session ID associated with it. During token generation step, if you decide to omit the Session ID, it will not be present in the URL path, and only JSON Web Token (JWT) elements will remain. In both cases, there is no need to modify CloudFront Functions as it handles the process of recognizing if Session ID is present.

 The process of validating and processing the token can be broadly broken into three discrete stages:
+  Verifying JWT signature to validate token integrity. The signing key used here is derived from the unique key identifier that is set in the JWT header UUID. From that UUID, CloudFront Functions determines the corresponding key value.
+  Checking access conditions as per claims included in the token. These conditions can be categorized as follows:
  +  Time-bounding conditions: to verify if the token is within its validity period
  +  Asset attributes conditions: to check if requested object matches with the content the token was issued for
  +  Viewer attributes conditions: tokens can be generated for specific viewer attributes for example, source IP, user-agent headers, session ID etc., to improve the uniqueness of a token. In this category, additional signature is calculated from the viewer’s attributes available in the function invocation context, and compared with the signature included in the token calculated at playback API stage when token was vended to the viewer.
+  Token acceptance decision – if token verification failed in any of the previous stages, the request is terminated by the function and a 403 (Forbidden) status code is returned back to the viewer. If the request satisfies all of the access conditions and validation steps, it is permitted. After removing the token from the URL path, the request continues the normal processing path on CloudFront.

 It is important to note that the viewer attribute conditions checks, on viewer’s request, are based on metadata included in the [event object](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/functions-event-structure.html) available in CloudFront Functions. While some of the viewer request attributes are always available and present in that object, for example, viewer’s IP, headers, and query string parameters, some of the viewer specific attributes require additional configuration steps. Those attributes are location-specific attributes that can be included in the token, for example, viewer’s country and region. This information is conveyed through specific [CloudFront generated headers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-cloudfront-headers.html): CloudFront-Viewer-Country, CloudFront-Viewer-Country-Region, which are only generated and made available in the event object, when each of these headers is listed either in [cache or origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html). Configuring these headers in the cache policy split the object in the cache per country the traffic is coming from, and effectively decrease the cache hit ratio. Therefore, we recommend including these headers in the origin request policy as additional headers.

## AWS services in this solution
<a name="aws-services"></a>

|  AWS service  |  Description  |
| --- | --- |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  Core. Validates secure tokens, permitting or denying access to video content.  |
|  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)  |  Core. Stores secrets holding signing keys for generating and validating viewer’s tokens  |
|  [AWS Step Functions](https://aws.amazon.com/step-functions/)  |  Core. Coordinates key rotation processes.  |
|  [Amazon API Gateway](https://aws.amazon.com/api-gateway/)  |  Core. Processes requests to generate the tokens for video playback, and to manually revoke specified playback sessions.  |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  Core. Supports API Gateway to generate token for video playback and signs outgoing requests.  |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  Core. Provides storage of static assets for the demo website and CloudFront access logs.  |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  Core. Stores metadata about video assets and corresponding parameters used to generate tokens.  |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  Core. Invokes session revocation workflow in AWS Step Functions.  |
|  [Amazon Athena](https://aws.amazon.com/athena/)  |  Core. Runs SQL queries against CloudFront access logs to list the suspicious video playback session ids with abnormal traffic characteristics.  |
|  [AWS WAF](https://aws.amazon.com/waf/)  |  Core. Provides the list of playback sessions that should be blocked as they get identified as compromised.  |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  Supporting. Provides application-level resource monitoring and visualization of resource operations and cost data.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
