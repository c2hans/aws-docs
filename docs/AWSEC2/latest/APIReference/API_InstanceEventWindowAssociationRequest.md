---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceEventWindowAssociationRequest.html
---

# InstanceEventWindowAssociationRequest
<a name="API_InstanceEventWindowAssociationRequest"></a>

One or more targets associated with the specified event window. Only one *type* of target (instance ID, instance tag, or Dedicated Host ID) can be associated with an event window.

## Contents
<a name="API_InstanceEventWindowAssociationRequest_Contents"></a>

 ** DedicatedHostId.N **
The IDs of the Dedicated Hosts to associate with the event window.
Type: Array of strings
Required: No

 ** InstanceId.N **
The IDs of the instances to associate with the event window. If the instance is on a Dedicated Host, you can't specify the Instance ID parameter; you must use the Dedicated Host ID parameter.
Type: Array of strings
Required: No

 ** InstanceTag.N **
The instance tags to associate with the event window. Any instances associated with the tags will be associated with the event window.
Note that while you can't create tag keys beginning with `aws:`, you can specify existing AWS managed tag keys (with the `aws:` prefix) when specifying them as targets to associate with the event window.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_InstanceEventWindowAssociationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceEventWindowAssociationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceEventWindowAssociationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceEventWindowAssociationRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
