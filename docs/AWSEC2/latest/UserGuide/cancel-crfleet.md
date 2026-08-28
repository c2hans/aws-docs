---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-crfleet.html
---

# Cancel a Capacity Reservation Fleet
<a name="cancel-crfleet"></a>

When you no longer need a Capacity Reservation Fleet and the capacity it reserves, you can cancel it. When you cancel a Fleet, its status changes to `cancelled` and it can no longer create new Capacity Reservations. Additionally, all of the individual Capacity Reservations in the Fleet are canceled. The instances that were previously running in the reserved capacity continue to run normally in the shared capacity.

------
#### [ AWS CLI ]

**To cancel a Capacity Reservation Fleet**
Use the [cancel-capacity-reservation-fleets](https://docs.aws.amazon.com/cli/latest/reference/ec2/cancel-capacity-reservation-fleets.html) command.

```
aws ec2 cancel-capacity-reservation-fleets \
    --capacity-reservation-fleet-ids {{crf-abcdef01234567890}}
```

The following is example output.

```
{
    "SuccessfulFleetCancellations": [
        {
            "CurrentFleetState": "cancelling",
            "PreviousFleetState": "active",
            "CapacityReservationFleetId": "crf-abcdef01234567890"
        }
    ],
    "FailedFleetCancellations": []
}
```

------
#### [ PowerShell ]

**To cancel a Capacity Reservation Fleet**
Use the [Stop-EC2CapacityReservationFleet](https://docs.aws.amazon.com/powershell/latest/reference/items/Stop-EC2CapacityReservationFleet.html) cmdlet.

```
Stop-EC2CapacityReservationFleet `
    -CapacityReservationFleetId {{crf-abcdef01234567890}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
