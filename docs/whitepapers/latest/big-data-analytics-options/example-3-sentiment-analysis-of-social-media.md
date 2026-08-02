---
source_url: https://docs.aws.amazon.com/whitepapers/latest/big-data-analytics-options/example-3-sentiment-analysis-of-social-media.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Example 3: sentiment analysis of social media
<a name="example-3-sentiment-analysis-of-social-media"></a>

A large toy maker has been growing very quickly and expanding their product line. After each new toy release, the company wants to understand how consumers are enjoying and using their products. Additionally, the company wants to ensure that their consumers are having a good experience with their products. As the toy system grows, the company wants to ensure that their products are still relevant to their customers and that they can plan future roadmaps items based on customer feedback. The company wants to capture the following insights from social media:
+  Understand how consumers are using their products
+  Ensure customer satisfaction
+  Plan future roadmaps

Capturing the data from various social networks is relatively easy but the challenge is building the intelligence programmatically. After the data is ingested, the company wants to be able to analyze and classify the data in a cost-effective and programmatic way. To do this, they can use the architecture in the following figure.

![Architecture diagram showing Twitter data flowing through Kinesis, Lambda, S3, to analytics services.](http://docs.aws.amazon.com/whitepapers/latest/big-data-analytics-options/images/bigdata4.png)

*Sentiment analysis of social media *

1. First, deploy an Amazon EC2 instance in an Amazon VPC that ingests tweets from Twitter.

1. Next, create an Amazon Data Firehose delivery stream that loads the streaming tweets into the raw prefix in the solution's S3 bucket.

1. S3 invokes a Lambda function to analyze the raw tweets using Amazon Translate to translate non-English tweets into English, and Amazon Comprehend to use natural language-processing (NLP) to perform entity extraction and sentiment analysis.

1. A second Firehose delivery stream loads the translated tweets and sentiment values into the sentiment prefix in the S3 bucket. A third delivery stream loads entities in the entities prefix in the S3 bucket.

1. This architecture also deploys a data lake that includes AWS Glue for data transformation, Amazon Athena for data analysis, and Quick for data visualization. AWS Glue Data Catalog contains a logical database used to organize the tables for the data in S3. Athena uses these table definitions to query the data stored in S3 and return the information to an Quick dashboard.

By using ML and BI services from AWS including [Amazon Translate](https://aws.amazon.com/translate/), [Amazon Comprehend](https://aws.amazon.com/comprehend/), Amazon Kinesis, Amazon Athena, and Amazon Quick, you can build meaningful, low-cost social media dashboards to analyze customer sentiment, which can lead to better opportunities for acquiring leads, improve website traffic, strengthen customer relationships, and improve customer service.

This example solution automatically provisions and configures the AWS services necessary to capture multi-language tweets in near-real-time, translate them, and display them on a dashboard powered by Amazon Quick. You can also capture both the raw and enriched datasets and durably store them in the solution's data lake. This enables data analysts to quickly and easily perform new types of analytics and ML on this data. For more information, see the [AI-Driven Social Media Dashboard solution](https://aws.amazon.com/solutions/implementations/ai-driven-social-media-dashboard/).
