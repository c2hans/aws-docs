---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials.html
---

# Using credentials providers in the AWS SDK for Java 2.x
<a name="credentials"></a>

The role of a credentials provider in the AWS SDK for Java 2.x is to source and supply credentials to the SDK's AWS service clients. The SDK uses the credentials it sources to authenticate with the service by cryptographically signing each request. Credentials usually consist of access keys—an access key ID and a secret access key together.

When you use temporary credentials, which are used when you setup [SSO token provider configuration](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html#sso-token-config) or configure your runtime to [assume an IAM (AWS Identity and Access Management) role](https://docs.aws.amazon.com/sdkref/latest/guide/access-assume-role.html#credOrSourceAssumeRole) as examples, a session token is added to the access keys, providing time-limited access to AWS resources.

This topic discusses several ways that you enable the SDK to access credentials.

**Topics**
+ [Interactive development work](credentials-temporary.md)
+ [Default credentials provider chain](credentials-chain.md)
+ [Credentials caching](credential-caching.md)
+ [Specify a specific credentials provider](credentials-providers.md)
+ [Use shared configuration profiles](credentials-profiles.md)
+ [Use an external process](credentials-process.md)
+ [Supply credentials in code](credentials-explicit.md)
+ [Read IAM role credentials on Amazon EC2](ec2-iam-roles.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
