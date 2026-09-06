---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CaseDetails.html
---

# CaseDetails
<a name="API_CaseDetails"></a>

A JSON-formatted object that contains the metadata for a support case. It is contained in the response from a [DescribeCases](API_DescribeCases.md) request. **CaseDetails** contains the following fields:
+  **caseId** - The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-exen-2025-c4c1d2bf33c5cf47*.
+  **categoryCode** - The category of problem for the support case. Corresponds to the `CategoryCode` values returned by a call to [DescribeServices](API_DescribeServices.md).
+  **displayId** - The identifier for the case on pages in the AWS Support Center.
+  **language** - The language in which AWS Support handles the case. AWS Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the `language` parameter if you want support in that language.
+  **nextToken** - A resumption point for pagination.
+  **recentCommunications** - One or more [Communication](API_Communication.md) objects. Fields of these objects are `attachments`, `body`, `caseId`, `submittedBy`, and `timeCreated`.
+  **serviceCode** - The identifier for the AWS service that corresponds to the service code defined in the call to [DescribeServices](API_DescribeServices.md).
+  **severityCode** - The severity code assigned to the case. Contains one of the values returned by the call to [DescribeSeverityLevels](API_DescribeSeverityLevels.md). The possible values are: `low`, `normal`, `high`, `urgent`, and `critical`.
+  **status** - The status of the case in the AWS Support Center. Valid values:
  +  `all-open`
  +  `customer-action-completed`
  +  `opened`
  +  `pending-customer-action`
  +  `reopened`
  +  `resolved`
  +  `unassigned`
  +  `work-in-progress`
+  **subject** - The subject line of the case.
+  **submittedBy** - The email address of the account that submitted the case.
+  **timeCreated** - The time the case was created, in ISO-8601 format.

## Contents
<a name="API_CaseDetails_Contents"></a>

 ** caseId **   <a name="AWSSupport-Type-CaseDetails-caseId"></a>
The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-exen-2025-c4c1d2bf33c5cf47*
Type: String

 ** categoryCode **   <a name="AWSSupport-Type-CaseDetails-categoryCode"></a>
The category of problem for the support case.
Type: String

 ** ccEmailAddresses **   <a name="AWSSupport-Type-CaseDetails-ccEmailAddresses"></a>
The email addresses that receive copies of communication about the case.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** displayId **   <a name="AWSSupport-Type-CaseDetails-displayId"></a>
The ID displayed for the case in the AWS Support Center. This is a numeric string.
Type: String

 ** language **   <a name="AWSSupport-Type-CaseDetails-language"></a>
The language in which AWS Support handles the case. AWS Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the `language` parameter if you want support in that language.
Type: String

 ** recentCommunications **   <a name="AWSSupport-Type-CaseDetails-recentCommunications"></a>
The five most recent communications between you and AWS Support Center, including the IDs of any attachments to the communications. Also includes a `nextToken` that you can use to retrieve earlier communications.
Type: [RecentCaseCommunications](API_RecentCaseCommunications.md) object

 ** serviceCode **   <a name="AWSSupport-Type-CaseDetails-serviceCode"></a>
The code for the AWS service. You can get a list of codes and the corresponding service names by calling [DescribeServices](API_DescribeServices.md).
Type: String

 ** severityCode **   <a name="AWSSupport-Type-CaseDetails-severityCode"></a>
The code for the severity level returned by the call to [DescribeSeverityLevels](API_DescribeSeverityLevels.md).
Type: String

 ** status **   <a name="AWSSupport-Type-CaseDetails-status"></a>
The status of the case.
Valid values:
+  `all-open`
+  `customer-action-completed`
+  `opened`
+  `pending-customer-action`
+  `reopened`
+  `resolved`
+  `unassigned`
+  `work-in-progress`
Type: String

 ** subject **   <a name="AWSSupport-Type-CaseDetails-subject"></a>
The subject line for the case in the AWS Support Center.
Type: String

 ** submittedBy **   <a name="AWSSupport-Type-CaseDetails-submittedBy"></a>
The email address of the account that submitted the case.
Type: String

 ** timeCreated **   <a name="AWSSupport-Type-CaseDetails-timeCreated"></a>
The time that the case was created in the AWS Support Center.
Type: String

## See Also
<a name="API_CaseDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/CaseDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/CaseDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/CaseDetails)
