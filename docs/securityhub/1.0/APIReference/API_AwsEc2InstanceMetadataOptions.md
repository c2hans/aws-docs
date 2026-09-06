---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2InstanceMetadataOptions.html
---

# AwsEc2InstanceMetadataOptions
<a name="API_AwsEc2InstanceMetadataOptions"></a>

Metadata options that allow you to configure and secure the Amazon EC2 instance.

## Contents
<a name="API_AwsEc2InstanceMetadataOptions_Contents"></a>

 ** HttpEndpoint **   <a name="securityhub-Type-AwsEc2InstanceMetadataOptions-HttpEndpoint"></a>
Enables or disables the HTTP metadata endpoint on the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HttpProtocolIpv6 **   <a name="securityhub-Type-AwsEc2InstanceMetadataOptions-HttpProtocolIpv6"></a>
Enables or disables the IPv6 endpoint for the instance metadata service.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HttpPutResponseHopLimit **   <a name="securityhub-Type-AwsEc2InstanceMetadataOptions-HttpPutResponseHopLimit"></a>
The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.
Type: Integer
Required: No

 ** HttpTokens **   <a name="securityhub-Type-AwsEc2InstanceMetadataOptions-HttpTokens"></a>
The state of token usage for your instance metadata requests.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceMetadataTags **   <a name="securityhub-Type-AwsEc2InstanceMetadataOptions-InstanceMetadataTags"></a>
Specifies whether to allow access to instance tags from the instance metadata.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2InstanceMetadataOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2InstanceMetadataOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2InstanceMetadataOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2InstanceMetadataOptions)
