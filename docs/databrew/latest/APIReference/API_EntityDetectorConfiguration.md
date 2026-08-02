---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_EntityDetectorConfiguration.html
---

# EntityDetectorConfiguration
<a name="API_EntityDetectorConfiguration"></a>

Configuration of entity detection for a profile job. When undefined, entity detection is disabled.

## Contents
<a name="API_EntityDetectorConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EntityTypes **   <a name="databrew-Type-EntityDetectorConfiguration-EntityTypes"></a>
Entity types to detect. Can be any of the following:
+ USA\_SSN
+ EMAIL
+ USA\_ITIN
+ USA\_PASSPORT\_NUMBER
+ PHONE\_NUMBER
+ USA\_DRIVING\_LICENSE
+ BANK\_ACCOUNT
+ CREDIT\_CARD
+ IP\_ADDRESS
+ MAC\_ADDRESS
+ USA\_DEA\_NUMBER
+ USA\_HCPCS\_CODE
+ USA\_NATIONAL\_PROVIDER\_IDENTIFIER
+ USA\_NATIONAL\_DRUG\_CODE
+ USA\_HEALTH\_INSURANCE\_CLAIM\_NUMBER
+ USA\_MEDICARE\_BENEFICIARY\_IDENTIFIER
+ USA\_CPT\_CODE
+ PERSON\_NAME
+ DATE
The Entity type group USA\_ALL is also supported, and includes all of the above entity types except PERSON\_NAME and DATE.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[A-Z_][A-Z\\d_]*$`
Required: Yes

 ** AllowedStatistics **   <a name="databrew-Type-EntityDetectorConfiguration-AllowedStatistics"></a>
Configuration of statistics that are allowed to be run on columns that contain detected entities. When undefined, no statistics will be computed on columns that contain detected entities.
Type: Array of [AllowedStatistics](API_AllowedStatistics.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_EntityDetectorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/EntityDetectorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/EntityDetectorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/EntityDetectorConfiguration)
