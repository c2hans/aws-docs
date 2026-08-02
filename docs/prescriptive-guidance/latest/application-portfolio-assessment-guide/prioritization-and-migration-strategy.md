---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/prioritization-and-migration-strategy.html
---

# Prioritization and migration strategy
<a name="prioritization-and-migration-strategy"></a>

A key element of migration planning is to establish prioritization criteria. The point of this exercise is to understand the order in which applications will be migrated. The strategy is to take an iterative and progressive approach to evolve the prioritization model.

## Prioritizing applications
<a name="prioritizing-applications"></a>

This stage of assessment focuses on establishing initial criteria to prioritize low-risk and low-complexity workloads. These workloads are good candidates for pilot applications. Using low-risk, low-complexity workloads in initial migrations reduces the risk and gives teams the opportunity to gain experience. These criteria will be evolved in further assessment stages to align prioritization with business drivers when creating the migration wave plan.

The initial criteria should prioritize applications with a small number of dependencies, running in cloud-supported infrastructure, and from non-production environments. An example would be applications with 0–3 dependencies ready to rehost as-is in a development or test environment. These criteria are valid for defining the pilot applications and potentially the first and second migration waves, depending on the level of cloud adoption maturity and confidence levels.

### Deciding what initial criteria to use
<a name="deciding-what-initial-criteria-to-use.81da4993-597d-586a-a0bc-e88a2807c112"></a>

Select 2–10 data points to use for prioritizing your first workloads. These data points come from your initial data collection (refer to the [data collection](initiating-data-collection.md) section).

Next, define a score, or weight, for each possible value of each data point. For example, if the environment attribute is selected, and the possible values are production, development, and test, each value is assigned a score, a greater number representing higher priority. Although it is optional, we recommend assigning a multiplying factor for importance or relevance to each data point. This optional step provides a higher-level differentiator to emphasize what is more important, which helps to keep the criteria aligned as you iterate on assigning scores to the values.

Based on the strategy to prioritize low-risk, simple applications for the first few migration waves, the following table shows example attributes selection and their value assignments.

|
|
| Attribute (data point) | Possible values | Score (0-99) | Importance or relevance multiplying factor |
| --- |--- |--- |--- |
| Environment | Test | 80 | High (1x) |
| Development | 50 |
| Production | 20 |
| Business criticality | Low | 60 | High (1x) |
| Medium | 40 |
| High | 20 |
| Regulatory or compliance framework | None | 60 | High (1x) |
| FedRAMP | 10 |
| Operating system support | Cloud ready | 60 | Medium-high (0.8x) |
| Unsupported in cloud | 10 |
| Number of compute instances | 1-3 | 60 | Medium-high (0.8x) |
| 4-10 | 40 |
| 11 or more | 20 |
| Number of dependencies | 0-3 | 70 | High (1x) |
| 4-10 | 30 |
| 11 or more | 10 |
| Migration strategy | Rehost | 70 | Medium (0.6x) |
| Replatform | 30 |
| Refactor, or re-architect | 10 |
| Operations team cloud maturity or readiness | High | 80 | High (1x) |
| Medium | 50 |
| Low | 10 |

Make sure that you select attributes that can act as key differentiators between applications. Otherwise, the criteria will result in many workloads sharing the same priority. After you apply the model, we recommend looking at the top and bottom of the resulting ranking to see if you agree. If you don't generally agree, you can revisit the criteria that you used to score the workloads.

After you obtain a ranking, look at the distribution of scores across the entire portfolio. The scores themselves do not matter. It is the difference between scores that matters. For example, you might find that the top total score is 8,000 and the bottom score is 800. Consider plotting the resulting scores as a histogram, so you can verify that you have a good distribution. The ideal distribution looks like a standard bell curve, with a few very high-priority workloads and a few very low-priority workloads. The majority of applications will be somewhere in the middle.

Another key aspect of initial prioritization is to include internal teams or business units that show interest in being early adopters of the cloud. These could be a considerable lever in obtaining business support to migrate a given application, especially in the early days. If this is the case in your organization, include the business unit attribute in the preceding table. Assign a high score to those business units that are willing to come forward with their applications. Using the business unit attribute will help bring those applications to the top of the list.

After you agree with the resulting ranking, select the top 5–10 applications. These will be your initial application migration candidates. Refine the list so that you confirm 3–5 applications. This helps you to take a targeted approach when performing a detailed application assessment. For more information, see [Prioritized applications assessment](prioritized-applications-assessment.md).

## Determining the R type for migration
<a name="migration-r-type"></a>

Deciding on a migration strategy for each application and associated infrastructure will have implications to migration speed, cost, and level of benefits. It is key to determine strategy based on a balanced combination of factors, including business drivers, technical guiding principles, prioritization criteria, and business strategy.

Sometimes these factors create conflicting views. For example, the primary driver for migration might be innovation and agility. At the same time, you might need to reduce costs quickly. Modernizing all applications in-scope will reduce costs in the long-run, but it will require a greater investment upfront. In that case, one approach is to migrate applications by using strategies that require less effort, such as rehost or replatform. That can provide quick efficiencies and cost reduction in the short term. Then reinvest the savings into modernizing the application at a later stage, and achieve further cost reduction.

However, starting with a complete rehost of all applications delays the greater benefits of modernization. The key is to find balance between migration strategies so that business-strategic applications are prioritized for modernization while other applications can be rehosted or replatformed first then modernized.

### How to determine a migration strategy for your applications?
<a name="how-to-determine-a-migration-strategy-for-your-applications-.1712ed21-85eb-582f-9a59-a8d305d106d1"></a>

At this stage of assessment, the focus is to incorporate an initial model for guiding migration strategy selection. To validate the migration strategy for the initial applications, use the model in conjunction with the business drivers and the prioritization criteria. The default logic of the decision tree will help you to determine the initial treatment for the scope. In the tree, the most complex approaches, such as refactor, or re-architect, are reserved for your strategic workloads.

![The 6 R decision process discussed in this guide.](http://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/images/guide-img/252c3f6c-9941-4934-9262-6561a28cd5f7/images/089b1c22-02d9-4e67-a9f5-413a2a60d13c.png)

The first step to an initial model is to update the business drivers at the top of the tree with those defined by your organization. Next, apply the tree to application components rather than applications as a whole. For example, in the case of a three-tier application that has three components (front-end, application layer, and database), each component should transit the tree independently and be assigned a specific strategy and pattern. This is because in some cases you might want to rehost or replatform a given tier and refactor (re-architect) other tiers.

Before using the decision tree to establish migration strategies, test the logic with a few applications and confirm that you generally agree with the outcome. The decision tree is a guide that does not replace the analysis required to determine its correctness. The tree logic might not apply to particular cases. Treat those cases as exceptions, and proceed to override the decision driven by the tree by documenting the rationale for the override rather than changing the tree logic. This prevents multiple decision tree versions, which could become difficult to manage. General guidance is that the tree should be valid for at least 70–80 percent of the workloads. For the rest, there will be exceptions. At this stage of the assessment, any adjustments to the tree logic should be focused on establishing an initial model to enable planning. Further iterations and refinement occur in later stages, such as [portfolio analysis and migration planning](portfolio-analysis-migration-planning.md).
