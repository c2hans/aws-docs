---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations-access-configuration.html
---

# Configuring authentication for your source location
<a name="channel-assembly-source-locations-access-configuration"></a>

Use **access configuration** to configure authentication for your source location. When access configuration is on, MediaTailor only retrieves source manifests from your origin if the request is authorized between MediaTailor and your origin. Access configuration is turned off by default.

MediaTailor supports the following authentication types:
+ SigV4 for Amazon S3 authentication
+ AWS Secrets Manager access token
+ SigV4 for MediaPackage version 2 (v2) authentication

 This chapter explains how to use SigV4 for Amazon S3, MediaPackage v2, and AWS Secrets Manager access tokens for source location authentication.

 For more information, select the applicable topic.

**Topics**
+ [Authenticating requests to Amazon S3 with SigV4](channel-assembly-access-configuration-sigv4.md)
+ [Working with SigV4 for MediaPackage Version 2](channel-assembly-access-configuration-sigv4-empv2.md)
+ [Working with AWS Secrets Manager access token authentication](channel-assembly-access-configuration-access-token.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
