---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/best-practices-for-migrating-oracle-e-business-suite-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Best practices for migrating Oracle E-Business Suite on AWS
<a name="best-practices-for-migrating-oracle-e-business-suite-on-aws"></a>

## Proof of concept
<a name="proof-of-concept"></a>

 After you perform the migration assessment, identify the migration path, and design the target architecture for running Oracle E-Business Suite on AWS, it is important to perform a proof of concept (PoC). Note all the required input and output parameters.

## Migrate versus upgrade
<a name="migrate-vs-upgrade"></a>

 For homogeneous migrations, you can either upgrade your Oracle E-Business Suite on-premises first and then perform the migration as a separate step, or perform the migration and the upgrade at the same time in AWS. This decision differs per customer dependent on their use case, both are viable options.

 If you are only doing homogeneous migration and do not want to upgrade, you can directly migrate you Oracle E-Business Suite environment to AWS.

 For heterogeneous/cross-platform migrations, you can perform re-platforming and migrations at once. Do however expect a longer cutover window since this requires a [Oracle Rapid Install](https://docs.oracle.com/cd/E26401_01/doc.122/e22950/T422699g54568.htm) application tech stack install and database platform conversion. Once migrated to the cloud, you can later upgrade to the latest Oracle E-Business Suite version.

## DB tier and app-tier
<a name="db-tier-and-app-tier"></a>

 Due to latency considerations and integration issues, AWS recommends that you perform database tier and application tier migration at the same time.

## Identification of read-only workloads
<a name="identification-of-read-only-workloads"></a>

 If you haven’t done this for your on-premises environment, AWS recommends that you identify the read-only workloads such as reports, batch jobs, and ETL jobs, and use Oracle Active Data Guard read-only standby for offloading the read-only workload. This allows you to scale the environment and serve transactional workloads with optimal performance.

## AWS native services for customizations
<a name="aws-native-services-for-customizations"></a>

 Customers often develop custom user interfaces and APIs on top of Oracle E-Business Suite functionality for their business-specific requirements. Although Oracle E-Business Suite has all the underlying technical infrastructure available for building and hosting custom UI, AWS recommends that customers make use of AWS services such as [AWS](https://aws.amazon.com/elasticbeanstalk/) [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/), [AWS Lambda](https://aws.amazon.com/lambda/), [Amazon AppFlow](https://aws.amazon.com/appflow/), [AWS Glue](https://aws.amazon.com/glue/), and so on for UI development and data integration. This approach helps customers reduce the load on Oracle E-Business Suite environment, and helps achieve agility and CI/CD adoption.

 You can also build solutions such as serverless data lakes and machine learning (ML) solutions on AWS surrounding your ERP systems such as Oracle E-Business Suite to analyze data, generate insights, and for predictions.

## Right stakeholders in the discussion
<a name="right-stakeholders-in-the-discussion"></a>

 It is important to engage the right stakeholders throughout the process. In AWS discussions with customers, AWS engaged personas such as Head of IT, database administrators (DBAs), and Chief Information Officers (CIOs). When working with AWS teams, it is also helpful to set up deep dive technical discussions in the form of workshops. Also bring everyone on the same page in terms of current skills in the team, implementation timelines, and post-migration activities.
