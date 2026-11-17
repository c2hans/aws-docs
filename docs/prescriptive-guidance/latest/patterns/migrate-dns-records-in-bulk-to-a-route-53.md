---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-dns-records-in-bulk-to-a-route-53.html
---

# Migrate DNS records in bulk to an Amazon Route 53 private hosted zone
<a name="migrate-dns-records-in-bulk-to-a-route-53"></a>

*Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="migrate-dns-records-in-bulk-to-a-route-53-summary"></a>

This pattern automates the bulk migration of DNS records into an Amazon Route 53 hosted zone. It uses a Python script with the AWS SDK for Python (Boto3) to read record data from a JSON file stored in Amazon Simple Storage Service (Amazon S3) and create the records programmatically by using the Route 53 API.

If your source system exports standard BIND zone files, the Route 53 native import feature or [cli53](https://github.com/barnybug/cli53) (a community-maintained, open-source CLI tool not affiliated with AWS) can handle the migration without custom scripting. However, in many enterprise environments, DNS records live in Excel worksheets rather than zone files. Excel exports often contain data quality issues, such as non-breaking spaces and Unicode characters, that standard import tools don't handle. This pattern addresses that gap: it reads from Excel, cleans the data, and creates records end to end.

Use this pattern when you need to migrate a large number of DNS records from an existing system into a Route 53 hosted zone without creating each record manually in the AWS Management Console.

## Prerequisites and limitations
<a name="migrate-dns-records-in-bulk-to-a-route-53-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ An Excel worksheet that contains hosted zone records with columns for fully qualified domain name (FQDN), record type, Time to Live (TTL), and value
+ Python 3.12 or later (see [Download Python](https://www.python.org/downloads/))
+ The pandas Python library installed (`pip3 install pandas`)
+ Familiarity with DNS record types such as A, NAPTR, and SRV records (see [Supported DNS record types](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html))
+ Familiarity with the Python language and its libraries

**Limitations**
+ This pattern does not use all available properties of the `change_resource_record_sets` API call. Extend the code as needed for your use case.
+ This pattern assumes that the value in each row of the Excel worksheet is unique and that multiple values for the same FQDN appear in the same row. If your worksheet doesn't follow this format, modify the code to concatenate multiple values for the same FQDN.
+ This pattern calls the Route 53 API directly by using Boto3. You can enhance the code to use an AWS CloudFormation wrapper for the `create_stack` and `update_stack` commands and use the JSON values to populate template resources.
+ If your source system can export records in BIND zone file format, consider using the Route 53 import feature instead.
+ Some AWS services aren't available in all AWS Regions. For Region availability, see AWS[ services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="migrate-dns-records-in-bulk-to-a-route-53-architecture"></a>

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a81c29ea-f0c5-4d4a-ba87-93111a0f1ee9/images/e5c65fa5-346e-4a24-bddf-a523f30afa95.png)

1. The user uploads an Excel worksheet with DNS record data to an Amazon S3 bucket. For more information, see [What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/)

1. A Python script running locally (or in an IDE such as Kiro) reads the uploaded file from the Amazon S3 bucket by using the AWS SDK for Python (Boto3).

1. The script processes the records and calls the Amazon Route 53 `change_resource_record_sets` API operation to create records in the hosted zone.

## Tools
<a name="migrate-dns-records-in-bulk-to-a-route-53-tools"></a>

*AWS services*
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) –  Provides the hosted zone where DNS records are created. This pattern uses the `create_hosted_zone` and `change_resource_record_sets` API operations.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) - Stores the JSON file that contains the DNS record data to migrate.

