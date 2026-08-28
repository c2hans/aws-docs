---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/architecture-gain-visibility.html
---

# Gaining visibility
<a name="architecture-gain-visibility"></a>

The ability to view the security events that have occurred is just as important as establishing proper security controls. In the security pillar of the AWS Well-Architected Framework, detection best practices include [Configure service and application logging](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_app_service_logging.html) and [Capture logs, findings, and metrics in standardized locations](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_logs.html). To implement these best practices, you must record the information that helps you identify events and then process that information into a human-consumable format, ideally in a centralized location.

This guide recommends that you use [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) to centralize log data. Amazon S3 supports log storage for both AWS Network Firewall and Amazon Route 53 Resolver DNS Firewall. Then, you use [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) and [Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) to centralize the Amazon GuardDuty findings and other security findings into a single location.

## Logging network traffic
<a name="architecture-gain-visibility-logging"></a>

The [Automating preventative and detective security controls](architecture-automate-controls.md) section of this guide describes using AWS Network Firewall and Amazon Route 53 Resolver DNS Firewall to automate responses to cyber threat intelligence (CTI). We recommend that you configure logging for both of these services. You can create detective controls that monitor the log data and alert you if a restricted domain or IP address tries to send traffic through the firewall.

When configuring these resources, consider your individual logging requirements. For instance, logging for Network Firewall is available only for traffic that you forward to the stateful rules engine. We recommend that you follow a zero-trust model and forward all traffic to the stateful rules engine. However, if you want to reduce costs, you can exclude traffic that your organization trusts.

Both Network Firewall and DNS Firewall support logging to Amazon S3. For more information about setting up logging for these services, see [Logging network traffic from AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging.html) and [Configuring logging for DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/firewall-resolver-query-logs-configuring.html). For both services, you can configure logging to an Amazon S3 bucket through the AWS Management Console.

## Centralizing security findings in AWS
<a name="architecture-gain-visibility-security-hub"></a>

[AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides a comprehensive view of your security state in AWS and helps you assess your AWS environment against security industry standards and best practices. Security Hub CSPM can generate findings that are associated with your security controls. It can also receive findings from other AWS services, such as Amazon GuardDuty. You can use Security Hub CSPM to centralize findings and data from across your AWS accounts, AWS services, and supported third-party products. For more information about integrations, see [Understanding integrations in Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-providers.html) in the Security Hub CSPM documentation.

Security Hub CSPM also includes automation features that help you triage and remediate security issues. For example, you can use automation rules to automatically update critical findings when a security check fails. You can also use the integration with Amazon EventBridge to initiate automatic responses to specific findings. For more information, see [Automatically modifying and acting on Security Hub CSPM findings](https://docs.aws.amazon.com/securityhub/latest/userguide/automations.html) in the Security Hub CSPM documentation.

If you use Amazon GuardDuty, we recommend that you configure GuardDuty to send its findings to Security Hub CSPM. Security Hub CSPM can then include those findings in its analysis of your security posture. For more information, see [Integrating with AWS Security Hub CSPM](https://docs.aws.amazon.com/guardduty/latest/ug/securityhub-integration.html) in the GuardDuty documentation.

For both Network Firewall and Route 53 Resolver DNS Firewall, you can create custom findings from the network traffic that you're logging. [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon S3 by using standard SQL. You can construct queries in Athena that scan the logs in Amazon S3 and extract the relevant data. For instructions, see [Getting Started](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) in the Athena documentation. Then, you can use an AWS Lambda function to convert the relevant log data into [AWS Security Finding Format (ASFF)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html) and send the finding to Security Hub CSPM. The following is a sample Lambda function that converts log data from Network Firewall into a Security Hub CSPM finding:

```
Import { SecurityHubClient, BatchImportFindingsCommand, GetFindingsCommand } from "@aws-sdk/client-securityhub";

Export const handler = async(event) => {
   const date = new Date().toISOString();

   const config = {
      Region: REGION
   };

   const input = {
      Findings: [
         {
            SchemaVersion: '2018-10-08',
            Id: ALERTLOGS3BUCKETID,
            ProductArn: FIREWALLMANAGERARN,
            GeneratorId: 'alertlogs-to-findings',
            AwsAccountId: ACCOUNTID,
            Types: 'Unusual Behaviours/Network Flow/Alert',
            CreatedAt: date,
            UpdatedAt: date,
            Severity: {
               Normalized: 80,
               Product: 8
            },
            Confidence: 100,
            Title: 'Alert Log to Findings',
            Description: 'Network Firewall Alert Log into Finding – add
               top level dynamic detail',
            Resources: [
               {
                  /*these are custom resources. Contain deeper details of your event here*/
                  firewallName: 'Example Name',
                  event: 'Example details here'
               }
            ]
         }
      ]
   };

   const client = new SecurityHubClient(config);
   const command = new BatchImportFindingsCommand(input);
   const response = await client.send(command);
   return { statusCode: 200, response };
};
```

The pattern that you follow for extracting and sending information to Security Hub CSPM is dependent on your individual business needs. If you need the data to be sent on a regular schedule, you can use EventBridge to initiate the process. If you want to receive an alert when the information is added, you can use [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html). There are many ways to approach this architecture, so it's important to properly plan so that your business needs are achieved.

## Integrating AWS security data with other enterprise data
<a name="architecture-gain-visibility-enterprise-data"></a>

[Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) can automate the collection of security-related log and event data from integrated AWS services and third-party services. It also helps you manage the lifecycle of data with customizable retention and replication settings. Security Lake converts ingested data into Apache Parquet format and a standard open-source schema called the Open Cybersecurity Schema Framework (OCSF). With OCSF support, Security Lake normalizes and combines security data from AWS and a broad range of enterprise security data sources. Other AWS services and third-party services can subscribe to the data that's stored in Security Lake for incident response and security data analytics.

You can configure Security Lake to receive findings from Security Hub CSPM. To activate this integration, you must enable both services and add Security Hub CSPM as a source in Security Lake. Once you complete these steps, Security Hub CSPM begins to send all findings to Security Lake. Security Lake automatically normalizes Security Hub CSPM findings and converts them to OCSF. In Security Lake, you can add one or more subscribers to consume Security Hub CSPM findings. For more information, see [Integration with AWS Security Hub CSPM](https://docs.aws.amazon.com/security-lake/latest/userguide/aws-integrations.html#securityhub-integration) in the Security Lake documentation.

The following video, [AWS re:Inforce 2024 - Cyber threat intelligence sharing on AWS](https://www.youtube.com/watch?v=ufNNHBPPjQU), discusses how you can use Security Hub CSPM and Security Lake integrations to share CTI.

[https://www.youtube-nocookie.com/embed/ufNNHBPPjQU?controls=0](https://www.youtube-nocookie.com/embed/ufNNHBPPjQU?controls=0)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
