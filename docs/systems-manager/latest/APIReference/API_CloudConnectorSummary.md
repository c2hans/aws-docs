---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CloudConnectorSummary.html
---

# CloudConnectorSummary
<a name="API_CloudConnectorSummary"></a>

Summary information about a cloud connector.

## Contents
<a name="API_CloudConnectorSummary_Contents"></a>

 ** CloudConnectorId **   <a name="systemsmanager-Type-CloudConnectorSummary-CloudConnectorId"></a>
The ID of the cloud connector.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** CreatedAt **   <a name="systemsmanager-Type-CloudConnectorSummary-CreatedAt"></a>
The date and time the cloud connector was created.
Type: Timestamp
Required: No

 ** Description **   <a name="systemsmanager-Type-CloudConnectorSummary-Description"></a>
The description of the cloud connector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
Required: No

 ** DisplayName **   <a name="systemsmanager-Type-CloudConnectorSummary-DisplayName"></a>
The friendly name of the cloud connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
Required: No

 ** RoleArn **   <a name="systemsmanager-Type-CloudConnectorSummary-RoleArn"></a>
The ARN of the IAM role used by the cloud connector.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z0-9-]*:iam::\d{12}:role\/[\w-\/.@+=,]{1,1017}$`
Required: No

 ** UpdatedAt **   <a name="systemsmanager-Type-CloudConnectorSummary-UpdatedAt"></a>
The date and time the cloud connector was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_CloudConnectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CloudConnectorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CloudConnectorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CloudConnectorSummary)
