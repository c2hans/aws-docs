---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tagging-best-practices/best-practice-tagging.html
---

# Best practices
<a name="best-practice-tagging"></a>

When using tags, it's important to understand current or potential company and use-case structure. Using this information, you can choose the right tags. For example, if you are building a data lake for the presales department, and you know that there are plans to expand the data lake to include data from the after-sales department, using the tag `department` will help identify the costs and performance of each department separately. Planning, cost allocation, and optimization of code or data can be identified with more accuracy. Without the `department` tag, if presales data needs 15 minutes for data modeling and aftersales data needs 45 minutes, developers must spend more time in root cause analysis. With the `department` tag, developers would know exactly where to look.

## Tagging ontology
<a name="ontology"></a>

Business and technology together play an important role in identifying the right tags to use. From a business perspective, a company and a project will always follow a certain structure. For example, in the EMEA *region*, in the HR *department*, there could be a *project* about predicting the need for hiring. In this case, including metadata from the existing structure would be important for reporting, monitoring, cleanup, and rollouts. At the same time, the technical department understands that the project will need the following:
+ *Phases* of data collection through a data pipeline that is made up of data ingestion, cleaning and processing
+ An ML team** **to do data modeling for forecasting
+ A DevOps pipeline for code orchestration, spread through a dev, test, and prod environment

All of the italicized keywords are business and technical group structures that are important to be associated with the components of an application. This is an example of a typical tagging ontology. Using the example, the following table shows the corresponding key-value pairs for the tags.

|
|
| Key | Values |
| --- |--- |
| `department` | `human resources` |
| `region` | `EMEA` |
| `project` | `hiring forecast` |
| `phase` | `3` |
| `process` | `data ingestion`, `data cleaning`, `processing`, `modeling`, or `sales forecasting` |
| `domain` | `machine learning` or `data pipeline` |
| `creation` | `cdk`, `x framework`, `ingest pipeline`, or `manual - empty` |
| `status` | `development`, `testing`, `production access`, `reporting`, or `onboarding` |

## Governance of tags
<a name="governance"></a>

Setting up governance mechanisms helps make tagging consistent and programmable across all AWS resources:
+ *Reactive governance* means finding resources that are not properly tagged. You can use tools such as the [Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/overview.html), [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html), and custom scripts.
+ *Proactive governance* means that users are not allowed to create any untagged resources. You can use tools such as [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/userguide/end-user-console.html), [tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) in AWS Organizations, or IAM resource-level permissions.
