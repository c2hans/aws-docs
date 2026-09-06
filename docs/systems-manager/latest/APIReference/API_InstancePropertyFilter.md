---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InstancePropertyFilter.html
---

# InstancePropertyFilter
<a name="API_InstancePropertyFilter"></a>

Describes a filter for a specific list of managed nodes. You can filter node information by using tags. You specify tags by using a key-value mapping.

## Contents
<a name="API_InstancePropertyFilter_Contents"></a>

 ** key **   <a name="systemsmanager-Type-InstancePropertyFilter-key"></a>
The name of the filter.
Type: String
Valid Values: `InstanceIds | AgentVersion | PingStatus | PlatformTypes | DocumentName | ActivationIds | IamRole | ResourceType | AssociationStatus`
Required: Yes

 ** valueSet **   <a name="systemsmanager-Type-InstancePropertyFilter-valueSet"></a>
The filter values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 40 items.
Length Constraints: Minimum length of 1. Maximum length of 100000.
Pattern: `^.{1,100000}$`
Required: Yes

## See Also
<a name="API_InstancePropertyFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InstancePropertyFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InstancePropertyFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InstancePropertyFilter)
