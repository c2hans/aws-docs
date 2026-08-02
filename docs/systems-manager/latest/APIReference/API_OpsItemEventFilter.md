---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsItemEventFilter.html
---

# OpsItemEventFilter
<a name="API_OpsItemEventFilter"></a>

Describes a filter for a specific list of OpsItem events. You can filter event information by using tags. You specify tags by using a key-value pair mapping.

## Contents
<a name="API_OpsItemEventFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-OpsItemEventFilter-Key"></a>
The name of the filter key. Currently, the only supported value is `OpsItemId`.
Type: String
Valid Values: `OpsItemId`
Required: Yes

 ** Operator **   <a name="systemsmanager-Type-OpsItemEventFilter-Operator"></a>
The operator used by the filter call. Currently, the only supported value is `Equal`.
Type: String
Valid Values: `Equal`
Required: Yes

 ** Values **   <a name="systemsmanager-Type-OpsItemEventFilter-Values"></a>
The values for the filter, consisting of one or more OpsItem IDs.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `^(oi)-[0-9a-f]{12}$`
Required: Yes

## See Also
<a name="API_OpsItemEventFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsItemEventFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsItemEventFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsItemEventFilter)
