---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GeneratorDetails.html
---

# GeneratorDetails
<a name="API_GeneratorDetails"></a>

 Provides metadata for the Amazon CodeGuru detector associated with a finding. This field pertains to findings that relate to AWS Lambda functions. Amazon Inspector identifies policy violations and vulnerabilities in Lambda function code based on internal detectors developed in collaboration with Amazon CodeGuru. AWS Security Hub CSPM receives those findings.

## Contents
<a name="API_GeneratorDetails_Contents"></a>

 ** Description **   <a name="securityhub-Type-GeneratorDetails-Description"></a>
 The description of the detector used to identify the code vulnerability.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Labels **   <a name="securityhub-Type-GeneratorDetails-Labels"></a>
 An array of tags used to identify the detector associated with the finding.
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-GeneratorDetails-Name"></a>
 The name of the detector used to identify the code vulnerability.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_GeneratorDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GeneratorDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GeneratorDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GeneratorDetails)
