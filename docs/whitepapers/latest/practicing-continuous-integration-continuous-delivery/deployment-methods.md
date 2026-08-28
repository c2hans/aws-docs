---
source_url: https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/deployment-methods.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Deployment methods
<a name="deployment-methods"></a>

 You can consider multiple deployment strategies and variations for rolling out new versions of software in a continuous delivery process. This section discusses the most common deployment methods: all at once (deploy in place), rolling, immutable, and blue/green.

 The following table summarizes the characteristics of each deployment method.

|  **Method**  |  **Impact of failed deployment**  |  **Deploy time**  |  **Zero downtime**  |  **No DNS change**  |  **Rollback process**  |  **Code deployed to**  |
| --- | --- | --- | --- | --- | --- | --- |
|  Deploy in place  |  Downtime  |  1x  |  ☓  |  ✓  |  Re-deploy  |  Existing instances  |
|  Rolling  |  Single batch out of service. Any successful batches prior to failure running new application version.  |  2x  |  ✓  |  ✓  |  Re-deploy  |  Existing instances  |
|  Immutable  |  Minimal  |  4x  |  ✓  |  ✓  |  Re-deploy  |  New instances  |
|  Traffic splitting  |  Minimal  |  4x  |  ✓  |  ✓  |  Re-route traffic and terminate new instances  |  New instances  |
|  Blue/green  |  Minimal  |  4x  |  ✓  |  ☓  |  Switch back to old environment  |  New instances  |

## All at once (in-place deployment)
<a name="all-at-once-in-place-deployment"></a>

 All at once (in-place deployment) is a method you can use to roll out new application code to an existing fleet of servers. This method replaces all the code in one deployment action. It requires downtime because all servers in the fleet are updated at once. There is no need to update existing DNS records. In case of a failed deployment, the only way to restore operations is to redeploy the code on all servers again.

## Rolling deployment
<a name="rolling-deployment"></a>

 With rolling deployment, the fleet is divided into portions so that all of the fleet isn’t upgraded at once. During the deployment process two software versions, new and old, are running on the same fleet. This method allows a zero-downtime update. If the deployment fails, only the updated portion of the fleet will be affected.

 A variation of the rolling deployment method, called canary release, involves deployment of the new software version on a very small percentage of servers at first. This way, you can observe how the software behaves in production on a few servers, while minimizing the impact of breaking changes. If there is an elevated rate of errors from a canary deployment, the software is rolled back. Otherwise, the percentage of servers with the new version is gradually increased.

## Immutable and blue/green deployment
<a name="immutable-and-bluegreen-deployment"></a>

 The immutable pattern specifies a deployment of application code by starting an entirely new set of servers with a new configuration or version of application code. This pattern leverages the cloud capability that new server resources are created with simple API calls.

 The blue/green deployment strategy is a type of immutable deployment which also requires creation of another environment. Once the new environment is up and passed all tests, traffic is shifted to this new deployment. Crucially the old environment, that is the "blue" environment, is kept idle in case a rollback is needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
