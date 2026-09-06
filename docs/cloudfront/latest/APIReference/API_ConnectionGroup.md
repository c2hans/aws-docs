---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ConnectionGroup.html
---

# ConnectionGroup
<a name="API_ConnectionGroup"></a>

The connection group for your distribution tenants. When you first create a distribution tenant and you don't specify a connection group, CloudFront will automatically create a default connection group for you. When you create a new distribution tenant and don't specify a connection group, the default one will be associated with your distribution tenant.

## Contents
<a name="API_ConnectionGroup_Contents"></a>

 ** AnycastIpListId **   <a name="cloudfront-Type-ConnectionGroup-AnycastIpListId"></a>
The ID of the Anycast static IP list.
Type: String
Required: No

 ** Arn **   <a name="cloudfront-Type-ConnectionGroup-Arn"></a>
The Amazon Resource Name (ARN) of the connection group.
Type: String
Required: No

 ** CreatedTime **   <a name="cloudfront-Type-ConnectionGroup-CreatedTime"></a>
The date and time when the connection group was created.
Type: Timestamp
Required: No

 ** Enabled **   <a name="cloudfront-Type-ConnectionGroup-Enabled"></a>
Whether the connection group is enabled.
Type: Boolean
Required: No

 ** Id **   <a name="cloudfront-Type-ConnectionGroup-Id"></a>
The ID of the connection group.
Type: String
Required: No

 ** Ipv6Enabled **   <a name="cloudfront-Type-ConnectionGroup-Ipv6Enabled"></a>
IPv6 is enabled for the connection group.
Type: Boolean
Required: No

 ** IsDefault **   <a name="cloudfront-Type-ConnectionGroup-IsDefault"></a>
Whether the connection group is the default connection group for the distribution tenants.
Type: Boolean
Required: No

 ** LastModifiedTime **   <a name="cloudfront-Type-ConnectionGroup-LastModifiedTime"></a>
The date and time when the connection group was updated.
Type: Timestamp
Required: No

 ** Name **   <a name="cloudfront-Type-ConnectionGroup-Name"></a>
The name of the connection group.
Type: String
Required: No

 ** RoutingEndpoint **   <a name="cloudfront-Type-ConnectionGroup-RoutingEndpoint"></a>
The routing endpoint (also known as the DNS name) that is assigned to the connection group, such as d111111abcdef8.cloudfront.net.
Type: String
Required: No

 ** Status **   <a name="cloudfront-Type-ConnectionGroup-Status"></a>
The status of the connection group.
Type: String
Required: No

 ** Tags **   <a name="cloudfront-Type-ConnectionGroup-Tags"></a>
A complex type that contains zero or more `Tag` elements.
Type: [Tags](API_Tags.md) object
Required: No

## See Also
<a name="API_ConnectionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ConnectionGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ConnectionGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ConnectionGroup)
