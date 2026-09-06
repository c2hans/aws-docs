---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2LaunchTemplateDataMetadataOptionsDetails.html
---

# AwsEc2LaunchTemplateDataMetadataOptionsDetails
<a name="API_AwsEc2LaunchTemplateDataMetadataOptionsDetails"></a>

 Specifies the metadata options for an Amazon EC2 instance.

## Contents
<a name="API_AwsEc2LaunchTemplateDataMetadataOptionsDetails_Contents"></a>

 ** HttpEndpoint **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataMetadataOptionsDetails-HttpEndpoint"></a>
 Enables or disables the HTTP metadata endpoint on your instances. If the parameter is not specified, the default state is enabled, and you won't be able to access your instance metadata.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HttpProtocolIpv6 **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataMetadataOptionsDetails-HttpProtocolIpv6"></a>
 Enables or disables the IPv6 endpoint for the instance metadata service.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HttpPutResponseHopLimit **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataMetadataOptionsDetails-HttpPutResponseHopLimit"></a>
 The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.
Type: Integer
Required: No

 ** HttpTokens **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataMetadataOptionsDetails-HttpTokens"></a>
 The state of token usage for your instance metadata requests.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceMetadataTags **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataMetadataOptionsDetails-InstanceMetadataTags"></a>
 When set to `enabled`, this parameter allows access to instance tags from the instance metadata. When set to `disabled`, it turns off access to instance tags from the instance metadata. For more information, see [Work with instance tags in instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#work-with-tags-in-IMDS) in the *Amazon EC2 User Guide*.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2LaunchTemplateDataMetadataOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2LaunchTemplateDataMetadataOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2LaunchTemplateDataMetadataOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2LaunchTemplateDataMetadataOptionsDetails)
