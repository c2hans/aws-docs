---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/sig-v4-authenticating-requests.html
---

# Authenticating Requests (AWS Signature Version 4)
<a name="sig-v4-authenticating-requests"></a>

Every interaction with MediaPackage is either authenticated or anonymous. This section explains request authentication with the AWS Signature Version 4 algorithm.

**Note**
If you use the AWS SDKs or AWS CLI to send your requests, you don't need to read this section because these tools authenticate your requests by using access keys that you provide. You must only sign AWS API requests as described in this documentation if you do not use an AWS SDK or AWS CLI to send AWS API requests.

When you send API requests to AWS, you must sign them so that AWS can identify the sender. For security, most requests are signed using your AWS security credentials.

When MediaPackage receives an authenticated request, it recreates the signature using the authentication information contained in the request. If the signatures match, MediaPackage processes the request. Otherwise, it rejects the request.

AWS Signature Version 4 is the AWS signing protocol. AWS also supports an extension, Signature Version 4A, which supports signatures for multi-Region API requests.

For additional information about AWS Signature Version 4, see:
+ [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in the *IAM User Guide*
+ [Authenticating Requests (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) in the *Amazon Simple Storage Service API Reference*

## Creating a signed AWS API request
<a name="create-api-request"></a>

For steps to create a signed AWS API request, see:
+ [Create a signed AWS API request](https://docs.aws.amazon.com/IAM/latest/UserGuide/create-signed-request.html) in the *IAM User Guide*
+ [Signature Calculations for the Authorization Headers: Transferring Payload in a Single Chunk](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-header-based-auth.html) in the *Amazon Simple Storage Service API Reference*

## Troubleshooting signed AWS API requests
<a name="troubleshoot-signed-requests"></a>

For troubleshooting help with your signed requests, see [Troubleshoot signed requests for AWS APIs](https://docs.aws.amazon.com/IAM/latest/UserGuide/signature-v4-troubleshooting.html) in the *IAM User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