*Other tools*
+ **Kiro** – An integrated development environment (IDE) with agentic AI capabilities that you use to develop and run the Python migration script. For more information, see [Kiro](https://kiro.dev/).
+ **pandas** – A Python data analysis library that you use to convert the Excel worksheet to JSON format.

## Best practices
<a name="migrate-dns-records-in-bulk-to-a-route-53-best-practices"></a>
+ Test with a small subset of 5–10 records before you run the script against all records to verify data formatting and correct record creation.
+ Use the `UPSERT` action instead of `CREATE`. The `UPSERT` action creates a record if it doesn't exist or updates it if it does. This makes the script idempotent and safe to rerun.
+ [Batch your changes](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-requests-changeresourcerecordsets) to stay within the `ChangeResourceRecordSets` request limits. When you use the `UPSERT` action, each `ResourceRecord` element counts twice toward the 1,000-element maximum.
+ [Validate data before insertion](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html). Verify that fully qualified domain names (FQDNs) end with a period (`.`), that time to live (TTL) values are positive integers, and that record types match the supported DNS record types.
+ [Back up existing records](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_resource_record_sets) before you make bulk changes. Export the current hosted zone records by using `list_resource_record_sets` to provide a rollback point.
+ Implement retry logic with exponential backoff to handle Route 53 API rate limits. For more information, see [Error retries and exponential backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html).
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the AWS Identity and Access Management (IAM) documentation.

## Epics
<a name="migrate-dns-records-in-bulk-to-a-route-53-epics"></a>

### Prepare data for automation
<a name="prepare-data-for-automation"></a>

<table>
<thead>
  <tr><th>Task</th><th>Description</th><th>Skills required</th></tr>
</thead>
<tbody>
  <tr><td>Create an Excel file for your records.</td><td><ol><li>Export records from your current Domain Name System (DNS) provider.</li><li>Create a Microsoft Excel worksheet with these columns: <code>FqdnName</code>, <code>RecordType</code>, <code>Value</code>, <code>TTL</code>.</li><li>For naming authority pointer (NAPTR) and service (SRV) records, use the Excel CONCAT function to combine multiple property values into the <code>Value</code> column.</li><li>Verify that each fully qualified domain name (FQDN) ends with a period (<code>.</code>) and that each time to live (TTL) value is a positive integer.</li></ol>Example row:
<table>
<tbody>
</tbody>
</table>
</td><td>Data engineer</td></tr>
  <tr><td>Convert the Excel worksheet data to JSON.</td><td><ol><li>In the terminal, run <code>python3 --version</code> to verify that you have Python 3.12 or later installed.</li><li>In the terminal, run <code>pip3 install pandas --user</code> to install the pandas library.</li><li>Create a Python file with the following code to convert the Excel worksheet to JSON:</li></ol><pre>import pandas as pd<br /><br />data=pd.read_excel('./Book1.xls')<br />data.to_json(path_or_buf='my.json',orient='records')</pre><ol><li>Run the script. Verify that the output file <code>my.json</code> contains the expected records.</li></ol></td><td>Data engineer, Python developer</td></tr>
  <tr><td>Upload the JSON file to an Amazon S3 bucket.</td><td><ol><li>Create an Amazon S3 bucket if one does not already exist. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html">Creating a bucket</a> in the Amazon S3 documentation. </li><li>Upload the <code>my.json</code> file to the bucket.</li></ol></td><td>App developer</td></tr>
</tbody>
</table>

### Insert records into the hosted zone
<a name="insert-records-into-the-hosted-zone"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a hosted zone. | 1. Create a Python file with the following code to create a hosted zone. Replace `<hosted-zone-name>`, `<vpc-region>`, and `<vpc-id>` with your values.<pre>import boto3<br />import random<br /><br />hostedZoneName ="xxx"<br />vpcRegion = "us-east-1"<br />vpcId="vpc-xxxx"<br />route53_client = boto3.client('route53')<br />response = route53_client.create_hosted_zone(<br />        Name= hostedZoneName,<br />        VPC={<br />            'VPCRegion': vpcRegion,<br />            'VPCId': vpcId<br />        },<br />        CallerReference=str(random.random()*100000),<br />        HostedZoneConfig={<br />            'Comment': "private hosted zone created by automation",<br />            'PrivateZone': True<br />        }<br />    )<br /><br /> print(response)</pre>1. Run the script and note the hosted zone ID from the response.You can also use an infrastructure as code (IaC) tool such as AWS CloudFormation to replace these steps with a template that creates a stack containing the hosted zone resource and its properties. For more information, see [AWS Route 53::HostedZone](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-hostedzone.html) in the CloudFormation documentation. | Cloud architect, Network administrator, Python skills |
| Read the JSON data from Amazon S3. | 1. Use this code to read the JSON file from the Amazon S3 bucket and load the data as a Python dictionary. Replace `<your-bucket-name>` with the name of your bucket.<pre>import json<br />import boto3<br /><br />s3_client = boto3.client('s3')<br />fileobj = s3_client.get_object(<br />    Bucket='<your-bucket-name>',<br />    Key='my.json'<br />)<br /><br />filedata = fileobj['Body'].read()<br />contents = filedata.decode('utf-8')<br />json_content = json.loads(contents)</pre>1. Verify that `json_content` contains the expected records by printing the first few entries. | App developer, Python developer |
| Clean data values and insert records. | 1. Use this code to clean data values and insert records into the hosted zone. Replace `<hosted-zone-id>` with the ID of the hosted zone that you created earlier.<pre>import unicodedata<br />import time<br /><br />for item in json_content:<br />    fqn_name = unicodedata.normalize(<br />        "NFKD",<br />        item["FqdnName"].replace("u'", "'").replace('\xa0', '').strip()<br />    )<br />    rec_type = item["RecordType"].replace('\xa0', '').strip()<br />    res_rec = {'Value': item["Value"].replace('\xa0', '').strip()}<br /><br />    change_response = route53_client.change_resource_record_sets(<br />        HostedZoneId='<hosted-zone-id>',<br />        ChangeBatch={<br />            'Comment': 'Created by automation',<br />            'Changes': [<br />                {<br />                    'Action': 'UPSERT',<br />                    'ResourceRecordSet': {<br />                        'Name': fqn_name,<br />                        'Type': rec_type,<br />                        'TTL': item["TTL"],<br />                        'ResourceRecords': [res_rec]<br />                    }<br />                }<br />            ]<br />        }<br />    )<br /><br />    time.sleep(1)  # Delay to avoid PriorRequestNotComplete errors</pre>1. Monitor the output for errors. If throttling occurs, increase the delay or implement exponential backoff. | App developer, Python skills |

## Troubleshooting
<a name="migrate-dns-records-in-bulk-to-a-route-53-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| `PriorRequestNotComplete` error  | Add a `time.sleep()` delay of 1–2 seconds between `change_resource_record_sets` calls. Route 53 processes changes asynchronously, and a previous change may still be in progress. |
| `InvalidChangeBatch` error | This error occurs when you try to create a record that already exists by using the `CREATE` action. Use `UPSERT` instead to make the script idempotent. |
| Throttling error (rate limit exceeded)  | You have exceeded the Route 53 API rate limit. Implement exponential backoff with jitter. For more information, see [Throttling for Amazon Route 53 API requests](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/throttling-api-requests.html) and [Error retries and exponential backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html). |
| Records are not resolving | Verify that the [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/) is associated with the hosted zone and that DNS resolution is enabled on the VPC. Set both `enableDnsSupport` and `enableDnsHostnames` to `true`. |
| `InvalidInput` error on record values | The data contains non-breaking spaces (`\xa0`) or leading/trailing whitespace. Apply the data cleaning code from the "Clean data values and insert records" task before insertion. |

## Related resources
<a name="migrate-dns-records-in-bulk-to-a-route-53-resources"></a>

**References**
+ [Creating records by importing a zone file](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating-import.html) (Route 53 documentation)
+ [create\_hosted\_zone](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/client/create_hosted_zone.html) (Boto3 documentation)
+ [change\_resource\_record\_sets](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/client/change_resource_record_sets.html) (Boto3 documentation)
+ [Supported DNS record types](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html) (Route 53 documentation)
+ [Error retries and exponential backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html)

**Tutorials and videos **

[DNS design using Amazon Route 53](https://www.youtube.com/watch?v=example) (video)

## Additional information
<a name="migrate-dns-records-in-bulk-to-a-route-53-additional"></a>

For NAPTR and SRV records, the `Value` field in the Excel worksheet must contain all required components concatenated into a single string. Use Excel's CONCAT function to combine the individual properties (order, preference, flags, service, regexp, replacement for NAPTR; priority, weight, port, target for SRV) before exporting to JSON.

If your migration involves more than 1,000 records, split the JSON file into batches and process each batch separately to stay within Route 53 API limits. When you use the `UPSERT` action, each `ResourceRecord` element counts twice toward the 1,000-element maximum per `ChangeResourceRecordSets` request.

## Attachments
<a name="attachments-a81c29ea-f0c5-4d4a-ba87-93111a0f1ee9"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/a81c29ea-f0c5-4d4a-ba87-93111a0f1ee9/attachments/attachment.zip)
