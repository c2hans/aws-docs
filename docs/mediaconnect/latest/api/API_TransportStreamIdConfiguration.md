---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_TransportStreamIdConfiguration.html
---

# TransportStreamIdConfiguration
<a name="API_TransportStreamIdConfiguration"></a>

The configuration settings for the transport stream ID (TSID).

## Contents
<a name="API_TransportStreamIdConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** passthrough **   <a name="mediaconnect-Type-TransportStreamIdConfiguration-passthrough"></a>
The TSID configuration that passes through the TSID from the source.
Type: [Passthrough](API_Passthrough.md) object
Required: No

 ** set **   <a name="mediaconnect-Type-TransportStreamIdConfiguration-set"></a>
The TSID to use for the router output.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

## See Also
<a name="API_TransportStreamIdConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/TransportStreamIdConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/TransportStreamIdConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/TransportStreamIdConfiguration)
