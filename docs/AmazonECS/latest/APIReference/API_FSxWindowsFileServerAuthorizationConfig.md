---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_FSxWindowsFileServerAuthorizationConfig.html
---

# FSxWindowsFileServerAuthorizationConfig
<a name="API_FSxWindowsFileServerAuthorizationConfig"></a>

The authorization configuration details for Amazon FSx for Windows File Server file system. See [FSxWindowsFileServerVolumeConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_FSxWindowsFileServerVolumeConfiguration.html) in the *Amazon ECS API Reference*.

For more information and the input format, see [Amazon FSx for Windows File Server Volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/wfsx-volumes.html) in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_FSxWindowsFileServerAuthorizationConfig_Contents"></a>

 ** credentialsParameter **   <a name="ECS-Type-FSxWindowsFileServerAuthorizationConfig-credentialsParameter"></a>
The authorization credential option to use. The authorization credential options can be provided using either the Amazon Resource Name (ARN) of an AWS Secrets Manager secret or SSM Parameter Store parameter. The ARN refers to the stored credentials.
Type: String
Required: Yes

 ** domain **   <a name="ECS-Type-FSxWindowsFileServerAuthorizationConfig-domain"></a>
A fully qualified domain name hosted by an [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) Managed Microsoft AD (Active Directory) or self-hosted AD on Amazon EC2.
Type: String
Required: Yes

## See Also
<a name="API_FSxWindowsFileServerAuthorizationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/FSxWindowsFileServerAuthorizationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/FSxWindowsFileServerAuthorizationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/FSxWindowsFileServerAuthorizationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
