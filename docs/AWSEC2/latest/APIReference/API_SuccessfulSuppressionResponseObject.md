---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SuccessfulSuppressionResponseObject.html
---

# SuccessfulSuppressionResponseObject
<a name="API_SuccessfulSuppressionResponseObject"></a>

Describes a successful application status check suppression.

## Contents
<a name="API_SuccessfulSuppressionResponseObject_Contents"></a>

 ** instanceId **
The ID of the instance.
Type: String
Required: No

 ** resumeAt **
The date and time when suppression ends and health checks resume.
Type: Timestamp
Required: No

 ** suppressAt **
The date and time when suppression started.
Type: Timestamp
Required: No

## See Also
<a name="API_SuccessfulSuppressionResponseObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SuccessfulSuppressionResponseObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SuccessfulSuppressionResponseObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SuccessfulSuppressionResponseObject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
