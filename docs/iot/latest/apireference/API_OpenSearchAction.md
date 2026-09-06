---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_OpenSearchAction.html
---

# OpenSearchAction
<a name="API_OpenSearchAction"></a>

Describes an action that writes data to an Amazon OpenSearch Service domain.

## Contents
<a name="API_OpenSearchAction_Contents"></a>

 ** endpoint **   <a name="iot-Type-OpenSearchAction-endpoint"></a>
The endpoint of your OpenSearch domain.
Type: String
Pattern: `https?://.*`
Required: Yes

 ** id **   <a name="iot-Type-OpenSearchAction-id"></a>
The unique identifier for the document you are storing.
Type: String
Required: Yes

 ** index **   <a name="iot-Type-OpenSearchAction-index"></a>
The OpenSearch index where you want to store your data.
Type: String
Required: Yes

 ** roleArn **   <a name="iot-Type-OpenSearchAction-roleArn"></a>
The IAM role ARN that has access to OpenSearch.
Type: String
Required: Yes

 ** type **   <a name="iot-Type-OpenSearchAction-type"></a>
The type of document you are storing.
Type: String
Required: Yes

## See Also
<a name="API_OpenSearchAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/OpenSearchAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/OpenSearchAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/OpenSearchAction)
