---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-vehicles-cli.html
---

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Update multiple AWS IoT FleetWise vehicles
<a name="update-vehicles-cli"></a>

You can use the [BatchUpdateVehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_BatchUpdateVehicle.html) API operation to update multiple existing vehicles at one time. The following example uses the AWS CLI.

To update multiple vehicles, run the following command.

Replace {{file-name}} with the name of the .json file that contains the configurations of multiple vehicles.

```
aws iotfleetwise batch-update-vehicle --cli-input-json file://{{file-name}}.json
```

**Example – vehicle configurations**

```
{
   "vehicles": [
      {
         "vehicleName": "vehicle-name",
         "modelManifestArn": "model-manifest-arn",
         "decoderManifestArn": "decoder-manifest-arn",
         "mergeAttributes": true,
         "attributes": {
         "key": "value"
         }
      },
      {
         "vehicleName": "vehicle-name",
         "modelManifestArn": "model-manifest-arn",
         "decoderManifestArn": "decoder-manifest-arn",
         "mergeAttributes": true,
         "attributes": {
         "key": "value"
         }
      }
   ]
}
```

You can update up to 10 vehicles for each batch operation. For more information about the configuration of each vehicle, see [Update an AWS IoT FleetWise vehicle](update-vehicle-cli.md).

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `BatchUpdateVehicle` API operation.

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
