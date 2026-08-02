---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ProspectingResultAws.html
---

# ProspectingResultAws
<a name="API_ProspectingResultAws"></a>

Contains the prospecting data that AWS sources. This includes task execution details, customer account information, and insights that AI generates from the prospecting analysis.

## Contents
<a name="API_ProspectingResultAws_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Customer **   <a name="AWSPartnerCentral-Type-ProspectingResultAws-Customer"></a>
Contains details about the prospected customer account, including geographic, industry, and segment classifications.
Type: [ProspectingResultCustomer](API_ProspectingResultCustomer.md) object
Required: No

 ** EndTime **   <a name="AWSPartnerCentral-Type-ProspectingResultAws-EndTime"></a>
The timestamp when the prospecting task completed processing. The format is ISO 8601 (UTC).
Type: Timestamp
Required: No

 ** Insights **   <a name="AWSPartnerCentral-Type-ProspectingResultAws-Insights"></a>
Insights that AI generates from the prospecting analysis. These insights include engagement scores and solution fit assessments for the prospected customer.
Type: [ProspectingInsights](API_ProspectingInsights.md) object
Required: No

 ** StartTime **   <a name="AWSPartnerCentral-Type-ProspectingResultAws-StartTime"></a>
The timestamp when the prospecting result context was created. The format is ISO 8601 (UTC).
Type: Timestamp
Required: No

 ** TaskArn **   <a name="AWSPartnerCentral-Type-ProspectingResultAws-TaskArn"></a>
The Amazon Resource Name (ARN) of the prospecting task. Use this ARN to track and manage the task within AWS.
Type: String
Pattern: `arn:.*`
Required: No

 ** TaskId **   <a name="AWSPartnerCentral-Type-ProspectingResultAws-TaskId"></a>
The unique identifier of the prospecting task that generates this result.
Type: String
Pattern: `task-[0-9a-z]{14}`
Required: No

 ** TaskName **   <a name="AWSPartnerCentral-Type-ProspectingResultAws-TaskName"></a>
The name that the user provides for the prospecting task that generates this result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ProspectingResultAws_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ProspectingResultAws)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ProspectingResultAws)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ProspectingResultAws)
