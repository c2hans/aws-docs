---
source_url: https://docs.aws.amazon.com/MSKC/latest/mskc/API_ConnectorOperationStep.html
---

# ConnectorOperationStep
<a name="API_ConnectorOperationStep"></a>

Details of a step that is involved in a connector's operation.

## Contents
<a name="API_ConnectorOperationStep_Contents"></a>

 ** stepState **   <a name="MSKC-Type-ConnectorOperationStep-stepState"></a>
The step state of the operation.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | CANCELLED`
Required: No

 ** stepType **   <a name="MSKC-Type-ConnectorOperationStep-stepType"></a>
The step type of the operation.
Type: String
Valid Values: `INITIALIZE_UPDATE | FINALIZE_UPDATE | UPDATE_WORKER_SETTING | UPDATE_CONNECTOR_CONFIGURATION | VALIDATE_UPDATE`
Required: No

## See Also
<a name="API_ConnectorOperationStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/ConnectorOperationStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/ConnectorOperationStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/ConnectorOperationStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MSK Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query MSKC` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
