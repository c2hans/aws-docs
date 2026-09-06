---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ImportErrorData.html
---

# ImportErrorData
<a name="API_ImportErrorData"></a>

Import error data.

## Contents
<a name="API_ImportErrorData_Contents"></a>

 ** accountID **   <a name="mgn-Type-ImportErrorData-accountID"></a>
Import error data source account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** applicationID **   <a name="mgn-Type-ImportErrorData-applicationID"></a>
Import error data application ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `app-[0-9a-zA-Z]{17}`
Required: No

 ** ec2LaunchTemplateID **   <a name="mgn-Type-ImportErrorData-ec2LaunchTemplateID"></a>
Import error data ec2 LaunchTemplate ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** rawError **   <a name="mgn-Type-ImportErrorData-rawError"></a>
Import error data raw error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

 ** rowNumber **   <a name="mgn-Type-ImportErrorData-rowNumber"></a>
Import error data row number.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** sourceServerID **   <a name="mgn-Type-ImportErrorData-sourceServerID"></a>
Import error data source server ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: No

 ** waveID **   <a name="mgn-Type-ImportErrorData-waveID"></a>
Import error data wave id.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `wave-[0-9a-zA-Z]{17}`
Required: No

## See Also
<a name="API_ImportErrorData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ImportErrorData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ImportErrorData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ImportErrorData)
