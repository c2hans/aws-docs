---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_MitigationActionIdentifier.html
---

# MitigationActionIdentifier
<a name="API_MitigationActionIdentifier"></a>

Information that identifies a mitigation action. This information is returned by ListMitigationActions.

## Contents
<a name="API_MitigationActionIdentifier_Contents"></a>

 ** actionArn **   <a name="iot-Type-MitigationActionIdentifier-actionArn"></a>
The IAM role ARN used to apply this mitigation action.
Type: String
Required: No

 ** actionName **   <a name="iot-Type-MitigationActionIdentifier-actionName"></a>
The friendly name of the mitigation action.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** creationDate **   <a name="iot-Type-MitigationActionIdentifier-creationDate"></a>
The date when this mitigation action was created.
Type: Timestamp
Required: No

## See Also
<a name="API_MitigationActionIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/MitigationActionIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/MitigationActionIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/MitigationActionIdentifier)
