---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ManagedView.html
---

# ManagedView
<a name="API_ManagedView"></a>

An AWS-managed view is how other AWS services can access resource information indexed by Resource Explorer for your AWS account or organization with your consent. For more information, see [Managed views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html).

## Contents
<a name="API_ManagedView_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Filters **   <a name="resourceexplorer-Type-ManagedView-Filters"></a>
A search filter defines which resources can be part of a search query result set.
Type: [SearchFilter](API_SearchFilter.md) object
Required: No

 ** IncludedProperties **   <a name="resourceexplorer-Type-ManagedView-IncludedProperties"></a>
A structure that contains additional information about the managed view.
Type: Array of [IncludedProperty](API_IncludedProperty.md) objects
Required: No

 ** LastUpdatedAt **   <a name="resourceexplorer-Type-ManagedView-LastUpdatedAt"></a>
The date and time when this managed view was last modified.
Type: Timestamp
Required: No

 ** ManagedViewArn **   <a name="resourceexplorer-Type-ManagedView-ManagedViewArn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the managed view.
Type: String
Required: No

 ** ManagedViewName **   <a name="resourceexplorer-Type-ManagedView-ManagedViewName"></a>
The name of the managed view.
Type: String
Required: No

 ** Owner **   <a name="resourceexplorer-Type-ManagedView-Owner"></a>
The AWS account that owns this managed view.
Type: String
Required: No

 ** ResourcePolicy **   <a name="resourceexplorer-Type-ManagedView-ResourcePolicy"></a>
The resource policy that defines access to the managed view. To learn more about this policy, review [Managed views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html).
Type: String
Required: No

 ** Scope **   <a name="resourceexplorer-Type-ManagedView-Scope"></a>
An [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of an AWS account or organization that specifies whether this managed view includes resources from only the specified AWS account or all accounts in the specified organization.
Type: String
Required: No

 ** TrustedService **   <a name="resourceexplorer-Type-ManagedView-TrustedService"></a>
The service principal of the AWS service that created and manages the managed view.
Type: String
Required: No

 ** Version **   <a name="resourceexplorer-Type-ManagedView-Version"></a>
The version of the managed view.
Type: String
Required: No

## See Also
<a name="API_ManagedView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/ManagedView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/ManagedView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/ManagedView)
