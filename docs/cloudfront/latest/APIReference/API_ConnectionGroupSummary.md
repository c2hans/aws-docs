---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ConnectionGroupSummary.html
---

# ConnectionGroupSummary
<a name="API_ConnectionGroupSummary"></a>

A summary that contains details about your connection groups.

## Contents
<a name="API_ConnectionGroupSummary_Contents"></a>

 ** Arn **   <a name="cloudfront-Type-ConnectionGroupSummary-Arn"></a>
The Amazon Resource Name (ARN) of the connection group.
Type: String
Required: Yes

 ** CreatedTime **   <a name="cloudfront-Type-ConnectionGroupSummary-CreatedTime"></a>
The date and time when the connection group was created.
Type: Timestamp
Required: Yes

 ** ETag **   <a name="cloudfront-Type-ConnectionGroupSummary-ETag"></a>
The current version of the connection group.
Type: String
Required: Yes

 ** Id **   <a name="cloudfront-Type-ConnectionGroupSummary-Id"></a>
The ID of the connection group.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-ConnectionGroupSummary-LastModifiedTime"></a>
The date and time when the connection group was updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="cloudfront-Type-ConnectionGroupSummary-Name"></a>
The name of the connection group.
Type: String
Required: Yes

 ** RoutingEndpoint **   <a name="cloudfront-Type-ConnectionGroupSummary-RoutingEndpoint"></a>
The routing endpoint (also known as the DNS name) that is assigned to the connection group, such as d111111abcdef8.cloudfront.net.
Type: String
Required: Yes

 ** AnycastIpListId **   <a name="cloudfront-Type-ConnectionGroupSummary-AnycastIpListId"></a>
The ID of the Anycast static IP list.
Type: String
Required: No

 ** Enabled **   <a name="cloudfront-Type-ConnectionGroupSummary-Enabled"></a>
Whether the connection group is enabled
Type: Boolean
Required: No

 ** IsDefault **   <a name="cloudfront-Type-ConnectionGroupSummary-IsDefault"></a>
Whether the connection group is the default connection group for the distribution tenants.
Type: Boolean
Required: No

 ** Status **   <a name="cloudfront-Type-ConnectionGroupSummary-Status"></a>
The status of the connection group.
Type: String
Required: No

## See Also
<a name="API_ConnectionGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ConnectionGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ConnectionGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ConnectionGroupSummary)
