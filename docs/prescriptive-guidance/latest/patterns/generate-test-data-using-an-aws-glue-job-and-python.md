---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-test-data-using-an-aws-glue-job-and-python.html
---

# Generate test data using an AWS Glue job and Python
<a name="generate-test-data-using-an-aws-glue-job-and-python"></a>

*Moinul Al-Mamun, Amazon Web Services*

## Summary
<a name="generate-test-data-using-an-aws-glue-job-and-python-summary"></a>

This pattern shows you how to quickly and easily generate millions of sample files concurrently by creating an AWS Glue job written in Python. The sample files are stored in an Amazon Simple Storage Service (Amazon S3) bucket. The ability to quickly generate a large number of sample files is important for testing or evaluating services in the AWS Cloud. For example, you can test the performance of AWS Glue Studio or AWS Glue DataBrew jobs by performing data analysis on millions of small files in an Amazon S3 prefix.

Although you can use other AWS services to generate sample datasets, we recommend that you use AWS Glue. You don’t need to manage any infrastructure because AWS Glue is a serverless data processing service. You can just bring your code and run it in an AWS Glue cluster. Additionally, AWS Glue provisions, configures, and scales the resources required to run your jobs. You pay only for the resources that your jobs use while running.

## Prerequisites and limitations
<a name="generate-test-data-using-an-aws-glue-job-and-python-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) to work with the AWS account

**Product versions**
+ Python 3.9
+ AWS CLI version 2

**Limitations**

The maximum number of AWS Glue jobs per trigger is 50. For more information, see [AWS Glue endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/glue.html).

## Architecture
<a name="generate-test-data-using-an-aws-glue-job-and-python-architecture"></a>

The following diagram depicts an example architecture centered around an AWS Glue job that writes its output (that is, sample files) to an S3 bucket.

![Workflow shows AWS CLI initiates AWS Glue job that writes output to S3 bucket.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f35943e8-3b2b-410e-a3f0-05e1ebd357d0/images/452ccbda-71f2-42b8-976d-bcc968bb1dab.png)

The diagram includes the following workflow:

1. You use the AWS CLI, AWS Management Console, or an API to initiate the AWS Glue job. The AWS CLI or API enables you to automate the parallelization of the invoked job and reduce the runtime for generating sample files.

1. The AWS Glue job generates file content randomly, converts the content into CSV format, and then stores the content as an Amazon S3 object under a common prefix. Each file is less than a kilobyte. The AWS Glue job accepts two user-defined job parameters: `START_RANGE` and `END_RANGE`. You can use these parameters to set file names and the number of files generated in Amazon S3 by each job run. You can run multiple instances of this job in parallel (for example, 100 instances).

## Tools
<a name="generate-test-data-using-an-aws-glue-job-and-python-tools"></a>
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed extract, transform, and load (ETL) service. It helps you reliably categorize, clean, enrich, and move data between data stores and data streams.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.

## Best practices
<a name="generate-test-data-using-an-aws-glue-job-and-python-best-practices"></a>

