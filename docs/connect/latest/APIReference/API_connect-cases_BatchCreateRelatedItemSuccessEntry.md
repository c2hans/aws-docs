---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_BatchCreateRelatedItemSuccessEntry.html
---

# BatchCreateRelatedItemSuccessEntry
<a name="API_connect-cases_BatchCreateRelatedItemSuccessEntry"></a>

Information about a related item that was created.

## Contents
<a name="API_connect-cases_BatchCreateRelatedItemSuccessEntry_Contents"></a>

 ** caseIdentifier **   <a name="connect-Type-connect-cases_BatchCreateRelatedItemSuccessEntry-caseIdentifier"></a>
The identifiers of the case that the related item is associated with.
Type: [CaseIdentifier](API_connect-cases_CaseIdentifier.md) object
Required: Yes

 ** relatedItemArn **   <a name="connect-Type-connect-cases_BatchCreateRelatedItemSuccessEntry-relatedItemArn"></a>
The Amazon Resource Name (ARN) of the related item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** relatedItemId **   <a name="connect-Type-connect-cases_BatchCreateRelatedItemSuccessEntry-relatedItemId"></a>
The unique identifier of the related item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## See Also
<a name="API_connect-cases_BatchCreateRelatedItemSuccessEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/BatchCreateRelatedItemSuccessEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/BatchCreateRelatedItemSuccessEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/BatchCreateRelatedItemSuccessEntry)
