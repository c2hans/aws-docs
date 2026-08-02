---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/data-driven-architectural-patterns.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data driven architectural patterns
<a name="data-driven-architectural-patterns"></a>

 Many data-driven organizations seek the truth by treating data like an organizational asset, no longer the property of individual departments. They set up systems to collect, store, organize, and process valuable data and make it available in a secure way, to the people and applications that need it. They also use technologies such as ML to unlock new value from their data such as improving operational efficiency, optimizing processes, developing new products and revenue streams, and building better customer experiences.

 We depict the five most commonly seen architecture patterns on AWS, that cover several use cases for various different industries and customer sizes:
+  Customer 360 architecture
+  Event-driven architecture with IOT data
+  Personalized architecture recommendations
+  Near real-time customer engagement
+  Data anomaly and fraud detection

## Build Customer 360 architecture on AWS
<a name="build-customer-360-architecture-on-aws"></a>

 As customer expectations continue to rise, organizations face a gap between their need to use their data to meet customer expectations, and their current data management practices’ ability to deliver. So how can companies close this gap? They must work toward taking back ownership of their data to harness the power of their customer and prospect information, to compete and win on customer experience.

 Customer 360 describes the trend of building a complete and accurate picture of every customer’s structured and unstructured data across an organization. Customer 360 is not a single solution, nor a single service. It is the aggregation of all customer data into a single unified location, that can be queried and used to generate insights for improving the overall customer experience.

 Some of the common use cases and solutions that fit under these Customer 360 architecture patterns are as follows:
+  **Marketing and demand generation**
  +  Enrich customer profiles and identify the best prospects to drive customer acquisition.
  +  Enable affinity marketing to achieve greater wallet share.
  +  Personalize offers and website experiences based on historical customer data and micro-targeted segments to increase conversion rates.
  +  Monitor campaign effectiveness and key performance indicators to improve the return on investment (ROI) of marketing efforts.
  +  Predict consumer churn so you can take proactive actions to drive retention and repeat purchase.
+  **Sales growth**
  +  Gain insights to identify opportunities, predict customer intent, and foster stronger relationships.
  +  Foster relationships with a complete view of a customer’s interactions to better understand the health of the relationship.
  +  Increase customer lifetime value with data-driven, next best action suggestions, and intelligent cross-sell and upsell recommendations.
  +  Deliver consistent cross-channel experiences. enabling an online-offline feedback loop.
+  **Customer service**
  +  Use holistic customer profiles to accelerate issue resolution and improve customer satisfaction.
  +  Detect anomalies and strengthen trust.
  +  Implement self-service tools and chatbots that allow customers to resolve issues themselves.
  +  Deliver personalized loyalty offers to increase customer lifetime values and reduce churn.
  +  Generate customer lifetime value and next best action recommendations.

 The following diagram illustrates customer 360 architecture on AWS.

