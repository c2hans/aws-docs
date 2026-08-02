---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SelfManagedInput.html
---

# SelfManagedInput
<a name="API_SelfManagedInput"></a>

Configuration for a self-managed Private Connection.

## Contents
<a name="API_SelfManagedInput_Contents"></a>

 ** resourceConfigurationId **   <a name="devopsagent-Type-SelfManagedInput-resourceConfigurationId"></a>
The ID or ARN of the resource configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}|rcfg-[0-9a-z]{17})`
Required: Yes

 ** certificate **   <a name="devopsagent-Type-SelfManagedInput-certificate"></a>
Certificate for the Private Connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Required: No

## See Also
<a name="API_SelfManagedInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SelfManagedInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SelfManagedInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SelfManagedInput)
