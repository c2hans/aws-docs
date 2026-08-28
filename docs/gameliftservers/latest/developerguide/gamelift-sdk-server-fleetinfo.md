---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-sdk-server-fleetinfo.html
---

# Let your game server access Amazon GameLift Servers fleet data
<a name="gamelift-sdk-server-fleetinfo"></a>

There are some situations where your custom game build or Amazon GameLift Servers Realtime script may require information about the Amazon GameLift Servers fleet. For example, your game build or script might include code to:
+ Monitor activity based on fleet data.
+ Roll up metrics to track activity by fleet data. (Many games use this data for LiveOps activities.)
+ Provide relevant data to custom game services, such as for matchmaking, additional capacity scaling, or testing.

Fleet information is available as a JSON file on each instance in the following locations:
+ Windows: `C:\GameMetadata\gamelift-metadata.json`
+ Linux: `/local/gamemetadata/gamelift-metadata.json`

The `gamelift-metadata.json` file includes the [attributes of an Amazon GameLift Servers fleet resource](https://docs.aws.amazon.com/gamelift/latest/apireference/API_FleetAttributes.html).

Example JSON file:

```
{
    "buildArn":"arn:aws:gamelift:us-west-2:123456789012:build/build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "buildId":"build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "fleetArn":"arn:aws:gamelift:us-west-2:123456789012:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "fleetDescription":"Test fleet for Really Fun Game v0.8",
    "fleetId":"fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "name":"ReallyFunGameTestFleet08",
    "fleetType":"ON_DEMAND",
    "instanceRoleArn":"arn:aws:iam::123456789012:role/S3AccessForGameLift",
    "instanceType":"c5.large",
    "serverLaunchPath":"/local/game/reallyfungame.exe"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
