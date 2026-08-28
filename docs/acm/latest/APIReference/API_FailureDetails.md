---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_FailureDetails.html
---

# FailureDetails
<a name="API_FailureDetails"></a>

Contains details about a failure.

## Contents
<a name="API_FailureDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Message **   <a name="ACM-Type-FailureDetails-Message"></a>
A message describing the failure.
Type: String
Required: No

 ** Reason **   <a name="ACM-Type-FailureDetails-Reason"></a>
The reason for the failure.
Type: String
Valid Values: `ACCESS_DENIED | DOMAIN_MISMATCH | DOMAIN_NOT_ALLOWED | ENDPOINT_NOT_ACTIVE | HOSTED_ZONE_NOT_FOUND | INTERNAL_FAILURE | INVALID_CHANGE_BATCH | INVALID_PUBLIC_DOMAIN | TIMED_OUT`
Required: No

## See Also
<a name="API_FailureDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/FailureDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/FailureDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/FailureDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
