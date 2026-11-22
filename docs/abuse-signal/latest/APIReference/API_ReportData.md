---
source_url: https://docs.aws.amazon.com/abuse-signal/latest/APIReference/API_ReportData.html
---

# ReportData

The abuse report data in XARF format. This is a union type, so exactly one member must be specified.

## Contents
<a name="API_ReportData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** xarf **   <a name="abusesignal-Type-ReportData-xarf"></a>
A JSON object that conforms to the XARF v4 specification. At a minimum, the document must include the XARF core fields, including the required `category` and `type` fields that classify the report (for example, `category` `content` with `type` `phishing`). For the XARF core fields and detailed schema definitions of each report type, see the [XARF v4 Technical Specification on the XARF website](https://xarf.org/docs/specification/).
Never include images, video, or copies of child sexual abuse or child sexual exploitation material in a report, in any field and for any report type. Send URLs, hash values, and reference identifiers only.
If you suspect that content or activity is illegal, use the XARF `description` field to explain why and name the laws concerned.
 **Testing your integration**
To test your integration, add the tag `lifecycle:test` to the report. AWS validates test reports and returns a report ID and status in the same way as other reports, but doesn't process them as abuse reports. AWS deletes test reports shortly after submission.
Use test values only, such as example.com and the IP address ranges reserved for documentation (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24). Don't add this tag to a real abuse report.
Tag keys that begin with `aws:` are reserved.
Type: JSON value
Required: No

## See Also
<a name="API_ReportData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/abuse-signal-2026-01-12/ReportData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/abuse-signal-2026-01-12/ReportData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/abuse-signal-2026-01-12/ReportData)
