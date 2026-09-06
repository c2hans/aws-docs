---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_SchemaChangeRequestDetails.html
---

# SchemaChangeRequestDetails
<a name="API_SchemaChangeRequestDetails"></a>

Extra details specific to this schema change type notification.

## Contents
<a name="API_SchemaChangeRequestDetails_Contents"></a>

 ** SchemaChangeAt **   <a name="dataexchange-Type-SchemaChangeRequestDetails-SchemaChangeAt"></a>
A date in the future when the schema change is taking effect.
Type: Timestamp
Required: Yes

 ** Changes **   <a name="dataexchange-Type-SchemaChangeRequestDetails-Changes"></a>
List of schema changes happening in the scope of this notification. This can have up to 100 entries.
Type: Array of [SchemaChangeDetails](API_SchemaChangeDetails.md) objects
Required: No

## See Also
<a name="API_SchemaChangeRequestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/SchemaChangeRequestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/SchemaChangeRequestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/SchemaChangeRequestDetails)
