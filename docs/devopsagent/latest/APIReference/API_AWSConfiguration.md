---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_AWSConfiguration.html
---

# AWSConfiguration
<a name="API_AWSConfiguration"></a>

Configuration for AWS monitor account integration, allowing AIDevOps to monitor AWS resources.

## Contents
<a name="API_AWSConfiguration_Contents"></a>

 ** accountId **   <a name="devopsagent-Type-AWSConfiguration-accountId"></a>
AWS Account Id corresponding to provided resources.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** accountType **   <a name="devopsagent-Type-AWSConfiguration-accountType"></a>
Account Type 'monitor' for AIDevOps monitoring.
Type: String
Valid Values: `monitor`
Required: Yes

 ** assumableRoleArn **   <a name="devopsagent-Type-AWSConfiguration-assumableRoleArn"></a>
Role ARN to be assumed by AIDevOps to operate on behalf of customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

## See Also
<a name="API_AWSConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/AWSConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/AWSConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/AWSConfiguration)
