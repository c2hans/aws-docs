---
source_url: https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_CrlDetail.html
---

# CrlDetail
<a name="API_CrlDetail"></a>

The state of the certificate revocation list (CRL) after a read or write operation.

## Contents
<a name="API_CrlDetail_Contents"></a>

 ** createdAt **   <a name="rolesanywhere-Type-CrlDetail-createdAt"></a>
The ISO-8601 timestamp when the certificate revocation list (CRL) was created.
Type: Timestamp
Required: No

 ** crlArn **   <a name="rolesanywhere-Type-CrlDetail-crlArn"></a>
The ARN of the certificate revocation list (CRL).
Type: String
Required: No

 ** crlData **   <a name="rolesanywhere-Type-CrlDetail-crlData"></a>
The state of the certificate revocation list (CRL) after a read or write operation.
Type: Base64-encoded binary data object
Required: No

 ** crlId **   <a name="rolesanywhere-Type-CrlDetail-crlId"></a>
The unique identifier of the certificate revocation list (CRL).
Type: String
Length Constraints: Fixed length of 36.
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`
Required: No

 ** enabled **   <a name="rolesanywhere-Type-CrlDetail-enabled"></a>
Indicates whether the certificate revocation list (CRL) is enabled.
Type: Boolean
Required: No

 ** name **   <a name="rolesanywhere-Type-CrlDetail-name"></a>
The name of the certificate revocation list (CRL).
Type: String
Required: No

 ** trustAnchorArn **   <a name="rolesanywhere-Type-CrlDetail-trustAnchorArn"></a>
The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for.
Type: String
Required: No

 ** updatedAt **   <a name="rolesanywhere-Type-CrlDetail-updatedAt"></a>
The ISO-8601 timestamp when the certificate revocation list (CRL) was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_CrlDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/CrlDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/CrlDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/CrlDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Roles Anywhere. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rolesanywhere` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
