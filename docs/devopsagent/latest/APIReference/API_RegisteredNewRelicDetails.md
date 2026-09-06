---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RegisteredNewRelicDetails.html
---

# RegisteredNewRelicDetails
<a name="API_RegisteredNewRelicDetails"></a>

Details specific to a registered NewRelic instance.

## Contents
<a name="API_RegisteredNewRelicDetails_Contents"></a>

 ** accountId **   <a name="devopsagent-Type-RegisteredNewRelicDetails-accountId"></a>
The NewRelic account ID.
Type: String
Required: Yes

 ** region **   <a name="devopsagent-Type-RegisteredNewRelicDetails-region"></a>
The NewRelic region (determines API endpoint).
Type: String
Valid Values: `US | EU | JP`
Required: Yes

 ** description **   <a name="devopsagent-Type-RegisteredNewRelicDetails-description"></a>
Optional user description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: No

## See Also
<a name="API_RegisteredNewRelicDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RegisteredNewRelicDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RegisteredNewRelicDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RegisteredNewRelicDetails)
