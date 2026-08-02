---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GraphLink.html
---

# GraphLink
<a name="API_GraphLink"></a>

 The relation between two services.

## Contents
<a name="API_GraphLink_Contents"></a>

 ** DestinationTraceIds **   <a name="xray-Type-GraphLink-DestinationTraceIds"></a>
 Destination traces of a link relationship.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 35.
Required: No

 ** ReferenceType **   <a name="xray-Type-GraphLink-ReferenceType"></a>
 Relationship of a trace to the corresponding service.
Type: String
Required: No

 ** SourceTraceId **   <a name="xray-Type-GraphLink-SourceTraceId"></a>
 Source trace of a link relationship.
Type: String
Required: No

## See Also
<a name="API_GraphLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GraphLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GraphLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GraphLink)
