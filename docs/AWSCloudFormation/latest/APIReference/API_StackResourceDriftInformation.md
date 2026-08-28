---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_StackResourceDriftInformation.html
---

# StackResourceDriftInformation
<a name="API_StackResourceDriftInformation"></a>

Contains information about whether the resource's actual configuration differs, or has *drifted*, from its expected configuration.

## Contents
<a name="API_StackResourceDriftInformation_Contents"></a>

 ** StackResourceDriftStatus **
Status of the resource's actual configuration compared to its expected configuration
+  `DELETED`: The resource differs from its expected configuration in that it has been deleted.
+  `MODIFIED`: The resource differs from its expected configuration.
+  `NOT_CHECKED`: CloudFormation has not checked if the resource differs from its expected configuration.

  Any resources that do not currently support drift detection have a status of `NOT_CHECKED`. For more information, see [Resource type support for imports and drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html).
+  `IN_SYNC`: The resource's actual configuration matches its expected configuration.
Type: String
Valid Values: `IN_SYNC | MODIFIED | DELETED | NOT_CHECKED | UNKNOWN | UNSUPPORTED`
Required: Yes

 ** LastCheckTimestamp **
When CloudFormation last checked if the resource had drifted from its expected configuration.
Type: Timestamp
Required: No

## See Also
<a name="API_StackResourceDriftInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StackResourceDriftInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StackResourceDriftInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StackResourceDriftInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
