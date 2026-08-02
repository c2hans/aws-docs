---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_UpdateWebAppEndpointDetails.html
---

# UpdateWebAppEndpointDetails
<a name="API_UpdateWebAppEndpointDetails"></a>

Contains the endpoint configuration details for updating a web app, including VPC settings for endpoints hosted within a VPC.

## Contents
<a name="API_UpdateWebAppEndpointDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Vpc **   <a name="TransferFamily-Type-UpdateWebAppEndpointDetails-Vpc"></a>
The VPC configuration details for updating a web app endpoint hosted within a VPC. This includes the subnet IDs for endpoint deployment.
Type: [UpdateWebAppVpcConfig](API_UpdateWebAppVpcConfig.md) object
Required: No

## See Also
<a name="API_UpdateWebAppEndpointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/UpdateWebAppEndpointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/UpdateWebAppEndpointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/UpdateWebAppEndpointDetails)
