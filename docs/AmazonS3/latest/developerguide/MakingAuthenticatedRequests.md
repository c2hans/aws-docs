---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/developerguide/MakingAuthenticatedRequests.html
---

# Making requests using the AWS SDKs
<a name="MakingAuthenticatedRequests"></a>

**Topics**
+ [Making requests using AWS account or IAM user credentials](AuthUsingAcctOrUserCredentials.md)
+ [Making requests using IAM user temporary credentials](AuthUsingTempSessionToken.md)
+ [Making requests using federated user temporary credentials](AuthUsingTempFederationToken.md)

You can send authenticated requests to Amazon S3 using either the AWS SDK or by making the REST API calls directly in your application. The AWS SDK API uses the credentials that you provide to compute the signature for authentication. If you use the REST API directly in your applications, you must write the necessary code to compute the signature for authenticating your request. For a list of available AWS SDKs go to, [Sample Code and Libraries](https://aws.amazon.com/code/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
