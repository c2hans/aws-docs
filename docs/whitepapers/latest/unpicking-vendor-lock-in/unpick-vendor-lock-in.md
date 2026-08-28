---
source_url: https://docs.aws.amazon.com/whitepapers/latest/unpicking-vendor-lock-in/unpick-vendor-lock-in.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Unpicking vendor lock-in
<a name="unpick-vendor-lock-in"></a>

 Customers should have the freedom to choose what they like, when they like. This is a win-win scenario for customers and vendors—as customers have access to the things they need and want, and vendors keep their service offerings relevant and market-leading. That’s why constant innovation, and constant improvement is good for the vendor and good for the customer. Many of the new services offered by AWS are created in response to specific customer needs––strengthening the AWS service offering for customers.

 AWS wants to solve customer needs every moment of the day; this is imperative, given that AWS cloud services are provided on an on-demand, pay-as-you-go basis. AWS enjoys the challenge of ensuring that customers have the freedom to choose from the broadest range of innovative cloud services, so that customers continue to *want* to use AWS. Should a customer choose to move away, AWS makes this as simple as possible.

 Offering customer choice and freedom are core principles throughout AWS. For example, where customers might have been locked into a legacy database provider before, AWS offers a large number of [different types of databases](https://aws.amazon.com/products/databases/), suitable for different types of data. There is no contractual obligation for customers to stay with one type of database. You can run databases from other vendors on AWS, and can change the type of instance your databases run on at any time. AWS makes it easy to manage your data so that you can take advantage of fit-for-purpose database solutions, including exporting your data out of AWS, if desired. Everything AWS does gives customers the freedom to choose the best-fit cloud services and features available. If you find your choices limited in this way, a cloud provider might be trying to lock you in.

## Defining “Lock-In” and “Switching Costs”
<a name="defining-lock-in-and-switching-costs"></a>

 Avoiding lock-in means that if you decide to move, you can do so, at speed, and without unreasonable difficulty. This does *not* mean that if you decide to move all of your workloads to a different CSP today, you will have everything up and running on them tomorrow. There are always some tradeoffs or *switching costs*, such as time to switch technology stacks, migrate data, or train staff on new vendor services. Switching “costs” include time, flexibility, functionality and sometimes financial cost.

 The term lock-in can be misleading from a technology perspective. “Vendor lock-in” is really about switching costs which make it prohibitively difficult or risky to move away from a vendor, rather than being explicitly blocked from doing so.

 Switching costs have existed throughout the history of IT. As soon as you decide on a technology vendor, product, or service, you will have switching costs should you decide to change. For example, if you choose Java and then migrate to Node.js, you will have a cost. You’re not actually locked in, you simply have switching costs that may be large or small depending on the situation.

 Vendor lock-in and data portability are not the only lenses that customers look at cloud services through. Ultimately, you want to benefit from the advantages that cloud services can bring to your organization. In many cases, customers select a cloud provider because they offer capabilities that their competitors do not provide.

### Using CSP-native services
<a name="using-csp-native-services"></a>

 An early decision that customers need to consider is: “Am I going to make a commitment to a high-value service from a Cloud Service Provider for the business value that it returns; or am I going to take on the cost and complexity of building it myself (and often conforming to the lowest common denominator) in favor of perceived portability?”

 The answer, of course, is that you should use the service which best meets your business needs. There is no need to spend resources to reinvent the wheel, if your needs can be met with a CSP’s services, as long as there are no known egregious switching costs.

 For example, if you need machine learning (ML) capabilities, choosing a CSP that allows for the use of multiple technology approaches gives you speed and agility, which can save time and money with respect to innovation and responding to changing business needs. You’re not locking yourself into the vendor, you’re making a decision to use the CSP-native service because it’s the best fit for your needs. Trying to use cloud services across multiple providers without the technical justification to do so is likely to lead to greater complexity and less service depth.

 AWS has made open source accessible to the widest possible audience, enabling customers to make their own technology choice at any point up the stack. For example, you might choose AWS-native services to manage massive datasets, but you might also choose to drop Apache Spark onto an [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instance to meet that need. It isn’t always a case of having to pick a CSP-native service versus a service that a different CSP offers.

 Defining what business outcomes you need to achieve, and doing due diligence of a CSP’s offerings, can help you choose the best solutions for your organization’s needs. Making everything easy to switch isn’t the only consideration—it best to focus on adopting services which are best for your organization.

 Remember to factor in switching costs into your evaluation of cloud providers so you don’t get locked in technically or contractually. Build a plan that anticipates the potential need to switch technology in the future, and evaluate vendors on how they help to minimize switching time and cost.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
