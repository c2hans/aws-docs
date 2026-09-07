---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-semicon-workloads/securing-collaboration-with-third-parties.html
---

# Securing engineering collaboration with third parties
<a name="securing-collaboration-with-third-parties"></a>

Collaboration with third parties is essential during development in order to debug tool problems, get help with IP integration for designs, and to bring in external contractors with specialized skills. It can be difficult to provide secure access to third parties from on-premises infrastructure. By using AWS infrastructure as code (IaC), you can create a copy of your primary secure development environment, called a *collaboration chamber*. To help prevent data exfiltration, tighten the security posture of a collaboration chamber by not allowing access to the internet. A collaboration chamber has accounts for the collaborators, and you can curate the data, tools, and infrastructure in the chamber to include only what is required for the collaboration. When the collaboration is done, delete the collaboration chamber in order to reduce costs and to remove any potential access to the data. The following diagram shows how different participants in the design and manufacturing process might use various types of collaboration chambers.

![Diagram of connections between collaboration chambers for semiconductor workloads running on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-semicon-workloads/images/guide-img/f421e0e1-7aa6-442a-ac92-5451f69fd602/images/37acbc68-d238-412a-b6b9-83028b06dbf6.png)

The following image is a reference architecture for a collaboration chamber. This architecture can be used as reference when designing and building a collaboration chamber on AWS. The AWS security, governance, and monitoring services in the diagram help secure the chamber in order to protect IP. For more information about these services, see [AWS security services for semiconductor development environments](aws-security-services.md) in this guide.

![Diagram of a collaboration chamber in the AWS Cloud with access from the on-premises network](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-semicon-workloads/images/guide-img/f421e0e1-7aa6-442a-ac92-5451f69fd602/images/fbf30cad-6125-4c53-aace-8b7472455b66.png)
