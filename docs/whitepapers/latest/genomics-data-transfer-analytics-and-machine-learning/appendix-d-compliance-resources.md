---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/appendix-d-compliance-resources.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix D: Compliance resources
<a name="appendix-d-compliance-resources"></a>

 Genomics data is generally considered the most private of personal data. From a regulatory perspective it is certainly considered [Protected Health Information](https://www.hhs.gov/hipaa/for-professionals/faq/354/does-hipaa-protect-genetic-information/index.html) (PHI) or a special class of [Personal Data](https://gdpr-info.eu/recitals/no-34/).

 Privacy, reliability, and security must be kept in mind at every stage, from data creation, collection and processing, to storage and transfer. Customers need to have a solid understanding of regulatory privacy requirements, for example, GINA, HIPAA, the EU’s GDPR or local equivalents, and comply with them at every stage of data handling.

 Although customers are ultimately accountable for their own regulatory compliance, AWS does take steps to help.

 In the case of [Health Insurance Portability and Accountability Act](https://www.hhs.gov/hipaa/for-professionals/index.html) of 1996 (HIPAA) in the US, cloud service providers (CSPs) such as AWS are considered business associates. For customers subject to this regulation, the [Business Associate Agreement (BAA)](https://aws.amazon.com/artifact/getting-started/) is an AWS contract that is required under HIPAA rules to ensure that AWS appropriately safeguards protected health information (PHI). Customers who execute an AWS BAA may use any AWS service in an account designated as a HIPAA Account, but they may only process, store, and transmit PHI using the HIPAA-eligible services defined in the AWS BAA. For the latest list of HIPAA-eligible AWS services, see the [HIPAA Eligible Services Reference](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/) webpage. Throughout this whitepaper we have used HIPAA-eligible services.

 Additional relevant US regulations include:
+  [Genetic Information Nondiscrimination Act of 2008](http://www.gpo.gov/fdsys/pkg/PLAW-110publ233/pdf/PLAW-110publ233.pdf) (GINA). GINA was used to modify the HIPAA Privacy Rule to strengthen the privacy protections for genetic information by implementing section 105 of Title I of the Genetic Information Nondiscrimination Act of 2008 (GINA) [1](https://www.hhs.gov/hipaa/for-professionals/faq/354/does-hipaa-protect-genetic-information/index.html).
+  [Health Information Technology for Economic and Clinical Health Act](https://www.healthit.gov/topic/laws-regulation-and-policy/health-it-legislation) (HITECH)
+  [The Health Information Trust Alliance](https://hitrustalliance.net/hitrust-framework) (HITRUST) Common Security Framework (CSF)

 For more information about AWS’ compliance programs for HIPAA, HITECH and HITRUST, refer to the [HIPAA compliance program](https://aws.amazon.com/compliance/hipaa-compliance/) webpage.

 As for EU regulations, AWS acts as both a data processor and a data controller under the GDPR which clearly states in [recital 34](https://gdpr-info.eu/recitals/no-34/) that genetics data is considered personal data. Under the shared responsibility model, AWS is responsible for securing the underlying infrastructure that supports the cloud, and customers and APN partners, acting either as data controllers or data processors, are responsible for any personal data they put on the cloud.

 We can confirm that all AWS services can be used in compliance with the GDPR. This means that, in addition to benefiting from all of the measures that AWS already takes to maintain services security, customers can deploy AWS services as a key part of their GDPR compliance plans. For more details, see our GDPR services readiness announcement in the [AWS Security Blog](https://aws.amazon.com/blogs/security/all-aws-services-gdpr-ready/).

 For further information about AWS’ compliance program for GDPR, refer to the [GDPR compliance program](https://aws.amazon.com/compliance/gdpr-center/) webpage.

 Depending on where the genomics data is used in the customers business, from drug discovery to clinical trial patient recruitment, GxP regulations may apply. In particular, Title 21 CFR part 11 in the US or Eudralex volume 4 Annex 11 in the EU.

 For further information about AWS’ compliance program for GxP, refer to the [GxP compliance program](https://aws.amazon.com/compliance/gxp-part-11-annex-11/) webpage.

 For further information about any of the numerous AWS compliance programs, refer to the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) webpage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
