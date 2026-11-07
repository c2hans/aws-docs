---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_BatchCreateRelatedItemErrorEntry.html
---

# BatchCreateRelatedItemErrorEntry
<a name="API_connect-cases_BatchCreateRelatedItemErrorEntry"></a>

Information about a related item that wasn't created.

## Contents
<a name="API_connect-cases_BatchCreateRelatedItemErrorEntry_Contents"></a>

 ** caseIdentifier **   <a name="connect-Type-connect-cases_BatchCreateRelatedItemErrorEntry-caseIdentifier"></a>
The identifiers of the case that the related item wasn't created for.
Type: [CaseIdentifier](API_connect-cases_CaseIdentifier.md) object
Required: Yes

 ** errorCode **   <a name="connect-Type-connect-cases_BatchCreateRelatedItemErrorEntry-errorCode"></a>
The error code. For possible values, see `failedItems`.
Type: String
Required: Yes

 ** errorMessage **   <a name="connect-Type-connect-cases_BatchCreateRelatedItemErrorEntry-errorMessage"></a>
A message that describes the error.
Type: String
Required: Yes

## See Also
<a name="API_connect-cases_BatchCreateRelatedItemErrorEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/BatchCreateRelatedItemErrorEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/BatchCreateRelatedItemErrorEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/BatchCreateRelatedItemErrorEntry)
