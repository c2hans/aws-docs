---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ImportFindingsError.html
---

# ImportFindingsError
<a name="API_ImportFindingsError"></a>

The list of the findings that cannot be imported. For each finding, the list provides the error.

## Contents
<a name="API_ImportFindingsError_Contents"></a>

 ** ErrorCode **   <a name="securityhub-Type-ImportFindingsError-ErrorCode"></a>
The code of the error returned by the `BatchImportFindings` operation.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ErrorMessage **   <a name="securityhub-Type-ImportFindingsError-ErrorMessage"></a>
The message of the error returned by the `BatchImportFindings` operation.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Id **   <a name="securityhub-Type-ImportFindingsError-Id"></a>
The identifier of the finding that could not be updated.
Type: String
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_ImportFindingsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ImportFindingsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ImportFindingsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ImportFindingsError)
