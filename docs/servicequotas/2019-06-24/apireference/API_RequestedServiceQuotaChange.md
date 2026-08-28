---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestedServiceQuotaChange.html
---

# RequestedServiceQuotaChange
<a name="API_RequestedServiceQuotaChange"></a>

Information about a quota increase request.

## Contents
<a name="API_RequestedServiceQuotaChange_Contents"></a>

 ** CaseId **   <a name="servicequotas-Type-RequestedServiceQuotaChange-CaseId"></a>
The case ID.
Type: String
Required: No

 ** Created **   <a name="servicequotas-Type-RequestedServiceQuotaChange-Created"></a>
The date and time when the quota increase request was received and the case ID was created.
Type: Timestamp
Required: No

 ** DesiredValue **   <a name="servicequotas-Type-RequestedServiceQuotaChange-DesiredValue"></a>
The new, increased value for the quota.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 10000000000.
Required: No

 ** GlobalQuota **   <a name="servicequotas-Type-RequestedServiceQuotaChange-GlobalQuota"></a>
Indicates whether the quota is global.
Type: Boolean
Required: No

 ** Id **   <a name="servicequotas-Type-RequestedServiceQuotaChange-Id"></a>
The unique identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-zA-Z][a-zA-Z0-9-]{1,128}`
Required: No

 ** LastUpdated **   <a name="servicequotas-Type-RequestedServiceQuotaChange-LastUpdated"></a>
The date and time of the most recent change.
Type: Timestamp
Required: No

 ** QuotaArn **   <a name="servicequotas-Type-RequestedServiceQuotaChange-QuotaArn"></a>
The Amazon Resource Name (ARN) of the quota.
Type: String
Required: No

 ** QuotaCode **   <a name="servicequotas-Type-RequestedServiceQuotaChange-QuotaCode"></a>
Specifies the quota identifier. To find the quota code for a specific quota, use the [ListServiceQuotas](API_ListServiceQuotas.md) operation, and look for the `QuotaCode` response in the output for the quota you want.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,128}`
Required: No

 ** QuotaContext **   <a name="servicequotas-Type-RequestedServiceQuotaChange-QuotaContext"></a>
The context for this service quota.
Type: [QuotaContextInfo](API_QuotaContextInfo.md) object
Required: No

 ** QuotaName **   <a name="servicequotas-Type-RequestedServiceQuotaChange-QuotaName"></a>
Specifies the quota name.
Type: String
Required: No

 ** QuotaRequestedAtLevel **   <a name="servicequotas-Type-RequestedServiceQuotaChange-QuotaRequestedAtLevel"></a>
Filters the response to return quota requests for the `ACCOUNT`, `RESOURCE`, or `ALL` levels. `ACCOUNT` is the default.
Type: String
Valid Values: `ACCOUNT | RESOURCE | ALL`
Required: No

 ** Requester **   <a name="servicequotas-Type-RequestedServiceQuotaChange-Requester"></a>
The IAM identity of the requester.
Type: String
Required: No

 ** RequestType **   <a name="servicequotas-Type-RequestedServiceQuotaChange-RequestType"></a>
The type of quota increase request. Possible values include:
+  `AutomaticManagement` - The request was automatically created by Service Quotas Automatic Management when quota utilization approached the limit.
If this field is not present, the request was manually created by a user.
Type: String
Valid Values: `AutomaticManagement`
Required: No

 ** ServiceCode **   <a name="servicequotas-Type-RequestedServiceQuotaChange-ServiceCode"></a>
Specifies the service identifier. To find the service code value for an AWS service, use the [ListServices](API_ListServices.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,63}`
Required: No

 ** ServiceName **   <a name="servicequotas-Type-RequestedServiceQuotaChange-ServiceName"></a>
Specifies the service name.
Type: String
Required: No

 ** Status **   <a name="servicequotas-Type-RequestedServiceQuotaChange-Status"></a>
The state of the quota increase request.
+  `PENDING`: The quota increase request is under review by AWS.
+  `CASE_OPENED`: Service Quotas opened a support case to process the quota increase request. Follow-up on the support case for more information.
+  `APPROVED`: The quota increase request is approved.
+  `DENIED`: The quota increase request can't be approved by Service Quotas. Contact AWS Support for more details.
+  `NOT APPROVED`: The quota increase request can't be approved by Service Quotas. Contact AWS Support for more details.
+  `CASE_CLOSED`: The support case associated with this quota increase request was closed. Check the support case correspondence for the outcome of your quota request.
+  `INVALID_REQUEST`: Service Quotas couldn't process your resource-level quota increase request because the Amazon Resource Name (ARN) specified as part of the `ContextId` is invalid.
Type: String
Valid Values: `PENDING | CASE_OPENED | APPROVED | DENIED | CASE_CLOSED | NOT_APPROVED | INVALID_REQUEST`
Required: No

 ** Unit **   <a name="servicequotas-Type-RequestedServiceQuotaChange-Unit"></a>
The unit of measurement.
Type: String
Required: No

## See Also
<a name="API_RequestedServiceQuotaChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/RequestedServiceQuotaChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/RequestedServiceQuotaChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/RequestedServiceQuotaChange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Service Quotas. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicequotas` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
