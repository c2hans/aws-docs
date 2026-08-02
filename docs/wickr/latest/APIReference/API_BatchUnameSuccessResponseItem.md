---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchUnameSuccessResponseItem.html
---

# BatchUnameSuccessResponseItem
<a name="API_BatchUnameSuccessResponseItem"></a>

Contains information about a username hash that was successfully resolved in a batch uname lookup operation.

## Contents
<a name="API_BatchUnameSuccessResponseItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** uname **   <a name="wickr-Type-BatchUnameSuccessResponseItem-uname"></a>
The username hash that was successfully resolved.
Type: String
Required: Yes

 ** username **   <a name="wickr-Type-BatchUnameSuccessResponseItem-username"></a>
The email address or username corresponding to the username hash.
Type: String
Pattern: `[\S\s]*`
Required: Yes

## See Also
<a name="API_BatchUnameSuccessResponseItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/BatchUnameSuccessResponseItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/BatchUnameSuccessResponseItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/BatchUnameSuccessResponseItem)
