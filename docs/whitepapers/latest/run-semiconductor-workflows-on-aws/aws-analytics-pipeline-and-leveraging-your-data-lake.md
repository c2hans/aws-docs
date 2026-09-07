---
source_url: https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/aws-analytics-pipeline-and-leveraging-your-data-lake.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS analytics pipeline and leveraging your data lake
<a name="aws-analytics-pipeline-and-leveraging-your-data-lake"></a>

 This guide has emphasized moving data in to your data lake that is built on an Amazon S3 bucket. Next, you learn about what you can do with the data you have collected. Archival data can be an invaluable source when performing analytics and model training for AI/ML. The archival data provides historical comparison to accurately determine trends, and provide helpful insights. For more information, see the [AI/ML for workflow optimization](aiml-for-workflow-optimization.md) section.

![This image shows an analytics pipeline built from Amazon S3 data lake, AWS Glue, Amazon Redshift, Amazon Athena, and Amazon QuickSight.](https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/images/semiconductor-analytics-pipeline.png)

**Analytics pipeline and leveraging your data lake**

 Starting with all of the data that you have collected, both current and archival, you use several AWS managed services, to include visualizing your data with an [Amazon Quick](https://aws.amazon.com/quicksight/) dashboard. For example, a QuickSight dashboard can help you analyze wafer data that is sent over from the foundry and provide valuable insights into future designs. The following figure shows a QuickSight dashboard analyzing wafer defect data.

![This image shows an example Amazon QuickSight dashboard for wafer data analysis.](https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/images/example-quicksight-dashboard.png)

**QuickSight dashboard showing wafer defect types and foundry location **

 In this example, the dashboard shows the defect type and the location of the fab where the defect occurred. From this data, it appears that defects are occurring about the same rate and type across all of the fabs. If, for example, there was an increase in defects at a specific fab when fabrication started on your design, this may indicate a problem with the PDK or another design issue. With this insight, you can make decisions about designs in-flight, that could result in reduced re-spins and increased fabrication yields.
