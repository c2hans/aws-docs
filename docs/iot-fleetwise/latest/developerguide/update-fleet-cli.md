---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-fleet-cli.html
---

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Update an AWS IoT FleetWise fleet
<a name="update-fleet-cli"></a>

You can use the [UpdateFleet](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateFleet.html) API operation to update the description for a fleet. The following example uses AWS CLI.

To update a fleet, run the following command.
+ Replace {{fleet-id}} with the ID of the fleet that you're updating.
+ Replace {{description}} with a new description.

  The description can have 1-2048 characters.

```
aws iotfleetwise update-fleet --fleet-id {{fleet-id}} --description {{description}}
```

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `UpdateFleet` API operation.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kms:GenerateDataKey*",
                "kms:Decrypt"
            ],
            "Resource": [
                "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{KMS_KEY_ID}}"
            ]
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
