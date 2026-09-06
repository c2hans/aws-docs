---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_DnsRecord.html
---

# DnsRecord
<a name="API_DnsRecord"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

A DNS record uploaded to your DNS provider.

## Contents
<a name="API_DnsRecord_Contents"></a>

 ** Hostname **   <a name="workmail-Type-DnsRecord-Hostname"></a>
The DNS hostname.- For example, `domain.example.com`.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Type **   <a name="workmail-Type-DnsRecord-Type"></a>
The RFC 1035 record type. Possible values: `CNAME`, `A`, `MX`.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Value **   <a name="workmail-Type-DnsRecord-Value"></a>
The value returned by the DNS for a query to that hostname and record type.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_DnsRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/DnsRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/DnsRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/DnsRecord)
