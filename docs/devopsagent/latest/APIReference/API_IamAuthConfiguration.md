---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_IamAuthConfiguration.html
---

# IamAuthConfiguration
<a name="API_IamAuthConfiguration"></a>

Configuration for IAM-based authentication flow for the Operator App.

## Contents
<a name="API_IamAuthConfiguration_Contents"></a>

 ** createdAt **   <a name="devopsagent-Type-IamAuthConfiguration-createdAt"></a>
The timestamp when the Operator App IAM auth flow was enabled.
Type: Timestamp
Required: Yes

 ** operatorAppRoleArn **   <a name="devopsagent-Type-IamAuthConfiguration-operatorAppRoleArn"></a>
The IAM role end users assume to access AIDevOps APIs
Type: String
Required: Yes

 ** updatedAt **   <a name="devopsagent-Type-IamAuthConfiguration-updatedAt"></a>
The timestamp when the Operator App IAM auth flow was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_IamAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/IamAuthConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/IamAuthConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/IamAuthConfiguration)
