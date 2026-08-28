---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

A resource in AWS that AWS Resource Explorer has discovered, and for which it has stored information in the index of the AWS Region that contains the resource.

## Contents
<a name="API_Resource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="resourceexplorer-Type-Resource-Arn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource.
Type: String
Required: No

 ** LastReportedAt **   <a name="resourceexplorer-Type-Resource-LastReportedAt"></a>
The date and time that Resource Explorer last queried this resource and updated the index with the latest information about the resource.
Type: Timestamp
Required: No

 ** OwningAccountId **   <a name="resourceexplorer-Type-Resource-OwningAccountId"></a>
The AWS account that owns the resource.
Type: String
Required: No

 ** Properties **   <a name="resourceexplorer-Type-Resource-Properties"></a>
A structure with additional type-specific details about the resource. These properties can be added by turning on integration between Resource Explorer and other AWS services.
Type: Array of [ResourceProperty](API_ResourceProperty.md) objects
Required: No

 ** Region **   <a name="resourceexplorer-Type-Resource-Region"></a>
The AWS Region in which the resource was created and exists.
Type: String
Required: No

 ** ResourceType **   <a name="resourceexplorer-Type-Resource-ResourceType"></a>
The type of the resource.
Type: String
Required: No

 ** Service **   <a name="resourceexplorer-Type-Resource-Service"></a>
The AWS service that owns the resource and is responsible for creating and updating it.
Type: String
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/Resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
