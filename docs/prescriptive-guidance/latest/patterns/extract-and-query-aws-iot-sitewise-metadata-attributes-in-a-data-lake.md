---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/extract-and-query-aws-iot-sitewise-metadata-attributes-in-a-data-lake.html
---

# Extract and query AWS IoT SiteWise metadata attributes in a data lake
<a name="extract-and-query-aws-iot-sitewise-metadata-attributes-in-a-data-lake"></a>

*Ambarish Dongaonkar, Amazon Web Services*

## Summary
<a name="extract-and-query-aws-iot-sitewise-metadata-attributes-in-a-data-lake-summary"></a>

AWS IoT SiteWise uses asset models and hierarchies to represent your industrial equipment, processes, and facilities. Each model or asset can have multiple attributes that are specific to your environment. Example metadata attributes include the site or physical location of the asset, plant details, and equipment identifiers. These attribute values complement asset measurement data to maximize the business value. Machine learning (ML) can provide additional insights into this metadata and streamline engineering tasks.

However, metadata attributes can’t be queried directly from the AWS IoT SiteWise service. To make the attributes queryable, you must extract and ingest them into a data lake. This pattern uses a Python script to extract the attributes for all AWS IoT SiteWise assets and ingest them into a data lake in an Amazon Simple Storage Service (Amazon S3) bucket. When you have completed this process, you can use SQL queries in Amazon Athena to access the AWS IoT SiteWise metadata attributes and other datasets, such as measurement datasets. The metadata attribute information is also useful when working with AWS IoT SiteWise monitors or dashboards. You can also build an [Amazon Quick Sight dashboard](https://docs.aws.amazon.com/quicksuite/latest/userguide/quick-bi.html) by using the extracted attributes in the Amazon S3 bucket.

The pattern has reference code, and you can you can implement the code by using the best compute services for your use case, such as AWS Lambda or AWS Glue.

## Prerequisites and limitations
<a name="extract-and-query-aws-iot-sitewise-metadata-attributes-in-a-data-lake-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ Permissions to set up AWS Lambda functions or AWS Glue jobs.
+ An Amazon S3 bucket.
+ The asset models and hierarchies are set up in AWS IoT SiteWise. For more information, see [Creating asset models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-asset-models.html) in the AWS IoT SiteWise documentation.

## Architecture
<a name="extract-and-query-aws-iot-sitewise-metadata-attributes-in-a-data-lake-architecture"></a>

You can use a Lambda function or an AWS Glue job to complete this process. We recommend using Lambda if you have less than 100 models and each model has an average of 15 or fewer attributes. For all other use cases, we recommend using AWS Glue.

The solution architecture and workflow are shown in the following diagram.

![Architecture diagram showing the extraction and query process described.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/22b59ff7-3df3-4a5b-9973-d43967bd58fd/images/fa3d80bf-df9a-49fe-971c-a055339b2cd2.png)

1. The scheduled AWS Glue job or Lambda function runs. It extracts the asset metadata attributes from AWS IoT SiteWise and ingests them into an Amazon S3 bucket.

1. An AWS Glue crawler crawls the extracted data in the Amazon S3 bucket and creates tables in an AWS Glue Data Catalog.

1. Using standard SQL, Amazon Athena queries the tables in the AWS Glue Data Catalog.

**Automation and scale**

You can schedule the Lambda function or AWS Glue job to run daily or weekly, according to the update frequency of your AWS IoT SiteWise asset configurations.

There is no limit to the number of AWS IoT SiteWise assets that the sample code can process, but a large number of assets can increase the amount of time required to complete the process.

## Tools
<a name="extract-and-query-aws-iot-sitewise-metadata-attributes-in-a-data-lake-tools"></a>
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon S3 by using standard SQL.
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed extract, transform, and load (ETL) service. It helps you reliably categorize, clean, enrich, and move data between data stores and data streams.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html) helps you collect, model, analyze, and visualize data from industrial equipment at scale.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) is a software development kit that helps you integrate your Python application, library, or script with AWS services.

## Epics
<a name="extract-and-query-aws-iot-sitewise-metadata-attributes-in-a-data-lake-epics"></a>

