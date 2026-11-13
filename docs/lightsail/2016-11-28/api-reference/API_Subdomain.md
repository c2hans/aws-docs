---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Subdomain.html
---

# Subdomain
<a name="API_Subdomain"></a>

Describes a Lightsail subdomain. A subdomain is the name that you choose, such as `mysite` or `blog.mysite`. Its web address is the subdomain followed by `amazonlightsail.com`, such as `blog.mysite.amazonlightsail.com`. You can associate a subdomain with a Lightsail resource to make the resource reachable at the web address.

## Contents
<a name="API_Subdomain_Contents"></a>

 ** arn **   <a name="Lightsail-Type-Subdomain-arn"></a>
The Amazon Resource Name (ARN) of the subdomain.
If you create a subdomain with a depth of 2, such as `blog.mysite`, without first creating the subdomain with a depth of 1 (`mysite`), Lightsail holds `mysite` for your account in the `IMPLICIT` state. It doesn't have an ARN until you create a subdomain with that name.
Type: String
Pattern: `.*\S.*`
Required: No

 ** attachedResource **   <a name="Lightsail-Type-Subdomain-attachedResource"></a>
An object that describes the resource that the subdomain is associated with.
When the subdomain is in the `TRANSFERRING` state, this is the resource that the subdomain is being moved from.
Type: [SubdomainAttachableResource](API_SubdomainAttachableResource.md) object
Required: No

 ** attachingResource **   <a name="Lightsail-Type-Subdomain-attachingResource"></a>
An object that describes the resource that the subdomain is being associated with.
This parameter is returned only when the subdomain is in the `ATTACHING` or `TRANSFERRING` state.
Type: [SubdomainAttachableResource](API_SubdomainAttachableResource.md) object
Required: No

 ** children **   <a name="Lightsail-Type-Subdomain-children"></a>
An array of objects that describe the nested subdomains of the subdomain.
This parameter is returned only by the `GetSubdomains` action when you don't specify a subdomain.
Type: Array of [Subdomain](#API_Subdomain) objects
Required: No

 ** createdAt **   <a name="Lightsail-Type-Subdomain-createdAt"></a>
The timestamp when the subdomain was created.
Type: Timestamp
Required: No

 ** depth **   <a name="Lightsail-Type-Subdomain-depth"></a>
The number of labels in the subdomain. A top-level subdomain, such as `mysite`, has a depth of `1`. A nested subdomain, such as `blog.mysite`, has a depth of `2`.
Type: Integer
Required: No

 ** fqdn **   <a name="Lightsail-Type-Subdomain-fqdn"></a>
The web address of the subdomain, which is the subdomain followed by `amazonlightsail.com` (for example, `blog.mysite.amazonlightsail.com`).
Type: String
Required: No

 ** location **   <a name="Lightsail-Type-Subdomain-location"></a>
An object that describes the location of the subdomain, such as the AWS Region.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** parentFqdn **   <a name="Lightsail-Type-Subdomain-parentFqdn"></a>
The web address of the parent subdomain (for example, `mysite.amazonlightsail.com` for `blog.mysite`).
This parameter isn't returned for a subdomain with a depth of 1.
Type: String
Required: No

 ** state **   <a name="Lightsail-Type-Subdomain-state"></a>
The state of the subdomain.
The following states are possible:
+  `CREATING` – The subdomain is being created.
+  `CREATE_FAILED` – The subdomain couldn't be created. Delete the subdomain, and then create it again if the name is still available.
+  `UNATTACHED` – The subdomain is ready, and isn't associated with a resource.
+  `ATTACHING` – The subdomain is being associated with a resource.
+  `ATTACHED` – The subdomain is associated with a resource, and routes traffic to it.
+  `DETACHING` – The subdomain is being disassociated from a resource.
+  `TRANSFERRING` – The subdomain is being moved from one resource to another resource.
+  `IMPLICIT` – The subdomain is the parent of one or more nested subdomains that you created, but you didn't create the parent subdomain itself. You can't associate or delete a subdomain in this state. To use it, create it with the `CreateSubdomain` action.
Type: String
Valid Values: `CREATING | CREATE_FAILED | UNATTACHED | ATTACHING | ATTACHED | DETACHING | TRANSFERRING | IMPLICIT`
Required: No

 ** subdomainName **   <a name="Lightsail-Type-Subdomain-subdomainName"></a>
The subdomain (for example, `mysite` or `blog.mysite`). To get the web address, use the `fqdn` parameter.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-Subdomain-tags"></a>
The tag keys and optional values for the subdomain. For more information about tags in Lightsail, see the [Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
This parameter is returned only by the `GetSubdomains` action when you specify a subdomain.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_Subdomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Subdomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Subdomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Subdomain)
