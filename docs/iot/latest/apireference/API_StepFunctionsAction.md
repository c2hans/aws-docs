---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_StepFunctionsAction.html
---

# StepFunctionsAction
<a name="API_StepFunctionsAction"></a>

Starts execution of a Step Functions state machine.

## Contents
<a name="API_StepFunctionsAction_Contents"></a>

 ** roleArn **   <a name="iot-Type-StepFunctionsAction-roleArn"></a>
The ARN of the role that grants IoT permission to start execution of a state machine ("Action":"states:StartExecution").
Type: String
Required: Yes

 ** stateMachineName **   <a name="iot-Type-StepFunctionsAction-stateMachineName"></a>
The name of the Step Functions state machine whose execution will be started.
Type: String
Required: Yes

 ** executionNamePrefix **   <a name="iot-Type-StepFunctionsAction-executionNamePrefix"></a>
(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.
Type: String
Required: No

## See Also
<a name="API_StepFunctionsAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/StepFunctionsAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/StepFunctionsAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/StepFunctionsAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
