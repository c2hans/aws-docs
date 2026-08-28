---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ServiceSummary.html
---

# ServiceSummary
<a name="API_ServiceSummary"></a>

Summary information about a service.

## Contents
<a name="API_ServiceSummary_Contents"></a>

 ** arn **   <a name="vpclattice-Type-ServiceSummary-arn"></a>
The Amazon Resource Name (ARN) of the service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}`
Required: No

 ** createdAt **   <a name="vpclattice-Type-ServiceSummary-createdAt"></a>
The date and time that the service was created, in ISO-8601 format.
Type: Timestamp
Required: No

 ** customDomainName **   <a name="vpclattice-Type-ServiceSummary-customDomainName"></a>
The custom domain name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: No

 ** dnsEntry **   <a name="vpclattice-Type-ServiceSummary-dnsEntry"></a>
The DNS information.
Type: [DnsEntry](API_DnsEntry.md) object
Required: No

 ** id **   <a name="vpclattice-Type-ServiceSummary-id"></a>
The ID of the service.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `svc-[0-9a-z]{17}`
Required: No

 ** lastUpdatedAt **   <a name="vpclattice-Type-ServiceSummary-lastUpdatedAt"></a>
The date and time that the service was last updated, in ISO-8601 format.
Type: Timestamp
Required: No

 ** name **   <a name="vpclattice-Type-ServiceSummary-name"></a>
The name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!svc-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: No

 ** status **   <a name="vpclattice-Type-ServiceSummary-status"></a>
The status.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`
Required: No

## See Also
<a name="API_ServiceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ServiceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ServiceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ServiceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
