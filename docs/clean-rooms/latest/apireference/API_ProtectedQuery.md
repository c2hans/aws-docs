---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedQuery.html
---

# ProtectedQuery
<a name="API_ProtectedQuery"></a>

The parameters for an AWS Clean Rooms protected query.

## Contents
<a name="API_ProtectedQuery_Contents"></a>

 ** createTime **   <a name="API-Type-ProtectedQuery-createTime"></a>
The time at which the protected query was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-ProtectedQuery-id"></a>
The identifier for a protected query instance.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipArn **   <a name="API-Type-ProtectedQuery-membershipArn"></a>
The ARN of the membership.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-ProtectedQuery-membershipId"></a>
The identifier for the membership.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** status **   <a name="API-Type-ProtectedQuery-status"></a>
The status of the query.
Type: String
Valid Values: `SUBMITTED | STARTED | CANCELLED | CANCELLING | FAILED | SUCCESS | TIMED_OUT`
Required: Yes

 ** computeConfiguration **   <a name="API-Type-ProtectedQuery-computeConfiguration"></a>
 The compute configuration for the protected query.
Type: [ComputeConfiguration](API_ComputeConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** differentialPrivacy **   <a name="API-Type-ProtectedQuery-differentialPrivacy"></a>
The sensitivity parameters of the differential privacy results of the protected query.
Type: [DifferentialPrivacyParameters](API_DifferentialPrivacyParameters.md) object
Required: No

 ** error **   <a name="API-Type-ProtectedQuery-error"></a>
An error thrown by the protected query.
Type: [ProtectedQueryError](API_ProtectedQueryError.md) object
Required: No

 ** queryComputePayerAccountId **   <a name="API-Type-ProtectedQuery-queryComputePayerAccountId"></a>
The account ID of the member that pays for the query compute costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** result **   <a name="API-Type-ProtectedQuery-result"></a>
The result of the protected query.
Type: [ProtectedQueryResult](API_ProtectedQueryResult.md) object
Required: No

 ** resultConfiguration **   <a name="API-Type-ProtectedQuery-resultConfiguration"></a>
Contains any details needed to write the query results.
Type: [ProtectedQueryResultConfiguration](API_ProtectedQueryResultConfiguration.md) object
Required: No

 ** sqlParameters **   <a name="API-Type-ProtectedQuery-sqlParameters"></a>
The protected query SQL parameters.
Type: [ProtectedQuerySQLParameters](API_ProtectedQuerySQLParameters.md) object
Required: No

 ** statistics **   <a name="API-Type-ProtectedQuery-statistics"></a>
Statistics about protected query execution.
Type: [ProtectedQueryStatistics](API_ProtectedQueryStatistics.md) object
Required: No

## See Also
<a name="API_ProtectedQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedQuery)
