---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpointListItem.html
---

# DataflowEndpointListItem
<a name="API_DataflowEndpointListItem"></a>

Item in a list of `DataflowEndpoint` groups.

## Contents
<a name="API_DataflowEndpointListItem_Contents"></a>

 ** dataflowEndpointGroupArn **   <a name="groundstation-Type-DataflowEndpointListItem-dataflowEndpointGroupArn"></a>
ARN of a dataflow endpoint group.
Type: String
Length Constraints: Minimum length of 97. Maximum length of 146.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:dataflow-endpoint-group/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** dataflowEndpointGroupId **   <a name="groundstation-Type-DataflowEndpointListItem-dataflowEndpointGroupId"></a>
UUID of a dataflow endpoint group.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## See Also
<a name="API_DataflowEndpointListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/DataflowEndpointListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/DataflowEndpointListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/DataflowEndpointListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
