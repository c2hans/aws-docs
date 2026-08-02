---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-enterprise-economics-with-serverless/case-studies.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Case studies
<a name="case-studies"></a>

 Companies have applied serverless architectures to use cases from stock trade validation to e-commerce website construction to natural language processing. AWS serverless portfolio offers the flexibility to create a wide array of applications, including those requiring assurance programs such as PCI or HIPAA compliance.

 The following sections illustrate some of the most common use cases but are not a comprehensive list. For a complete list of customer references and use case documentation, see [Serverless Computing](https://aws.amazon.com/serverless/).

## Serverless websites, web Apps, and mobile backends
<a name="serverless-websites-web-apps-and-mobile-backends"></a>

 Serverless approaches are ideal for applications where the load can vary dynamically. Using a serverless approach means no compute costs are incurred when there is no end-user traffic while still offering instant scale to meet high demand, such as a flash sale on an e-commerce site or a social media mention that drives a sudden wave of traffic.

 Compared to traditional infrastructure approaches, it is also often significantly less expensive to develop, deliver, and operate a web or mobile backend when architected in a serverless fashion.

 AWS provides the services developers need to construct these applications rapidly:
+  Amazon Simple Storage Service (Amazon S3) and AWS Amplify offer a simple hosting solution for static content.
+  AWS Lambda, in conjunction with Amazon API Gateway, provides support for dynamic API requests using functions.
+  Amazon DynamoDB offers a simple storage solution for the session and per-user state.
+  Amazon Cognito provides an easy way to handle end-user registration, authentication, and access control to resources.
+  Developers can use AWS Serverless Application Model (SAM ) to describe the various elements of an application.
+  AWS CodeStar can set up a CI/CD toolchain with just a few clicks.

 To learn more, see the whitepaper [AWS Serverless Multi-Tier Architectures](https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/welcome.html), which provides a detailed examination of patterns for building serverless web applications. For complete reference architectures, see [Serverless Reference Architecture for creating a Web Application](https://github.com/awslabs/lambda-refarch-webapp) and [Serverless Reference Architecture for creating a Mobile Backend](https://github.com/awslabs/lambda-refarch-mobilebackend) on GitHub.

### Customer example – Neiman Marcus
<a name="customer-example-neiman-marcus"></a>

 A luxury household name, Neiman Marcus has a reputation for delivering a first-class, personalized customer service experience. To modernize and enhance that experience, the company wanted to develop Connect, an omnichannel digital selling application that would empower associates to view rich, personalized customer information with the goal of making each customer interaction unforgettable.

 Choosing a serverless architecture with mobile development solutions on Amazon Web Services (AWS) enabled the development team to launch the app much faster than in the 4 months it had originally planned. “Using AWS cloud-native and serverless technologies, we increased our speed to market by at least 50 percent and were able to accelerate the launch of Connect,” says Sriram Vaidyanathan, senior director of omni engineering at Neiman Marcus.

 This approach also greatly reduced app-building costs and provided developers with more agility for the development and rapid deployment of updates. The app elastically scales to support traffic at any volume for greater cost efficiency, and it has increased associate productivity. For more information, see the [Neiman Marcus case study](https://aws.amazon.com/solutions/case-studies/neimanmarcus-case-study).

## IoT backends
<a name="iot-backends"></a>

 The benefits that a serverless architecture brings to web and mobile apps make it easy to construct IoT backends and device-based analytic processing systems that seamlessly scale with the number of devices.

 For an example reference architecture, see [Serverless Reference Architecture for creating an IoT Backend](https://github.com/awslabs/lambda-refarch-iotbackend) on GitHub.

### Customer example – iRobot
<a name="customer-example-irobot"></a>

 iRobot, which makes robots such as the Roomba cleaning robot, uses AWS Lambda in conjunction with the AWS IoT service to create a serverless backend for its IoT platform. As a popular gift on any holiday, iRobot experiences increased traffic on these days.

 While huge traffic spikes could also mean huge headaches for the company and its customers alike, iRobot’s engineering team doesn’t have to worry about managing infrastructure or manually writing code to handle availability and scaling by running on serverless. This enables them to innovate faster and stay focused on customers. Watch the AWS re:Invent 2020 video [Building the next generation of residential robots](https://www.youtube.com/watch?v=-1PDC6UOFtE) for more information.

## Data processing
<a name="data-processing"></a>

 The largest serverless applications process massive volumes of data, much of it in real-time. Typical serverless data processing architectures use a combination of Amazon Kinesis and AWS Lambda to process streaming data, or they combine Amazon S3 and AWS Lambda to trigger computation in response to object creation or update events.

 When workloads require more complex orchestration than a simple trigger, developers can use AWS Step Functions to create stateful or long-running workflows that invoke one or more Lambda functions as they progress. To learn more about serverless data processing architectures, see the following on GitHub:
+  [Serverless Reference Architecture for Real-time Stream Processing](https://github.com/awslabs/lambda-refarch-streamprocessing)
+  [Serverless Reference Architecture for Real-time File Processing](https://github.com/awslabs/lambda-refarch-fileprocessing)
+  [Image Recognition and Processing Backend reference architecture](https://github.com/awslabs/lambda-refarch-imagerecognition)

### Customer example – FINRA
<a name="customer-example-finra"></a>

 The Financial Industry Regulatory Authority (FINRA) used AWS Lambda to build a serverless data processing solution that enables them to perform half a trillion data validations on 37 billion stock market events daily.

 In his talk at AWS re:Invent 2016 entitled [The State of Serverless Computing (SVR311)](https://youtu.be/AcGv3qUrRC4?t=1153), Tim Griesbach, Senior Director at FINRA, said, “We found that Lambda was going to provide us with the best solution for this serverless cloud solution. With Lambda, the system was faster, cheaper, and more scalable. So at the end of the day, we’ve reduced our costs by over 50 percent, and we can track it daily, even hourly.”

### Customer example – Toyota Connected
<a name="customer-example-toyota-connected"></a>

 Toyota Connected is a subsidiary of Toyota and a technology company offering connected platforms, big data, mobility services and other automotive-related services.

 Toyota Connected chose serverless computing architecture to build its Toyota Mobility Services Platform, leveraging AWS Lambda, Amazon Kinesis Data Streams (Amazon KDS), and Amazon S3 to offer personalized, localized, and predictive data to enhance the driving experience.

 With its serverless architecture, Toyota Connected seamlessly scaled to 18 times its usual traffic volume, with 18 billion transactions per month running through the platform, reducing aggregation job times from 15\+ hours to 1/40th of the time while reducing operational burden. Additionally, serverless enabled Toyota Connected to deploy the same pipeline in other geographies with smaller volumes and only pay for the resources consumed.

 For more information, read our [Big Data Blog on Toyota Connected](https://aws.amazon.com/blogs/big-data/enhancing-customer-safety-by-leveraging-the-scalable-secure-and-cost-optimized-toyota-connected-data-lake/) or watch the re:Invent 2020 video [Reimagining mobility with Toyota Connected (AUT303)](https://www.youtube.com/watch?v=IpuRyJY3B4k).

## Big data
<a name="big-data"></a>

 AWS Lambda is a perfect match for many high-volume, parallel processing workloads. For an example of a reference architecture using MapReduce, see [Reference Architecture for running serverless MapReduce jobs](https://github.com/awslabs/lambda-refarch-mapreduce).

### Customer example – Fannie Mae
<a name="customer-example-fannie-mae"></a>

 Fannie Mae, a leading source of financing for mortgage lenders, uses AWS Lambda to run an “embarrassingly parallel” workload for its financial modeling. Fannie Mae uses Monte Carlo simulation processes to project future cash flows of mortgages that help manage mortgage risk.

 The company found that its existing HPC grids were no longer meeting its growing business needs. So Fannie Mae built its new platform on Lambda, and the system successfully scaled up to 15,000 concurrent function executions during testing. The new system ran one simulation on 20 million mortgages completed in 2 hours, which is three times faster than the old system. Using a serverless architecture, Fannie Mae can run large-scale Monte Carlo simulations effectively because it doesn’t pay for idle compute resources. It can also speed up its computations by running multiple Lambda functions concurrently.

 Fannie Mae also experienced shorter than typical time-to-market because they were able to dispense with server management and monitoring, along with the ability to eliminate much of the complex code previously required to manage application scaling and reliability. See the Fannie Mae AWS Summit 2017 presentation [SMC303: Real-time Data Processing Using AWS Lambda](https://www.slideshare.net/AmazonWebServices/smc303-realtime-data-processing-using-aws-lambda/28) for more information.

## IT automation
<a name="it-automation"></a>

 Serverless approaches eliminate the overhead of managing servers, making most infrastructure tasks, including provisioning, configuration, management, alarms/monitors, and timed cron jobs, easier to create and manage.

### Customer example – Autodesk
<a name="customer-example-autodesk"></a>

 Autodesk, which makes 3D design and engineering software, uses AWS Lambda to automate its AWS account creation and management processes across its engineering organization.

 Autodesk estimates that it realized cost savings of 98 percent (factoring in estimated savings in labor hours spent provisioning accounts). It can now provision accounts in just 10 minutes instead of the 10 hours it took to provision with the previous, infrastructure-based process.

 The serverless solution enables Autodesk to automatically provision accounts, configure and enforce standards, and run audits with increased automation and fewer manual touchpoints. For more information, see the Autodesk AWS Summit 2017 presentation [SMC301: The State of Serverless Computing](https://www.slideshare.net/AmazonWebServices/smc301-the-state-of-serverless-computing-75290821/22). Visit [GitHub](https://github.com/alanwill/aws-tailor) to see the Autodesk Tailor service.

## Machine learning
<a name="machine-learning"></a>

 You can use serverless services to capture, store, and preprocess data before feeding it to your machine learning model. After training the model, you can also serve the model for prediction at scale for inference without providing or managing any infrastructure.

### Customer example – Genworth
<a name="customer-example-genworth"></a>

 Genworth Mortgage Insurance Australia Limited is a leading provider of lenders’ mortgage insurance in Australia. Genworth has more than 50 years of experience and data in this industry and wanted to use this historical information to train predictive analytics for loss mitigation machine learning models.

 To achieve this task, Genworth built a serverless machine learning pipeline at scale using services like AWS Glue, a serverless managed ETL processing service to ingest and transform data, and Amazon SageMaker AI to batch transform jobs and, perform ML inference, and process and publish the results of the analysis.

 With the ML models, Genworth could analyze recent repayment patterns for each insurance policy to prioritize them in likelihood and impact for each claim. This process was automated end-to-end to help the business make data-driven decisions and simplify high-value manual work performed by the Loss Mitigation team. Read the Machine Learning blog [How Genworth built a serverless ML pipeline on AWS using Amazon SageMaker AI and AWS Glue](https://aws.amazon.com/blogs/machine-learning/how-genworth-built-a-serverless-ml-pipeline-on-aws-using-amazon-sagemaker-and-aws-glue/) for more information.
