---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Treatment.html
---

# Treatment
<a name="API_Treatment"></a>

Describes a treatment in an experiment, including its traffic allocation weight and feature flag value.

## Contents
<a name="API_Treatment_Contents"></a>

 ** FlagValue **   <a name="appconfig-Type-Treatment-FlagValue"></a>
The feature flag value served to users assigned to this treatment.
Type: [FlagValue](API_FlagValue.md) object
Required: Yes

 ** Weight **   <a name="appconfig-Type-Treatment-Weight"></a>
The traffic allocation weight for this treatment.
Type: Float
Valid Range: Minimum value of 0.0.
Required: Yes

 ** Description **   <a name="appconfig-Type-Treatment-Description"></a>
A description of the treatment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Key **   <a name="appconfig-Type-Treatment-Key"></a>
The unique key that identifies this treatment.
Type: String
Pattern: `^[a-zA-Z0-9]{1,8}`
Required: No

## See Also
<a name="API_Treatment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/Treatment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/Treatment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/Treatment)