Consider the following AWS Glue best practices as you implement this pattern:
+ **Use the right AWS Glue worker type to reduce cost.** We recommend that you understand the different properties of worker types, and then choose the right worker type for your workload based on CPU and memory requirements. For this pattern, we recommend that you use a Python shell job as your job type to minimize DPU and reduce cost. For more information, see [Adding jobs in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) in the AWS Glue Developer Guide.
+ **Use the right concurrency limit to scale your job.** We recommend that you base the maximum concurrency of your AWS Glue job on your time requirement and required number of files.
+ **Start generating a small number of files at first.** To reduce cost and save time when you build your AWS Glue jobs, start with a small number of files (such as 1,000). This can make troubleshooting easier. If generating a small number of files is successful, then you can scale to a larger number of files.
+ **Run locally first.** To reduce cost and save time when you build your AWS Glue jobs, start the development locally and test your code. For instructions on setting up a Docker container that can help you write AWS Glue extract, transform, and load (ETL) jobs both in a shell and in an integrated development environment (IDE), see the [Developing AWS Glue ETL jobs locally using a container](https://aws.amazon.com/blogs/big-data/developing-aws-glue-etl-jobs-locally-using-a-container/) post on the AWS Big Data Blog.

For more AWS Glue best practices, see [Best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/best-practices.html) in the AWS Glue documentation.

## Epics
<a name="generate-test-data-using-an-aws-glue-job-and-python-epics"></a>

### Create a destination S3 bucket and IAM role
<a name="create-a-destination-s3-bucket-and-iam-role"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket for storing the files. | Create an [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) and a [prefix](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) within it.This pattern uses the `s3://{your-s3-bucket-name}/small-files/` location for demonstration purposes. | App developer |
| Create and configure an IAM role. | You must create an IAM role that your AWS Glue job can use to write to your S3 bucket.1. Create an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) (for example, called `"AWSGlueServiceRole-smallfiles"`).<br />2. Choose AWS Glue as the policy’s trusted entity.<br />3. Attach an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) called `"AWSGlueServiceRole"` to the role.<br />4. Create an inline policy or [customer managed policy](https://docs.aws.amazon.com/acm/latest/userguide/authen-custmanagedpolicies.html) called `"s3-small-file-access"` based on the following configuration. Replace `"{bucket}"` with your bucket name.<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Action": [<br />                "s3:GetObject",<br />                "s3:PutObject"<br />            ],<br />            "Resource": [<br />                "arn:aws:s3:::{bucket}/small-files/input/*"<br />            ]<br />        }<br />    ]<br />}</pre><br />5. Attach the `"s3-small-file-access"` policy to your role. | App developer |

### Create and configure an AWS Glue job to handle concurrent runs
<a name="create-and-configure-an-aws-glue-job-to-handle-concurrent-runs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS Glue job. | You must create an AWS Glue job that generates your content and stores it in an S3 bucket.<br />Create an [AWS Glue job](https://docs.aws.amazon.com/glue/latest/dg/console-jobs.html), and then configure your job by completing the following steps:1. Sign in to the AWS Management Console and open the [AWS Glue console](https://console.aws.amazon.com/glue/).<br />2. In the navigation pane, under **Data Integration and ETL**, choose **Jobs**.<br />3. In the **Create job** section, choose **Python Shell script editor**.<br />4. In the **Options** section, select **Create a new script with boilerplate code**, and then choose **Create**.<br />5. Choose **Job details**.<br />6. For **Name**, enter **create\_small\_files**.<br />7. For **IAM Role**, select the IAM role that you created earlier.<br />8. In the **This job runs** section, choose **A new script to be authored by you**.<br />9. Expand **Advanced properties**.<br />10. For **Maximum concurrency**, enter **100** for demonstration purposes. **Note**: Maximum concurrency defines how many instances of the job that you can run in parallel.<br />11. Choose **Save**. | App developer |
| Update the job code. | 1. Open the [AWS Glue console](https://console.aws.amazon.com/glue/).<br />2. In the navigation pane, choose **Jobs**.<br />3. In the **Your jobs** section, choose the job that you created earlier.<br />4. Choose the **Script** tab, and then update the script based on the following code. Update the `BUCKET_NAME`, `PREFIX`, and `text_str` variables with your values.<pre>from awsglue.utils import getResolvedOptions<br />import sys<br />import boto3<br />from random import randrange<br /> <br /># Two arguments <br />args = getResolvedOptions(sys.argv, ['START_RANGE', 'END_RANGE'])<br /> <br />START_RANGE = int(args['START_RANGE'])<br />END_RANGE = int(args['END_RANGE'])<br /> <br />BUCKET_NAME = '{BUCKET_NAME}'<br />PREFIX = 'small-files/input/'<br />s3 = boto3.resource('s3')<br />for x in range(START_RANGE, END_RANGE):<br />    # generate file name<br />    file_name = f"input_{x}.txt"<br />    # generate text<br />    text_str = str(randrange(100000))+","+str(randrange(100000))+", " + str(randrange(10000000)) + "," + str(randrange(10000))<br />    # write in s3<br />s3.Object(BUCKET_NAME, PREFIX + file_name).put(Body=text_str)</pre><br />5. Choose **Save**. | App developer |

### Run the AWS Glue job from the command line or console
<a name="run-the-aws-glue-job-from-the-command-line-or-console"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the AWS Glue job from the command line. | To run your AWS Glue job from the AWS CLI , run the following command using your values:<pre>cmd:~$ aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"0","--END_RANGE":"1000000"}'<br />cmd:~$ aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"1000000","--END_RANGE":"2000000"}'</pre>For instructions on running the AWS Glue job from the AWS Management Console, see the *Run the AWS Glue job in the AWS Management Console* story in this pattern.We recommend using the AWS CLI to run AWS Glue jobs if you want to run multiple executions at a time with different parameters, as shown in the example above.<br />To generate all AWS CLI commands that are required to generate a defined number of files using a certain parallelization factor, run the following bash code (using your values):<pre># define parameters<br />NUMBER_OF_FILES=10000000;<br />PARALLELIZATION=50; <br /> <br /># initialize<br />_SB=0;<br />      <br /># generate commands<br />for i in $(seq 1 $PARALLELIZATION); <br />do <br />      echo aws glue start-job-run --job-name create_small_files --arguments "'"'{"--START_RANGE":"'$(((NUMBER_OF_FILES/PARALLELIZATION) * (i-1) + _SB))'","--END_RANGE":"'$(((NUMBER_OF_FILES/PARALLELIZATION) * (i)))'"}'"'";<br />      _SB=1; <br />done</pre><br />If you use the script above, consider the following:+ The script simplifies the invocation and generation of small files at scale.<br />+ Update `NUMBER_OF_FILES` and `PARALLELIZATION` with your values.<br />+ The script above prints a list of commands that you must run. Copy those output commands, and then run them in your terminal.<br />+ If you want to run the commands directly from within the script, remove the `echo` statement in line 11. To see an example of output from the above script, see *Shell script output* in the *Additional information *section of this pattern. | App developer |
| Run the AWS Glue job in the AWS Management Console. | 1. Sign in to the AWS Management Console and open the [AWS Glue console](https://console.aws.amazon.com/glue/).<br />2. In the navigation pane, under **Data Integration and ETL**, choose **Jobs**.<br />3. In the **Your jobs** section, choose your job.<br />4. In the **Parameters (optional)** section, update your parameters.<br />5. Choose **Action**, and then choose **Run job**.<br />6. Repeat steps 3-5 as many times as you require. For example, to create 10 million files, repeat this process 10 times. | App developer |
| Check the status of your AWS Glue job. | 1. Open the [AWS Glue console](https://console.aws.amazon.com/glue/).<br />2. In the navigation pane, choose **Jobs**.<br />3. In the **Your jobs** section, choose the job that you created earlier (that is, `create_small_files`).<br />4. For insight into the progress and generation of your files, review the **Run ID**, **Run Status**, and other columns. | App developer |

## Related resources
<a name="generate-test-data-using-an-aws-glue-job-and-python-resources"></a>

**References**
+ [Registry of Open Data on AWS](https://registry.opendata.aws/)
+ [Data sets for analytics](https://aws.amazon.com/marketplace/solutions/data-analytics/data-sets)
+ [Open Data on AWS](https://aws.amazon.com/opendata/)
+ [Adding jobs in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/add-job.html)
+ [Getting started with AWS Glue](https://aws.amazon.com/glue/getting-started/)

**Guides and patterns**
+ [AWS Glue best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/best-practices.html)
+ [Load testing applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/welcome.html)

## Additional information
<a name="generate-test-data-using-an-aws-glue-job-and-python-additional"></a>

**Benchmarking test**

This pattern was used to generate 10 million files using different parallelization parameters as part of a benchmarking test. The following table shows the output of the test:

|
|
| Parallelization | Number of files generated by a job run | Job duration | Speed |
| --- |--- |--- |--- |
| 10 | 1,000,000 | 6 hours, 40 minutes | Very slow |
| 50 | 200,000 | 80 minutes | Moderate |
| 100 | 100,000 | 40 minutes | Fast |

If you want to make the process faster, you can configure more concurrent runs in your job configuration. You can easily adjust the job configuration based on your requirements, but keep in mind that there is an AWS Glue service quota limit. For more information, see [AWS Glue endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/glue.html).

**Shell script output**

The following example shows the output of the shell script from the *Run the AWS Glue job from the command line* story in this pattern.

```
user@MUC-1234567890 MINGW64 ~
  $ # define parameters
  NUMBER_OF_FILES=10000000;
  PARALLELIZATION=50;
  # initialize
  _SB=0;

  # generate commands
  for i in $(seq 1 $PARALLELIZATION);
   do
         echo aws glue start-job-run --job-name create_small_files --arguments "'"'{"--START_RANGE":"'$(((NUMBER_OF_FILES/PARALLELIZATION)  (i-1) + SB))'","--ENDRANGE":"'$(((NUMBER_OF_FILES/PARALLELIZATION)  (i)))'"}'"'";
         _SB=1;
   done

  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"0","--END_RANGE":"200000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"200001","--END_RANGE":"400000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"400001","--END_RANGE":"600000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"600001","--END_RANGE":"800000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"800001","--END_RANGE":"1000000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"1000001","--END_RANGE":"1200000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"1200001","--END_RANGE":"1400000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"1400001","--END_RANGE":"1600000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"1600001","--END_RANGE":"1800000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"1800001","--END_RANGE":"2000000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"2000001","--END_RANGE":"2200000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"2200001","--END_RANGE":"2400000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"2400001","--END_RANGE":"2600000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"2600001","--END_RANGE":"2800000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"2800001","--END_RANGE":"3000000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"3000001","--END_RANGE":"3200000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"3200001","--END_RANGE":"3400000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"3400001","--END_RANGE":"3600000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"3600001","--END_RANGE":"3800000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"3800001","--END_RANGE":"4000000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"4000001","--END_RANGE":"4200000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"4200001","--END_RANGE":"4400000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"4400001","--END_RANGE":"4600000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"4600001","--END_RANGE":"4800000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"4800001","--END_RANGE":"5000000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"5000001","--END_RANGE":"5200000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"5200001","--END_RANGE":"5400000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"5400001","--END_RANGE":"5600000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"5600001","--END_RANGE":"5800000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"5800001","--END_RANGE":"6000000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"6000001","--END_RANGE":"6200000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"6200001","--END_RANGE":"6400000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"6400001","--END_RANGE":"6600000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"6600001","--END_RANGE":"6800000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"6800001","--END_RANGE":"7000000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"7000001","--END_RANGE":"7200000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"7200001","--END_RANGE":"7400000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"7400001","--END_RANGE":"7600000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"7600001","--END_RANGE":"7800000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"7800001","--END_RANGE":"8000000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"8000001","--END_RANGE":"8200000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"8200001","--END_RANGE":"8400000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"8400001","--END_RANGE":"8600000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"8600001","--END_RANGE":"8800000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"8800001","--END_RANGE":"9000000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"9000001","--END_RANGE":"9200000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"9200001","--END_RANGE":"9400000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"9400001","--END_RANGE":"9600000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"9600001","--END_RANGE":"9800000"}'
  aws glue start-job-run --job-name create_small_files --arguments '{"--START_RANGE":"9800001","--END_RANGE":"10000000"}'

  user@MUC-1234567890 MINGW64 ~
```

**FAQ**

*How many concurrent runs or parallel jobs should I use?*

The number of concurrent runs and parallel jobs depend on your time requirement and desired number of test files. We recommend that you check the size of the files that you’re creating. First, check how much time an AWS Glue job takes to generate your desired number of files. Then, use the right number of concurrent runs to meet your goals. For example, if you assume that 100,000 files takes 40 minutes to complete the run but your target time is 30 minutes, then you must increase the concurrency setting for your AWS Glue job.

*What type of content can I create using this pattern?*

You can create any type of content, such as text files with different delimiters (for example, PIPE, JSON, or CSV). This pattern uses Boto3 to write to a file and then saves the file in an S3 bucket.

*What level of IAM permission do I need in the S3 bucket?*

You must have an identity-based policy that allows `Write` access to objects in your S3 bucket. For more information, see [Amazon S3: Allows read and write access to objects in an S3 bucket](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html) in the Amazon S3 documentation.
