---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-mainframe-apps-shared-db2/mainframe-modernization.html
---

# AWS Mainframe Modernization
<a name="mainframe-modernization"></a>

**Note**
AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

The [AWS Mainframe Modernization service](https://docs.aws.amazon.com/m2/latest/userguide/what-is-m2.html) enables you to migrate your legacy mainframe applications to a cloud-native environment, preserve existing business logic and investments, use automated tools and managed runtime services, optimize application performance, and reduce operational costs. This service streamlines the modernization process, so you can harness the power of the cloud while maintaining the value of your core mainframe systems. AWS provides two key approaches to mainframe modernization: replatforming and automated refactoring.

## Replatforming
<a name="replatforming"></a>

[AWS Mainframe Modernization Replatform with Rocket Software](https://aws.amazon.com/mainframe-modernization/capabilities/replatform-rocketsoftware/) (formerly Micro Focus) provides a powerful replatforming option for businesses that want to migrate their mainframe applications to the cloud with minimal disruption. This solution enables you to recompile and run your existing COBOL and PL/I applications on AWS without requiring significant code changes.

Key benefits of the AWS Replatform with Rocket Software solution include:
+ Preservation of existing business logic and investments
+ Reduced risk and faster time to market
+ Improved scalability and performance on AWS infrastructure
+ Access to modern development tools and practices

You can use this solution to maintain your familiar mainframe programming languages while taking advantage of the flexibility, cost-effectiveness, and innovation of the AWS Cloud.

## Automated refactoring
<a name="refactoring"></a>

For a more transformative approach than replatforming, you can use [AWS Blu Age](https://aws.amazon.com/mainframe-modernization/capabilities/refactor/), which offers automated refactoring of mainframe applications to Java-based cloud-native applications. This solution helps you modernize your legacy systems more comprehensively, and convert them into applications that can take full advantage of cloud-native technologies.

Key advantages of AWS Blu Age include:
+ Conversion of legacy code to modern, maintainable Java applications
+ Automated transformation that reduces manual effort and potential errors
+ Creation of cloud-native applications that are optimized for AWS services
+ Improved agility and easier integration with modern technologies

AWS Blu Age helps you migrate your applications and prepare them for the cloud, to open up new possibilities for innovation and growth. For more information about this approach, see [Refactoring applications automatically with AWS Blu Age](https://docs.aws.amazon.com/m2/latest/userguide/refactoring-m2.html) in the AWS Mainframe Modernization documentation.

## Benefits of replatforming
<a name="benefits"></a>

This guide discusses an approach for replatforming mainframe COBOL applications on AWS. This approach aims to modernize legacy systems while temporarily retaining IBM Db2 for z/OS to streamline the transition process. By maintaining the existing database structure initially, you can reduce complexity and risk during migration. This phased approach helps you benefit from the scalability and cost-effectiveness of the AWS Cloud while preserving critical data integrity. The advantages of phased replatforming include the following:
+ **Accelerated modernization:** Replatforming and refactoring typically require less time and resources compared with re-imagining a legacy application in the cloud, because they don't involve rewriting the entire application. This approach also supports a more gradual transition that enables organizations to modernize at their own pace while immediately benefiting from the scalability and cost-effectiveness of the AWS Cloud.
+ **Risk mitigation:** Replatforming offers several advantages over refactoring for many organizations. Companies can maintain their existing COBOL and PL/I codebases, preserve years of business logic, and minimize the risk associated with large-scale code changes.
+ **Data continuity and phased migration:** A significant benefit of replatforming is the option to initially keep data in Db2 for z/OS in its original data format. This strategy avoids the need for immediate, complex, and potentially risky data migration processes. By maintaining data in its original environment during the initial phase, you can preserve data integrity, reduce downtime, and minimize the risk of data loss or corruption during the modernization process. As a second step, you can plan for a controlled, phased data migration to cloud-native databases that involves thorough testing and validation while the application continues to run on the replatformed environment.
+ **Flexibility and future-proofing:** For companies that have significant investments in mainframe skills and applications, replatforming provides a pragmatic path to modernization that balances innovation with continuity. It offers the flexibility to retain critical data structures and access methods initially, while also setting the stage for future modernization efforts, including eventual data migration to fully cloud-native solutions.

Organizations can follow the replatforming approach to modernize at their own pace and address immediate needs while planning for long-term digital transformation goals. This approach also gives companies the opportunity to train their staff on cloud-native services.
