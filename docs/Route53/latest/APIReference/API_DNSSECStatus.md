---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_DNSSECStatus.html
---

# DNSSECStatus
<a name="API_DNSSECStatus"></a>

A string representing the status of DNSSEC signing.

## Contents
<a name="API_DNSSECStatus_Contents"></a>

 ** ServeSignature **   <a name="Route53-Type-DNSSECStatus-ServeSignature"></a>
A string that represents the current hosted zone signing status.
Status can have one of the following values:
SIGNING
DNSSEC signing is enabled for the hosted zone.
NOT\_SIGNING
DNSSEC signing is not enabled for the hosted zone.
DELETING
DNSSEC signing is in the process of being removed for the hosted zone.
ACTION\_NEEDED
There is a problem with signing in the hosted zone that requires you to take action to resolve. For example, the customer managed key might have been deleted, or the permissions for the customer managed key might have been changed.
INTERNAL\_FAILURE
There was an error during a request. Before you can continue to work with DNSSEC signing, including with key-signing keys (KSKs), you must correct the problem by enabling or disabling DNSSEC signing for the hosted zone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** StatusMessage **   <a name="Route53-Type-DNSSECStatus-StatusMessage"></a>
The status message provided for the following DNSSEC signing status: `INTERNAL_FAILURE`. The status message includes information about what the problem might be and steps that you can take to correct the issue.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

## See Also
<a name="API_DNSSECStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/DNSSECStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/DNSSECStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/DNSSECStatus)
