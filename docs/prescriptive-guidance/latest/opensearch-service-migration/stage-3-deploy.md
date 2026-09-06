---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/stage-3-deploy.html
---

# Stage 3 - Deployment
<a name="stage-3-deploy"></a>

By the time you reach the deployment stage, you have completed your PoC, and you have a good idea of how to deploy your target environment to production. Keep in mind the following considerations:
+ **Validate automation** – During the deployment, run the automation that you created during the PoC, and validate that it's working as expected. Also validate that your CI/CD automation is working as expected when you make configuration code changes.
+ **Verify security** – It's critical to verify that all your security configurations are working as expected and that your data is secure. Confirm that the solution is vetted against your company's security standards, such as identity provider integration, and that your key users are able to log in and access data that they are authorized to access.
+ **Monitoring** – Make sure that you have tested your monitoring configurations and have set up the recommended alerts. Monitor key metrics such as CPU, memory, disks, JVMs, and shard allocations. To give you the insights about the health of your Amazon OpenSearch Service domain and associated integrations, you can build a dashboard in Amazon CloudWatch. You can verify that your operations support team has access to the dashboard. The [Operational excellence](stage-6-operational-excellence.md) section provides links to useful tips for setting up a highly performant, resilient OpenSearch Service domain.
+ **Exercise alarms** – Make sure that you test all your alarms. If you are using Amazon CloudWatch or an alerting plugin, validate that all integrations, such as Amazon Simple Notification Service (Amazon SNS), Amazon Chime, or Slack, work as expected. Simulate alerts to validate that the alerts are delivered correctly to the destination channel. Confirm that the alert text provides helpful information. For example, the alert could provide a link to the associated runbook for your support team to implement an associated remediation process.
