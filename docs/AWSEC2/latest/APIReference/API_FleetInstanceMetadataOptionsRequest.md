---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FleetInstanceMetadataOptionsRequest.html
---

# FleetInstanceMetadataOptionsRequest
<a name="API_FleetInstanceMetadataOptionsRequest"></a>

Describes the metadata options for the instances. Supported only for fleets of type `instant`.

## Contents
<a name="API_FleetInstanceMetadataOptionsRequest_Contents"></a>

 ** HttpEndpoint **
Enables or disables the HTTP metadata endpoint on your instances.
+  `enabled` - The HTTP metadata endpoint is enabled.
+  `disabled` - The HTTP metadata endpoint is disabled.
Type: String
Valid Values: `disabled | enabled`
Required: No

 ** HttpPutResponseHopLimit **
The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.
Default: `1`
Possible values: Integers from 1 to 64
Type: Integer
Required: No

 ** HttpTokens **
Indicates whether IMDSv2 is required.
+  `optional` - IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.
+  `required` - IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.
Type: String
Valid Values: `optional | required`
Required: No

## See Also
<a name="API_FleetInstanceMetadataOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FleetInstanceMetadataOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FleetInstanceMetadataOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FleetInstanceMetadataOptionsRequest)
