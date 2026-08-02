---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnaSrdUdpSpecificationRequest.html
---

# EnaSrdUdpSpecificationRequest
<a name="API_EnaSrdUdpSpecificationRequest"></a>

Configures ENA Express for UDP network traffic from your launch template.

## Contents
<a name="API_EnaSrdUdpSpecificationRequest_Contents"></a>

 ** EnaSrdUdpEnabled ** (request), ** EnaSrdUdpEnabled ** (response)
Indicates whether UDP traffic uses ENA Express for your instance. To ensure that UDP traffic can use ENA Express when you launch an instance, you must also set **EnaSrdEnabled** in the **EnaSrdSpecificationRequest** to `true`.
Type: Boolean
Required: No

## See Also
<a name="API_EnaSrdUdpSpecificationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnaSrdUdpSpecificationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnaSrdUdpSpecificationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnaSrdUdpSpecificationRequest)
