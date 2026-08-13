---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_EffectiveLimit.html
---

# EffectiveLimit
<a name="API_EffectiveLimit"></a>

The effective limit for a resource type that applies to a user, considering all applicable profile assignments and inheritance rules.

## Contents
<a name="API_EffectiveLimit_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** limitUnit **   <a name="QS-Type-EffectiveLimit-limitUnit"></a>
The unit of measurement for the limit.
Type: String
Valid Values: `MB | GB | HOURS | DAYS`
Required: Yes

 ** limitValue **   <a name="QS-Type-EffectiveLimit-limitValue"></a>
The maximum allowed value for the resource.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** profileId **   <a name="QS-Type-EffectiveLimit-profileId"></a>
The identifier of the limits profile that defines this limit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `lp-[a-f0-9-]+`
Required: Yes

 ** resourceType **   <a name="QS-Type-EffectiveLimit-resourceType"></a>
The type of resource that the limit applies to.
Type: String
Valid Values: `INDEX_STORAGE | AGENT_HOURS`
Required: Yes

 ** source **   <a name="QS-Type-EffectiveLimit-source"></a>
The source from which this limit was inherited. Possible values:
+  `DIRECT_USER` – The limit comes from a profile directly assigned to the user.
+  `GROUP` – The limit comes from a profile assigned to a group the user belongs to.
+  `ROLE` – The limit comes from a profile assigned to a role the user has.
+  `ACCOUNT` – The limit comes from the account-level default profile.
+  `SYSTEM_DEFAULT` – The limit comes from the built-in system default.
Type: String
Valid Values: `DIRECT_USER | GROUP | ROLE | ACCOUNT | SYSTEM_DEFAULT`
Required: Yes

## See Also
<a name="API_EffectiveLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/EffectiveLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/EffectiveLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/EffectiveLimit)