![A diagram depicting Customer 360 architecture on AWS.](http://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/images/customer-360.png)

 The steps that data follows through the architecture are as follows:

1.  **Data ingestion —** Establishing customer 360 data by consolidating your disparate data sources in a schemeless ingestion approach, with the guiding principle of:
   +  Getting the right data ingested as close to the source system as possible from past data.
   +  Predicting future data and persisting them in object storage such as Amazon S3 or capturing them as streams in near real-time using:
   +  SAP connectors.
   +  AppFlow services that intuitively connect you to your Salesforce account.
   +  Google analytics services and data movement service to connect to JDBC/ODBC sources to capture the data in incremental fashion with zero coding.

1.  **Building a unified customer profile** — You need to extract and link elements from each customer record, creating a customer 360° dataset that will serve as a single source of truth for your customer data hub, with a data model to build your customers context on their journey. Using [Amazon Neptune](https://aws.amazon.com/neptune/), you can create a near real-time, persistent, and precise view of the customer and their journey in a graph-based storage system. Use Neptune to store entities that provide context through an associated and predefined set of rules, allowing relationship traversals viewed in a connected fashion.

    This 360° knowledge graph serves the potential information to uncover hidden customer segments, and deepens customer hierarchy, provides cluster analysis resulting in the creation of customer personas, and evaluates the size of each segment. The unique customer journey is preserved by writing reusable Gremlin/SPARQL libraries that are automated through a serverless data lake framework.

1.  **Intelligence layer** — Offloading this journey into analytical store such as [Amazon Redshift](https://aws.amazon.com/redshift/) or S3 enables your data scientists and data analysts to refine the ontologies and shorten the graph path with access to raw information already preserved in S3 using AWS Glue DataBrew and Amazon Athena serverless.

1.  **Activation layer** — This refinement to customer ontology represents connectedness between customer 360° data using AWS lake house architecture. It enriches customer profiles with recommendations, predictions using AI/ML to test the customer journey hypothesis, and creates the next best action APIs by sensing and responding to signals through the customer lifecycle using Amazon personalize and pinpoint. Actions offered via next-best APIs are now integrated and presented across distribution systems and channels for resilient and optimized personal experience.

## Build event driven architectures with IOT sensor data
<a name="build-event-driven-architectures-with-iot-sensor-data"></a>

 Organizations create value by making decisions from their data in near real-time. Some of the common use cases and solutions that fit under this event driven architecture pattern include:
+  [Industrial IOT use cases](https://aws.amazon.com/blogs/iot/industrial-iot-from-condition-based-monitoring-to-predictive-quality-to-digitize-your-factory-with-aws-iot-services/) to monitor industrial equipment quality, to determine actions such as adjusting machine settings, using different sources of raw materials, or doing additional worker training that will improve the quality of the factory output.
+  Medical device data collection for personalized patient health monitoring, adverse event prediction, and avoidance.
+  [Connected vehicle use cases](https://aws.amazon.com/solutions/implementations/aws-connected-vehicle-solution/) such as voice interaction, navigation, location-based services, remote vehicle diagnostics and predictive maintenance, media streaming, and vehicle safety that includes computing within vehicles and in-the-cloud, near real-time predictive analytics.
+  [Sustainability and waste reduction solutions](https://aws.amazon.com/solutions/travel/sustainability-and-waste-reduction/?solutions-all.sort-by=item.additionalFields.sortDate&solutions-all.sort-order=desc&marketplace-ppa-and-quickstart.sort-by=item.additionalFields.sortDate&marketplace-ppa-and-quickstart.sort-order=desc&whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc) on AWS can provide access to dashboards, monitoring systems, data collection, and summarization tools that use ML algorithms that meet sustainability goals. Meeting sustainability goals is paramount to many use customers in travel and hospitality industries.

 The following diagram illustrates event-driven IOT sensor data for near real-time predictive analytics.

![A diagram that shows how you can derive near real-time predictive analytics from IOT data .](http://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/images/iot-data.png)

 The steps that data follows through the architecture are as follows:

1.  Data originates in IOT devices such as medical devices, car sensors, industrial IOT sensors, and so on. This telemetry data is collected close to the devices using [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-gg.html), which enables cloud capabilities to local devices.

1.  Data is then ingested into the cloud using edge-to-cloud interface services such as [AWS IOT Core](https://aws.amazon.com/iot-core/?nc=sn&loc=2&dn=3), which is a managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices, or [AWS IOT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html), which is a managed service that lets you collect, model, analyze, and visualize data from industrial equipment at scale.

1.  Stream data ingested into the cloud gets transformed in near-real time using [Amazon Managed Service for Apache Flink](https://aws.amazon.com/kinesis/data-analytics/?nc=sn&loc=1), which offers an easy way to transform and analyze streaming data in near real-time with Apache Flink and Apache Beam frameworks. Stream data often needs to be enriched using lookup data which is hosted in a data warehouse. Amazon Redshift uses customer integration or stream aggregates (for example, one minute or five minutes) from Managed Service for Apache Flink. The Flink application gets written into Amazon Redshift for further business intelligence (BI) reporting downstream.

1.  [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) is a fully ML learning service. Once the ML model is trained and deployed in SageMaker AI, inferences are invoked in micro-batch using [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html). Inferenced data is sent to [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/the-elk-stack/what-is-opensearch/) to create personalized monitoring dashboards using [Amazon OpenSearch Service Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/dashboards.html).

1.  The data lake stores telemetry data for future batch analytics. The data is micro-batch streamed into the S3 data lake using [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html), which is a fully managed service for delivering near real-time streaming data to destinations such as S3, Amazon Redshift, Amazon OpenSearch Service, Splunk, and any custom HTTP endpoints or owned by supported third-party service providers, including Datadog, Dynatrace, LogicMonitor, MongoDB, New Relic, and Sumo Logic.

## Build personalized recommendations architecture on AWS
<a name="build-personalized-recommendations-architecture-on-aws"></a>

 Consumers are increasingly engaging with businesses through digital surfaces and touchpoints. Every touchpoint is an opportunity for businesses to give their consumers an experience tailored to their preferences and needs. In fact, consumers now expect personalized experiences from businesses. [Market research tells us 63% of consumers](https://www.business2community.com/marketing/30-amazing-personalization-statistics-02289044) see personalization as the standard level of service. Generic recommendations no longer meet customer expectations.

 Some of the common use cases and solutions that fit under these personalized recommendations architecture patterns are as follows:
+  **Personalization experience** — Personalize users’ homepages with product or content recommendations based on their unique preferences and behavior. Personalize push notifications and marketing emails with individualized product, content, and promotional recommendations to help users find fresh, new products and content based on their unique tastes and preferences.
+  **Personalization in retail** — Improving the customer experience by providing product recommendations based on their shopping history. Recommend similar items on product details pages to help users easily find what they are looking for.
+  **Personalization in media and entertainment** — Deliver highly relevant, individualized content recommendations for videos, music, and e-books. Create personalized content carousels for every user based on their content consumption history.

 The following diagram illustrates the system for building personalized recommendations on AWS.

![A diagram that shows how you can build real-time recommendations on AWS .](http://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/images/real-time-recs.png)

 The steps through the architecture are as follows:

1.  **Data preparation —** Collect user interaction data such as item views, and item clicks. This plays a pivotal role in building a personalized recommendation. Once data is collected, upload your user interaction data into Amazon S3, then perform data cleaning using AWS Glue DataBrew to train the model in [Amazon Personalize](https://aws.amazon.com/personalize/) for real-time recommendations.

1.  **Train the model with Amazon Personalize** — The data we use for modeling on Amazon Personalize consists of three types:
   +  **The activity of your users, also known as events** — Examples include items your users click on, purchasing, and watching. The events you choose to send Amazon Personalize are dependent on your business domain. This dataset has the strongest signal for personalization, and is the only one required for personalization.
   +  **Details about your items**, such as price point, category information, genre, and so on. Essentially, information in your catalog. This dataset is optional, but very useful for scenarios such as recommending new items. Personalize also enables customers to unlock the information trapped in their product descriptions, reviews, item synopses, or other unstructured text using state-of-the-art natural language processing (NLP) techniques. Amazon Personalize automatically extracts key information about the items in your catalog to use when generating recommendations for your users.
   +  **Details about the users**, such as their location, age, and so on.

1.  **Get real time recommendations —** Once you have the data, you can, in just a few clicks, get a custom, private, personalization model trained and hosted for you. You can then vend recommendations for your users through an API exposed through [Amazon API Gateway](https://aws.amazon.com/api-gateway/).

## Build near real-time customer engagement on AWS
<a name="build-near-real-time-customer-engagement-on-aws"></a>

 This architecture is about maximizing customer engagement by delivering targeted messaging to your users in near real-time. For a business, engaging with customers is always an important day-to-day aspect, and those communications need to be clear, concise, and well-stated. There is even more of an impact if that messaging is also targeted and customized for the customer. Using this architecture, you can interact with that customer in near real-time and, utilizing advanced ML, access targeted messaging directly applicable to the customer. It enables the collection and analysis of campaign data, and the ability to use that data to create customized models within Amazon SageMaker AI. This allows you to be able to target a specific customer, or group of customers, and address their needs on a near real-time basis. This pattern can help you develop a production level SageMaker AI model, and a feedback loop that can unlock value from marketing campaign data.

 Some of the common use cases and solutions that would work with this architecture are as follows:
+  **Churn modeling** – Using all the relevant data stored within your data lake, you have the ability to create a churn model. This is an AI/ML algorithm using a known set of historical data to learn if similar customers will be more likely to leave in the future. This information can then be used to engage with the customer and save their business.
+  **Recommendation modeling via customer segmentation** – Not all customers are alike, and they won’t all respond to the same type of marketing campaign. But by creating multiple personas and assigning the customer base to those personas, a marketing team can create personalized messaging or promotions for specific groups.
+  **Marketing efficiency** – Collecting streaming event data such as opens and clicks, and allowing analysis of an ongoing campaign. Stream this data directly into your data lake, and augment this data with other data located there
+  **Customer engagement** – Use transactional messaging to communicate with customers based upon information that has just happened.

![A diagram that depicts near real-time customer engagement architecture on AWS .](http://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/images/customer-engagement.png)

 The steps in this architecture are as follows:

1.  **Initialize Pinpoint and create a marketing project** — You first need to configure your project to add your users and their contact info, such as email addresses. At this time, you also need to configure your metrics collection to ensure that you can capture your customer interactions to Amazon S3.

1.  **Near real-time data ingestion** — Grab data from Amazon Pinpoint in near real-time through [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/). Optionally, you can change this to an [Amazon Kinesis Data Stream](https://aws.amazon.com/kinesis/data-streams/) for near real-time use cases. This data is collected into S3, and used to both train the ML model and to analyze activity in your [Quick dashboard](https://docs.aws.amazon.com/quicksight/latest/user/example-create-a-dashboard.html).

1.  **SageMaker AI model implementation** — Using a combination of [Amazon Pinpoint](https://aws.amazon.com/pinpoint/) engagement data with other customer demographic data, you can train a model that predicts the likelihood of customer churn (or segmentation, or other customer modeling insight). This is done in an iterative manner until you validate that your model is effective. Once that’s done, you can set up a SageMaker AI endpoint to host this model and run inference against. This is done in a batch manner. It exports the results to Amazon Pinpoint and S3 for consumption.

1.  **Data consumption with Athena and QuickSight** — View and analyze all of the data being collected from the Amazon Pinpoint engagement, and combine it with other data facts from your data lake with Amazon Athena. You can explore this data and run ad-hoc SQL queries to gain direct insight directly from S3 storage. Combine this with Quick to visualize these insights and share them with others in the organization.

## Build fraud detection architectures on AWS
<a name="build-fraud-detection-architectures-on-aws"></a>

 The ability to move fast and serve customers in near real-time is becoming necessary for businesses to stop fraud in its tracks. Fraud represents a significant problem for businesses, and by addressing this challenge as soon as it occurs, the ability to recover from and reduce damages is greatly increased. Using this architecture, you can perform fraud detection in near real-time, and build fraud detection visualization dashboards for further analysis.

 The AWS Solutions Implementation, [Fraud Detection Using Machine Learning](https://aws.amazon.com/solutions/implementations/fraud-detection-using-machine-learning/), enables you to run automated transaction processing. This can be on an example dataset or your own dataset. The included ML model detects potentially fraudulent activity, and flags that activity for review. The following diagram presents an architecture you can automatically deploy using the solution’s implementation guide, and accompanying [AWS CloudFormation](https://aws.amazon.com/cloudformation/) template.

 Some of the common use cases and solutions that work with this architecture are as follows:
+  **Fraud detection** – Organizations with online businesses have to be on guard constantly for fraudulent activity, such as fake accounts or payments made with stolen credit cards.
+  **Near real-time analytics** – Use this architecture to understand the fraudulent activities data that you have streaming.

![A diagram depicting a fraud detection architecture on AWS .](http://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/images/fraud-detection.png)

 The steps through the architecture are as follows:

1.  **Develop a fraud prediction machine learning model —** The [AWS CloudFormation Template](https://aws.amazon.com/cloudformation/resources/templates/) deploys an example dataset of credit card transactions contained in an S3 bucket. An Amazon SageMaker AI notebook instance with different ML models is trained on the dataset.

1.  **Perform fraud prediction** — The solution also deploys an [AWS Lambda](https://aws.amazon.com/lambda) function that processes transactions from the example dataset. It invokes the two SageMaker AI endpoints that assign anomaly scores and classification scores to incoming data points. An [Amazon API Gateway](https://aws.amazon.com/api-gateway) REST API initiates predictions using signed HTTP requests. An [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose) delivery stream loads the processed transactions into another Amazon S3 bucket for storage. The solution also provides an example of how to invoke the prediction REST API as part of the Amazon SageMaker AI notebook.

1.  **Analyze fraud transactions —** Once the transactions have been loaded into S3, you can use analytics tools and services for visualization, reporting, ad-hoc queries, and more detailed analysis.
