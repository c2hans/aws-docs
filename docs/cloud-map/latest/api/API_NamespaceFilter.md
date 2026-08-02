---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_NamespaceFilter.html
---

# NamespaceFilter
<a name="API_NamespaceFilter"></a>

A complex type that identifies the namespaces that you want to list. You can choose to list public or private namespaces.

## Contents
<a name="API_NamespaceFilter_Contents"></a>

 ** Name **   <a name="cloudmap-Type-NamespaceFilter-Name"></a>
Specify the namespaces that you want to get using one of the following.
+  `TYPE`: Gets the namespaces of the specified type.
+  `NAME`: Gets the namespaces with the specified name.
+  `HTTP_NAME`: Gets the namespaces with the specified HTTP name.
+  `RESOURCE_OWNER`: Gets the namespaces created by your AWS account or by other accounts. This can be used to filter for shared namespaces. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Valid Values: `TYPE | NAME | HTTP_NAME | RESOURCE_OWNER`
Required: Yes

 ** Values **   <a name="cloudmap-Type-NamespaceFilter-Values"></a>
Specify the values that are applicable to the value that you specify for `Name`.
+  `TYPE`: Specify `HTTP`, `DNS_PUBLIC`, or `DNS_PRIVATE`.
+  `NAME`: Specify the name of the namespace, which is found in `Namespace.Name`.
+  `HTTP_NAME`: Specify the HTTP name of the namespace, which is found in `Namespace.Properties.HttpProperties.HttpName`.
+  `RESOURCE_OWNER`: Specify one of `SELF` or `OTHER_ACCOUNTS`. `SELF` can be used to filter namespaces created by you and `OTHER_ACCOUNTS` can be used to filter namespaces shared with you that were created by other accounts.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Condition **   <a name="cloudmap-Type-NamespaceFilter-Condition"></a>
Specify the operator that you want to use to determine whether a namespace matches the specified value. Valid values for `Condition` are one of the following.
+  `EQ`: When you specify `EQ` for `Condition`, you can specify only one value. `EQ` is supported for `TYPE`, `NAME`, `RESOURCE_OWNER` and `HTTP_NAME`. `EQ` is the default condition and can be omitted.
+  `BEGINS_WITH`: When you specify `BEGINS_WITH` for `Condition`, you can specify only one value. `BEGINS_WITH` is supported for `TYPE`, `NAME`, and `HTTP_NAME`.
Type: String
Valid Values: `EQ | IN | BETWEEN | BEGINS_WITH`
Required: No

## See Also
<a name="API_NamespaceFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/NamespaceFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/NamespaceFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/NamespaceFilter)
