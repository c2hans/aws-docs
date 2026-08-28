---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_NamespaceSummary.html
---

# NamespaceSummary
<a name="API_NamespaceSummary"></a>

A complex type that contains information about a namespace.

## Contents
<a name="API_NamespaceSummary_Contents"></a>

 ** Arn **   <a name="cloudmap-Type-NamespaceSummary-Arn"></a>
The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the namespace when you create it.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** CreateDate **   <a name="cloudmap-Type-NamespaceSummary-CreateDate"></a>
The date and time that the namespace was created.
Type: Timestamp
Required: No

 ** Description **   <a name="cloudmap-Type-NamespaceSummary-Description"></a>
A description for the namespace.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** Id **   <a name="cloudmap-Type-NamespaceSummary-Id"></a>
The ID of the namespace.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** Name **   <a name="cloudmap-Type-NamespaceSummary-Name"></a>
The name of the namespace. When you create a namespace, AWS Cloud Map automatically creates a Route 53 hosted zone that has the same name as the namespace.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[!-~]{1,1024}$`
Required: No

 ** Properties **   <a name="cloudmap-Type-NamespaceSummary-Properties"></a>
The properties of the namespace.
Type: [NamespaceProperties](API_NamespaceProperties.md) object
Required: No

 ** ResourceOwner **   <a name="cloudmap-Type-NamespaceSummary-ResourceOwner"></a>
The ID of the AWS account that created the namespace. If this isn't your account ID, it's the ID of the account that shared the namespace with your account. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** ServiceCount **   <a name="cloudmap-Type-NamespaceSummary-ServiceCount"></a>
The number of services that were created using the namespace.
Type: Integer
Required: No

 ** Type **   <a name="cloudmap-Type-NamespaceSummary-Type"></a>
The type of the namespace, either public or private.
Type: String
Valid Values: `DNS_PUBLIC | DNS_PRIVATE | HTTP`
Required: No

## See Also
<a name="API_NamespaceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/NamespaceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/NamespaceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/NamespaceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
