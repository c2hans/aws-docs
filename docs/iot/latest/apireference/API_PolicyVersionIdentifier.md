---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_PolicyVersionIdentifier.html
---

# PolicyVersionIdentifier
<a name="API_PolicyVersionIdentifier"></a>

Information about the version of the policy associated with the resource.

## Contents
<a name="API_PolicyVersionIdentifier_Contents"></a>

 ** policyName **   <a name="iot-Type-PolicyVersionIdentifier-policyName"></a>
The name of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

 ** policyVersionId **   <a name="iot-Type-PolicyVersionIdentifier-policyVersionId"></a>
The ID of the version of the policy associated with the resource.
Type: String
Pattern: `[0-9]+`
Required: No

## See Also
<a name="API_PolicyVersionIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/PolicyVersionIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/PolicyVersionIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/PolicyVersionIdentifier)
