---
source_url: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbParameterGroupSummary.html
---

# DbParameterGroupSummary
<a name="API_DbParameterGroupSummary"></a>

Contains a summary of a DB parameter group.

## Contents
<a name="API_DbParameterGroupSummary_Contents"></a>

 ** arn **   <a name="tsinfluxdb-Type-DbParameterGroupSummary-arn"></a>
The Amazon Resource Name (ARN) of the DB parameter group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws[a-z\-]*:timestream\-influxdb:[a-z0-9\-]+:[0-9]{12}:(db\-instance|db\-cluster|db\-parameter\-group)/[a-zA-Z0-9]{3,64}`
Required: Yes

 ** id **   <a name="tsinfluxdb-Type-DbParameterGroupSummary-id"></a>
A service-generated unique identifier.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** name **   <a name="tsinfluxdb-Type-DbParameterGroupSummary-name"></a>
This customer-supplied name uniquely identifies the parameter group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*`
Required: Yes

 ** description **   <a name="tsinfluxdb-Type-DbParameterGroupSummary-description"></a>
A description of the DB parameter group.
Type: String
Required: No

## See Also
<a name="API_DbParameterGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-influxdb-2023-01-27/DbParameterGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-influxdb-2023-01-27/DbParameterGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-influxdb-2023-01-27/DbParameterGroupSummary)
