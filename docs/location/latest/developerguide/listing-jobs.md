---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/listing-jobs.html
---

# List jobs
<a name="listing-jobs"></a>

Use the `ListJobs` operation to list all existing address validation jobs. You can use the results of this operation to check the status of multiple jobs at the same time, or to find the `Name` and `JobId` for a specific job that you want to cancel or monitor individually.

## Examples
<a name="listing-jobs-examples"></a>

### List running jobs
<a name="list-running-jobs-example"></a>

------
#### [ Sample request ]

```
{
    "Filter": {
        "JobStatus": "Running"
    },
    "MaxResults": 50,
    "NextToken": "<TOKEN_STRING>"
}
```

------
#### [ Sample response ]

```
{
    "Entries": [{
            "Action": "ValidateAddress",
            "CreatedAt": "2023-01-01T00:00:00Z",
            "ExecutionRoleArn": "arn:aws:iam::{{YOUR_ACCOUNT_ID}}:role/LocationServiceJobExecutionRole",
            "InputOptions": {
                "Location": "arn:aws:s3:::{{YOUR_INPUT_BUCKET}}",
                "Format": "Parquet"
            },
            "JobArn": "arn:aws:geo:us-west-2:{{YOUR_ACCOUNT_ID}}:job/{{YOUR_JOB_ID}}",
            "JobId": "{{YOUR_JOB_ID}}",
            "Name": "MyFirstValidationJob",
            "OutputOptions": {
                "Format": "Parquet",
                "Location": "arn:aws:s3:::{{YOUR_OUTPUT_BUCKET}}"
            },
            "Status": "Running",
            "UpdatedAt": "2023-01-01T01:00:00Z",
            "ActionOptions": {
                "ValidateAddress": {
                    "AdditionalFeatures": [
                        "Position",
                        "CountrySpecificAttributes"
                    ]
                }
            }
    }],
    "NextToken": "string"
}
```

------
#### [ AWS CLI ]

```
aws location list-jobs --region us-west-2
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