### Set up the job or function
<a name="set-up-the-job-or-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure permissions in IAM. | In the IAM console, grant permissions to the IAM role assumed by the Lambda function or AWS Glue job to do the following:+ Read from the AWS IoT SiteWise service<br />+ Write to the Amazon S3 bucket<br />For more information, see [Creating a role for an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console) in the IAM documentation. | General AWS |
| Create the Lambda function or AWS Glue job. | If you are using Lambda, create a new Lambda function. For **Runtime**, choose **Python**. For more information, see [Building Lambda functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html) in the Lambda documentation.<br />If you are using AWS Glue, create a new Python shell job in the AWS Glue console. For more information, see [Adding Python shell jobs](https://docs.aws.amazon.com/glue/latest/dg/add-job-python.html#create-job-python-properties) in the AWS Glue documentation.  | General AWS |
| Update the Lambda function or AWS Glue job. | Modify the new Lambda function or AWS Glue job, and enter the code sample in the [Additional information](#extract-and-query-aws-iot-sitewise-metadata-attributes-in-a-data-lake-additional) section. Modify the code as needed for your use case. For more information, see [Edit code using the console editor](https://docs.aws.amazon.com/lambda/latest/dg/foundation-console.html#code-editor) in the Lambda documentation and see [Working with scripts](https://docs.aws.amazon.com/glue/latest/dg/console-edit-script.html) in theAWS Glue documentation. | General AWS |

### Run the job or function
<a name="run-the-job-or-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the Lambda function or AWS Glue job. | Run the Lambda function or AWS Glue job. For more information, see [Invoke the Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html#get-started-invoke-manually) in the Lambda documentation or see [Starting jobs using triggers](https://docs.aws.amazon.com/glue/latest/dg/trigger-job.html) in the AWS Glue documentation. This extracts the metadata attributes for the assets and models in the AWS IoT SiteWise hierarchy and stores them in the specified Amazon S3 bucket. | General AWS |
| Set up an AWS Glue crawler. | Set up an AWS Glue crawler with the necessary format classifier for a CSV-formatted file. Use the Amazon S3 bucket and prefix details used in the Lambda function or AWS Glue job. For more information, see [Defining crawlers](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) in the AWS Glue documentation. | General AWS |
| Run the AWS Glue crawler. | Run the crawler to process the data file created by the Lambda function or AWS Glue job. The crawler creates a table in the specified AWS Glue Data Catalog. For more information, see or [Starting crawlers using triggers](https://docs.aws.amazon.com/glue/latest/dg/trigger-job.html) in the AWS Glue documentation. | General AWS |
| Query the metadata attributes. | Using Amazon Athena, use standard SQL to query the AWS Glue Data Catalog as needed for your use case. You can join the metadata attribute table with other databases and tables. For more information, see [Getting Started](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) in the Amazon Athena documentation. | General AWS |

## Related resources
<a name="extract-and-query-aws-iot-sitewise-metadata-attributes-in-a-data-lake-resources"></a>
+ [Amazon Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
+ [AWS Glue documentation](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
+ [AWS IoT SiteWise API reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/index.html)
+ [AWS IoT SiteWise user guide](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html)
  + [Getting started](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/getting-started.html)
  + [Modeling industrial assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/industrial-asset-models.html)
  + [Defining relationships between asset models (hierarchies)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html)
  + [Associating and disassociating assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-associated-assets.html)
  + [Creating the AWS IoT SiteWise demo](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/getting-started-demo.html#create-getting-started-demo)
+ [IOTSiteWise](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html) (SDK for Python documentation)
+ [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html)

## Additional information
<a name="extract-and-query-aws-iot-sitewise-metadata-attributes-in-a-data-lake-additional"></a>

**Code**

The sample code provided is for reference, and you can customize this code as needed for your use case.

```
# Following code can be used in an AWS Lambda function or in an AWS Glue Python shell job.
# IAM roles used for this job need read access to the AWS IoT SiteWise service and write access to the S3 bucket.
sw_client = boto3.client('iotsitewise')
s3_client = boto3.client('s3')
output = io.StringIO()

attribute_list=[]
bucket = '{3_bucket name}'
prefix = '{s3_bucket prefix}'
output.write("model_id,model_name,asset_id,asset_name,attribuet_id,attribute_name,attribute_value\n")

m_resp = sw_client.list_asset_models()
for m_rec in m_resp['assetModelSummaries']:
     model_id = m_rec['id']
     model_name = m_rec['name']

     attribute_list.clear()
     dam_response = sw_client.describe_asset_model(assetModelId=model_id)
     for rec in dam_response['assetModelProperties']:
         if 'attribute' in rec['type']:
            attribute_list.append(rec['name'])

     response = sw_client.list_assets(assetModelId=model_id, filter='ALL')
     for asset in response['assetSummaries']:
         asset_id = asset['id']
         asset_name = asset['name']
         resp = sw_client.describe_asset(assetId=asset_id)
         for rec in resp['assetProperties']:
            if rec['name'] in attribute_list:
                p_resp = sw_client.get_asset_property_value(assetId=asset_id, propertyId=rec['id'])
                if 'propertyValue' in p_resp:
                    if p_resp['propertyValue']['value']:
                        if 'stringValue' in p_resp['propertyValue']['value']:
                             output.write(model_id + "," + model_name + "," + asset_id + "," + asset_name + "," + rec['id'] + "," + rec['name'] + "," + str(p_resp['propertyValue']['value']['stringValue']) + "\n")
                        if 'doubleValue' in p_resp['propertyValue']['value']:
                             output.write(model_id + "," + model_name + "," + asset_id + "," + asset_name + "," + rec['id'] + "," + rec['name'] + "," + str(p_resp['propertyValue']['value']['doubleValue']) + "\n")
                        if 'integerValue' in p_resp['propertyValue']['value']:
                             output.write(model_id + "," + model_name + "," + asset_id + "," + asset_name + "," + rec['id'] + "," + rec['name'] + "," + str(p_resp['propertyValue']['value']['integerValue']) + "\n")
                         if 'booleanValue' in p_resp['propertyValue']['value']:
                             output.write(model_id + "," + model_name + "," + asset_id + "," + asset_name + "," + rec['id'] + "," + rec['name'] + "," + str(p_resp['propertyValue']['value']['booleanValue']) + "\n")

output.seek(0)
s3_client.put_object(Bucket=bucket, Key= prefix + '/data.csv', Body=output.getvalue())
output.close()
```
