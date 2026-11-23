---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CustomerAccountBulkJobFilter.html
---

# CustomerAccountBulkJobFilter

The criteria that limit which bulk jobs `ListCustomerAccountBulkJobs` returns.

## Contents
<a name="API_CustomerAccountBulkJobFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Identifier **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobFilter-Identifier"></a>
Filters the results to the bulk job with the specified ARN or identifier.
Type: String
Pattern: `(arn:.*|bulkjob-[0-9a-z]{13})`
Required: No

 ** Status **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobFilter-Status"></a>
Filters the results to bulk jobs with the specified status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | FAILED`
Required: No

## See Also
<a name="API_CustomerAccountBulkJobFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/CustomerAccountBulkJobFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CustomerAccountBulkJobFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/CustomerAccountBulkJobFilter)
