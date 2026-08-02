---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_ServiceFilter.html
---

# ServiceFilter
<a name="API_ServiceFilter"></a>

A complex type that lets you specify the namespaces that you want to list services for.

## Contents
<a name="API_ServiceFilter_Contents"></a>

 ** Name **   <a name="cloudmap-Type-ServiceFilter-Name"></a>
Specify the services that you want to get using one of the following.
+  `NAMESPACE_ID`: Gets the services associated with the specified namespace.
+  `RESOURCE_OWNER`: Gets the services associated with the namespaces created by your AWS account or by other accounts. This can be used to filter for services created in a shared namespace. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Valid Values: `NAMESPACE_ID | RESOURCE_OWNER`
Required: Yes

 ** Values **   <a name="cloudmap-Type-ServiceFilter-Values"></a>
The values that are applicable to the value that you specify for `Condition` to filter the list of services.
+  **NAMESPACE\_ID**: Specify one namespace ID or ARN. Specify the namespace ARN for namespaces that are shared with your AWS account.
+  **RESOURCE\_OWNER**: Specify one of `SELF` or `OTHER_ACCOUNTS`. `SELF` can be used to filter services associated with namespaces created by you and `OTHER_ACCOUNTS` can be used to filter services associated with namespaces that were shared with you.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Condition **   <a name="cloudmap-Type-ServiceFilter-Condition"></a>
The operator that you want to use to determine whether a service is returned by `ListServices`. Valid values for `Condition` include the following:
+  `EQ`: When you specify `EQ`, specify one value. `EQ` is the default condition and can be omitted.
Type: String
Valid Values: `EQ | IN | BETWEEN | BEGINS_WITH`
Required: No

## See Also
<a name="API_ServiceFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/ServiceFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/ServiceFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/ServiceFilter)
