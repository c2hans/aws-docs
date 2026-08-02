---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

 This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

 Deploying the Secure Media Delivery at the Edge on AWS solution in an existing environment with Amazon CloudFront and Media Origin service creates a number of resources. These resources play different roles and can be grouped into three functional modules as shown in the following reference architecture diagram.

![Secure Media Delivery at the Edge on AWS architecture diagram](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/image2.png)

 **Base module**

1.  An [Amazon CloudFront](https://aws.amazon.com/cloudfront/) Function that validates secure tokens, permitting or denying access to video content.

1.  An [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) stores secrets holding signing keys for generating and validating viewers’ tokens.

1.  An [AWS Step Functions](https://aws.amazon.com/step-functions/) workflow that coordinates key rotation process.

1.  An AWS WAF rule group containing the list of playback sessions that should be blocked as they get identified as compromised.

1.  An [Amazon API Gateway](https://aws.amazon.com/api-gateway/) public API used to process requests to generate the tokens for video playback, and to manually revoke specified playback sessions.

1.  An [AWS Lambda](https://aws.amazon.com/lambda) function associated with API Gateway that generates the token for video playback based on the retrieved metadata about the video assets and token parameters.

1.  A solution-provided library that provides the necessary methods to generate the tokens, imported into the AWS Lambda Function.

 **API Module**

1.  An [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) table to store metadata about video assets and corresponding parameters used to generate the tokens.

1.  An Amazon CloudFront distribution to deliver the traffic from API Gateway and deliver demo website when activated.

1.  A Lambda@Edge function that signs outgoing requests towards API Gateway according to SigV4 specification.

1.  A demo website (when activated) with video player embedded in it.

1.  An [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket that stores static assets for the demo website.

 **Auto session revocation module**

1.  An [Amazon EventBridge](https://aws.amazon.com/eventbridge/) rule that runs periodically to invoke session revocation workflow in AWS Step Functions.

1.  Lambda functions invoked in Step Functions workflow that produce SQL query submitted to Amazon Athena, to obtain the results from Amazon Athena, and push moving them forward in the processing pipeline.

1.  [Amazon Athena](https://aws.amazon.com/athena/) running SQL queries against CloudFront access logs to list the suspicious video playback session ids with abnormal traffic characteristics.

1.  An Amazon DynamoDB table revocation list to store session IDs that have been submitted to be revoked with additional information.

1.  A Lambda function which compiles a final list of the playback sessions marked to be blocked and updates AWS WAF rule group with the appropriate rules matching selected sessions.

**Note**
 AWS CloudFormation resources are created from AWS Cloud Development Kit (AWS CDK) (AWS CDK) constructs.
