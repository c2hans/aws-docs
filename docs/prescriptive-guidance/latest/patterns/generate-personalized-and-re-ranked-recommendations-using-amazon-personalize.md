---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-personalized-and-re-ranked-recommendations-using-amazon-personalize.html
---

# Generate personalized and re-ranked recommendations using Amazon Personalize
<a name="generate-personalized-and-re-ranked-recommendations-using-amazon-personalize"></a>

*Mason Cahill, Matthew Chasse, and Tayo Olajide, Amazon Web Services*

## Summary
<a name="generate-personalized-and-re-ranked-recommendations-using-amazon-personalize-summary"></a>

This pattern shows you how to use Amazon Personalize to generate personalized recommendations—including re-ranked recommendations—for your users based on the ingestion of real-time user-interaction data from those users. The example scenario used in this pattern is based on a pet adoption website that generates recommendations for its users based on their interactions (for example, what pets a user visits). By following the example scenario, you learn to use Amazon Kinesis Data Streams to ingest interaction data, AWS Lambda to generate recommendations and re-rank the recommendations, and Amazon Data Firehose to store the data in an Amazon Simple Storage Service (Amazon S3) bucket. You also learn to use AWS Step Functions to build a state machine that manages the solution version (that is, a trained model) that generates your recommendations.

## Prerequisites and limitations
<a name="generate-personalized-and-re-ranked-recommendations-using-amazon-personalize-prereqs"></a>

