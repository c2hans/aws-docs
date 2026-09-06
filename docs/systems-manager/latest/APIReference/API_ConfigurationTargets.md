---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ConfigurationTargets.html
---

# ConfigurationTargets
<a name="API_ConfigurationTargets"></a>

The target resources in the third-party cloud environment.

## Contents
<a name="API_ConfigurationTargets_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Subscriptions **   <a name="systemsmanager-Type-ConfigurationTargets-Subscriptions"></a>
A list of Azure subscriptions to target.
Type: Array of [AzureSubscription](API_AzureSubscription.md) objects
Array Members: Minimum number of 1 item. Maximum number of 75 items.
Required: No

## See Also
<a name="API_ConfigurationTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ConfigurationTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ConfigurationTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ConfigurationTargets)
