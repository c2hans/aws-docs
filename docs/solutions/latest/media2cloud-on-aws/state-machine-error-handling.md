---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/state-machine-error-handling.html
---

# State machine error handling
<a name="state-machine-error-handling"></a>

 The error handling of the main state machine is handled by using an Amazon CloudWatch Event Rule attached to an AWS Lambda function.

![State machine error handling diagram](http://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/images/media2cloud-state-machine-error-handling.png)

 The event rule is configured to listen to `Step Functions Run Status Change` events with error statuses of **FAILED**, **ABORTED**, and **TIMED\_OUT** of the ingestion and analysis state machine runs. It then invokes a Lambda `error-handler` function to process the state machine run error.

 The CloudWatch Events pattern is defined as follows:

```
{
    "detail-type": [
        "Step Functions Execution Status Change"
    ],
    "source": [
        "aws.states"
    ],
    "detail": {
        "stateMachineArn": [
            "<INGEST_STATE_MACHINE_ARN>",
            "<ANALYSIS_STATE_MACHINE_ARN>"
        ],
        "status": [
            "FAILED",
            "ABORTED",
            "TIMED_OUT"
        ]
    },
    "region": [
        "<REGION>"
    ]
}
```

 The `error-handler` Lambda function parses the run histories to find the last error from the state machine, updates the status in the Amazon DynamoDB ingestion table, publishes the status to an Amazon SNS status topic to notify subscribers, and publishes the status to an AWS Iot Core publish/subscribe service (a status topic) to notify the front-end web application.
