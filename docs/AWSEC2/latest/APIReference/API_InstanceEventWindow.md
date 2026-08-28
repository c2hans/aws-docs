---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceEventWindow.html
---

# InstanceEventWindow
<a name="API_InstanceEventWindow"></a>

The event window.

## Contents
<a name="API_InstanceEventWindow_Contents"></a>

 ** associationTarget **
One or more targets associated with the event window.
Type: [InstanceEventWindowAssociationTarget](API_InstanceEventWindowAssociationTarget.md) object
Required: No

 ** cronExpression **
The cron expression defined for the event window.
Type: String
Required: No

 ** instanceEventWindowId **
The ID of the event window.
Type: String
Required: No

 ** name **
The name of the event window.
Type: String
Required: No

 ** state **
The current state of the event window.
Type: String
Valid Values: `creating | deleting | active | deleted`
Required: No

 ** TagSet.N **
The instance tags associated with the event window.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TimeRangeSet.N **
One or more time ranges defined for the event window.
Type: Array of [InstanceEventWindowTimeRange](API_InstanceEventWindowTimeRange.md) objects
Required: No

## See Also
<a name="API_InstanceEventWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceEventWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceEventWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceEventWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
