---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchDeleteSuccessfulDeletion.html
---

# BatchDeleteSuccessfulDeletion
<a name="API_BatchDeleteSuccessfulDeletion"></a>

Represents a successfully deleted instrumentation configuration.

## Contents
<a name="API_BatchDeleteSuccessfulDeletion_Contents"></a>

 ** LocationHash **   <a name="applicationsignals-Type-BatchDeleteSuccessfulDeletion-LocationHash"></a>
The location hash of the deleted configuration. Populated only when deleting by scope.
Type: String
Required: No

 ** ResourceArn **   <a name="applicationsignals-Type-BatchDeleteSuccessfulDeletion-ResourceArn"></a>
The ARN of the deleted configuration. Populated only when deleting by ARN list.
Type: String
Required: No

 ** SignalType **   <a name="applicationsignals-Type-BatchDeleteSuccessfulDeletion-SignalType"></a>
The signal type of the deleted configuration. Populated only when deleting by scope.
Type: String
Required: No

## See Also
<a name="API_BatchDeleteSuccessfulDeletion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/BatchDeleteSuccessfulDeletion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/BatchDeleteSuccessfulDeletion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/BatchDeleteSuccessfulDeletion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
