---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets_scale-to-from-zero.html
---

# Manage Scaling an Amazon GameLift Servers Fleet To/From Zero
<a name="fleets_scale-to-from-zero"></a>

Amazon GameLift Servers supports automatic scaling to and from zero instances based on game session activity. This managed capacity option allows your Fleet locations to scale-in to zero instances following a defined period of no game session activity and automatically scale-out when game sessions are requested.

Scaling to and from zero instances provides several advantages:
+ **Cost optimization** – Eliminate compute costs during periods of inactivity by running zero instances when there is no game session activity.
+ **Automatic reactive scale-out** – Fleets locations automatically scale-out to one instance when a game session is requested, eliminating the need for manual intervention.
+ **Simplified management** – No need to manually adjust Fleet capacity to/from zero based on anticipated player demand or development needs.

When you enable Scale To/From Zero on a fleet, Amazon GameLift Servers monitors game session activity and automatically adjusts Fleet capacity:
+ **Scale-in to zero** – After a configured period with no game sessions activity, Amazon GameLift Servers scales-in the Fleet location to zero instances.
+ **Scale-out from zero** – When a game session creation request is received, Amazon GameLift Servers scales-out the Fleet location to one instance, allowing auto scaling to resume.
+ **Continued scaling** – Following scale-out the fleet resumes using configured auto scaling policies to manage capacity.

## Scale-in behavior
<a name="scale-in-behavior"></a>

Amazon GameLift Servers begins the scale-in process for a Fleet location after the configured inactivity period has elapsed with no game session activity. This is defined as a period where::
+ There are no active game sessions in the Fleet location.
+ No requests have been made to create new game sessions in the Fleet location.

During scale-in, Amazon GameLift Servers will set minimum and desired capacity for the Fleet location to zero, rapidly scaling-in for cost savings.

## Scale-out behavior
<a name="scale-out-behavior"></a>

When a game session creation request is received while the Fleet location is at zero instances:
+ Amazon GameLift Servers immediately initiates scale-out of one instance.
+ Attempted placement of the game session may continue with other Fleets or Fleet locations, depending on configuration of Queues (if used).

**Note**
Scale-out from zero takes time to provision and initialize instances. Players may experience longer wait times for the first game session after a period of inactivity. For this reason this feature is best paired with multi-location Fleets and/or Queues.

## Configuring Scale To/From Zero
<a name="configuring-scale-to-from-zero"></a>

Scaling To/From Zero is configured by updating an existing fleet.

------
#### [ Console ]

1. Open the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/).

1. In the navigation pane, choose **Hosting**, **Fleets**.

1. On the **Fleets** page, choose the name of an active fleet to open the fleet's detail page.

1. Under **Scaling**, select each location for which you want to configure scale to/from zero, and then choose **Edit**.

1. In the **Edit scaling capacity** dialog box, select "Automatic" for **Minimum capacity strategy**, set your preferred value in minutes for **Set minimum capacity to 0 after** and then choose **Confirm**.

Amazon GameLift Servers will then scale-in the selected fleet locations to 0 instances once there has been no game session activity for the configured duration. Following this, when a request for a game session is made in this location, Amazon GameLift Servers will scale-out one instance as quickly as possible. This process will take a little time.

------
#### [ AWS CLI ]
+ **Configure scale to/from zero.** In a command line window, use the [update-fleet-capacity](https://docs.aws.amazon.com/cli/latest/reference/gamelift/update-fleet-capacity.html) command with the fleet ID, location and managed capacity configuration to configure scale to/from zero.

  ```
  aws gamelift update-fleet-capacity \
                                  --fleet-id {{<fleet identifier>}} \
                                  --location {{<location name>}} \
                                  --managed-capacity-configuration ScaleInAfterInactivityMinutes=60,ZeroCapacityStrategy=SCALE_TO_AND_FROM_ZERO
  ```

  Example:

  ```
  aws gamelift update-fleet-capacity \
                                  --fleet-id fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa \
                                  --location us-west-2 \
                                  --desired-instances 5 \
                                  --max-size 10 \
                                  --managed-capacity-configuration ScaleInAfterInactivityMinutes=60,ZeroCapacityStrategy=SCALE_TO_AND_FROM_ZERO
  ```

If your request is successful, Amazon GameLift Servers returns the updated capacity configuration. Amazon GameLift Servers will then scale-in the selected fleet locations to 0 instances once there has been no game session activity for the configured duration. Following this, when a request for a game session is made in this location, Amazon GameLift Servers will scale-out one instance as quickly as possible. This process will take a little time.

------

## Best practices
<a name="best-practices"></a>

Consider the following recommendations when using Scale To/From Zero:
+ **Set appropriate inactivity periods** – Balance cost savings against the frequency of scale-in/scale-out cycles. Shorter wait time to scale to zero may maximize savings, but would result in more frequent cold starts.
+ **Use with predictable workloads** – Scale To/From Zero works best for games with clear periods of inactivity, such as development/test environments or games with distinct off-peak hours.
+ **Monitor CloudWatch metrics** – Track fleet scaling events and game session placement times to optimize your configuration.
+ **Combine with scaling policies** – Use Scale To/From Zero alongside target-based or rule-based auto scaling for comprehensive capacity management.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
