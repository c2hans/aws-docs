---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_WebAppEndpointDetails.html
---

# WebAppEndpointDetails
<a name="API_WebAppEndpointDetails"></a>

Contains the endpoint configuration for a web app, including VPC settings when the endpoint is hosted within a VPC.

## Contents
<a name="API_WebAppEndpointDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Vpc **   <a name="TransferFamily-Type-WebAppEndpointDetails-Vpc"></a>
The VPC configuration for hosting the web app endpoint within a VPC.
Type: [WebAppVpcConfig](API_WebAppVpcConfig.md) object
Required: No

## See Also
<a name="API_WebAppEndpointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/WebAppEndpointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/WebAppEndpointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/WebAppEndpointDetails)
