---
source_url: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html
---

# Working with deployment strategies
<a name="appconfig-creating-deployment-strategy"></a>

A deployment strategy enables you to slowly release changes to all targets or specific segments over minutes or hours—either session based or along your own target dimension by leveraging entity-based deployments.

**Note**
AWS AppConfig Agent (version 2.0.136060 or later) supports deploying feature flag or free-form configuration data to specific segments or individual users during a gradual rollout. Entity-based gradual deployments ensure that once a user or segment receives a configuration version, they continue to receive that same version throughout the deployment period, regardless of which compute resource serves their requests. For more information, see [Using AWS AppConfig Agent for user- or entity-based gradual deployments](appconfig-agent-how-to-use.md#appconfig-entity-based-gradual-deployments).

An AWS AppConfig deployment strategy defines the following important aspects of a configuration deployment.

****

| Setting | Description |
| --- | --- |
| Elapsed time | Deployment progress |
| --- | --- |
| Deployment type | Deployment type defines how the configuration deploys or *rolls out*. AWS AppConfig supports **Linear** and **Exponential** deployment types.[See the AWS documentation website for more details](http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html) |
| Step percentage (growth factor) | This setting specifies the percentage of callers to target during each step of the deployment. In the SDK and the [AWS AppConfig API Reference](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateDeploymentStrategy.html), `step percentage` is called `growth factor`.  |
| Deployment time | This setting specifies an amount of time during which AWS AppConfig deploys to hosts. This is not a timeout value. It is a window of time during which the deployment is processed in intervals. |
| Bake time | This setting specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. You must configure permissions for AWS AppConfig to roll back based on CloudWatch alarms. For more information, see [Configure permissions for automatic rollback](setting-up-appconfig.md#getting-started-with-appconfig-cloudwatch-alarms-permissions). |
| 0 hour | 0% |
| 2 hour | 20% |
| 4 hour | 40% |
| 6 hour | 60% |
| 8 hour | 80% |
| 10 hour | 100% |

You can choose a predefined strategy included with AWS AppConfig or create your own.

**Note**
AWS AppConfig Agent (version 2.0.136060 or later) supports deploying feature flag or free-form configuration data to specific segments or individual users during a gradual rollout. Entity-based gradual deployments ensure that once a user or segment receives a configuration version, they continue to receive that same version throughout the deployment period, regardless of which compute resource serves their requests. For more information, see [Using AWS AppConfig Agent for user- or entity-based gradual deployments](appconfig-agent-how-to-use.md#appconfig-entity-based-gradual-deployments).

**Topics**
+ [Using predefined deployment strategies](appconfig-creating-deployment-strategy-predefined.md)
+ [Create a deployment strategy](appconfig-creating-deployment-strategy-create.md)
