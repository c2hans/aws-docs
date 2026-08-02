---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_IdcAuthConfiguration.html
---

# IdcAuthConfiguration
<a name="API_IdcAuthConfiguration"></a>

Configuration for AWS Identity Center (IdC) authentication flow for the Operator App.

## Contents
<a name="API_IdcAuthConfiguration_Contents"></a>

 ** createdAt **   <a name="devopsagent-Type-IdcAuthConfiguration-createdAt"></a>
The timestamp when the Operator App IdC auth flow was enabled.
Type: Timestamp
Required: Yes

 ** idcInstanceArn **   <a name="devopsagent-Type-IdcAuthConfiguration-idcInstanceArn"></a>
The IdC instance Arn used to create an IdC auth application
Type: String
Required: Yes

 ** operatorAppRoleArn **   <a name="devopsagent-Type-IdcAuthConfiguration-operatorAppRoleArn"></a>
The IAM role end users assume to access AIDevOps APIs
Type: String
Required: Yes

 ** idcApplicationArn **   <a name="devopsagent-Type-IdcAuthConfiguration-idcApplicationArn"></a>
The IdC application Arn created for IdC auth
Type: String
Required: No

 ** updatedAt **   <a name="devopsagent-Type-IdcAuthConfiguration-updatedAt"></a>
The timestamp when the Operator App IdC auth flow was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_IdcAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/IdcAuthConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/IdcAuthConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/IdcAuthConfiguration)
