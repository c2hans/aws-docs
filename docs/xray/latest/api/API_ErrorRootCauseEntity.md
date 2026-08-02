---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_ErrorRootCauseEntity.html
---

# ErrorRootCauseEntity
<a name="API_ErrorRootCauseEntity"></a>

A collection of segments and corresponding subsegments associated to a trace summary error.

## Contents
<a name="API_ErrorRootCauseEntity_Contents"></a>

 ** Exceptions **   <a name="xray-Type-ErrorRootCauseEntity-Exceptions"></a>
The types and messages of the exceptions.
Type: Array of [RootCauseException](API_RootCauseException.md) objects
Required: No

 ** Name **   <a name="xray-Type-ErrorRootCauseEntity-Name"></a>
The name of the entity.
Type: String
Required: No

 ** Remote **   <a name="xray-Type-ErrorRootCauseEntity-Remote"></a>
A flag that denotes a remote subsegment.
Type: Boolean
Required: No

## See Also
<a name="API_ErrorRootCauseEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/ErrorRootCauseEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/ErrorRootCauseEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/ErrorRootCauseEntity)
