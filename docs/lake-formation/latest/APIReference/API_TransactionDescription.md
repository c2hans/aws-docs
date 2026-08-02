---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_TransactionDescription.html
---

# TransactionDescription
<a name="API_TransactionDescription"></a>

A structure that contains information about a transaction.

## Contents
<a name="API_TransactionDescription_Contents"></a>

 ** TransactionEndTime **   <a name="lakeformation-Type-TransactionDescription-TransactionEndTime"></a>
The time when the transaction committed or aborted, if it is not currently active.
Type: Timestamp
Required: No

 ** TransactionId **   <a name="lakeformation-Type-TransactionDescription-TransactionId"></a>
The ID of the transaction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: No

 ** TransactionStartTime **   <a name="lakeformation-Type-TransactionDescription-TransactionStartTime"></a>
The time when the transaction started.
Type: Timestamp
Required: No

 ** TransactionStatus **   <a name="lakeformation-Type-TransactionDescription-TransactionStatus"></a>
A status of ACTIVE, COMMITTED, or ABORTED.
Type: String
Valid Values: `ACTIVE | COMMITTED | ABORTED | COMMIT_IN_PROGRESS`
Required: No

## See Also
<a name="API_TransactionDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/TransactionDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/TransactionDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/TransactionDescription)
