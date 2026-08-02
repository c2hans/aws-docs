---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet.html
---

# Three AWS Glue ETL job types for converting data to Apache Parquet
<a name="three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet"></a>

*Adnan Alvee, Nith Govindasivan, and Karthikeyan Ramachandran, Amazon Web Services*

## Summary
<a name="three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet-summary"></a>

On the Amazon Web Services (AWS) Cloud, AWS Glue is a fully managed extract, transform, and load (ETL) service. AWS Glue makes it cost-effective to categorize your data, clean it, enrich it, and move it reliably between various data stores and data streams.

This pattern provides different job types in AWS Glue and uses three different scripts to demonstrate authoring ETL jobs.

You can use AWS Glue to write ETL jobs in a Python shell environment. You can also create both batch and streaming ETL jobs by using Python (PySpark) or Scala in a managed Apache Spark environment. To get you started with authoring ETL jobs, this pattern focuses on batch ETL jobs using Python shell, PySpark, and Scala. Python shell jobs are meant for workloads requiring lesser compute power. The managed Apache Spark environment is meant for workloads requiring high compute power.

Apache Parquet is built to support efficient compression and encoding schemes. It can speed up your analytics workloads because it stores data in a columnar fashion. Converting data to Parquet can save you storage space, cost, and time in the longer run. To learn more about Parquet, see the blog post [Apache Parquet: How to be a hero with the open-source columnar data format](https://blog.openbridge.com/how-to-be-a-hero-with-powerful-parquet-google-and-amazon-f2ae0f35ee04).

## Prerequisites and limitations
<a name="three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet-prereqs"></a>

**Prerequisites **
+ AWS Identity and Access Management (IAM) role (If you don’t have a role, see the [Additional information](#three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet-additional) section.)

## Architecture
<a name="three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet-architecture"></a>

**Target technology stack  **
+ AWS Glue
+ Amazon Simple Storage Service (Amazon S3)
+ Apache Parquet

**Automation and scale**
+ [AWS Glue workflows](https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html) support full automation of an ETL pipeline.
+ You can change the number of data processing units (DPUs), or worker types, to scale horizontally and vertically.

## Tools
<a name="three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet-tools"></a>

**AWS services**
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed ETL service for categorizing, cleaning, enriching, and moving your data between various data stores and data streams.

**Other tools**
+ [Apache Parquet](https://parquet.apache.org/) is an open-source column-oriented data file format designed for storage and retrieval.

**Configuration**

Use the following settings for configuring the compute power of AWS Glue ETL. To reduce costs, use the minimal settings when you run the workload that is provided in this pattern.
+ **Python shell** – You can use 1 DPU to utilize 16 GB of memory or 0.0625 DPU to utilize 1 GB of memory. This pattern uses 0.0625 DPU, which is the default in the AWS Glue console.
+ **Python or Scala for Spark** – If you choose the Spark-related job types in the console, AWS Glue by default uses 10 workers and the G.1X worker type. This pattern uses two workers, which is the minimum number allowed, with the standard worker type, which is sufficient and cost effective.

The following table displays the different AWS Glue worker types for the Apache Spark environment. Because a Python shell job does not use the Apache Spark environment to run Python, it is not included in the table.

|
|
|  | Standard | G.1X | G.2X |
| --- |--- |--- |--- |
| vCPU | 4 | 4 | 8 |
| Memory | 16 GB | 16 GB | 32 GB |
| Disk space | 50 GB | 64 GB | 128 GB |
| Executor per worker | 2 | 1  | 1 |

**Code**

For the code that is used in this pattern, including the IAM role and parameter configuration, see the [Additional information](#three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet-additional) section.

## Epics
<a name="three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet-epics"></a>

### Upload the data
<a name="upload-the-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload the data into a new or existing S3 bucket. | Create or use an existing S3 bucket in your account. Upload the sample\_data.csv file from the [Attachments](#attachments-8c926709-8fa4-417f-9aaf-bcc8113d018f) section, and note the S3 bucket and prefix location. | General AWS |

### Create and run the AWS Glue job
<a name="create-and-run-the-aws-glue-job"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the AWS Glue job. | Under the ETL section of the AWS Glue console, add an AWS Glue job. Select the appropriate job type, AWS Glue version, and the corresponding DPU/Worker type and number of workers. For details, see the *Configuration* section. | Developer, cloud or data |
| Change the input and output locations. | Copy the code corresponding to your AWS Glue job, and change the input and output location that you noted in the **Upload the data** epic. | Developer, cloud or data |
| Configure the parameters. | You can use the snippets provided in the [Additional information](#three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet-additional) section to set parameters for your ETL job. AWS Glue uses four argument names internally:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet.html)<br />The `--JOB_NAME` parameter must be explicitly entered on the AWS Glue console. Choose **Jobs**, **Edit Job**, **Security configuration, script libraries, and job parameters (optional)**. Enter `--JOB_NAME` as the key and provide a value. You can also use the AWS Command Line Interface (AWS CLI) or the AWS Glue API to set this parameter. The `--JOB_NAME` parameter is used by Spark and is not needed in a Python shell environment job.<br />You must add `--` before every parameter name; otherwise, the code will not work. For example, for the code snippets, the location parameters must be invoked by `--input_loc` and `--output_loc`. | Developer, cloud or data |
| Run the ETL job. | Run your job and check the output. Note how much space was reduced from the original file. | Developer, cloud or data |

## Related resources
<a name="three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet-resources"></a>

**References **
+ [Apache Spark](https://spark.apache.org/)
+ [AWS Glue: How it works](https://docs.aws.amazon.com/glue/latest/dg/how-it-works.html)
+ [AWS Glue pricing](https://aws.amazon.com/glue/pricing/)

**Tutorials and videos **
+ [What is AWS Glue?](https://www.youtube.com/watch?v=qgWMfNSN9f4)

## Additional information
<a name="three-aws-glue-etl-job-types-for-converting-data-to-apache-parquet-additional"></a>

**IAM role**

When you create the AWS Glue jobs, you can use either an existing IAM role that has the permissions shown in the following code snippet or a new role.

To create a new role, use the following YAML code.

```
# (c) 2022 Amazon Web Services, Inc. or its affiliates. All Rights Reserved. This AWS Content is provided subject to the terms of the AWS Customer
# Agreement available at https://aws.amazon.com/agreement/ or other written agreement between Customer and Amazon Web Services, Inc.

AWSTemplateFormatVersion: "2010-09-09"

Description: This template will setup IAM role for AWS Glue service.

Resources:
  rGlueRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Principal:
              Service:
                - "glue.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole
      Policies:
        - PolicyName: !Sub "${AWS::StackName}-s3-limited-read-write-inline-policy"
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - "s3:PutObject"
                  - "s3:GetObject"
                Resource: "arn:aws:s3:::*/*"
      Tags:
        - Key  : "Name"
          Value : !Sub "${AWS::StackName}"

Outputs:
  oGlueRoleName:
    Description: AWS Glue IAM role
    Value:
      Ref: rGlueRole
    Export:
      Name: !Join [ ":", [ !Ref "AWS::StackName", rGlueRole ] ]
```

**AWS Glue Python Shell**

The Python code uses the Pandas and PyArrow libraries to convert data to Parquet. The Pandas library is already available. The PyArrow library is downloaded when you run the pattern, because it is a one-time run. You can use wheel files to convert PyArrow to a library and provide the file as a library package. For more information about packaging wheel files, see [Providing your own Python library](https://docs.aws.amazon.com/glue/latest/dg/add-job-python.html).

*AWS Glue Python shell parameters*

```
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ["input_loc", "output_loc"])
```

*AWS Glue Python shell code*

```
from io import BytesIO
import pandas as pd
import boto3
import os
import io
import site
from importlib import reload
from setuptools.command import easy_install
install_path = os.environ['GLUE_INSTALLATION']
easy_install.main( ["--install-dir", install_path, "pyarrow"] )
reload(site)
import pyarrow

input_loc = "s3://bucket-name/prefix/sample_data.csv"
output_loc = "s3://bucket-name/prefix/"

input_bucket = input_loc.split('/', 1)[0]
object_key = input_loc.split('/', 1)[1]

output_loc_bucket = output_loc.split('/', 1)[0]
output_loc_prefix = output_loc.split('/', 1)[1]

s3 = boto3.client('s3')
obj = s3.get_object(Bucket=input_bucket, Key=object_key)
df = pd.read_csv(io.BytesIO(obj['Body'].read()))

parquet_buffer = BytesIO()
s3_resource = boto3.resource('s3')
df.to_parquet(parquet_buffer, index=False)
s3_resource.Object(output_loc_bucket, output_loc_prefix +  'data' + '.parquet').put(Body=parquet_buffer.getvalue())
```

**AWS Glue Spark job with Python**

To use an AWS Glue Spark job type with Python, choose **Spark** as the job type. Choose **Spark 3.1, Python 3 with improved job startup time (Glue Version 3.0)** as the AWS Glue version.

*AWS Glue Python parameters*

```
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ["JOB_NAME", "input_loc", "output_loc"])
```

*AWS Glue Spark job with Python code*

```
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.dynamicframe import DynamicFrame
from awsglue.utils import getResolvedOptions
from awsglue.job import Job

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

input_loc = "s3://bucket-name/prefix/sample_data.csv"
output_loc = "s3://bucket-name/prefix/"

inputDyf = glueContext.create_dynamic_frame_from_options(\
    connection_type = "s3", \
    connection_options = {
        "paths": [input_loc]}, \
    format = "csv",
    format_options={
        "withHeader": True,
        "separator": ","
    })

outputDF = glueContext.write_dynamic_frame.from_options(\
    frame = inputDyf, \
    connection_type = "s3", \
    connection_options = {"path": output_loc \
        }, format = "parquet")
```

For a large number of compressed big files (for example, 1,000 files that are each about 3 MB), use the `compressionType` parameter with the `recurse` parameter to read all the files that are available within the prefix, as shown in the following code.

```
input_loc = "bucket-name/prefix/"
output_loc = "bucket-name/prefix/"

inputDyf = glueContext.create_dynamic_frame_from_options(
                    connection_type = "s3",
                    connection_options = {"paths": [input_loc],
                                            "compressionType":"gzip","recurse" :"True",
                                            },
                    format = "csv",
                    format_options={"withHeader": True,"separator": ","}
                    )
```

For a large number of compressed small files (for example, 1,000 files that are each about 133 KB), use the `groupFiles` parameter, along with both the `compressionType` and the `recurse` parameters. The `groupFiles` parameter groups small files into multiple big files, and the `groupSize` parameter controls the grouping to the specified size in bytes (for example, 1 MB). The following code snippet provides an example of using these parameters within the code.

```
input_loc = "bucket-name/prefix/"
output_loc = "bucket-name/prefix/"

inputDyf = glueContext.create_dynamic_frame_from_options(
                    connection_type = "s3",
                    connection_options = {"paths": [input_loc],
                                            "compressionType":"gzip","recurse" :"True",
                                             "groupFiles" :"inPartition",  "groupSize" :"1048576",
                                            },
                    format = "csv",
                    format_options={"withHeader": True,"separator": ","}
                    )
```

Without any change in the worker nodes, these settings enable the AWS Glue job to read multiple files (large or small, with or without compression) and write them to the target in Parquet format.

**AWS Glue Spark job with Scala**

To use an AWS Glue Spark job type with Scala, choose **Spark** as the job type and **Language** as **Scala**. Choose **Spark 3.1, Scala 2 with improved job startup time (Glue Version 3.0)** as the AWS Glue version. To save on storage space, the following AWS Glue with Scala sample also uses the `applyMapping` feature to convert data types.

*AWS Glue Scala parameters*

```
import com.amazonaws.services.glue.util.GlueArgParser val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME", "inputLoc", "outputLoc").toArray)
```

*AWS Glue Spark job with Scala code*

```
import com.amazonaws.services.glue.GlueContext
import com.amazonaws.services.glue.MappingSpec
import com.amazonaws.services.glue.DynamicFrame
import com.amazonaws.services.glue.errors.CallSite
import com.amazonaws.services.glue.util.GlueArgParser
import com.amazonaws.services.glue.util.Job
import com.amazonaws.services.glue.util.JsonOptions
import org.apache.spark.SparkContext
import scala.collection.JavaConverters._

object GlueScalaApp {
  def main(sysArgs: Array[String]) {

    @transient val spark: SparkContext = SparkContext.getOrCreate()
    val glueContext: GlueContext = new GlueContext(spark)

    val inputLoc = "s3://bucket-name/prefix/sample_data.csv"
    val outputLoc = "s3://bucket-name/prefix/"

    val readCSV = glueContext.getSource("csv", JsonOptions(Map("paths" -> Set(inputLoc)))).getDynamicFrame()

    val applyMapping = readCSV.applyMapping(mappings = Seq(("_c0", "string", "date", "string"), ("_c1", "string", "sales", "long"),
    ("_c2", "string", "profit", "double")), caseSensitive = false)

    val formatPartition = applyMapping.toDF().coalesce(1)

    val dynamicFrame = DynamicFrame(formatPartition, glueContext)

    val dataSink = glueContext.getSinkWithFormat(
        connectionType = "s3",
        options = JsonOptions(Map("path" -> outputLoc )),
        transformationContext = "dataSink", format = "parquet").writeDynamicFrame(dynamicFrame)
  }
}
```

## Attachments
<a name="attachments-8c926709-8fa4-417f-9aaf-bcc8113d018f"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/8c926709-8fa4-417f-9aaf-bcc8113d018f/attachments/attachment.zip)
