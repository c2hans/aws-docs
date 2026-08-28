---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ml-best-practices-public-sector-organizations/ml-best-practices-public-sector-organizations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Machine Learning Best Practices for Public Sector Organizations
<a name="ml-best-practices-public-sector-organizations"></a>

Publication date: **September 29, 2021** ([Document history](document-revisions.md))

This whitepaper outlines some of the challenges for US public sector agencies in adoption and implementation of ML, and provides best practices to address these challenges. The target audience for this whitepaper includes executive leaders and agency IT Directors.

## Introduction
<a name="introduction"></a>

 In 2019, the White House issued an executive order promoting the use of trustworthy artificial intelligence (AI) in the federal government. (Source: [https://www.nitrd.gov/pubs/National-AI-RD-Strategy-2019.pdf](https://www.nitrd.gov/pubs/National-AI-RD-Strategy-2019.pdf)) This order launched the American AI Initiative, a concerted effort to promote and protect AI technology and innovation in the United States. This executive order also laid the foundation, with broad guidelines and policies, for agencies on the design, development, acquisition, and the use of AI in government.

 Machine learning (ML) and deep learning (DL) are computer science fields derived from the discipline of AI. Collectively called ML in this whitepaper, these fields help modernize the government and ensure federal agencies are effectively delivering on their mission objectives on behalf of the American people. AI & ML can help government agencies solve complex problems with citizen services, public safety, healthcare, transportation, and other service verticals. To enable these capabilities, agencies are investing in AI & ML solutions, especially to improve mission effectiveness, make evidence-based decisions, and automate repetitive tasks. As an example, in 2018 the Defense Advanced Research Project Agency (DARPA) announced a multi-year investment of more than $2 billion in new and existing programs and called it the “AI Next” campaign. (Source: [https://www.darpa.mil/work-with-us/ai-next-campaign](https://www.darpa.mil/work-with-us/ai-next-campaign)) The National Science Foundation (NSF) invests more than $500 million in AI research annually. (Source: [https://www.nsf.gov/cise/ai.jsp](https://www.nsf.gov/cise/ai.jsp))

 However, several challenges remain within the US public sector regarding the broader adoption of ML initiatives. Organizations have stringent federal, state, and local security and compliance mandates including the Federal Risk and Authorization Management Program (FedRAMP), Department of Defense (DOD) Cloud Computing Security Requirements Guide (CC SRG), and the Health Insurance Portability and Accountability Act (HIPAA), among others. These requirements include protecting sensitive citizen data, isolating environments from internet access, and the principles of least-privilege-access controls. Additionally, the ML lifecycle presents its own challenges in terms of data and model lifecycle management, including the bias within ML models that needs to be addressed to improve the trust with public.

 This whitepaper outlines some of the challenges for US public sector agencies in adoption and implementation of ML, and provides best practices to address these challenges. The target audience for this whitepaper includes executive leaders and agency IT Directors. You can get started on AI and ML by visiting [Machine Learning on AWS](https://aws.amazon.com/machine-learning/), [AWS Machine Learning Embark Program](https://aws.amazon.com/ml-embark/), or the [Amazon Machine Learning Solutions Lab](https://aws.amazon.com/ml-solutions-lab/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
