---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Hive.html
---

# Hive
<a name="API_Hive"></a>

The configurations for the Hive job driver.

## Contents
<a name="API_Hive_Contents"></a>

 ** query **   <a name="emrserverless-Type-Hive-query"></a>
The query for the Hive job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10280.
Pattern: `.*\S.*`
Required: Yes

 ** initQueryFile **   <a name="emrserverless-Type-Hive-initQueryFile"></a>
The query file for the Hive job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** parameters **   <a name="emrserverless-Type-Hive-parameters"></a>
The parameters for the Hive job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 102400.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Hive_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/Hive)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/Hive)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/Hive)
