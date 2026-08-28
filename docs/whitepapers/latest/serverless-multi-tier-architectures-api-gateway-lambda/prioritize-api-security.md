---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/prioritize-api-security.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Prioritize API security
<a name="prioritize-api-security"></a>

 All applications must ensure that only authorized clients have access to their API resources. When designing a multi-tier application, you can take advantage of several different ways in which Amazon API Gateway contributes to securing your logic tier:

## Transit security
<a name="transit-security"></a>

 All requests to your APIs can be made through HTTPS to enable encryption in transit.

 API Gateway provides built-in SSL/TLS Certificates – if using the custom domain name option for public-facing APIs, you can provide your own SSL/TLS certificate using [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/). API Gateway also supports mutual TLS (mTLS) authentication. Mutual TLS enhances the security of your API and helps protect your data from attacks such as client spoofing or man-in-the middle attacks.

## API authorization
<a name="api-authorization"></a>

 Each resource/method combination that you create as part of your API is granted a unique Amazon Resource Name (ARN) that can be referenced in AWS Identity and Access Management (IAM) policies.

 There are three general methods to add authorization to an API in API Gateway:
+  **IAM Roles and Policies:** Clients use [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) (SigV4) authorization and IAM policies for API access. The same credentials can restrict or permit access to other AWS services and resources as needed (for example, Amazon S3 buckets or Amazon DynamoDB tables).
+  **Amazon Cognito user pools:** Clients sign in through an [Amazon Cognito](https://aws.amazon.com/cognito/) user pool and obtain tokens, which are included in the authorization header of a request.
+  **Lambda authorizer:** Define a Lambda function that implements a custom authorization scheme that uses a bearer token strategy (for example, OAuth and SAML) or uses request parameters to identify users.

## Access restrictions
<a name="access-restrictions"></a>

 API Gateway supports generation of API keys and association of these keys with a configurable usage plan. You can monitor API key usage with CloudWatch.

 API Gateway supports throttling, rate limits, and burst rate limits for each method in your API.

## Private APIs
<a name="private-apis"></a>

Using API Gateway, you can create private REST APIs that can only be accessed from your virtual private cloud in Amazon VPC by using an interface VPC endpoint. This is an endpoint network interface that you create in your VPC.

Using resource policies, you can enable or deny access to your API from selected VPCs and VPC endpoints, including across AWS accounts. Each endpoint can be used to access multiple private APIs. You can also use AWS Direct Connect to establish a connection from an on-premises network to Amazon VPC and access your private API over that connection.

In all cases, traffic to your private API uses secure connections and does not leave the Amazon network—it is isolated from the public internet.

## Firewall protection using AWS WAF
<a name="firewall-protection-using-aws-waf"></a>

Internet-facing APIs are vulnerable to malicious attacks. AWS WAF is a web application firewall which helps protect APIs from such attacks. It protects APIs from common web exploits such as SQL injection and cross-site scripting attacks. You can use [AWS WAF](https://aws.amazon.com/waf/) with API Gateway to help protect APIs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
