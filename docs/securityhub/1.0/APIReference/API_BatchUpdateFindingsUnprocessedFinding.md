---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindingsUnprocessedFinding.html
---

# BatchUpdateFindingsUnprocessedFinding
<a name="API_BatchUpdateFindingsUnprocessedFinding"></a>

A finding from a `BatchUpdateFindings` request that Security Hub CSPM was unable to update.

## Contents
<a name="API_BatchUpdateFindingsUnprocessedFinding_Contents"></a>

 ** ErrorCode **   <a name="securityhub-Type-BatchUpdateFindingsUnprocessedFinding-ErrorCode"></a>
The code associated with the error. Possible values are:
+  `ConcurrentUpdateError` - Another request attempted to update the finding while this request was being processed. This error may also occur if you call [https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html) and [https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html) at the same time.
+  `DuplicatedFindingIdentifier` - The request included two or more findings with the same `FindingIdentifier`.
+  `FindingNotFound` - The `FindingIdentifier` included in the request did not match an existing finding.
+  `FindingSizeExceeded` - The finding size was greater than the permissible value of 240 KB.
+  `InternalFailure` - An internal service failure occurred when updating the finding.
+  `InvalidInput` - The finding update contained an invalid value that did not satisfy the [AWS Security Finding Format](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html) syntax.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ErrorMessage **   <a name="securityhub-Type-BatchUpdateFindingsUnprocessedFinding-ErrorMessage"></a>
The message associated with the error. Possible values are:
+  `Concurrent finding updates detected`
+  `Finding Identifier is duplicated`
+  `Finding Not Found`
+  `Finding size exceeded 240 KB`
+  `Internal service failure`
+  `Invalid Input`
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** FindingIdentifier **   <a name="securityhub-Type-BatchUpdateFindingsUnprocessedFinding-FindingIdentifier"></a>
The identifier of the finding that was not updated.
Type: [AwsSecurityFindingIdentifier](API_AwsSecurityFindingIdentifier.md) object
Required: Yes

## See Also
<a name="API_BatchUpdateFindingsUnprocessedFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/BatchUpdateFindingsUnprocessedFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/BatchUpdateFindingsUnprocessedFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/BatchUpdateFindingsUnprocessedFinding)
