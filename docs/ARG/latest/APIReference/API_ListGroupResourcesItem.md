---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroupResourcesItem.html
---

# ListGroupResourcesItem
<a name="API_ListGroupResourcesItem"></a>

A structure returned by the [ListGroupResources](API_ListGroupResources.md) operation that contains identity and group membership status information for one of the resources in the group.

## Contents
<a name="API_ListGroupResourcesItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Identifier **   <a name="ARG-Type-ListGroupResourcesItem-Identifier"></a>
A structure that contains the ARN of a resource and its resource type.
Type: [ResourceIdentifier](API_ResourceIdentifier.md) object
Required: No

 ** Status **   <a name="ARG-Type-ListGroupResourcesItem-Status"></a>
A structure that contains the status of this resource's membership in the group.
This field is present in the response only if the group is of type `AWS::EC2::HostManagement`.
Type: [ResourceStatus](API_ResourceStatus.md) object
Required: No

## See Also
<a name="API_ListGroupResourcesItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/ListGroupResourcesItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/ListGroupResourcesItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/ListGroupResourcesItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
