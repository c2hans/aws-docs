---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-storage-for-vmware-professionals/next-steps.html
---

# Next steps
<a name="next-steps"></a>

This guide was intended to help VMware professionals transition from on-premises environments to AWS storage solutions. It covered fundamental storage concepts, advanced management practices, and the required technical knowledge to successfully migrate workloads and adopt AWS technologies. The following lists provide an overview of AWS benefits, migration tools, and migration steps.

## Benefits of AWS
<a name="benefits-of-9999999999999999aws-.8d653b1d-d7f3-58ad-acbf-c32f1ebe92fd"></a>
+ **Scalability –** S3 and EFS automatically scale with demand without capacity planning
+ **Cost effectiveness –** Pay-as-you-go pricing eliminates upfront hardware investments
+ **Durability – **S3 provides 99.999999999% (11 nines) of durability across Availability Zones
+ **Enhanced security –** Built-in encryption at rest and in transit with IAM access controls
+ **Automation –** AWS DataSync and other tools automate large-scale transfers

## Migration tools
<a name="migration-tools.1e572141-c268-5994-93bc-67058d8088e7"></a>
+ **AWS Migration Hub –** Centralized tracking and monitoring of migration progress
+ **AWS DataSync –** Online data transfer between on-premises storage and AWS services
+ **AWS Storage Gateway –** Hybrid integration for gradual, phased migrations
+ **AWS Transfer Family –** Secure file transfers through FTP, SFTP, or FTPS protocols

## Migration steps
<a name="migration-steps.201f09bc-7089-5bdd-9ff0-009b5003941a"></a>
+ **Assessment –** Inventory current VMware storage types, capacity, and workload requirements
+ **Planning –** Map VMware storage to AWS equivalents (VMFS to EBS, NFS to EFS)
+ **Execution –** Transfer data using DataSync, Storage Gateway, or Transfer Family
+ **Validation –** Verify data integrity and test workload performance after migration
+ **Optimization –** Implement lifecycle policies and cost optimization strategies
