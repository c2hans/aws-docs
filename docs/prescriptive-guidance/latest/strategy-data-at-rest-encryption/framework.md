---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/framework.html
---

# Framework
<a name="framework"></a>

A *framework*, in this context, refers to a set of standard operating procedures that need to be followed when you modify the encryption standards or policy. The framework is the scaffolding that helps you implement the standards. It helps convert words into actions. The framework links the people who define standards with the people who implement them.

Frameworks typically include the following topics:
+ [Data classification](#data-classification)
+ [Environment classification](#environment-classification)
+ [Change events and processes](#change-events)

## Data classification
<a name="data-classification"></a>

Data classification plays a vital role in creating an encryption strategy. *Data classification* is the process of assigning data to a category based on the sensitivity of the data. The following are common data classification categories, in increasing order of sensitivity: public, private, internal, confidential, and restricted.

Your encryption framework should include the following information about data classification:
+ The data classification categories for your enterprise.
+ The classification criteria used to classify data into its appropriate category. For example, a company's trade recipe could be classified as *restricted*, employee PII could be *confidential*, and internal communication between employees through official channels might be *internal*.
+ The process used to promote and demote data among categories.
+ The access criteria for each data classification category.
+ The kind of encryption key required for each category.

## Environment classification
<a name="environment-classification"></a>

Your enterprise might have multiple environments, such as development, testing, sandbox, preproduction, and production. Each environment can contain different types of data and have different encryption requirements.

Your encryption framework should include the following information about your environments:
+ Define your enterprise environments.
+ Define the encryption requirements for each environment. For example, you might use a single encryption key for all the data categories in your development environment, and in your production environment, you might use different encryption keys for each business application or data classification category.

## Change events and processes
<a name="change-events"></a>

Encryption standards are subject to frequent change so that you can keep up with the latest technologies, best practices, and innovations. The following are common change events that might initiate a revision of your encryption standards:
+ Changes in the minimum length of encryption keys
+ Changes in the strength of an encryption algorithm
+ Changes to who can access encryption keys or how
+ Changes to the rotation intervals for your keys
+ Changes to the process for deleting keys
+ Changes to the key storage location or policies
+ Changes to the process for backing up and restoring keys

Your encryption framework should include the following to help prepare your organization to manage, implement, and communicate changes to the encryption standards or policy:
+ **Change control process** – The purpose of this process is to plan and prepare for the upcoming change. When you need to change your encryption standards or policy, this repeatable and scalable process is designed to define:
  + How your organization assesses the impact of the change
  + Who can initiate changes
  + Who is responsible for implementing the change
  + Who is responsible for approving the change
  + How your organization would roll back the change, if necessary
+ **Change auditability and traceability process** – This process defines how your organization audits and traces changes, both at the metadata level and at the data level. It should define how you keep and access records of:
  + What changed
  + When it was changed
  + Who initiated, approved, and implemented the change

  For example, if your organization changes the minimum encryption key strength, you should be able to determine the original and new requirements, when the change was effective, and who was involved in the change process.
+ **Change rollout process** – The purpose of this process is to define how your organization implements the change after you have decided to make it. This process defines:
  + Who are the stakeholders
  + Whether you should complete a pilot or proof of concept
  + How and when you should communicate the status of the change
  + How to roll back the change, if necessary.
  + What the observation period should be after implementing the change.
  + What the observation process will be to monitor the impact of the change, including how to collect feedback about the change and assess effectiveness
+ **Retirement process** – The purpose of this process is to define how your organization handles retirement of encryption-related resources and information. It includes instructions for the actual retirement as well as the communication process for retirement.
