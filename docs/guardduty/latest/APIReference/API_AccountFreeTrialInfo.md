---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AccountFreeTrialInfo.html
---

# AccountFreeTrialInfo
<a name="API_AccountFreeTrialInfo"></a>

Provides details of the GuardDuty member account that uses a free trial service.

## Contents
<a name="API_AccountFreeTrialInfo_Contents"></a>

 ** accountId **   <a name="guardduty-Type-AccountFreeTrialInfo-accountId"></a>
The account identifier of the GuardDuty member account.
Type: String
Required: No

 ** dataSources **   <a name="guardduty-Type-AccountFreeTrialInfo-dataSources"></a>
 *This member has been deprecated.*
Describes the data source enabled for the GuardDuty member account.
Type: [DataSourcesFreeTrial](API_DataSourcesFreeTrial.md) object
Required: No

 ** features **   <a name="guardduty-Type-AccountFreeTrialInfo-features"></a>
A list of features enabled for the GuardDuty account.
Type: Array of [FreeTrialFeatureConfigurationResult](API_FreeTrialFeatureConfigurationResult.md) objects
Required: No

## See Also
<a name="API_AccountFreeTrialInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AccountFreeTrialInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AccountFreeTrialInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AccountFreeTrialInfo)
