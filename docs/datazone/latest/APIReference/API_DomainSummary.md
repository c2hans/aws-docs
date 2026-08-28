---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DomainSummary.html
---

# DomainSummary
<a name="API_DomainSummary"></a>

A summary of a Amazon DataZone domain.

## Contents
<a name="API_DomainSummary_Contents"></a>

 ** arn **   <a name="datazone-Type-DomainSummary-arn"></a>
The ARN of the Amazon DataZone domain.
Type: String
Required: Yes

 ** createdAt **   <a name="datazone-Type-DomainSummary-createdAt"></a>
A timestamp of when a Amazon DataZone domain was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="datazone-Type-DomainSummary-id"></a>
The ID of the Amazon DataZone domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** managedAccountId **   <a name="datazone-Type-DomainSummary-managedAccountId"></a>
The identifier of the AWS account that manages the domain.
Type: String
Required: Yes

 ** name **   <a name="datazone-Type-DomainSummary-name"></a>
A name of an Amazon DataZone domain.
Type: String
Required: Yes

 ** status **   <a name="datazone-Type-DomainSummary-status"></a>
The status of the Amazon DataZone domain.
Type: String
Valid Values: `CREATING | AVAILABLE | CREATION_FAILED | DELETING | DELETED | DELETION_FAILED`
Required: Yes

 ** description **   <a name="datazone-Type-DomainSummary-description"></a>
A description of an Amazon DataZone domain.
Type: String
Required: No

 ** domainVersion **   <a name="datazone-Type-DomainSummary-domainVersion"></a>
The domain version.
Type: String
Valid Values: `V1 | V2`
Required: No

 ** lastUpdatedAt **   <a name="datazone-Type-DomainSummary-lastUpdatedAt"></a>
A timestamp of when a Amazon DataZone domain was last updated.
Type: Timestamp
Required: No

 ** portalUrl **   <a name="datazone-Type-DomainSummary-portalUrl"></a>
The data portal URL for the Amazon DataZone domain.
Type: String
Required: No

## See Also
<a name="API_DomainSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DomainSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DomainSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DomainSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
