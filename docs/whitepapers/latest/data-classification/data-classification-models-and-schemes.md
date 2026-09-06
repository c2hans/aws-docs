---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification-models-and-schemes.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data classification models and schemes
<a name="data-classification-models-and-schemes"></a>

 Classification models and schemes can be divided into government classification schemes, and commercial classification schemes. Government classification schemes provide a set standard based on laws, policies, and executive directives. Commercial classification schemes, on the other hand, are less standardized and depend on the respective organizational need for protection of data with varying levels of sensitivity, as well as the need to meet compliance and regulatory requirements.

The city of Washington, D.C. implemented a new data policy in 2017 focused on being more transparent, while still protecting sensitive data. While Washington D.C. implemented a five-tier model, these tiers can align with other widely-adopted three-tier classification schemes used in [cloud accreditation regimes](https://octo.dc.gov/page/district-columbia-data-policy).
+  **Level 0** — **Open Data**. Data readily available to the public on open government websites and datasets.
+ **Level 1** — **Public Data, Not Proactively Released**. Data not protected from public disclosure or subject to withholding under any law, regulation, or contract. Publication of the data on the public Internet would have the potential to jeopardize the safety, privacy, or security of anyone identified in the information.
+  **Level 2** — **For District Government Use**. Data that is not highly sensitive and may be distributed within the government without restriction by law, regulation, or contract. It is primarily daily government business operations data.
+  **Level 3** — **Confidential**. Data protected from disclosure by law, regulation, or contract and that is either highly sensitive or is lawfully, or contractually restricted from disclosure to other public bodies. This includes privacy-related data (such as PII, PHI, payment card industry data security standard (PCI DSS), federal tax information (FTI), and so on.
+  **Level 4** — **Restricted Confidential**. Data that unauthorized disclosure could potentially cause major damage or injury, including death to those identified in the information, or otherwise significantly impair the ability of the agency to perform its statutory functions.

## U.S. national classification scheme
<a name="u.s.-national-classification-scheme"></a>

 The U.S. government uses a three-tier classification scheme for national security information as described in Executive Order 135261. This scheme is focused on handling instructions based on potential impact to national security if it is disclosed (confidentiality).

1.  **Confidential** — Information where unauthorized disclosure reasonably could be expected to cause damage to national security.

1.  **Secret** — Information where unauthorized disclosure reasonably could be expected to cause serious damage to national security.

1.  **Top Secret** — Information where unauthorized disclosure reasonably could be expected to cause exceptionally grave damage to national security.

 Within these classification tiers, there are also secondary labels that can be applied that give origination information and can modify the handling instructions. The U.S. also uses the term *unclassified data* to refer to any data that is not classified under the three classification levels. Even with unclassified data, there is the potential use of secondary labels for sensitive information, such as For Official Use Only (FOUO) and Controlled Unclassified Information (CUI) that restrict disclosure to the public or unauthorized personnel.

## U.S. information categorization scheme
<a name="u.s.-information-categorization-scheme"></a>

 Due to the targeted focus of the U.S. classification system and to address additional risks to information beyond confidentiality, NIST developed a three-tiered categorization scheme based on the potential impact to the confidentiality, integrity, and availability of information and information systems applicable to an organization’s mission. Most of the data processed and stored by public sector organizations can be categorized into the following:
+  **Low** — Limited adverse effect on organization operations, organization assets, or individuals.
+  **Moderate** — Serious adverse effect on organization operations, organization assets, or individuals.
+  **High** — Severe or catastrophic adverse effect on organization operations, organization assets, or individuals.

 According to [Fiscal Year 2015 data](https://www.gao.gov/assets/710/700588.pdf), U.S. federal departments and agencies categorized 88 percent of their systems into the low and moderate categories. AWS has Regions and services that are accredited to support these types of data categories and classifications.

## United Kingdom (UK) government
<a name="united-kingdom-uk-government"></a>

 In 2014, the UK simplified its data classification scheme by reducing the levels from six to three. They are:

1.  **Official** — Routine business operations and services, some of which could have damaging consequences if lost, stolen, or published in the media, but none of which is subject to a heightened threat profile.

1.  **Secret** — Very sensitive information that justifies heightened protective measures to defend against determined and highly capable threat actors (e.g., compromise could significantly damage military capabilities, international relations, or the investigation of serious organized crime).

1.  **Top Secret** — Most sensitive information requiring the highest levels of protection from the most serious threats (such as compromise could cause widespread loss of life or could threaten the security or economic well-being of the country or friendly nations).

 According to a cabinet office core briefing in 2013, the UK government categorized approximately 90 percent of its data as *Official*, which serves as the basic level of data classification.. The UK uses a flexible, de-centralized accreditation approach where individual agencies determine the cloud services suitable for *Official* data based on a cloud service provider’s (CSP’s) security assurance against [14 cloud security principles](https://www.ncsc.gov.uk/collection/cloud-security?curPage=/collection/cloud-security/implementing-the-cloud-security-principles). Most UK government agencies have determined that it is appropriate to use reputable, hyper-scale CSPs when running workloads with *Official* data.

## Commercial data classification scheme
<a name="commercial-data-classification-scheme"></a>

 In contrast to government classification schemes that provide a set of standards based on laws, policies, and executive directives, classification schemes used in commercial and non-government organizations are more individual to the organization and the sensitivity of the data. A commercial classification scheme can range from a simple two-tiered approach with public and confidential data to a more granular approach (refer to the following table).

 There is no single formula for creating a commercial data classification scheme. Organizations should consider the individual need for protection of proprietary, business, or user data with varying levels of sensitivity, the need to meet compliance and regulatory requirements, and the possibility to align with [cloud security best practices](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-protection.html) when creating a scheme and the process for classification. The scheme should enable categorization of organizational data based on criticality and sensitivity in order to help determining appropriate protection and retention controls.

 For example, under certain conditions GDPR grants rights such as the *Right to be Forgotten*, the *Right to Know*, and the *Right to Data Portability*. To implement these rights organizations may seek to understand their data, especially how it is categorized and where it lives.

 The GDPR itself considers different categories of data: personal data, special categories of personal data, publicly available data (that contains personal data), and non-personal data. Non-personal data is not covered by GDPR, while certain special categories of personal data (such as health data) are considered very sensitive and require more protection. Therefore, organizations should consider implementing a classification scheme and process to help comply with regulatory obligations, and help prevent mishandling of data. Additional background on GDPR is provided in AWS whitepaper [Navigating GDPR Compliance on AWS](https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/welcome.html).

* Table 1 — Five-tiered commercial data classification approach according to the book [CISSP Security Management and Practices](https://www.pearsonitcertification.com/articles/article.aspx?p=30287&seqNum=9) *

|  Classification  |  Description  |
| --- | --- |
|  Sensitive  |  Data that is to have the most limited access and requires a high degree of integrity. This is typically data that will do the most damage to the organization should it be disclosed.  |
|  Confidential  |  Data that might be less restrictive within the company but might cause damage if disclosed.  |
|  Private  |  Private data is usually compartmental data that might not do the company damage but must be kept private for other reasons. Human resources data is one example of data that can be classified as private.  |
|  Proprietary  |  Proprietary data is data that is disclosed outside the company on a limited basis or contains information that could reduce the company's competitive advantage, such as the technical specifications of a new product.  |
|  Public  |  Public data is the least sensitive data used by the company and would cause the least harm if disclosed. This could be anything from data used for marketing to the number of employees in the company.  |

## Industry-specific approaches
<a name="industry-specific-approaches"></a>

 This section identifies industry-specific examples for data classification, which may include sector-specific requirements. As mentioned earlier, different data types (such as government, financial, and healthcare data) may require additional considerations for tiers and secondary labels to address different handling procedures. Regardless of data belonging to public or commercial entities, customers must conduct the due diligence of adhering to local compliance and regulatory requirements.

 The following chart contains examples of data classification schemes in practice today, descriptions of what can be included in that category based on tier, and examples of workload types for a particular tier.

### Example 1
<a name="example-1"></a>

* Table 2 — Data classification – public sector*

|  Data classification  |  Examples of workloads  |
| --- | --- |
|  Tier 3 – Government confidential and above-sensitive data  |  -National security and defense information <br /> -Government intelligence information <br /> -Law enforcement information <br /> -Government program monitoring or oversight investigations information  |
|  Tier 2 – Restricted  |  -Personally, identifying information about individuals <br /> -Human Resources Management <br /> -Personal profile information <br /> -Aggregated financial or market data  |
|  Tier 1 – Public data  |  -Marketing or promotional information <br /> -Information related to other general government administrative or program activities <br /> -Intra-agency workplace policy development and management  |

### Example 2
<a name="example-2"></a>

* Table 3 — Data classification – enterprises *

|   Data   classification   |  Examples  |
| --- | --- |
|  Tier 3 – Highly Strategic  |  Highly sensitive trade secret and material confidential business information (such as certain pricing, merger and acquisition information, marketing plan, proprietary processes, marketing plans, new product designs, inventions prior to a patent application or held as trade secret) the public disclosure of which could be expected to cause severe or catastrophic legal, financial or reputational damage.  |
|  Tier 2 – Restricted  |  -Most material and non-material business data (such as email, sales and marketing account data, signed contracts, receipts) <br /> -Information required by law to be protected from unauthorized disclosure <br /> -Employee HR records (including employee disciplinary reports)  |
|  Tier 1 – Protected data  |  -CRM systems <br /> -Vendor bank account numbers and payment instructions <br /> -Information that is available only to a specific group of the company’s employees for the purpose of conducting business <br /> -Information for internal use only  |

## AWS recommendations
<a name="aws-recommendations"></a>

 In most cases, AWS recommends starting with a three-tiered data classification approach (refer to the following table), which has been shown by public and commercial organizations that have adopted the AWS cloud, to sufficiently meet their data classification needs and requirements. As an example, the table below includes three tiers, and a naming convention for each tier. For organizations that have more complex data environments or varied data types, secondary labeling is helpful without adding complexity with more tiers. AWS recommends using the minimal number of tiers that make sense for the organization.

* Table 4 — Three-tiered data classification approach *

|  Data classification  |  System security categorization  |  Cloud deployment model options  |
| --- | --- | --- |
|  Unclassified  |  Low to High  |  Accredited public cloud  |
|  Official  |  Moderate to High  |  Accredited public cloud  |
|  Secret and above  |  Moderate to High  |  Accredited private/hybrid/community cloud/public cloud  |

 **Data residency consideration** — AWS encourages customers to assess their data classification approach and hone in on which data needs to stay within their country or region, and why. By doing so, customers may find that their data, potentially even sensitive and critical data, may be stored and/or replicated elsewhere if there is no particular law or policy requiring geographic restrictions. The ability to failover to another region can help further reduce risk of loss in the event of a disaster and provide access to technologies and capabilities that may not be available in their area. Learn more in the AWS [Data Residency](https://d1.awsstatic.com/whitepapers/compliance/Data_Residency_Whitepaper.pdf) whitepaper.

 The NIST data classification scheme is widely recognized as adequate classification scheme in sector-specific, national, and international certifications. In fact, governments such as the Philippines and Indonesia are evaluating and adopting data classification schemes that apply similar principles as the US (like NIST) and UK models. However, organizations are best positioned to develop their own classification schemes based on organizational and risk management needs. Organizations seeking to move away from complex, burdensome tiered schemes can run risk impact assessments to evaluate whether a simpler scheme, such as the three-tiered model, would more effectively meet their management and classification needs.

 Organizations should select the appropriate cloud deployment model according to their specific needs, the type of data they handle, and assessed risk. Depending on the classification of the data, they will need to apply the relevant security controls (such as encryption) within their cloud environment.

 When assessing risk and determining security controls, it is important to understand how cloud services differ from on-premises systems, alternate controls to consider as compared to traditional IT implementation, and the differences in implementation of controls (such as the shared responsibility model).

 When organizations have fully evaluated the commercial cloud with its numerous security benefits (such as the potential for improved availability, resiliency, visibility and automation, and a continually audited infrastructure), they may find that the vast majority of their workloads can be deployed in the cloud with due regard to a data classification scheme, similar to what the US and UK governments have done.

 Globally, public sector organizations are increasingly using the native security benefits of the commercial cloud, and taking steps to help them meet their security and compliance requirements through appropriate data classification and implementation of security controls.

 When organizations have fully evaluated the commercial cloud with its numerous security benefits, they may find that the vast majority of their workloads can be deployed in the cloud with due regard to a data classification scheme, similar to what the US and UK governments have done.
