---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_MembershipJobComputePaymentConfig.html
---

# MembershipJobComputePaymentConfig
<a name="API_MembershipJobComputePaymentConfig"></a>

An object representing the payment responsibilities accepted by the collaboration member for query and job compute costs.

## Contents
<a name="API_MembershipJobComputePaymentConfig_Contents"></a>

 ** isResponsible **   <a name="API-Type-MembershipJobComputePaymentConfig-isResponsible"></a>
Indicates whether the collaboration member has accepted to pay for job compute costs (`TRUE`) or has not accepted to pay for query and job compute costs (`FALSE`).
There can be one or more members who are designated as payer candidates for queries and jobs.
An error message is returned for the following reasons:
+ If you set the value to `FALSE` but you are responsible to pay for query and job compute costs.
+ If you set the value to `TRUE` but you are not responsible to pay for query and job compute costs.
Type: Boolean
Required: Yes

## See Also
<a name="API_MembershipJobComputePaymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/MembershipJobComputePaymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/MembershipJobComputePaymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/MembershipJobComputePaymentConfig)
