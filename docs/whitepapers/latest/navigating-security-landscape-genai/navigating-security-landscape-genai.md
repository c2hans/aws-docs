---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-security-landscape-genai/navigating-security-landscape-genai.html
---

# Navigating the security landscape of generative AI
<a name="navigating-security-landscape-genai"></a>

Publication date: **April 8, 2025** ([Document history](doc-history.md))

 Generative artificial intelligence, specifically large language models (LLMs), is reshaping how organizations handle data, automate processes, and drive innovation. However, as these capabilities expand, they also expand current security risks and introduce new ones. Security frameworks and teams need to account for the new challenges that generative AI brings, such as context window overflow, agent mismanagement, and indirect prompt injections. As generative AI becomes a core technology within organizations, we also need to ensure that it's held to the same standard and compliance requirements as other technologies. Organizations that learn to take an agile approach to security will be well positioned in the marketplace as adoption of AI grows. This white paper provides an approach for CISOs to navigate these risks, offering detailed mitigation strategies, including enhanced input validation, real-time monitoring, and modular system architecture. We focused on eight initial threat vectors and have suggested mitigation strategies for each.

 We view a strong security foundation as an accelerant to adopting generative AI that enables organizations to safely and confidently add it to their mix of technologies. While many current technologies can also help tighten security, generative AI brings a few additional nuances that must be addressed and are novel to security. Many of the recommendations in this paper are easier said than done, but augmenting technologies, both from AWS and our partners, are evolving to help address those gaps and should be considered.

 Finally, this paper is intended to complement, and potentially reinforce, newly emerging generative AI security strategies such as OWASP Top 10 for LLM, MITRE ATLAS, and so on. AWS continues to participate in global standards bodies such as the [Coalition for Secure AI (CoSAI)](https://www.coalitionforsecureai.org/), [Frontier Model Forum](https://www.frontiermodelforum.org/), and more to provide insights.

 The following challenges represent a prescriptive point of view from the AWS proactive security team.
