---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_data_classification_lifecycle_management.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC07-BP04 Define data lifecycle management
<a name="sec_data_classification_lifecycle_management"></a>

 Your defined lifecycle strategy should be based on sensitivity level as well as legal and organization requirements. Aspects including the duration for which you retain data, data destruction processes, data access management, data transformation, and data sharing should be considered. When choosing a data classification methodology, balance usability versus access. You should also accommodate the multiple levels of access and nuances for implementing a secure, but still usable, approach for each level. Always use a defense in depth approach and reduce human access to data and mechanisms for transforming, deleting, or copying data. For example, require users to strongly authenticate to an application, and give the application, rather than the users, the requisite access permission to perform action at a distance. In addition, ensure that users come from a trusted network path and require access to the decryption keys. Use tools, such as dashboards and automated reporting, to give users information from the data rather than giving them direct access to the data.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Identify data types: Identify the types of data that you are storing or processing in your workload. That data could be text, images, binary databases, and so forth.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Data Classification Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification.html)
+  [Getting started with Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/getting-started.html)

 **Related videos:**
+  [Introducing the New Amazon Macie](https://youtu.be/I-ewoQekdXE)
