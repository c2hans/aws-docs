---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_StackDriftInformationSummary.html
---

# StackDriftInformationSummary
<a name="API_StackDriftInformationSummary"></a>

Contains information about whether the stack's actual configuration differs, or has *drifted*, from its expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted.

## Contents
<a name="API_StackDriftInformationSummary_Contents"></a>

 ** StackDriftStatus **
Status of the stack's actual configuration compared to its expected template configuration.
+  `DRIFTED`: The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted.
+  `NOT_CHECKED`: CloudFormation hasn't checked if the stack differs from its expected template configuration.
+  `IN_SYNC`: The stack's actual configuration matches its expected template configuration.
+  `UNKNOWN`: CloudFormation could not run drift detection for a resource in the stack.
Type: String
Valid Values: `DRIFTED | IN_SYNC | UNKNOWN | NOT_CHECKED`
Required: Yes

 ** LastCheckTimestamp **
Most recent time when a drift detection operation was initiated on the stack, or any of its individual resources that support drift detection.
Type: Timestamp
Required: No

## See Also
<a name="API_StackDriftInformationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackDriftInformationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackDriftInformationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackDriftInformationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
