---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/aws-well-architected-pillars.html
---

# AWS Well-Architected pillars
<a name="aws-well-architected-pillars"></a>

This guidance uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this guidance.

The machine-learning lifecycle is the iterative process, with instructions and best practices, to use across defined phases while developing an ML workload. It adds clarity and structure for making a machine learning project successful. The [Well-Architected machine learning lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/well-architected-machine-learning-lifecycle.html) superimposes the Well-Architected Framework pillars to each of the machine learning lifecycle phases illustrated in the center of the following figure.

 **The Well-Architected machine learning lifecycle**

![The Well-Architected machine learning lifecycle](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/wa-diagram.png)

## Operational Excellence
<a name="operational-excellence"></a>

This section describes how we architected this guidance using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).

The QnABot on AWS guidance pushes metrics to Amazon CloudWatch at various stages to provide observability into the infrastructure; Lambda functions, AI services, Amazon S3 buckets, and the rest of the guidance components. AWS Amplify manages CI/CD and infrastructure deployment in code. The application layer adds data processing errors to the Amazon Simple Queue Service (Amazon SQS) queue and displays them for user response.

## Security
<a name="security"></a>

This section describes how we architected this guidance using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+ Content designer UI app users and the Amazon Lex client are authenticated and authorized with Amazon Cognito.
+ User permissions to app accounts are managed in the Amazon DynamoDB.
+ All inter-service communications use AWS Identity and Access Management (IAM) roles.
+ All multi-account communications use IAM roles.
+ All roles used by the guidance follow least-privilege access. That is, they contain only the minimum permissions required so the service can function properly.
+ Communication end user and Amazon API Gateway uses Bearer token generated and handed by Amazon Cognito.
+ All data storage including Amazon S3 buckets have encryption at rest.

## Reliability
<a name="reliability"></a>

This section describes how we architected this guidance using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ The guidance uses AWS Serverless Services wherever possible (examples Lambda, API Gateway, Amazon S3, and Amazon Lex) to ensure high availability and recovery from service failure.
+ The guidance protects against state machine definition errors by having automated tests performed on the guidance.
+ Data processing uses AWS Lambda functions. Data is stored in DynamoDB and Amazon S3, so it persists in multiple Availability Zones by default.

## Performance Efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this guidance using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+ The guidance as mentioned earlier uses serverless architecture throughout this guidance.
+ The guidance can be launched in any Region that supports AWS services in this guidance such as: AWS Lambda, Amazon API Gateway, AWS S3, Amazon Lex, Amazon Kendra, and Amazon Comprehend.
+ AWS automatically tests and deploys the guidance every day. Solutions architects and subject matter experts also review it to identify areas for experimentation and improvement.
+ The QnABot on AWS CLI supports the capability to import and export questions and answers from your QnABot setup are designed to reduce IT overhead for maintenance and upkeep.

## Cost Optimization
<a name="cost-optimization"></a>

This section describes how we architected this guidance using the principles and best practices of the [cost optimization](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+ The guidance uses serverless architecture therefore, customers only get charged for what they use.
+ The compute layer defaults to AWS Lambda, so it provides pay per use. DynamoDB indexes are selected to reduce throughput cost for queries.
+ The guidance provides an option to the user to use more advanced AI/ML services. Services such as Amazon Kendra are optional and can be turned on or off to reduce the cost for users who don’t intend to use these features.

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this guidance using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+ The guidance uses managed and serverless services to minimize the environmental impact of backend services. To support sustainability, the guidance maximizes the use of AWS AI services. The serverless design (using Lambda and DynamoDB) and managed services (such as AWS Amplify) reduce carbon footprint compared to continually operating on-premises servers.
