---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_MapRunListItem.html
---

# MapRunListItem
<a name="API_MapRunListItem"></a>

Contains details about a specific Map Run.

## Contents
<a name="API_MapRunListItem_Contents"></a>

 ** executionArn **   <a name="StepFunctions-Type-MapRunListItem-executionArn"></a>
The `executionArn` of the execution from which the Map Run was started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** mapRunArn **   <a name="StepFunctions-Type-MapRunListItem-mapRunArn"></a>
The Amazon Resource Name (ARN) of the Map Run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: Yes

 ** startDate **   <a name="StepFunctions-Type-MapRunListItem-startDate"></a>
The date on which the Map Run started.
Type: Timestamp
Required: Yes

 ** stateMachineArn **   <a name="StepFunctions-Type-MapRunListItem-stateMachineArn"></a>
The Amazon Resource Name (ARN) of the executed state machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** stopDate **   <a name="StepFunctions-Type-MapRunListItem-stopDate"></a>
The date on which the Map Run stopped.
Type: Timestamp
Required: No

## See Also
<a name="API_MapRunListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/MapRunListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/MapRunListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/MapRunListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
