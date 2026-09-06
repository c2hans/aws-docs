---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/cost.html
---

# Cost
<a name="cost"></a>

 You are responsible for the cost of the AWS services used while running this solution. The total cost for running this solution depends on the amount of data being ingested and analyzed, running the solution's OpenSearch Service cluster, and the size and length of media files analyzed with Amazon Rekognition, Amazon Transcribe, and Amazon Comprehend.

 As of this revision, the cost for running this solution on 100 hours of videos totaling one terabyte with the default settings in the US East (N. Virginia) Region is **$2,149.95 (one time processing)** with **$104.60/month** **(recurring)** for Amazon S3 data storage and OpenSearch Service search engine.

 We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html)  through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each [AWS service used in this solution](aws-services-in-this-solution.md). For customers who want to process large-scale video archives, we recommend that you contact your AWS account representative for at-scale pricing.

## Example monthly cost
<a name="example-monthly-cost"></a>

 The following example is for a total file size of one terabyte, which equates to one hundred total hours of video content where each video is one hour in duration. The cost is broken down to the following categories:

1.  **Migration cost** – When the video files are uploaded and stored in Amazon Glacier Deep Archive storage. The cost is estimated based on the total size of the video files.

1.  **Ingestion cost** – When the uploaded video files are transcoded with AWS Elemental MediaConvert to create low resolution proxy video files *­*plus the ingestion workflow cost composed of AWS Step Functions state transitions and AWS Lambda compute runtime, and Amazon DynamoDB Read/Write request units.

1.  **Analysis cost** – When proxy files are analyzed with Amazon Rekognition, Amazon Transcribe, and Amazon Comprehend plus the analysis workflow cost composed of AWS Step Functions state transitions and AWS Lambda Compute runtime, and Amazon DynamoDB Read/Write request units.

1.  **Search engine cost** – When the generated metadata are indexed to an OpenSearch Service cluster. The cost depends on the number of dedicated nodes, the number of instance nodes, and the amount of Amazon EBS volume.

|  AWS service  |  Dimensions  |  Cost [USD]  |
| --- | --- | --- |
|  Migration cost (one terabyte)  |   |   |
|  S3 Glacier Deep Archive  |  $0.00099 per GB / Month \* 1024 GB  |  $1.01  |
|  Ingestion cost (100 hours)  |   |   |
|  AWS Elemental MediaConvert (SD, AVC with Professional Tier)  |  $0.012 per minutes \* 100 hours  |  $72.00  |
|  AWS Elemental MediaConvert (Audio only)  |  $0.003 per minutes \* 100 hours  |  $18.00  |
|  AWS Step Functions State transitions, AWS Lambda Compute unit (MB per 1ms), and Amazon DynamoDB Read Write Request Units  |  Varies depending on number of state transitions, the Lambda function memory size and runtime duration, and read write request to DynamoDB tables.  |  \~$1.05  |
|  Analysis cost (100 hours)  |   |   |
|  Amazon Rekognition Celebrity Recognition  |  $0.10 per minute \* 100 hours  |  $600.00  |
|  Amazon Rekognition Label Detection  |  $0.10 per minute \* 100 hours  |  $600.00  |
|  Amazon Rekognition Segment Detection (Shot and Technical Cues detections)  |  ($0.05 \+ $0.05 per minute) \* 100 hours  |  $600.00  |
|  Amazon Transcribe  |  $0.024 per minute \* 100 hours  |  $144.00  |
|  Amazon Comprehend Key Phrase Extraction  |  $0.0001 per unit <br /> Vary depends on number of characters extracted from audio dialogue of the video files  |  \~$5.00  |
|  Amazon Comprehend Entity Recognition  |  $0.0001 per unit <br /> Vary depends on number of characters extracted from audio dialogue of the video files  |  \~$5.00  |
|  AWS Step Functions State transitions, AWS Lambda Compute unit (MB per 1ms), and Amazon DynamoDB Read Write Request Units  |  Varies depending on number of state transitions, the Lambda function memory size and runtime duration, and read write request to DynamoDB tables.  |  \~$ 0.30  |
|  Search engine cost  |   |   |
|  Amazon OpenSearch Service dedicated node (t3.small.search)  |  $0.036 per hour \* 0 node  |  $0.00  |
|  Amazon OpenSearch Service instance node (m5.large.search)  |  $0.142 per hour \* 1 node  |  $102.24  |
|  Amazon OpenSearch Service EBS Volume (GP2)  |  $0.135 per GB / month \* 10 GB  |  $1.35  |
|  Total cost (based on one terabyte with 100 hours of videos)  |   |   |
|  Monthly recurring cost (S3 storage and Amazon OpenSearch Service cluster)  |  $1.01 \+ $102.24 \+ 1.35  |  $104.60  |
|  One-time processing cost (AWS Elemental MediaConvert, Amazon Rekognition, Transcribe, Comprehend, AWS Step Functions, AWS Lambda)  |  ($72 \+ $18) \+ $1.05 \+ ($600 \+ $600 \+ $600) \+ $144 \+ ($5 \+ $5) \+ $0.30  |  $2,045.35  |
|  Total:  |   |  $2,149.95  |
