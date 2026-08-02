---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ReviewInformation.html
---

# ReviewInformation
<a name="API_ReviewInformation"></a>

Information about the result of a document review request.

## Contents
<a name="API_ReviewInformation_Contents"></a>

 ** ReviewedTime **   <a name="systemsmanager-Type-ReviewInformation-ReviewedTime"></a>
The time that the reviewer took action on the document review request.
Type: Timestamp
Required: No

 ** Reviewer **   <a name="systemsmanager-Type-ReviewInformation-Reviewer"></a>
The reviewer assigned to take action on the document review request.
Type: String
Length Constraints: Maximum length of 50.
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`
Required: No

 ** Status **   <a name="systemsmanager-Type-ReviewInformation-Status"></a>
The current status of the document review request.
Type: String
Valid Values: `APPROVED | NOT_REVIEWED | PENDING | REJECTED`
Required: No

## See Also
<a name="API_ReviewInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ReviewInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ReviewInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ReviewInformation)
