---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SourceAwsConfiguration.html
---

# SourceAwsConfiguration
<a name="API_SourceAwsConfiguration"></a>

Configuration for AWS source account integration. Note: passRole check on 'assumableRoleArn' is not supported.

## Contents
<a name="API_SourceAwsConfiguration_Contents"></a>

 ** accountId **   <a name="devopsagent-Type-SourceAwsConfiguration-accountId"></a>
AWS Account Id corresponding to provided resources.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** accountType **   <a name="devopsagent-Type-SourceAwsConfiguration-accountType"></a>
Account Type 'source' for AIDevOps monitoring.
Type: String
Valid Values: `source`
Required: Yes

 ** assumableRoleArn **   <a name="devopsagent-Type-SourceAwsConfiguration-assumableRoleArn"></a>
Role ARN to be assumed by AIDevOps to operate on behalf of customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

 ** externalId **   <a name="devopsagent-Type-SourceAwsConfiguration-externalId"></a>
External ID for additional security when assuming the role. Used to prevent the confused deputy problem.
Type: String
Required: No

## See Also
<a name="API_SourceAwsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SourceAwsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SourceAwsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SourceAwsConfiguration)