**Prerequisites**
+ An active [AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) with a [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) AWS Cloud Development Kit (AWS CDK)
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) with configured credentials
+ [Python 3.9](https://www.python.org/downloads/release/python-390/)

**Product versions**
+ Python 3.9
+ AWS CDK 2.23.0 or later
+ AWS CLI 2.7.27 or later

## Architecture
<a name="generate-personalized-and-re-ranked-recommendations-using-amazon-personalize-architecture"></a>

**Technology stack**
+ Amazon Data Firehose
+ Amazon Kinesis Data Streams
+ Amazon Personalize
+ Amazon Simple Storage Service (Amazon S3)
+ AWS Cloud Development Kit (AWS CDK)
+ AWS Command Line Interface (AWS CLI)
+ AWS Lambda
+ AWS Step Functions

**Target architecture**

The following diagram illustrates a pipeline for ingesting real-time data into Amazon Personalize. The pipeline then uses that data to generate personalized and re-ranked recommendations for users.

![Data ingestion architecture for Amazon Personalize](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/42eb193b-2347-408a-8b25-46beeb3b29ca/images/786dbd56-7d7f-41bb-90f6-d4485d73fe15.png)

The diagram shows the following workflow:

1. Kinesis Data Streams ingests real-time user data (for example, events like visited pets) for processing by Lambda and Firehose.

1. A Lambda function processes the records from Kinesis Data Streams and makes an API call to add the user-interaction in the record to an event tracker in Amazon Personalize.

1. A time-based rule invokes a Step Functions state machine and generates new solution versions for the recommendation and re-ranking models by using the events from the event tracker in Amazon Personalize.

1. Amazon Personalize [campaigns](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html) are updated by the state machine to use the new [solution version](https://docs.aws.amazon.com/personalize/latest/dg/creating-a-solution-version.html).

1. Lambda re-ranks the list of recommended items by calling the Amazon Personalize re-ranking campaign.

1. Lambda retrieves the list of recommended items by calling the Amazon Personalize recommendations campaign.

1. Firehose saves the events to an S3 bucket where they can be accessed as historical data.

## Tools
<a name="generate-personalized-and-re-ranked-recommendations-using-amazon-personalize-tools"></a>

**AWS tools**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) helps you deliver real-time [streaming data](https://aws.amazon.com/streaming-data/) to other AWS services, custom HTTP endpoints, and HTTP endpoints owned by supported third-party service providers.
+ [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) helps you collect and process large streams of data records in real time.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/what-is-personalize.html) is a fully managed machine learning (ML) service that helps you generate item recommendations for your users based on your data.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine Lambda functions and other AWS services to build business-critical applications.

**Other tools**
+ [pytest ](https://docs.pytest.org/en/7.2.x/index.html)is a Python framework for writing small, readable tests.
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**Code**

The code for this pattern is available in the GitHub [Animal Recommender](https://github.com/aws-samples/personalize-pet-recommendations) repository. You can use the AWS CloudFormation template from this repository to deploy the resources for the example solution.

**Note**
The Amazon Personalize solution versions, event tracker, and campaigns are backed by [custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) (within the infrastructure) that expand on native CloudFormation resources.

## Epics
<a name="generate-personalized-and-re-ranked-recommendations-using-amazon-personalize-epics"></a>

### Create the infrastructure
<a name="create-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an isolated Python environment. | **Mac/Linux setup**1. To manually create a virtual environment, run the `$ python3 -m venv .venv` command from your terminal.<br />2. After the init process completes, run the `$ source .venv/bin/activate` command to activate the virtual environment.<br />**Windows setup**<br />To manually create a virtual environment, run the `% .venv\Scripts\activate.bat` command from your terminal. | DevOps engineer |
| Synthesize the CloudFormation template. | 1. To install the required dependencies, run the `$ pip install -r requirements.txt` command from your terminal.<br />2. In the AWS CLI, set the following environment variables:`export ACCOUNT_ID=123456789``export CDK_DEPLOY_REGION=us-east-1``export CDK_ENVIRONMENT=dev`<br />3. In the `config/{env}.yml` file, update `vpcId` to match your virtual private cloud (VPC) ID.<br />4. To synthesize the CloudFormation template for this code, run the `$ cdk synth` command.In step 2, `CDK_ENVIRONMENT` refers to the `config/{env}.yml` file. | DevOps engineer |
| Deploy resources and create infrastructure. | To deploy the solution resources, run the `./deploy.sh` command from your terminal.<br />This command installs the required Python dependencies. A Python script creates an S3 bucket and an AWS Key Management Service (AWS KMS) key, and then adds the seed data for the initial model creations. Finally, the script runs `cdk deploy` to create the remaining infrastructure.The initial model training happens during stack creation. It can take up to two hours for the stack to finish getting created. | DevOps engineer |

## Related resources
<a name="generate-personalized-and-re-ranked-recommendations-using-amazon-personalize-resources"></a>
+ [Animal Recommender](https://github.com/aws-samples/personalize-pet-recommendations) (GitHub)
+ [AWS CDK Reference Documentation](https://docs.aws.amazon.com/cdk/api/v2/)
+ [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
+ [Optimize personalized recommendations for a business metric of your choice with Amazon Personalize](https://aws.amazon.com/blogs/machine-learning/optimize-personalized-recommendations-for-a-business-metric-of-your-choice-with-amazon-personalize/) (AWS Machine Learning Blog)

## Additional information
<a name="generate-personalized-and-re-ranked-recommendations-using-amazon-personalize-additional"></a>

**Example payloads and responses**

*Recommendation Lambda function*

To retrieve recommendations, submit a request to the recommendation Lambda function with a payload in the following format:

```
{
  "userId": "3578196281679609099",
  "limit": 6
}
```

The following example response contains a list of animal groups:

```
[{"id": "1-domestic short hair-1-1"},
{"id": "1-domestic short hair-3-3"},
{"id": "1-domestic short hair-3-2"},
{"id": "1-domestic short hair-1-2"},
{"id": "1-domestic short hair-3-1"},
{"id": "2-beagle-3-3"},
```

If you leave out the `userId` field, the function returns general recommendations.

*Re-ranking Lambda function*

To use re-ranking, submit a request to the re-ranking Lambda function. The payload contains the `userId` of all the item IDs to be re-ranked and their metadata. The following example data uses the Oxford Pets classes for `animal_species_id` (1=cat, 2=dog) and integers 1-5 for `animal_age_id` and `animal_size_id`:

```
{
   "userId":"12345",
   "itemMetadataList":[
      {
         "itemId":"1",
         "animalMetadata":{
            "animal_species_id":"2",
            "animal_primary_breed_id":"Saint_Bernard",
            "animal_size_id":"3",
            "animal_age_id":"2"
         }
      },
      {
         "itemId":"2",
         "animalMetadata":{
            "animal_species_id":"1",
            "animal_primary_breed_id":"Egyptian_Mau",
            "animal_size_id":"1",
            "animal_age_id":"1"
         }
      },
      {
         "itemId":"3",
         "animalMetadata":{
            "animal_species_id":"2",
            "animal_primary_breed_id":"Saint_Bernard",
            "animal_size_id":"3",
            "animal_age_id":"2"
         }
      }
   ]
}
```

The Lambda function re-ranks these items, and then returns an ordered list that includes the item IDs and the direct response from Amazon Personalize. This is a ranked list of the animal groups that the items are in and their score. Amazon Personalize uses [User-Personalization](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html) and [Personalized-Ranking](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-search.html) recipes to include a score for each item in the recommendations. These scores represent the relative certainty that Amazon Personalize has about which item the user will choose next. Higher scores represent greater certainty.

```
{
   "ranking":[
      "1",
      "3",
      "2"
   ],
   "personalizeResponse":{
      "ResponseMetadata":{
         "RequestId":"a2ec0417-9dcd-4986-8341-a3b3d26cd694",
         "HTTPStatusCode":200,
         "HTTPHeaders":{
            "date":"Thu, 16 Jun 2022 22:23:33 GMT",
            "content-type":"application/json",
            "content-length":"243",
            "connection":"keep-alive",
            "x-amzn-requestid":"a2ec0417-9dcd-4986-8341-a3b3d26cd694"
         },
         "RetryAttempts":0
      },
      "personalizedRanking":[
         {
            "itemId":"2-Saint_Bernard-3-2",
            "score":0.8947961
         },
         {
            "itemId":"1-Siamese-1-1",
            "score":0.105204
         }
      ],
      "recommendationId":"RID-d97c7a87-bd4e-47b5-a89b-ac1d19386aec"
   }
}
```

*Amazon Kinesis payload*

The payload to send to Amazon Kinesis has the following format:

```
{
    "Partitionkey": "randomstring",
    "Data": {
        "userId": "12345",
        "sessionId": "sessionId4545454",
        "eventType": "DetailView",
        "animalMetadata": {
            "animal_species_id": "1",
            "animal_primary_breed_id": "Russian_Blue",
            "animal_size_id": "1",
            "animal_age_id": "2"
        },
        "animal_id": "98765"

    }
}
```

**Note**
The `userId` field is removed for an unauthenticated user.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
