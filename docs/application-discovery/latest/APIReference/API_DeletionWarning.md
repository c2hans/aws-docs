---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DeletionWarning.html
---

# DeletionWarning
<a name="API_DeletionWarning"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

 A configuration ID paired with a warning message.

## Contents
<a name="API_DeletionWarning_Contents"></a>

 ** configurationId **   <a name="DiscServ-Type-DeletionWarning-configurationId"></a>
 The unique identifier of the configuration that produced a warning.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: No

 ** warningCode **   <a name="DiscServ-Type-DeletionWarning-warningCode"></a>
 The integer warning code associated with the warning message.
Type: Integer
Required: No

 ** warningText **   <a name="DiscServ-Type-DeletionWarning-warningText"></a>
 A descriptive message of the warning the associated configuration ID produced.
Type: String
Required: No

## See Also
<a name="API_DeletionWarning_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/DeletionWarning)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/DeletionWarning)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/DeletionWarning)
