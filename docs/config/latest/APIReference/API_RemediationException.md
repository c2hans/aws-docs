---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationException.html
---

# RemediationException
<a name="API_RemediationException"></a>

An object that represents the details about the remediation exception. The details include the rule name, an explanation of an exception, the time when the exception will be deleted, the resource ID, and resource type.

## Contents
<a name="API_RemediationException_Contents"></a>

 ** ConfigRuleName **   <a name="config-Type-RemediationException-ConfigRuleName"></a>
The name of the AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** ResourceId **   <a name="config-Type-RemediationException-ResourceId"></a>
The ID of the resource (for example., sg-xxxxxx).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ResourceType **   <a name="config-Type-RemediationException-ResourceType"></a>
The type of a resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ExpirationTime **   <a name="config-Type-RemediationException-ExpirationTime"></a>
The time when the remediation exception will be deleted.
Type: Timestamp
Required: No

 ** Message **   <a name="config-Type-RemediationException-Message"></a>
An explanation of an remediation exception.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_RemediationException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/RemediationException)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/RemediationException)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/RemediationException)
