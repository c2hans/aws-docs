---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_AccessRights.html
---

# AccessRights
<a name="API_AccessRights"></a>

 Allow or deny permissions for an Active Directory group to enroll or autoenroll certificates for a template.

## Contents
<a name="API_AccessRights_Contents"></a>

 ** AutoEnroll **   <a name="PcaConnectorAd-Type-AccessRights-AutoEnroll"></a>
Allow or deny an Active Directory group from autoenrolling certificates issued against a template. The Active Directory group must be allowed to enroll to allow autoenrollment
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** Enroll **   <a name="PcaConnectorAd-Type-AccessRights-Enroll"></a>
Allow or deny an Active Directory group from enrolling certificates issued against a template.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

## See Also
<a name="API_AccessRights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/AccessRights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/AccessRights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/AccessRights)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for Active Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-ad` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
