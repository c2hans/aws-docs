---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/configuring-storage-profiles-for-fleets.html
---

# Configure storage profiles for fleets
<a name="configuring-storage-profiles-for-fleets"></a>

You can configure a fleet to include a storage profile that models the file system locations on all workers in the fleet. The host file system configuration of all workers in a fleet must match their fleet's storage profile. Workers with different file system configurations must be in separate fleets.

To set your fleet's configuration to use the `WorkerConfig` storage profile use the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html):

```
# Change the value of FARM_ID to your farm's identifier
FARM_ID=farm-{{00112233445566778899aabbccddeeff}}
# Change the value of FLEET_ID to your fleet's identifier
FLEET_ID=fleet-{{00112233445566778899aabbccddeeff}}
# Change the value of WORKER_CFG_ID to your storage profile named WorkerConfig
WORKER_CFG_ID=sp-{{00112233445566778899aabbccddeeff}}

FLEET_WORKER_MODE=$( \
  aws deadline get-fleet --farm-id $FARM_ID --fleet-id $FLEET_ID \
   --query 'configuration.customerManaged.mode' \
)
FLEET_WORKER_CAPABILITIES=$( \
  aws deadline get-fleet --farm-id $FARM_ID --fleet-id $FLEET_ID \
   --query 'configuration.customerManaged.workerCapabilities' \
)

aws deadline update-fleet --farm-id $FARM_ID --fleet-id $FLEET_ID \
  --configuration \
  "{
    \"customerManaged\": {
      \"storageProfileId\": \"$WORKER_CFG_ID\",
      \"mode\": $FLEET_WORKER_MODE,
      \"workerCapabilities\": $FLEET_WORKER_CAPABILITIES
    }
  }"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
