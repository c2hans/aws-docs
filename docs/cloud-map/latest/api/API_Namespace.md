---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_Namespace.html
---

# Namespace
<a name="API_Namespace"></a>

A complex type that contains information about a specified namespace.

## Contents
<a name="API_Namespace_Contents"></a>

 ** Arn **   <a name="cloudmap-Type-Namespace-Arn"></a>
The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the namespace when you create it.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** CreateDate **   <a name="cloudmap-Type-Namespace-CreateDate"></a>
The date that the namespace was created, in Unix date/time format and Coordinated Universal Time (UTC). The value of `CreateDate` is accurate to milliseconds. For example, the value `1516925490.087` represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** CreatorRequestId **   <a name="cloudmap-Type-Namespace-CreatorRequestId"></a>
A unique string that identifies the request and that allows failed requests to be retried without the risk of running an operation twice.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** Description **   <a name="cloudmap-Type-Namespace-Description"></a>
The description that you specify for the namespace when you create it.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** Id **   <a name="cloudmap-Type-Namespace-Id"></a>
The ID of a namespace.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** Name **   <a name="cloudmap-Type-Namespace-Name"></a>
The name of the namespace, such as `example.com`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[!-~]{1,1024}$`
Required: No

 ** Properties **   <a name="cloudmap-Type-Namespace-Properties"></a>
A complex type that contains information that's specific to the type of the namespace.
Type: [NamespaceProperties](API_NamespaceProperties.md) object
Required: No

 ** ResourceOwner **   <a name="cloudmap-Type-Namespace-ResourceOwner"></a>
The ID of the AWS account that created the namespace. If this isn't your account ID, it's the ID of the account that shared the namespace with your account. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** ServiceCount **   <a name="cloudmap-Type-Namespace-ServiceCount"></a>
The number of services that are associated with the namespace.
Type: Integer
Required: No

 ** Type **   <a name="cloudmap-Type-Namespace-Type"></a>
The type of the namespace. The methods for discovering instances depends on the value that you specify:
HTTP
Instances can be discovered only programmatically, using the AWS Cloud Map `DiscoverInstances` API.
DNS\_PUBLIC
Instances can be discovered using public DNS queries and using the `DiscoverInstances` API.
DNS\_PRIVATE
Instances can be discovered using DNS queries in VPCs and using the `DiscoverInstances` API.
Type: String
Valid Values: `DNS_PUBLIC | DNS_PRIVATE | HTTP`
Required: No

## See Also
<a name="API_Namespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/Namespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/Namespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/Namespace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
