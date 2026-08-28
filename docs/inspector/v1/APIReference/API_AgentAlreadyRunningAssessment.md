---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AgentAlreadyRunningAssessment.html
---

# AgentAlreadyRunningAssessment
<a name="API_AgentAlreadyRunningAssessment"></a>

Used in the exception error that is thrown if you start an assessment run for an assessment target that includes an EC2 instance that is already participating in another started assessment run.

## Contents
<a name="API_AgentAlreadyRunningAssessment_Contents"></a>

 ** agentId **   <a name="Inspector-Type-AgentAlreadyRunningAssessment-agentId"></a>
ID of the agent that is running on an EC2 instance that is already participating in another started assessment run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** assessmentRunArn **   <a name="Inspector-Type-AgentAlreadyRunningAssessment-assessmentRunArn"></a>
The ARN of the assessment run that has already been started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## See Also
<a name="API_AgentAlreadyRunningAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AgentAlreadyRunningAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AgentAlreadyRunningAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AgentAlreadyRunningAssessment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
