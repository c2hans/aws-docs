---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ExpectedContractDuration.html
---

# ExpectedContractDuration
<a name="API_ExpectedContractDuration"></a>

The expected duration of a partner's contract with the customer. Used to convert Total Contract Value (TCV) to Monthly Recurring Revenue (MRR) for opportunity dealsizing calculations.

## Contents
<a name="API_ExpectedContractDuration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Term **   <a name="AWSPartnerCentral-Type-ExpectedContractDuration-Term"></a>
The unit of measurement for the contract duration value. Currently accepts only `Months`.
Type: String
Valid Values: `Months`
Required: Yes

 ** Value **   <a name="AWSPartnerCentral-Type-ExpectedContractDuration-Value"></a>
A String representation of the contract duration as an integer, expressed in the unit defined by `Term`. Valid values range from `1` to `144`.
Type: String
Required: Yes

## See Also
<a name="API_ExpectedContractDuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ExpectedContractDuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ExpectedContractDuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ExpectedContractDuration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
