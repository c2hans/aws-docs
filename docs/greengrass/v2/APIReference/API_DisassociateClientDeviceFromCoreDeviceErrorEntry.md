---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DisassociateClientDeviceFromCoreDeviceErrorEntry.html
---

# DisassociateClientDeviceFromCoreDeviceErrorEntry
<a name="API_DisassociateClientDeviceFromCoreDeviceErrorEntry"></a>

Contains an error that occurs from a request to disassociate a client device from a core device. The [BatchDisassociateClientDeviceWithCoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_BatchDisassociateClientDeviceWithCoreDevice.html) operation returns a list of these errors.

## Contents
<a name="API_DisassociateClientDeviceFromCoreDeviceErrorEntry_Contents"></a>

 ** code **   <a name="greengrassv2-Type-DisassociateClientDeviceFromCoreDeviceErrorEntry-code"></a>
The error code for the request.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** message **   <a name="greengrassv2-Type-DisassociateClientDeviceFromCoreDeviceErrorEntry-message"></a>
A message that provides additional information about the error.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** thingName **   <a name="greengrassv2-Type-DisassociateClientDeviceFromCoreDeviceErrorEntry-thingName"></a>
The name of the AWS IoT thing whose disassociate request failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_DisassociateClientDeviceFromCoreDeviceErrorEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/DisassociateClientDeviceFromCoreDeviceErrorEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/DisassociateClientDeviceFromCoreDeviceErrorEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/DisassociateClientDeviceFromCoreDeviceErrorEntry)
