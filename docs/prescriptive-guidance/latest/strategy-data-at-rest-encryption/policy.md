---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/policy.html
---

# Policy
<a name="policy"></a>

The purpose of an encryption policy is to establish, at a senior management level, the business and compliance expectations that the organization needs to meet. The policy serves as a starting point to define a suitable encryption strategy. The policy should be abstract enough to provide freedom and flexibility for implementation. At the same time, it must be specific enough to define the confines of an acceptable implementation that meets organizational objectives. In general, policies are technology-agnostic and very infrequently changed because they define the fundamental characteristics of your enterprise encryption strategy.

Typically, encryption policies contain, but are not limited to, the following:
+ Any regulatory or compliance regimes that your enterprise must meet
+ Any business commitments or expectations for data encryption
+ The type of data that must be encrypted
+ Criteria for when to use data-protection techniques other than encryption, such as hashing or tokenization

The highest management level of the organization, such as the CIO, CTO, and CISO, usually define and approve the encryption policy.

Consider the following when creating your encryption policy:
+ Your line of business determines the compliance and regulatory regimes you need to adhere to. These regimes dictate the data encryption requirements. Executive-level decisions to expand the business into new regions or expand product offerings can affect which regulations apply for your data. For example, if a bank decides to offer credit cards to its customers, they probably need to be compliant with the [payment card industry Data Security Standard](https://www.pcisecuritystandards.org/document_library/) (PCI-DSS), which requires data encryption.
+ Your policy should specify what type of data needs to be encrypted. This varies based on compliance requirements and the data-handling objectives of your enterprise. For example, your policy might state that any data that the business captures or owns must be encrypted at rest.
+ Your encryption policy must align with your internal data categorization standards. To formulate an effective encryption policy, determination of data categories at the metadata level is required. For example, your categories might include public, internal, confidential, secret, or customer data.
+ Include criteria for how to determine which data should be encrypted and which data should be protected with another technique, such as tokenization or hashing. For example, your policy might state *Any personally identifiable information (PII) that goes to the audit, trace, or application logs must be tokenized*.
