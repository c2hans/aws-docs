---
source_url: https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/the-challenge-of-software-delivery.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# The challenge of software delivery
<a name="the-challenge-of-software-delivery"></a>

Enterprises today face the challenges of rapidly changing competitive landscapes, evolving security requirements, and performance scalability. Enterprises must bridge the gap between operations stability and rapid feature development. Continuous integration and continuous delivery (CI/CD) are practices that enable rapid software changes while maintaining system stability and security.

 Amazon realized early on that the business needs of delivering features for [Amazon.com](http://Amazon.com) retail customers, Amazon subsidiaries, and Amazon Web Services (AWS) would require new and innovative ways of delivering software. At the scale of a company like Amazon, thousands of independent software teams must be able to work in parallel to deliver software quickly, securely, reliably, and with zero tolerance for outages.

 By learning how to deliver software at high velocity, Amazon and other forward-thinking organizations pioneered [DevOps](https://aws.amazon.com/devops/what-is-devops/) . DevOps is a combination of cultural philosophies, practices, and tools that increases an organization’s ability to deliver applications and services at high velocity. Using DevOps principles, organizations can evolve and improve products at a faster pace than organizations that use traditional software development and infrastructure management processes. This speed enables organizations to better serve their customers and compete more effectively in the market.

 Some of these principles, such as [two-pizza teams](https://www.businessinsider.com/jeff-bezos-two-pizza-rule-for-productive-meetings-2013-10), microservices, and service-oriented architecture (SOA), are out of the scope of this whitepaper. This whitepaper discusses the CI/CD capability that Amazon has built and continuously improved. CI/CD is key to delivering software features rapidly and reliably.

 AWS now offers these CI/CD capabilities as a set of developer services such as [Amazon CodeCatalyst](https://aws.amazon.com/codecatalyst/) and [AWS CodePipeline](https://aws.amazon.com/codepipeline/). Developers and IT operations professionals practicing DevOps can use these services to rapidly, safely, and securely deliver software. Together, they help you securely store and apply version control to your application's source code. Amazon CodeCatalyst is a fully managed, unified software development service that makes it faster to build and deliver software on AWS. For an existing environment, AWS CodePipeline has the flexibility to integrate each service independently with your existing tools. These are highly available, easily integrated services that can be accessed through the AWS Management Console, AWS application programming interfaces (APIs), and AWS software development toolkits (SDKs) like any other AWS service
