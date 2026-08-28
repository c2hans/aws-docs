---
source_url: https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_ConnectionRecordingPreferences.html
---

# ConnectionRecordingPreferences
<a name="API_ConnectionRecordingPreferences"></a>

The set of preferences used for recording RDP connections in the requesting AWS account and AWS Region. This includes details such as which S3 bucket recordings are stored in.

## Contents
<a name="API_ConnectionRecordingPreferences_Contents"></a>

 ** KMSKeyArn **   <a name="ssmguiconnect-Type-ConnectionRecordingPreferences-KMSKeyArn"></a>
The ARN of a AWS KMS key that is used to encrypt data while it is being processed by the service. This key must exist in the same AWS Region as the node you start an RDP connection to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** RecordingDestinations **   <a name="ssmguiconnect-Type-ConnectionRecordingPreferences-RecordingDestinations"></a>
Determines where recordings of RDP connections are stored.
Type: [RecordingDestinations](API_RecordingDestinations.md) object
Required: Yes

## See Also
<a name="API_ConnectionRecordingPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-guiconnect-2021-05-01/ConnectionRecordingPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-guiconnect-2021-05-01/ConnectionRecordingPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-guiconnect-2021-05-01/ConnectionRecordingPreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager GUI Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssm-guiconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
