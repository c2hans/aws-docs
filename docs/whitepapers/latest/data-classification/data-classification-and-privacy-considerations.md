---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification-and-privacy-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data classification and privacy considerations
<a name="data-classification-and-privacy-considerations"></a>

 Data classification is particularly important as new global privacy laws and regulations provide consumers with rights to access, deletion, and other controls over personal data.

 At the time of this writing, according to the [United Nations Conference on Trade and Development](https://unctad.org/page/data-protection-and-privacy-legislation-worldwide) (UNCTAD) 71% of the world’s countries have data protection and privacy legislation in place while 9% have a draft legislation in progress.

 For example, under the European Union’s [General Data Protection Regulation](https://gdpr.eu/tag/gdpr/) (GDPR), certain organizations are required to respond to certain consumer requests within a month of receipt. Similarly, acts such as the [California Consumer Protection Act](https://oag.ca.gov/privacy/ccpa) (CCPA) and [Health Insurance Portability and Accountability Act](https://www.hhs.gov/hipaa/index.html) (HIPAA) gives patients and consumers the right to control how their Personally Identifiable Information (PII) and Protected Health Information (PHI) is handled.

 To respond appropriately, organizations must generally verify a requester’s identity, locate the requestor’s personal data, ensure the data returned only contains the requestor’s personal data, and possibly refuse a request if it’s inconsistent with applicable law.

 Organizations that adopt strong data classification policies are better positioned to provide timely responses to these requests. A data classification framework along with proper tagging and labeling will help protect this personal data. Secondary labels can be used within a classification tier to assist with the tagging and discovery of relevant privacy data. This allows an organization to quickly address issues as they arise. Such additional mechanisms also aid in traceability and access monitoring of sensitive data sets.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
