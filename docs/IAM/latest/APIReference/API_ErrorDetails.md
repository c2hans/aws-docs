---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ErrorDetails.html
---

# ErrorDetails
<a name="API_ErrorDetails"></a>

Contains information about the reason that the operation failed.

This data type is used as a response element in the [GetOrganizationsAccessReport](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOrganizationsAccessReport.html), [GetServiceLastAccessedDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLastAccessedDetails.html), and [GetServiceLastAccessedDetailsWithEntities](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLastAccessedDetailsWithEntities.html) operations.

## Contents
<a name="API_ErrorDetails_Contents"></a>

 ** Code **
The error code associated with the operation failure.
Type: String
Required: Yes

 ** Message **
Detailed information about the reason that the operation failed.
Type: String
Required: Yes

## See Also
<a name="API_ErrorDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ErrorDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ErrorDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ErrorDetails)
