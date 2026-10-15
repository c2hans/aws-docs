---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ServiceQuotaWarningSummary.html
---

# ServiceQuotaWarningSummary
<a name="API_ServiceQuotaWarningSummary"></a>

A service quota warning for a plan. Region switch creates a warning when the applied quota value in one Region of a plan is lower than the value for the matching resource in another Region or account in the plan, or when it can't complete a service quota check.

## Contents
<a name="API_ServiceQuotaWarningSummary_Contents"></a>

 ** accountId **   <a name="regionswitch-Type-ServiceQuotaWarningSummary-accountId"></a>
The AWS account ID that owns the plan that the warning applies to.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** planArn **   <a name="regionswitch-Type-ServiceQuotaWarningSummary-planArn"></a>
The Amazon Resource Name (ARN) of the plan that the warning applies to.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

 ** quotaRegion **   <a name="regionswitch-Type-ServiceQuotaWarningSummary-quotaRegion"></a>
The AWS Region that the quota applies to.
Type: String
Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: Yes

 ** status **   <a name="regionswitch-Type-ServiceQuotaWarningSummary-status"></a>
The status of the service quota warning.
Type: String
Valid Values: `pending | denied | insufficientPermissions | maxRegionSwitchRequestsExceeded | maxAccountRequestsExceeded`
Required: Yes

 ** caseId **   <a name="regionswitch-Type-ServiceQuotaWarningSummary-caseId"></a>
The ID of the support case associated with the quota increase request, if Region switch submitted one for this quota.
Type: String
Required: No

 ** lastCheckedAt **   <a name="regionswitch-Type-ServiceQuotaWarningSummary-lastCheckedAt"></a>
The time (UTC) when Region switch last checked this quota.
Type: Timestamp
Required: No

 ** quotaCode **   <a name="regionswitch-Type-ServiceQuotaWarningSummary-quotaCode"></a>
The quota code of the quota that the warning applies to, as defined in Service Quotas.
Type: String
Required: No

 ** quotaName **   <a name="regionswitch-Type-ServiceQuotaWarningSummary-quotaName"></a>
The name of the quota that the warning applies to, as defined in Service Quotas.
Type: String
Required: No

 ** requestId **   <a name="regionswitch-Type-ServiceQuotaWarningSummary-requestId"></a>
The ID of the quota increase request that Region switch submitted, if it submitted one for this quota.
Type: String
Required: No

 ** serviceCode **   <a name="regionswitch-Type-ServiceQuotaWarningSummary-serviceCode"></a>
The service code of the service that the quota belongs to, as defined in Service Quotas. For example, `ec2`.
Type: String
Required: No

 ** warningCreatedAt **   <a name="regionswitch-Type-ServiceQuotaWarningSummary-warningCreatedAt"></a>
The time (UTC) when Region switch created this warning.
Type: Timestamp
Required: No

 ** warningMessage **   <a name="regionswitch-Type-ServiceQuotaWarningSummary-warningMessage"></a>
A message that describes the service quota warning.
Type: String
Required: No

## See Also
<a name="API_ServiceQuotaWarningSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/ServiceQuotaWarningSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/ServiceQuotaWarningSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/ServiceQuotaWarningSummary)
