---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/introduction.html
---

# Modernizing manufacturing execution systems (MES) in the AWS Cloud
<a name="introduction"></a>

*Ravi Soni, Steve Blackwell, Nishant Saini, and Pratik Yeole, Amazon Web Services*

Manufacturing execution systems (MES) originated as a set of data collection tools and extensions of planning systems in the 1970s. Over time, they have evolved into a comprehensive software solution for monitoring, tracking, documenting, and controlling production processes that convert raw materials to finished products on the shop floor. MES integrates with existing shop floor systems such as programmable logic controllers (PLCs), supervisory control and data acquisition (SCADA) systems, and historians to enable seamless production control. It also integrates with enterprise systems such as enterprise resource planning (ERP) and product lifecycle management (PLM) systems to enable a seamless flow of information from the enterprise to the shop floor.

With cloud computing, businesses are increasingly looking to migrate MES to the cloud to improve scalability, flexibility, and performance efficiency, and to reduce costs. Additionally, the emergence of Internet of Things (IoT), artificial intelligence and machine learning (AI/ML), and microservices is disrupting the landscape of MES. In addition to hosting traditional, monolithic MES in the cloud, manufacturers and independent software vendors (ISVs) that serve manufacturers now have the option to develop a modular MES by using microservices. Choosing between a conventional monolithic MES or a modern MES can be challenging and requires a thorough analysis of organizational capabilities, budgetary allocations, timeline expectations, and business priorities. A modern, cloud-native, microservice-based MES that uses APIs is the preferred choice for businesses that leverage fourth industrial revolution (Industry 4.0) concepts, because it offers agility, scalability, flexibility, accelerated time to value, and compatibility with IoT.

A modern MES provides several advantages:
+ It supports agile development and supports frequent updates through modifications to specific services instead of affecting the entire application, and adapts to evolving business processes.
+ Microservices provide technological flexibility and accommodate unique requirements through various programming languages, databases, and user interface technologies.
+ It offers scalability, making it suitable for geographically dispersed manufacturers that might have diverse production processes.
+ It enables faster time to market by allowing swift responses to changing customer needs and supply chain disruptions.

By adopting a microservice-based MES, businesses can harness the benefits of Industry 4.0. This guide describes an approach to implementing a microservice-based MES by using AWS services and technologies. This approach involves determining the microservices structure based on the specific business outcomes and selecting the right technologies for each outcome. The guide suggests possible ways of integrating, enhancing, monitoring, and managing those microservices. Microservice-based architectures tend to be operationally complex. Therefore, the guidance also shares best practices and architectural patterns on how manufacturers can simplify the operational governance of the microservice-based MES. It presents the available options and provides direction to decision-makers. The final responsibility for decision-making lies with architects, analysts, and technology leaders, who must determine the most suitable option based on their unique situations, expected business outcomes, and available resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
