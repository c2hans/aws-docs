---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FailedSpaceResourceOperation.html
---

# FailedSpaceResourceOperation
<a name="API_FailedSpaceResourceOperation"></a>

A resource operation that failed.

## Contents
<a name="API_FailedSpaceResourceOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ErrorMessage **   <a name="QS-Type-FailedSpaceResourceOperation-ErrorMessage"></a>
The error message that describes why the operation failed.
Type: String
Required: Yes

 ** ResourceType **   <a name="QS-Type-FailedSpaceResourceOperation-ResourceType"></a>
The type of the resource.
Type: String
Valid Values: `TOPIC | DASHBOARD | KNOWLEDGE_BASE | ACTION_CONNECTOR | DATA_SET`
Required: Yes

 ** ResourceDetails **   <a name="QS-Type-FailedSpaceResourceOperation-ResourceDetails"></a>
The details of the resource.
Type: [SpaceQuickSightResourceDetails](API_SpaceQuickSightResourceDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_FailedSpaceResourceOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FailedSpaceResourceOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FailedSpaceResourceOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FailedSpaceResourceOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
