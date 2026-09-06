---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_FreeTrialAccountInfo.html
---

# FreeTrialAccountInfo
<a name="API_FreeTrialAccountInfo"></a>

Information about the Amazon Inspector free trial for an account.

## Contents
<a name="API_FreeTrialAccountInfo_Contents"></a>

 ** accountId **   <a name="inspector2-Type-FreeTrialAccountInfo-accountId"></a>
The account associated with the Amazon Inspector free trial information.
Type: String
Pattern: `.*[0-9]{12}.*`
Required: Yes

 ** freeTrialInfo **   <a name="inspector2-Type-FreeTrialAccountInfo-freeTrialInfo"></a>
Contains information about the Amazon Inspector free trial for an account.
Type: Array of [FreeTrialInfo](API_FreeTrialInfo.md) objects
Required: Yes

## See Also
<a name="API_FreeTrialAccountInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/FreeTrialAccountInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/FreeTrialAccountInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/FreeTrialAccountInfo)
