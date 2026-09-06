---
source_url: https://docs.aws.amazon.com/whitepapers/latest/unpicking-vendor-lock-in/six-lock-in-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Six lock-in considerations
<a name="six-lock-in-considerations"></a>

 A CSP should succeed by the breadth, depth, global reach, innovation, agility, reliability, and security of its services. Unless you have access to the broadest range of cloud services, with a CSP that adds new capabilities and services at an accelerating pace, customers risk becoming locked-in to outdated technology. A CSP which is not retaining customer trust through the quality of its services, may tend to lean towards lock-in practices. Following are six lock-in considerations to help you understand what to ask of CSPs, what to avoid, and how to build a plan to switch technology, if desired.

## Minimum commitments or long-term contracts
<a name="minimum-commitments-or-long-term-contracts"></a>

 A CSP should not have *mandatory* minimum commitments, or *mandatory* long-term contracts. Long-term contracts should only be offered as a *choice* for the customer’s convenience, and should typically come with a compensating feature such as reduced pricing or commitment to through-life improvement to the functionality and/or performance of the service.

 Historically, customers have entered into contracts that last years or even decades— with technology often frozen in time for the duration of the contract, inhibiting innovation and experimentation. The key problem when it comes to these commitments or contracts in the cloud, is when they are mandatory. If you want to use cloud as pay-as- you-go, it should be available. Pay-as-you-go pricing with no contractual commitment provides customers with the ability to shut down their environment, export their data and virtual machines (VMs), and walk away without incurring further expense.

 However, customers should still feel free to *choose* a longer-term contract, if that fits their business needs best. Customers should keep in mind that a longer-term contract should provide advantages over and above a pay-as-you-go style contract, whether this is reduced pricing, a commitment to in-contract upgrades or some other factor which benefits your organization. A CSP should give you the freedom to choose whichever pricing and contractual model suits them and their workloads best—this way you can adopt the cloud on your own terms.

## Licensing
<a name="licensing"></a>

 A CSP should provide a range of licensing options for customers. Examples include a marketplace with a curated digital catalog that helps reduce costs by not over- purchasing with an in-perpetuity license, multiple database offerings, robust open-source software support, alternative virtualization environments to support hybrid cloud services, and tools to help you assess and reduce license costs.

 AWS works with independent software vendors (ISVs) who have permitted the use of their product on AWS, enabling customers to bring their own license (BYOL) and apply it to the product on the AWS Cloud—which helps to reduce switching costs when moving away from the AWS Cloud. Additionally, the AWS Marketplace enables you to find, buy, deploy, and manage third-party software and services.

 You can choose a utility pricing model with a support package, which is a pay-as- you-go license in which you do not incur any upfront licensing costs and only pay for the resources you consume. Some ISVs also offer their software as a service and charge a monthly subscription fee. [AWS License Manager](https://aws.amazon.com/license-manager) makes it easier to bring your existing software licenses from vendors such as Microsoft, SAP, Oracle, and IBM to AWS, and centrally manage these licenses across AWS and on-premises environments.

 Alternatively, customers can also consider moving to a fully managed, open-sourced solution. For example, instead of paying long-term contracts and support fees for a commercial messaging broker, you can migrate to the fully managed, industry standards-based Amazon MQ service.

## Data portability
<a name="data-portability"></a>

 A CSP should provide portability tools and services that enable customers to move data as needed on and off a CSPs storage *at any time*.

 Cloud customers need detailed, clear, and transparent information regarding the processes, technical requirements, timeframes, and charges that will be applied should they want to switch to another provider or port data back to their own IT systems. This should also include the processes and locations of any data back-up, available data formats, the required IT configuration, and minimum network bandwidth. CSPs should also confirm the timeframe during which customer data will remain available for porting upon ending a contract.

 The cloud-shared responsibility model is an important factor when it comes to data portability. Some key concepts regarding data ownership and management in the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) include:
