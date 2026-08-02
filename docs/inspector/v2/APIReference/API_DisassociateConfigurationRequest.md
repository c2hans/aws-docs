---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_DisassociateConfigurationRequest.html
---

# DisassociateConfigurationRequest
<a name="API_DisassociateConfigurationRequest"></a>

Contains details about a request to disassociate a code repository from a scan configuration.

## Contents
<a name="API_DisassociateConfigurationRequest_Contents"></a>

 ** resource **   <a name="inspector2-Type-DisassociateConfigurationRequest-resource"></a>
Identifies a specific resource in a code repository that will be scanned.
Type: [CodeSecurityResource](API_CodeSecurityResource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** scanConfigurationArn **   <a name="inspector2-Type-DisassociateConfigurationRequest-scanConfigurationArn"></a>
The Amazon Resource Name (ARN) of the scan configuration to disassociate from a code repository.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/codesecurity-configuration/[a-f0-9-]{36}`
Required: Yes

## See Also
<a name="API_DisassociateConfigurationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/DisassociateConfigurationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/DisassociateConfigurationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/DisassociateConfigurationRequest)
