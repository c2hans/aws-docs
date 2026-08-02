---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeInfo.html
---

# ChangeInfo
<a name="API_ChangeInfo"></a>

A complex type that describes change information about changes made to your hosted zone.

## Contents
<a name="API_ChangeInfo_Contents"></a>

 ** Id **   <a name="Route53-Type-ChangeInfo-Id"></a>
This element contains an ID that you use when performing a [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) action to get detailed information about the change.
Type: String
Length Constraints: Maximum length of 32.
Required: Yes

 ** Status **   <a name="Route53-Type-ChangeInfo-Status"></a>
The current state of the request. `PENDING` indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.
Type: String
Valid Values: `PENDING | INSYNC`
Required: Yes

 ** SubmittedAt **   <a name="Route53-Type-ChangeInfo-SubmittedAt"></a>
The date and time that the change request was submitted in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) and Coordinated Universal Time (UTC). For example, the value `2017-03-27T17:48:16.751Z` represents March 27, 2017 at 17:48:16.751 UTC.
Type: Timestamp
Required: Yes

 ** Comment **   <a name="Route53-Type-ChangeInfo-Comment"></a>
A comment you can provide.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_ChangeInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ChangeInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ChangeInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ChangeInfo)