+  Customers own their data.
+  Customers have the ability to store content in the format they choose.
+  Customers choose the geographic location(s) in which to store their data, and it doesn’t move unless the customer decides to move it.
+  Customers can download or delete their data whenever they like.

 AWS services are built to support both [data migration into and out of AWS](https://aws.amazon.com/cloud-data-migration/). Additionally, AWS provides many tools and documented techniques to make it easy to do both. Many CSPs offer several tools to help move data between networks and technology partners. AWS services, for example, are built on numerous open standards like SQL, Linux, and Xen. This flexible foundation enables our customers to securely move information in and out of the cloud regardless of where that information is going, such as cloud-to- cloud or cloud-to-data center.

 As a best practice, customers should request that CSPs demo their data portability tools and services as part of a cloud services/CSP evaluation process.

 AWS understands that freedom of choice is a fundamental customer need. As mentioned previously, AWS customers always retain ownership and control of their data, including where it is stored, how it is stored, and who has access. AWS has contributed to industry initiatives such as the code of conduct on [Switching Cloud Provider and Porting Data](https://swipo.eu/) (SWIPO), a multi-stakeholder group facilitated by the European Commission, in order to develop voluntary Codes of Conduct for the proper application of the EU Free Flow of Non-Personal Data Regulation / Article 6 "Porting of Data".

## Application portability
<a name="application-portability"></a>

 To minimize the risk of vendor lock-in, applications should be built or migrated to be as flexible and loosely coupled as possible.

 Mitigating potential switching costs requires good architecture, standard deployment practices, and pre-planning. Your cloud services should be architected with transience in mind.

 There are several ways to improve the portability of your applications:
+  Use Docker containers that can be deployable virtually anywhere; build using microservices to reduce the “blast radius” of changes to parts of your application (enabling the testing of each one independently if you need to make changes on a large scale).
+  Have loosely coupled services, especially when using a service specific to a CSP—building a façade for each CSP service so you can swap it out as transparently as possible.
+  Build your cloud platform on open standards like Xen, SQL, KVM, and Linux.

 Clearly demarcating services’ interdependencies helps to create and maintain a dynamic back-out or reversibility plan. Depending on the level of risk you perceive, you can make this plan more or less detailed. In this plan, you can itemize what the major switching costs would be if you had to leave a CSP, and what steps you will take to manage them. You can also make a high-level project plan for how you would go about moving, as well as estimate these costs.

 Hyperscale CSPs provide standardized services to millions of customers, and these standardized services are used by customers to build their unique cloud environments. A CSP cannot know what a customer environment will look like at any point in time, and a back-out or reversibility plan should not expect this kind of detail from a CSP. Instead, a CSP should provide detailed technical documentation for each of its standardized services, so that customers can use this information to create and maintain their own back-out plans.

 In summary, some important application portability considerations are:
+  Cloud application components should be loosely linked with the application components that interact with them. You can do this by incorporating REST APIs with popular industry standards like HTTP, JSON, and OAuth to abstract your applications from the underlying proprietary cloud infrastructure.
+  Any business logic should be separated from the application logic and be clearly defined and documented. This will avoid the need to decipher business rules in case a migration to a new CSP occurs.
+  DevOps tools are being implemented to maximize code portability. Configuration management tools such as Chef and Puppet help you automate the configuration of the infrastructure on which your apps run. This allows you to deploy your application to diverse IT environments, which can reduce the difficulty of moving to a new CSP. These technologies reduce the lock-in risks that can come from proprietary configurations, and can ease the transition from one CSP to another.
+  Container technology provided by companies such as Docker, Kubernetes, and CoreOS help isolate software from its environment and abstract dependencies away from the cloud provider. Since most CSPs support standard container formats, it should be easy to transfer your application to a new cloud vendor, if necessary.

## Service availability and vendor innovation
<a name="service-availability-and-vendor-innovation"></a>

 In order to justify committing to a CSP, the CSP should be able to demonstrate a proven history of innovation and service availability. If a CSP offers the most innovative, highly available, flexible service on the market, and makes moving away easy and safe; then there’s no reason not to choose their service from a vendor lock-in perspective.

 Vendor lock-in is an important factor, but it’s not the only consideration when adopting new technology. When you move to a CSP, you’re not just solely focused on avoiding vendor lock-in. Ultimately, you want to unlock vendor capabilities and the benefits they bring to your organization. A CSP’s proven pace of innovation reassures customers that the CSP intends to keep winning their business by offering them more service options, with the knowledge that they can move to another cloud provider if they choose.

 AWS gives customers the services and features they want, and avoids locking them in to using services AWS *thinks* they want. The AWS culture of innovation provides customers with the ability to both tap into and influence AWS innovation, and the innovation of third- party services available via the [AWS Partner Network](https://aws.amazon.com/partners/) (APN).

 Unlocking vendor capabilities extends to ensuring that services are available. A CSP can offer peerless services, but if they’re not reliable, you’ll probably want to move to a different CSP that offers reliable services. Availability and reliability are key benefits of the cloud, and CSPs needs to show SLAs that clearly demonstrate the service commitment and compensation terms if those SLAs are not met. Customers can use AWS’s distinct and geographically diverse Regions and Availability Zones (AZs) to protect applications from the failure of a single location. A [2018 IDC study](https://www.synthesis.co.za/wp-content/uploads/2019/02/IDC-Fostering-Business-and-Organizational-Transformation-to-Generate-Business-Value-with-AWS1.pdf) of enterprises that migrated to AWS found that they experienced, on average, 94 percent less downtime as compared to their on-premises environments.

## Cost
<a name="cost"></a>

 CSPs should be able to demonstrate a history of ensuring that operational efficiencies flow down to customers in the form of price reductions.

 If a CSP increases prices, customers think about moving away. If a CSP has a history of increasing prices, it’s likely they will try to make it difficult for their customers to move away by increasing switching costs, often through punitive licensing practices or arbitrary technological barriers.

 AWS operates at a massive scale, offering standardized services in a self-service manner. This low-touch model enables us to focus on innovating on behalf of customers to provide more services, enhance services already available, and find operational efficiencies that can be passed back to customers in the form of price cuts. *AWS has reduced prices 107 times*, largely in the absence of competitive pressure to do so. AWS has tried to make it as easy as possible to leave if you want to, because AWS is confident that AWS services speak for themselves, and that service quality will make customers want to stay with AWS.
