---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_OciIdentityDomain.html
---

# OciIdentityDomain
<a name="API_OciIdentityDomain"></a>

Information about an Oracle Cloud Infrastructure (OCI) identity domain configuration.

## Contents
<a name="API_OciIdentityDomain_Contents"></a>

 ** accountSetupCloudFormationUrl **   <a name="odb-Type-OciIdentityDomain-accountSetupCloudFormationUrl"></a>
The AWS CloudFormation URL for setting up the account integration with the OCI identity domain.
Type: String
Required: No

 ** ociIdentityDomainId **   <a name="odb-Type-OciIdentityDomain-ociIdentityDomainId"></a>
The unique identifier of the OCI identity domain.
Type: String
Required: No

 ** ociIdentityDomainResourceUrl **   <a name="odb-Type-OciIdentityDomain-ociIdentityDomainResourceUrl"></a>
The resource URL for accessing the OCI identity domain.
Type: String
Required: No

 ** ociIdentityDomainUrl **   <a name="odb-Type-OciIdentityDomain-ociIdentityDomainUrl"></a>
The URL of the OCI identity domain.
Type: String
Required: No

 ** status **   <a name="odb-Type-OciIdentityDomain-status"></a>
The current status of the OCI identity domain.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`
Required: No

 ** statusReason **   <a name="odb-Type-OciIdentityDomain-statusReason"></a>
Additional information about the current status of the OCI identity domain, if applicable.
Type: String
Required: No

## See Also
<a name="API_OciIdentityDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/OciIdentityDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/OciIdentityDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/OciIdentityDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
