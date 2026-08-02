---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstanceMetadataOptions.html
---

# InstanceMetadataOptions
<a name="API_InstanceMetadataOptions"></a>

The metadata options for the instance.

## Contents
<a name="API_InstanceMetadataOptions_Contents"></a>

 ** httpEndpoint **   <a name="Lightsail-Type-InstanceMetadataOptions-httpEndpoint"></a>
Indicates whether the HTTP metadata endpoint on your instances is enabled or disabled.
If the value is `disabled`, you cannot access your instance metadata.
Type: String
Valid Values: `disabled | enabled`
Required: No

 ** httpProtocolIpv6 **   <a name="Lightsail-Type-InstanceMetadataOptions-httpProtocolIpv6"></a>
Indicates whether the IPv6 endpoint for the instance metadata service is enabled or disabled.
Type: String
Valid Values: `disabled | enabled`
Required: No

 ** httpPutResponseHopLimit **   <a name="Lightsail-Type-InstanceMetadataOptions-httpPutResponseHopLimit"></a>
The desired HTTP PUT response hop limit for instance metadata requests. A larger number means that the instance metadata requests can travel farther.
Type: Integer
Required: No

 ** httpTokens **   <a name="Lightsail-Type-InstanceMetadataOptions-httpTokens"></a>
The state of token usage for your instance metadata requests.
If the state is `optional`, you can choose whether to retrieve instance metadata with a signed token header on your request. If you retrieve the IAM role credentials without a token, the version 1.0 role credentials are returned. If you retrieve the IAM role credentials by using a valid signed token, the version 2.0 role credentials are returned.
If the state is `required`, you must send a signed token header with all instance metadata retrieval requests. In this state, retrieving the IAM role credential always returns the version 2.0 credentials. The version 1.0 credentials are not available.
Not all instance blueprints in Lightsail support version 2.0 credentials. Use the `MetadataNoToken` instance metric to track the number of calls to the instance metadata service that are using version 1.0 credentials. For more information, see [Viewing instance metrics in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-instance-health-metrics) in the *Amazon Lightsail Developer Guide*.
Type: String
Valid Values: `optional | required`
Required: No

 ** state **   <a name="Lightsail-Type-InstanceMetadataOptions-state"></a>
The state of the metadata option changes.
The following states are possible:
+  `pending` - The metadata options are being updated. The instance is not yet ready to process metadata traffic with the new selection.
+  `applied` - The metadata options have been successfully applied to the instance.
Type: String
Valid Values: `pending | applied`
Required: No

## See Also
<a name="API_InstanceMetadataOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/InstanceMetadataOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/InstanceMetadataOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/InstanceMetadataOptions)
