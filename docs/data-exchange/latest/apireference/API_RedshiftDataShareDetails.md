---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_RedshiftDataShareDetails.html
---

# RedshiftDataShareDetails
<a name="API_RedshiftDataShareDetails"></a>

Extra details specific to the affected scope in this Redshift data set.

## Contents
<a name="API_RedshiftDataShareDetails_Contents"></a>

 ** Arn **   <a name="dataexchange-Type-RedshiftDataShareDetails-Arn"></a>
The ARN of the underlying Redshift data share that is being affected by this notification.
Type: String
Required: Yes

 ** Database **   <a name="dataexchange-Type-RedshiftDataShareDetails-Database"></a>
The database name in the Redshift data share that is being affected by this notification.
Type: String
Required: Yes

 ** Function **   <a name="dataexchange-Type-RedshiftDataShareDetails-Function"></a>
A function name in the Redshift database that is being affected by this notification.
Type: String
Required: No

 ** Schema **   <a name="dataexchange-Type-RedshiftDataShareDetails-Schema"></a>
A schema name in the Redshift database that is being affected by this notification.
Type: String
Required: No

 ** Table **   <a name="dataexchange-Type-RedshiftDataShareDetails-Table"></a>
A table name in the Redshift database that is being affected by this notification.
Type: String
Required: No

 ** View **   <a name="dataexchange-Type-RedshiftDataShareDetails-View"></a>
A view name in the Redshift database that is being affected by this notification.
Type: String
Required: No

## See Also
<a name="API_RedshiftDataShareDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/RedshiftDataShareDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/RedshiftDataShareDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/RedshiftDataShareDetails)
