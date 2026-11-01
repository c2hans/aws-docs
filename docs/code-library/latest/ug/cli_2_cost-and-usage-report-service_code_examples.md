---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_cost-and-usage-report-service_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS Cost and Usage Report examples using AWS CLI
<a name="cli_2_cost-and-usage-report-service_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Cost and Usage Report.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `delete-report-definition`
<a name="cost-and-usage-report-service_DeleteReportDefinition_cli_2_topic"></a>

The following code example shows how to use `delete-report-definition`.

**AWS CLI**
**To delete an AWS Cost and Usage Report**
The following `delete-report-definition` example deletes an AWS Cost and Usage Report.

```
aws cur delete-report-definition \
    --region {{us-east-1}} \
    --report-name {{"ExampleReport"}}
```
Output:

```
{
    "ResponseMessage": "Report ExampleReport deleted successfully."
}
```
For more information, see [What are AWS Cost and Usage Reports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) in the *AWS Data Exports User Guide*.
+  For API details, see [DeleteReportDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/delete-report-definition.html) in *AWS CLI Command Reference*.

### `describe-report-definitions`
<a name="cost-and-usage-report-service_DescribeReportDefinitions_cli_2_topic"></a>

The following code example shows how to use `describe-report-definitions`.

**AWS CLI**
**To retrieve a list of AWS Cost and Usage Reports**
The following `describe-report-definitions` example describes a list of AWS Cost and Usage Reports owned by an account.

```
aws cur describe-report-definitions \
    --region {{us-east-1}} \
    --max-items {{5}}
```
Output:

```
{
    "ReportDefinitions": [
        {
            "ReportName": "ExampleReport",
            "Compression": "ZIP",
            "S3Region": "us-east-1",
            "Format": "textORcsv",
            "S3Prefix": "exampleprefix",
            "S3Bucket": "example-s3-bucket",
            "TimeUnit": "DAILY",
            "AdditionalArtifacts": [
                "REDSHIFT",
                "QUICKSIGHT"
            ],
            "AdditionalSchemaElements": [
                "RESOURCES"
            ]
        }
    ]
}
```
For more information, see [What are AWS Cost and Usage Reports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) in the *AWS Data Exports User Guide*.
+  For API details, see [DescribeReportDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/describe-report-definitions.html) in *AWS CLI Command Reference*.

### `put-report-definition`
<a name="cost-and-usage-report-service_PutReportDefinition_cli_2_topic"></a>

The following code example shows how to use `put-report-definition`.

**AWS CLI**
**To create an AWS Cost and Usage Reports**
The following `put-report-definition` example creates a daily AWS Cost and Usage Report that you can upload into Amazon Redshift or Amazon QuickSight.

```
aws cur put-report-definition \
    --report-definition {{file://report-definition.json}}
```
Contents of `report-definition.json`:

```
{
    "ReportName": "ExampleReport",
    "TimeUnit": "DAILY",
    "Format": "textORcsv",
    "Compression": "ZIP",
    "AdditionalSchemaElements": [
        "RESOURCES"
    ],
    "S3Bucket": "example-s3-bucket",
    "S3Prefix": "exampleprefix",
    "S3Region": "us-west-2",
    "AdditionalArtifacts": [
        "REDSHIFT",
        "QUICKSIGHT"
    ]
}
```
This command produces no output.
For more information, see [Creating a Legacy CUR export](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create-legacy.html) in the *AWS Data Exports User Guide*.
+  For API details, see [PutReportDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/put-report-definition.html) in *AWS CLI Command Reference*.
