---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_CertificateFilterStatement.html
---

# CertificateFilterStatement
<a name="API_CertificateFilterStatement"></a>

A filter statement used to search for certificates. Can contain AND, OR, NOT logical operators or a single filter.

## Contents
<a name="API_CertificateFilterStatement_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** And **   <a name="ACM-Type-CertificateFilterStatement-And"></a>
A list of filter statements that must all be true.
Type: Array of [CertificateFilterStatement](#API_CertificateFilterStatement) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: No

 ** Filter **   <a name="ACM-Type-CertificateFilterStatement-Filter"></a>
A single certificate filter.
Type: [CertificateFilter](API_CertificateFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Not **   <a name="ACM-Type-CertificateFilterStatement-Not"></a>
A filter statement that must not be true.
Type: [CertificateFilterStatement](#API_CertificateFilterStatement) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Or **   <a name="ACM-Type-CertificateFilterStatement-Or"></a>
A list of filter statements where at least one must be true.
Type: Array of [CertificateFilterStatement](#API_CertificateFilterStatement) objects
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Required: No

## See Also
<a name="API_CertificateFilterStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/CertificateFilterStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/CertificateFilterStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/CertificateFilterStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
