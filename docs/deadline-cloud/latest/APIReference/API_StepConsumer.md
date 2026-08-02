---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_StepConsumer.html
---

# StepConsumer
<a name="API_StepConsumer"></a>

The details of a step consumer.

## Contents
<a name="API_StepConsumer_Contents"></a>

 ** status **   <a name="deadlinecloud-Type-StepConsumer-status"></a>
The step consumer status.
Type: String
Valid Values: `RESOLVED | UNRESOLVED`
Required: Yes

 ** stepId **   <a name="deadlinecloud-Type-StepConsumer-stepId"></a>
The step ID.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_StepConsumer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StepConsumer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StepConsumer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StepConsumer)
