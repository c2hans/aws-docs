---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/hybrid-connectivity-type-and-design-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hybrid connectivity type and design considerations
<a name="hybrid-connectivity-type-and-design-considerations"></a>

 This section of the whitepaper covers the considerations that affect your choices when selecting a hybrid network to connect your on-premises environments to AWS. It follows a logical thought process to support you selecting an optimal hybrid connectivity solution. The considerations affecting your design are categorized into considerations that impact your *connectivity type*, and considerations that affect your *connectivity design*. Connectivity type considerations will support you deciding between using an internet-based VPN or Direct Connect. Connectivity design considerations will support you deciding how to set up the connections.

 The following considerations that impact your *connectivity type* are covered: time to deploy, security, SLA, performance, and cost. After reviewing those considerations, and how they affect your design choices, you will be able to decide if using an internet-based connection or Direct Connect is recommended to meet your requirements.

 The following considerations that impact your *connectivity design* are covered: scalability, communication model, reliability, and third-party SD-WAN integration. After reviewing those considerations, and how they affect your design choices, you will be able to decide the optimal logical design recommended to meet your requirements.

 The following structure is used to discuss and analyze each of the selection and design considerations:
+  **Definition** - Brief definition of what is the consideration.
+  **Key questions** - Provides a set of questions to enable you to collect the requirements associated with the consideration.
+  **Capabilities to consider** - Solutions to address the requirements associated with the consideration.
+  **Decision tree** - For some considerations or a group of considerations, a decision tree is provided to help you select the optimal hybrid network solution.

 The considerations affecting your hybrid network design are covered in an order where the output of one consideration is part of the input for the subsequent consideration. As illustrated in Figure 2, the first step is to decide on the connectivity type, followed by refining it with the design selection considerations.

 Figure 2 demonstrates the two consideration categories, the individual considerations, and the logical order in which the considerations are covered in the subsequent sub-sections. Those are the essential considerations when making a hybrid network design decision. If the targeted design does not require all these considerations, you can focus on the considerations that apply to your requirements.

![Diagram showing consideration categories, individual considerations, and the logical order between them](http://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/images/consideration-categories.png)
