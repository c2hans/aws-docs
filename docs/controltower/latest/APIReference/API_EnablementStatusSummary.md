---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnablementStatusSummary.html
---

# EnablementStatusSummary
<a name="API_EnablementStatusSummary"></a>

The deployment summary of an `EnabledControl` or `EnabledBaseline` resource.

## Contents
<a name="API_EnablementStatusSummary_Contents"></a>

 ** lastOperationIdentifier **   <a name="controltower-Type-EnablementStatusSummary-lastOperationIdentifier"></a>
The last operation identifier for the enabled resource.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** status **   <a name="controltower-Type-EnablementStatusSummary-status"></a>
 The deployment status of the enabled resource.
Valid values:
+  `SUCCEEDED`: The `EnabledControl` or `EnabledBaseline` configuration was deployed successfully.
+  `UNDER_CHANGE`: The `EnabledControl` or `EnabledBaseline` configuration is changing.
+  `FAILED`: The `EnabledControl` or `EnabledBaseline` configuration failed to deploy.
Type: String
Valid Values: `SUCCEEDED | FAILED | UNDER_CHANGE`
Required: No

## See Also
<a name="API_EnablementStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/EnablementStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/EnablementStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/EnablementStatusSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
