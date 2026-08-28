---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-mainframe-apps-shared-db2/introduction.html
---

# Replatforming mainframe applications using a shared IBM Db2 for z/OS database for gradual migration
<a name="introduction"></a>

*Luis Gustavo Dantas and Andre Botura, Amazon Web Services*

In the constantly changing landscape of enterprise technology, mainframe modernization has become a critical requirement for organizations that need to remain competitive and agile. This transformation is not merely about replacing old systems with new ones; it's a strategic evolution that bridges the gap between the robust, reliable foundations of the past and the dynamic, innovative possibilities of the future.

The mainframe, which was once the undisputed leader of enterprise computing, is now at a turning point. Its peerless processing power and security features have kept it relevant for decades, but today's businesses require systems that can seamlessly integrate with cloud services, support mobile applications, and harness the power of artificial intelligence and big data analytics.

Modernization doesn't always require a complete migration away from mainframes. Some organizations are opting for hybrid approaches that take advantage of the strengths of both mainframe and cloud environments. This strategy enables them to maintain critical legacy applications while they gradually transition to more modern platforms. This technological transition involves more than just system updates; it requires transforming organizational culture and skills. As companies modernize, they invest in both new technologies and their workforce by bridging generational gaps and promoting ongoing learning and innovation.

This guide discusses a gradual migration strategy that balances the benefits of mainframe systems with the advantages of modern cloud technologies. This phased replatforming approach first migrates the application layer, while maintaining connectivity to your existing IBM Db2 for z/OS database to streamline the transition process and minimize disruptions to your critical business operations while you adopt new capabilities in the cloud.

This guide is designed for technical decision-makers and implementation teams that are involved in mainframe modernization initiatives. Primary audiences include enterprise and solutions architects, technical project managers, and modernization program leaders who need to understand both the strategic and the technical aspects of mainframe replatforming. The content is equally valuable for implementation teams, including mainframe application developers, AWS or cloud engineers, database administrators, and DevOps engineers, who are responsible for executing implementing the modernization.

## Business outcomes
<a name="business-outcomes"></a>

Companies have many compelling reasons to update their legacy applications. This process creates a sense of urgency across industries. When older experts retire, they leave a significant knowledge gap, which makes it crucial to modernize systems before this expertise is lost. Additionally, companies are driven by the need to reduce costs, increase agility, and respond quickly to rapidly changing market conditions.

The push for digital transformation is further intensified by emerging technologies and the demand for enhanced customer experiences. These factors, combined with the risks associated with maintaining complex systems, are prompting organizations to act swiftly in modernizing their IT infrastructure.

Mainframe modernization, in particular, presents a delicate balancing act. Companies must preserve the stability and security that mainframes are known for, while they embrace the flexibility and scalability offered by modern architectures. This process involves complex decisions about which applications to migrate, which to rewrite, and which to retain on the mainframe.

Key drivers for modernization include agility and cost reduction:
+ **Agility and time to market**. Modern systems enable faster procurement processes and quicker responses to changing market demands. The adoption of DevOps and SysOps practices can significantly improve productivity and deployment speeds.
+ **Cost reduction**. Modernization often leads to reduced infrastructure costs through:
  + Pay-as-you-go models, which align costs with actual usage.
  + Reduced licensing fees associated with legacy systems.
  + Improved elasticity, which provides better resource allocation.
  + Active-active, high availability setups, which enhance system resilience while optimizing resource utilization.

Based on these business drivers, COBOL application replatforming is considered a strategic approach to modernization. You can use a shared database to follow a gradual migration path that balances the need for modernization with the imperative to maintain business continuity. This method allows you to capitalize on the benefits of modern architectures while preserving the reliability of your COBOL applications. As a result, you can achieve agility, cost efficiency, and innovation while mitigating the risks that are associated with large-scale, abrupt transitions. The shared Db2 database approach described in this guide provides a bridge between legacy systems and modern platforms, and enables a smoother, more controlled modernization process.

In this guide:
+ [AWS Mainframe Modernization](mainframe-modernization.md)
+ [The transformation process](phases.md)
+ [Best practices](best-practices.md)
+ [Next steps](next-steps.md)
+ [Resources](resources.md)
+ [Document history](doc-history.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
