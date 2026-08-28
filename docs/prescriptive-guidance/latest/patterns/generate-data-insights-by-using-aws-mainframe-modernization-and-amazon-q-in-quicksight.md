---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight.html
---

# Generate data insights by using AWS Mainframe Modernization and Amazon Q in Quick Sight
<a name="generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight"></a>

*Shubham Roy, Roshna Razack, and Santosh Kumar Singh, Amazon Web Services*

## Summary
<a name="generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-summary"></a>

Note: AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

If your organization is hosting business-critical data in a mainframe environment, gaining insights from that data is crucial for driving growth and innovation. By unlocking mainframe data, you can build faster, secure, and scalable business intelligence to accelerate data-driven decision-making, growth, and innovation in the Amazon Web Services (AWS) Cloud.

This pattern presents a solution for generating business insights and creating sharable narratives from mainframe data by using [AWS Mainframe Modernization file transfer](https://docs.aws.amazon.com/m2/latest/userguide/filetransfer.html) with BMC and [Amazon Q in Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-gen-bi.html). Mainframe datasets are transferred to [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) by using AWS Mainframe Modernization file transfer with BMC. An AWS Lambda function formats and prepares mainframe data file for loading into Quick Sight.

After the data is available in Quick Sight, you can use natural language prompts with [Amazon Q](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-gen-bi.html) in Quick Sight to create summaries of the data, ask questions, and generate data stories. You don't have to write SQL queries or learn a business intelligence (BI) tool.

**Business context**

This pattern presents a solution for mainframe data analytics and data insights use cases. Using the pattern, you build a visual dashboard for your company's data. To demonstrate the solution, this pattern uses a health care company that provides medical, dental, and vision plans to its members in the US. In this example, member demographics and plan information are stored in the mainframe datasets. The visual dashboard shows the following:
+ Member distribution by region
+ Member distribution by gender
+ Member distribution by age
+ Member distribution by plan type
+ Members who have not completed preventive immunization

After you create the dashboard, you generate a data story that explains the insights from the previous analysis. The data story provides recommendations for increasing the number of members who have completed preventive immunizations.

## Prerequisites and limitations
<a name="generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Mainframe datasets with business data
+ Access to install a file transfer agent on the mainframe

**Limitations**
+ Your mainframe data file should be in one of the file formats supported by Quick Sight. For a list supported file formats, see [Supported data sources](https://docs.aws.amazon.com/quicksuite/latest/userguide/supported-data-sources.html).
+ This pattern uses a Lambda function to convert the mainframe file into a format supported by Quick Sight.

## Architecture
<a name="generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-architecture"></a>

The following diagram shows an architecture for generating business insights from mainframe data by using AWS Mainframe Modernization file transfer with BMC and Amazon Q in Quick Sight.

![Architecture diagram description follows the diagram.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/53572abb-06c6-4dd7-add4-8fad7e9bfa68/images/6fe0f1d9-961c-4089-a746-e5b8d5fd6c1e.png)

The diagram shows the following workflow:

1. A mainframe dataset containing business data is transferred to Amazon S3 by using AWS Mainframe Modernization file transfer with BMC.

1. The Lambda function converts the file that's in the file-transfer destination S3 bucket to comma-separated values (CSV) format.

1. The Lambda function sends the converted file to the source dataset S3 bucket.

1. The data in the file is ingested by Quick Sight.

1. Users access the data in Quick Sight. You can use Amazon Q in Quick Sight to interact with the data by using natural language prompts.

## Tools
<a name="generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-tools"></a>

**AWS services**
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Mainframe Modernization file transfer with BMC](https://docs.aws.amazon.com/m2/latest/userguide/filetransfer.html) converts and transfers mainframe datasets to Amazon S3 for mainframe modernization, migration, and augmentation use cases.
+ [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) is a cloud-scale BI service that helps you visualize, analyze, and report your data in a single dashboard. This pattern uses the generative BI capabilities of [Amazon Q in Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-quicksight-q.html).
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

## Best practices
<a name="generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-best-practices"></a>
+ When you create the AWS Identity and Access Management (IAM) roles for AWS Mainframe Modernization file transfer with BMC and the Lambda function, follow the principle of [least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege).
+ Ensure that your source dataset has [supported data types](https://docs.aws.amazon.com/quicksight/latest/user/supported-data-types-and-values.html) for Quick Sight. If your source dataset contains unsupported data types, convert them to supported data types. For information about unsupported mainframe data types and how to convert them to data types supported by Amazon Q in Quick Sight, see the [Related resources](#generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-resources) section.

## Epics
<a name="generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-epics"></a>

### Set up AWS Mainframe Modernization file transfer with BMC
<a name="set-up-m2long-file-transfer-with-bmc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the file transfer agent. | To install AWS Mainframe Modernization file transfer agent, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/m2/latest/userguide/m2-agent-installation.html). | Mainframe system administrator |
| Create an S3 bucket for mainframe file transfer. | [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) to store the output file from AWS Mainframe Modernization file transfer with BMC. In the architecture diagram, this is the file-transfer destination bucket. | Migration engineer |
| Create the data transfer endpoint. | 1. Create an S3 bucket to stage the input mainframe file for AWS Mainframe Modernization file transfer with BMC.<br />2. To create the mainframe data transfer endpoint, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/m2/latest/userguide/filetransfer-data-transfer-endpoints.html). | AWS Mainframe Modernization specialist |

### Convert the mainframe file name extension for Quick Sight integration
<a name="convert-the-mainframe-file-name-extension-for-quick-sight-integration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket. | [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) for the Lambda function to copy the converted mainframe file from the source to the final destination bucket. | Migration engineer |
| Create a Lambda function. | To create a Lambda function that changes the file extension and copies the mainframe file to the destination bucket, do the following:1. Sign in to the AWS Management Console, and navigate to the AWS Lambda console.<br />2. Choose **Create function**, and then choose **Author from scratch**.<br />3. For **Function name**, enter a name for your function.<br />4. In the **Runtime** dropdown list, choose **Python.3.X**.<br />5. Expand **Change default execution role**, and then choose **Create a new role with basic Lambda permissions**.<br />6. Choose **Create function**.<br />7. Choose the **Code** tab, and then paste the `S3CopyLambda.py` Python code that's provided in the [Additional information](#generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-additional) section. The Python code was generated by using Amazon Q in the Microsoft Visual Studio integrated development environment (IDE).<br />8. Edit the `destination_bucket_name` to the name of the S3 bucket that you created previously, and `change destination_file_key` to the mainframe file name.<br />9. Deploy the Lambda function. | Migration engineer |
| Create an Amazon S3 trigger to invoke the Lambda function. | To configure a trigger that invokes the Lambda function, do the following:1. On the Lambda console, open the **Functions** page.<br />2. Choose the Lambda function.<br />3. In **Function overview**, choose **Add trigger**.<br />4. In the **Trigger configuration** dropdown list, choose **S3**.<br />5. In the **Bucket** field, enter the name of your source bucket.<br />6. In the **Event type** dropdown list, choose **All object create events**.<br />7. Select the **I acknowledge that using the same S3 bucket for both input and output is not recommended** check box, and then choose **Add**.<br />For more information, see [Tutorial: Using an Amazon S3 trigger to invoke a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html). | Migration lead |
| Provide IAM permissions for the Lambda function. | IAM permissions are required for the Lambda function to access the file-transfer destination and source dataset S3 buckets. Update the policy associated with the Lambda function execution role by allowing `s3:GetObject` and `s3:DeleteObject`** **permissions** **for the file-transfer destination S3 bucket and `s3:PutObject` access for the source dataset S3 bucket.<br />For more information, see the [Create a permissions policy](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html#with-s3-example-create-policy)** **section in *Tutorial: Using an Amazon S3 trigger to invoke a Lambda function*. | Migration lead |

### Define a mainframe data transfer task
<a name="define-a-mainframe-data-transfer-task"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a transfer task to copy the mainframe file to the S3 bucket. | To create a mainframe file transfer task, follow the instructions in the [AWS Mainframe Modernization documentation.](https://docs.aws.amazon.com/m2/latest/userguide/filetransfer-transfer-tasks.html)Specify **Source code page** encoding as **IBM1047 **and **Target code page** encoding as** UTF-8**. | Migration engineer |
| Verify the transfer task. | To verify that the data transfer is successful, follow the instructions in the [AWS Mainframe Modernization documentation](https://docs.aws.amazon.com/m2/latest/userguide/filetransfer-transfer-tasks.html#filetransfer-ts-view-console). Confirm that the mainframe file is in the file-transfer destination S3 bucket. | Migration lead |
| Verify the Lambda copy function. | Verify that the Lambda function is initiated and that the file is copied with a .csv extension to the source dataset S3 bucket.<br />The .csv file created by the Lambda function is the input data file for Quick Sight. For example data, see the `Sample-data-member-healthcare-APG` file in the [Attachments](#attachments-53572abb-06c6-4dd7-add4-8fad7e9bfa68) section. | Migration lead |

### Connect Quick Sight to the mainframe data
<a name="connect-quick-sight-to-the-mainframe-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Quick Sight. | To set up Quick Sight, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/setting-up.html). | Migration lead |
| Create a dataset for Quick Sight. | To create a dataset for Quick Sight, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-s3.html). The input data file is the converted mainframe file that was created when you defined the mainframe data transfer task. | Migration lead |

### Get business insights from the mainframe data by using Amazon Q in Quick Sight
<a name="get-business-insights-from-the-mainframe-data-by-using-qdev-in-quick-sight"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Amazon Q in Quick Sight. | This capability requires Enterprise Edition. To set up Amazon Q in Quick Sight, do the following:1. To get the Amazon Q add-on, follow the instructions Step 1: Get the Q add-on in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-get-started.html#quicksight-q-get-started-add-on).<br />2. To use the generative BI capabilities in Amazon Q, upgrade your users' accounts. Follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/generative-bi-opt-in.html).<br />3. Create an Amazon Q topic by using the dataset that you created previously. Follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-topics-create.html#quicksight-q-topics-create-how).<br />4. To configure the topic metadata so that it's natural language‒friendly, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-topics-natural-language.html). | Migration lead |
| Analyze mainframe data and build a visual dashboard. | To analyze and visualize your data in Quick Sight, do the following:1. To create the mainframe data analysis, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/creating-an-analysis.html). For the dataset, choose the dataset created in the previous step.<br />2. On the analysis page choose **Build visual**.<br />3. In the **Create topic for analysis** window, choose **Update existing topic**.<br />4. In the **Select a topic** dropdown list, choose the topic that you created previously.<br />5. Choose **Topic linking**.<br />6. After you link the topic, choose **Build visual** to open the Amazon Q **Build a Visual** window.<br />7. In the prompt bar. write your analysis questions. The example questions used for this pattern are the following:Show member distribution by regionShow members distribution by ageShow member distribution by genderShow member distribution by plan typeShow member not completed preventive immunization<br />After you enter your questions, choose **Build**. Amazon Q in Quick Sight creates the visuals.<br />8. To add the visuals to your visual dashboard, choose **ADD TO ANALYSIS**.<br />When you're finished, you can publish your dashboard to share with others in your organization. For examples, see *Mainframe visual dashboard* in the [Additional information](#generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-additional) section. | Migration engineer |

### Create a data story with Amazon Q in Quick Sight from the mainframe data
<a name="create-a-data-story-with-qdev-in-quick-sight-from-the-mainframe-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a data story. | Create a data story to explain insights from the previous analysis, and generate a recommendation to increase preventive immunization for members:1. To create the data story, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/working-with-stories-create.html).<br />2. For the data story prompt, use the following:<br />`Build a data story about Region with most numbers of members. Also show the member distribution by medical plan, vision plan, dental plan. Recommend how to motivate members to complete immunization. Include 4 points of supporting data for this pattern.`<br />You can also build your own prompt to generate data stories for other business insights.<br />3. Choose **Add visuals**, and add the visuals that are relevant to the data story. For this pattern, use the visuals that you created previously.<br />4. Choose **Build**.<br />5. For example data story output, see *Data story output* in the [Additional information](#generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-additional) section. | Migration engineer |
| View the generated data story. | To view the generated data story, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/working-with-stories-view.html). | Migration lead |
| Edit a generated data story. | To change the formatting, layout, or visuals in a data story, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/working-with-stories-edit.html). | Migration lead |
| Share a data story. | To share a data story, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/working-with-stories-share.html). | Migration engineer |

## Troubleshooting
<a name="generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Unable to discover the mainframe files or datasets entered in **Data sets search criteria **for **Create transfer task** in AWS Mainframe Modernization file transfer with BMC. | 1. First, check the connection by choosing **Data transfer endpoints** on the AWS Mainframe Modernization Transfer with BMC console. If the last heartbeat time is greater than two minutes, the connection for file transfer hasn't been established. If the last heartbeat time is less than 2 minutes for the agent running on the mainframe, the connection to the agent is successful. Proceed to step 2.<br />2. Check the AWS Secrets Manager setup. A secret key must be configured in Secrets Manager with a **key** of `userId` (uppercase I) with a **value** of the mainframe's user ID and a **key** of `password` with the **value** of the mainframe password. The `userId` and `password` secret keys are case-sensitive and must be entered as is. |

## Related resources
<a name="generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-resources"></a>

To convert mainframe data types such as [PACKED-DECIMAL (COMP-3)](https://www.ibm.com/docs/en/cobol-zos/6.3?topic=v6-packed-decimal-comp-3) or [BINARY (COMP or COMP-4)](https://www.ibm.com/docs/en/cobol-zos/6.3?topic=v6-binary-comp-comp-4) to a [data type](https://docs.aws.amazon.com/quicksight/latest/user/supported-data-types-and-values.html) supported by Quick Sight, see the following patterns:
+ [Convert and unpack EBCDIC data to ASCII on AWS by using Python](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/convert-and-unpack-ebcdic-data-to-ascii-on-aws-by-using-python.html)
+ [Convert mainframe files from EBCDIC format to character-delimited ASCII format in Amazon S3 using AWS Lambda](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/convert-mainframe-files-from-ebcdic-format-to-character-delimited-ascii-format-in-amazon-s3-using-aws-lambda.html)

## Additional information
<a name="generate-data-insights-by-using-aws-mainframe-modernization-and-amazon-q-in-quicksight-additional"></a>

**S3CopyLambda.py**

The following Python code was generated by using a prompt with Amazon Q in an IDE:

```
#Create a lambda function triggered by S3. display the S3 bucket name and key
import boto3
s3 = boto3.client('s3')
def lambda_handler(event, context):
print(event)
bucket = event['Records'][0]['s3']['bucket']['name']
key = event['Records'][0]['s3']['object']['key']
print(bucket, key)
#If key starts with object_created, skip copy, print "copy skipped". Return lambda with key value.
if key.startswith('object_created'):
print("copy skipped")
return {
'statusCode': 200,
'body': key
}
# Copy the file from the source bucket to the destination bucket. Destination_bucket_name = 'm2-filetransfer-final-opt-bkt'. Destination_file_key = 'healthdata.csv'
copy_source = {'Bucket': bucket, 'Key': key}
s3.copy_object(Bucket='m2-filetransfer-final-opt-bkt', Key='healthdata.csv', CopySource=copy_source)
print("file copied")
#Delete the file from the source bucket.
s3.delete_object(Bucket=bucket, Key=key)
return {
'statusCode': 200,
'body': 'Copy Successful'
}
```

**Mainframe visual dashboard**

The following data visual was created by Amazon Q in Quick Sight for the analysis question `show member distribution by region`*.*

![Chart showing numbers of members for southwest, midwest, northeast, and southeast.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/53572abb-06c6-4dd7-add4-8fad7e9bfa68/images/e5c1d049-407d-42ff-bc51-28f9d2b24d4f.png)

The following data visual was created by Amazon Q in Quick Sight for the question `show member distribution by Region who have not completed preventive immunization, in pie chart`.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/53572abb-06c6-4dd7-add4-8fad7e9bfa68/images/47efa1c1-54c9-47cc-b668-416090021d34.png)

**Data story output**

The following screenshots show sections of the data story created by Amazon Q in Quick Sight for the prompt `Build a data story about Region with most numbers of members. Also show the member distribution by medical plan, vision plan, dental plan. Recommend how to motivate members to complete immunization. Include 4 points of supporting data.`

In the introduction, the data story recommends choosing the region with the most members to gain the greatest impact from immunization efforts.

![Introduction page for data story focusing on immunization completion rates.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/53572abb-06c6-4dd7-add4-8fad7e9bfa68/images/4612fcc7-51fd-48a5-bc58-b6b0aa9b0ef3.png)

The data story provides an analysis of member numbers for the top three regions, and names the Southwest as the leading region for focusing on immunization efforts.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/53572abb-06c6-4dd7-add4-8fad7e9bfa68/images/30d3b56b-3b92-4748-9cef-a73ff9339fee.png)

**Note**
The Southwest and Northeast regions each have eight members. However, the Southwest has more members that aren't fully vaccinated, so it has more potential to benefit from initiatives to increase immunization rates.

## Attachments
<a name="attachments-53572abb-06c6-4dd7-add4-8fad7e9bfa68"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/53572abb-06c6-4dd7-add4-8fad7e9bfa68/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
