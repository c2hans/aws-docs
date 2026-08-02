---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/securityhub-integration.html
---

# Integrating with AWS Security Hub CSPM
<a name="securityhub-integration"></a>

[AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides you with a comprehensive view of your security state in AWS and helps you to check your environment against security industry standards and best practices. Security Hub CSPM collects security data from across AWS accounts, services, and supported third-party partner products and helps you to analyze your security trends and identify the highest priority security issues.

The Amazon GuardDuty integration with Security Hub CSPM enables you to send findings from GuardDuty to Security Hub CSPM. Security Hub CSPM can then include those findings in its analysis of your security posture.

**Contents**
+ [How Amazon GuardDuty sends findings to AWS Security Hub CSPM](#securityhub-integration-sending-findings)
  + [Types of findings that GuardDuty sends to Security Hub CSPM](#securityhub-integration-finding-types)
    + [Latency for sending new findings](#securityhub-integration-finding-latency)
    + [Retrying when Security Hub CSPM is not available](#securityhub-integration-retry-send)
    + [Updating existing findings in Security Hub CSPM](#securityhub-integration-finding-updates)
+ [Viewing GuardDuty findings in AWS Security Hub CSPM](#findings-in-securityhub)
  + [Interpreting GuardDuty finding names in AWS Security Hub CSPM](#interpreting-findings-in-securityhub)
  + [Typical finding from GuardDuty](#securityhub-integration-finding-example)
+ [Enabling and configuring the integration](#securityhub-integration-enable)
+ [Using GuardDuty controls in Security Hub CSPM](#securityhub-integration-using-guardduty-controls)
+ [Stopping the publication of findings to Security Hub CSPM](#securityhub-integration-disable)

## How Amazon GuardDuty sends findings to AWS Security Hub CSPM
<a name="securityhub-integration-sending-findings"></a>

In AWS Security Hub CSPM, security issues are tracked as findings. Some findings come from issues that are detected by other AWS services or by third-party partners. Security Hub CSPM also has a set of rules that it uses to detect security issues and generate findings.

Security Hub CSPM provides tools to manage findings from across all of these sources. You can view and filter lists of findings and view details for a finding. For more information, see [Viewing findings](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-viewing.html) in the *AWS Security Hub User Guide*. You can also track the status of an investigation into a finding. For more information, see [Taking action on findings](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-taking-action.html) in the *AWS Security Hub User Guide*.

All findings in Security Hub CSPM use a standard JSON format called the AWS Security Finding Format (ASFF). The ASFF includes details about the source of the issue, the affected resources, and the current status of the finding. See [AWS Security Finding Format (ASFF)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html) in the *AWS Security Hub User Guide*.

Amazon GuardDuty is one of the AWS services that sends findings to Security Hub CSPM.

### Types of findings that GuardDuty sends to Security Hub CSPM
<a name="securityhub-integration-finding-types"></a>

Once you enable GuardDuty and Security Hub CSPM in the same account within the same AWS Region, GuardDuty starts sending all the generated findings to Security Hub CSPM. These findings are sent to Security Hub CSPM using the [AWS Security Finding Format (ASFF)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html). In ASFF, the `Types` field provides the finding type.

#### Latency for sending new findings
<a name="securityhub-integration-finding-latency"></a>

When GuardDuty creates a new finding, it is usually sent to Security Hub CSPM within five minutes.

#### Retrying when Security Hub CSPM is not available
<a name="securityhub-integration-retry-send"></a>

If Security Hub CSPM is not available, GuardDuty retries sending the findings until they are received.

#### Updating existing findings in Security Hub CSPM
<a name="securityhub-integration-finding-updates"></a>

After it sends a finding to Security Hub CSPM, GuardDuty sends updates to reflect additional observations of the finding activity to Security Hub CSPM. The new observations of these findings are sent to Security Hub CSPM based on the [Step 5 – Frequency for exporting findings](guardduty_exportfindings.md#guardduty_exportfindings-frequency) settings in your AWS account.

When you archive or unarchive a finding, GuardDuty doesn't send that finding to Security Hub CSPM. Any manually unarchived finding that later become active in GuardDuty is not sent to Security Hub CSPM.

## Viewing GuardDuty findings in AWS Security Hub CSPM
<a name="findings-in-securityhub"></a>

Sign in to the AWS Management Console and open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

You can now use either of the following ways to view the GuardDuty findings in the Security Hub CSPM console:

**Option 1: Using *Integrations* in Security Hub CSPM**

1. In the left navigation pane, choose **Integrations**.

1. On the **Integrations** page, check the **Status** for **Amazon: GuardDuty**.
   + If the **Status** is **Accepting findings**, then choose **See findings** next to **Accepting findings**.
   + If not, then for more information about how **Integrations** work, see [Security Hub CSPM integrations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-providers.html) in *AWS Security Hub User Guide*.

**Option 2: Using *Findings* in Security Hub CSPM**

1. In the left navigation pane, choose **Findings**.

1. On the **Findings** page, add the filter **Product name** and enter **GuardDuty** to view only GuardDuty findings.

### Interpreting GuardDuty finding names in AWS Security Hub CSPM
<a name="interpreting-findings-in-securityhub"></a>

GuardDuty sends the findings to Security Hub CSPM using the [AWS Security Finding Format (ASFF)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html). In ASFF, the `Types` field provides the finding type. ASFF types use a different naming scheme than GuardDuty types. The table below details all the GuardDuty finding types with their ASFF counterpart as they appear in Security Hub CSPM.

**Note**
For some GuardDuty finding types Security Hub CSPM assigns different ASFF finding names depending on whether the finding detail's **Resource Role** was **ACTOR** or **TARGET**. For more information see [Finding details](guardduty_findings-summary.md).

|  GuardDuty finding type  |  ASFF finding type  |
| --- | --- |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-attack-sequence-finding-types.html#attack-sequence-iam-compromised-credentials](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-attack-sequence-finding-types.html#attack-sequence-iam-compromised-credentials) | TTPs/AttackSequence:IAM/CompromisedCredentials  |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-attack-sequence-finding-types.html#attack-sequence-s3-compromised-data](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-attack-sequence-finding-types.html#attack-sequence-s3-compromised-data) | TTPs/AttackSequence:S3/CompromisedData  |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-ccactivityb](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-ccactivityb) | TTPs/Command and Control/Backdoor:EC2-C&CActivity.B |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-ccactivitybdns](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-ccactivitybdns) | TTPs/Command and Control/Backdoor:EC2-C&CActivity.B\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-denialofservicedns](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-denialofservicedns) | TTPs/Command and Control/Backdoor:EC2-DenialOfService.Dns |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-denialofservicetcp](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-denialofservicetcp) | TTPs/Command and Control/Backdoor:EC2-DenialOfService.Tcp |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-denialofserviceudp](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-denialofserviceudp) | TTPs/Command and Control/Backdoor:EC2-DenialOfService.Udp |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-denialofserviceudpontcpports](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-denialofserviceudpontcpports) | TTPs/Command and Control/Backdoor:EC2-DenialOfService.UdpOnTcpPorts |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-denialofserviceunusualprotocol](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-denialofserviceunusualprotocol) | TTPs/Command and Control/Backdoor:EC2-DenialOfService.UnusualProtocol |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-spambot](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#backdoor-ec2-spambot) | TTPs/Command and Control/Backdoor:EC2-Spambot |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#behavior-ec2-networkportunusual](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#behavior-ec2-networkportunusual) | Unusual Behaviors/VM/Behavior:EC2-NetworkPortUnusual |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#behavior-ec2-trafficvolumeunusual](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#behavior-ec2-trafficvolumeunusual) | Unusual Behaviors/VM/Behavior:EC2-TrafficVolumeUnusual |
| [https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#backdoor-lambda-ccactivity-b](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#backdoor-lambda-ccactivity-b) | TTPs/Command and Control/Backdoor:Lambda-C&CActivity.B |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#backdoor-runtime-ccactivityb](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#backdoor-runtime-ccactivityb) | TTPs/Command and Control/Backdoor:Runtime-C&CActivity.B |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#backdoor-runtime-ccactivitybdns](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#backdoor-runtime-ccactivitybdns) | TTPs/Command and Control/Backdoor:Runtime-C&CActivity.B\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#credentialaccess-iam-anomalousbehavior](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#credentialaccess-iam-anomalousbehavior) | TTPs/Credential Access/IAMUser-AnomalousBehavior |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#credaccess-kubernetes-anomalousbehavior-secretsaccessed](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#credaccess-kubernetes-anomalousbehavior-secretsaccessed) | TTPs/AnomalousBehavior/CredentialAccess:Kubernetes-SecretsAccessed |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#credentialaccess-kubernetes-maliciousipcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#credentialaccess-kubernetes-maliciousipcaller)  | TTPs/CredentialAccess/CredentialAccess:Kubernetes-MaliciousIPCaller |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#credentialaccess-kubernetes-maliciousipcallercustom](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#credentialaccess-kubernetes-maliciousipcallercustom)  | TTPs/CredentialAccess/CredentialAccess:Kubernetes-MaliciousIPCaller.Custom |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#credentialaccess-kubernetes-successfulanonymousaccess](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#credentialaccess-kubernetes-successfulanonymousaccess)  | TTPs/CredentialAccess/CredentialAccess:Kubernetes-SuccessfulAnonymousAccess |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#credentialaccess-kubernetes-toripcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#credentialaccess-kubernetes-toripcaller)  | TTPs/CredentialAccess/CredentialAccess:Kubernetes-TorIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-anombehavior-failedlogin](https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-anombehavior-failedlogin) | TTPs/Credential Access/CredentialAccess:RDS-AnomalousBehavior.FailedLogin |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-anombehavior-successfulbruteforce](https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-anombehavior-successfulbruteforce) | TTPs/Credential Access/CredentialAccess:RDS-AnomalousBehavior.SuccessfulBruteForce |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-anombehavior-successlogin](https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-anombehavior-successlogin) | TTPs/Credential Access/CredentialAccess:RDS-AnomalousBehavior.SuccessfulLogin |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-maliciousipcaller-failedlogin](https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-maliciousipcaller-failedlogin) | TTPs/Credential Access/CredentialAccess:RDS-MaliciousIPCaller.FailedLogin |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-maliciousipcaller-successfullogin](https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-maliciousipcaller-successfullogin) | TTPs/Credential Access/CredentialAccess:RDS-MaliciousIPCaller.SuccessfulLogin |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-toripcaller-failedlogin](https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-toripcaller-failedlogin) | TTPs/Credential Access/CredentialAccess:RDS-TorIPCaller.FailedLogin |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-toripcaller-successfullogin](https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#credaccess-rds-toripcaller-successfullogin) | TTPs/Credential Access/CredentialAccess:RDS-TorIPCaller.SuccessfulLogin |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#cryptocurrency-ec2-bitcointoolb](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#cryptocurrency-ec2-bitcointoolb) | TTPs/Command and Control/CryptoCurrency:EC2-BitcoinTool.B |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#cryptocurrency-ec2-bitcointoolbdns](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#cryptocurrency-ec2-bitcointoolbdns) | TTPs/Command and Control/CryptoCurrency:EC2-BitcoinTool.B\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#cryptocurrency-lambda-bitcointool-b](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#cryptocurrency-lambda-bitcointool-b) | TTPs/Command and Control/CryptoCurrency:Lambda-BitcoinTool.B<br />Effects/Resource Consumption/CryptoCurrency:Lambda-BitcoinTool.B |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#cryptocurrency-runtime-bitcointoolb](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#cryptocurrency-runtime-bitcointoolb) | TTPs/Command and Control/CryptoCurrency:Runtime-BitcoinTool.B |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#cryptocurrency-runtime-bitcointoolbdns](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#cryptocurrency-runtime-bitcointoolbdns) | TTPs/Command and Control/CryptoCurrency:Runtime-BitcoinTool.B\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#defenseevasion-ec2-unusualdnsresolver](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#defenseevasion-ec2-unusualdnsresolver) | TTPs/DefenseEvasion/EC2:Unusual-DNS-Resolver |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#defenseevasion-ec2-unsualdohactivity](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#defenseevasion-ec2-unsualdohactivity) | TTPs/DefenseEvasion/EC2:Unusual-DoH-Activity |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#defenseevasion-ec2-unusualdotactivity](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#defenseevasion-ec2-unusualdotactivity) | TTPs/DefenseEvasion/EC2:Unusual-DoT-Activity |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#defenseevasion-iam-anomalousbehavior](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#defenseevasion-iam-anomalousbehavior) | TTPs/Defense Evasion/IAMUser-AnomalousBehavior |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#defenseevasion-iam-bedrockloggingdisabled](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#defenseevasion-iam-bedrockloggingdisabled) | TTPs/Defense Evasion/DefenseEvasion:IAMUser-BedrockLoggingDisabled |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#defenseevasion-kubernetes-maliciousipcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#defenseevasion-kubernetes-maliciousipcaller) | TTPs/DefenseEvasion/DefenseEvasion:Kubernetes-MaliciousIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#defenseevasion-kubernetes-maliciousipcallercustom](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#defenseevasion-kubernetes-maliciousipcallercustom) | TTPs/DefenseEvasion/DefenseEvasion:Kubernetes-MaliciousIPCaller.Custom |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#defenseevasion-kubernetes-successfulanonymousaccess](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#defenseevasion-kubernetes-successfulanonymousaccess) | TTPs/DefenseEvasion/DefenseEvasion:Kubernetes-SuccessfulAnonymousAccess |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#defenseevasion-kubernetes-toripcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#defenseevasion-kubernetes-toripcaller) | TTPs/DefenseEvasion/DefenseEvasion:Kubernetes-TorIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseeva-runtime-filelessexecution](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseeva-runtime-filelessexecution) | TTPs/Defense Evasion/DefenseEvasion:Runtime-FilelessExecution |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseevasion-runtime-kernelmoduleloaded](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseevasion-runtime-kernelmoduleloaded) | TTPs/Defense Evasion/DefenseEvasion:Runtime-KernelModuleLoaded |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defense-evasion-runtime-sensitive-file-modified](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defense-evasion-runtime-sensitive-file-modified) | TTPs/Defense Evasion/DefenseEvasion:Runtime-SensitiveFileModified |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseeva-runtime-processinjectionproc](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseeva-runtime-processinjectionproc) | TTPs/Defense Evasion/DefenseEvasion:Runtime-ProcessInjection.Proc |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseeva-runtime-processinjectionptrace](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseeva-runtime-processinjectionptrace) | TTPs/Defense Evasion/DefenseEvasion:Runtime-ProcessInjection.Ptrace |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseeva-runtime-processinjectionvirtualmemw](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseeva-runtime-processinjectionvirtualmemw) | TTPs/Defense Evasion/DefenseEvasion:Runtime-ProcessInjection.VirtualMemoryWrite |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseevasion-runtime-ptrace-anti-debug](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseevasion-runtime-ptrace-anti-debug) | TTPs/DefenseEvasion/DefenseEvasion:Runtime-PtraceAntiDebugging |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseevasion-runtime-suspicious-command](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#defenseevasion-runtime-suspicious-command) | TTPs/DefenseEvasion/DefenseEvasion:Runtime-SuspiciousCommand |
| [Discovery:IAMUser/AnomalousBehavior](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#discovery-iam-anomalousbehavior) | TTPs/Discovery/IAMUser-AnomalousBehavior |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#discovery-kubernetes-anomalousbehavrior-permissionchecked](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#discovery-kubernetes-anomalousbehavrior-permissionchecked)  | TTPs/AnomalousBehavior/Discovery:Kubernetes-PermissionChecked |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#discovery-kubernetes-maliciousipcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#discovery-kubernetes-maliciousipcaller)  | TTPs/Discovery/Discovery:Kubernetes-MaliciousIPCaller |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#discovery-kubernetes-maliciousipcallercustom](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#discovery-kubernetes-maliciousipcallercustom)  | TTPs/Discovery/Discovery:Kubernetes-MaliciousIPCaller.Custom |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#discovery-kubernetes-successfulanonymousaccess](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#discovery-kubernetes-successfulanonymousaccess)  | TTPs/Discovery/Discovery:Kubernetes-SuccessfulAnonymousAccess |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#discovery-kubernetes-toripcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#discovery-kubernetes-toripcaller)  | TTPs/Discovery/Discovery:Kubernetes-TorIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#discovery-rds-maliciousipcaller](https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#discovery-rds-maliciousipcaller) | TTPs/Discovery/RDS-MaliciousIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#discovery-rds-toripcaller](https://docs.aws.amazon.com/guardduty/latest/ug/findings-rds-protection.html#discovery-rds-toripcaller) | TTPs/Discovery/RDS-TorIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#discovery-runtime-suspicious-command](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#discovery-runtime-suspicious-command) | TTPs/Discovery/Discovery:Runtime-SuspiciousCommand |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#discovery-s3-anomalousbehavior](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#discovery-s3-anomalousbehavior) | TTPs/Discovery:S3-AnomalousBehavior |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#discovery-s3-bucketenumerationunusual](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#discovery-s3-bucketenumerationunusual) | TTPs/Discovery:S3-BucketEnumeration.Unusual |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#discovery-s3-maliciousipcallercustom.title](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#discovery-s3-maliciousipcallercustom.title) | TTPs/Discovery:S3-MaliciousIPCaller.Custom |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#discovery-s3-toripcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#discovery-s3-toripcaller) | TTPs/Discovery:S3-TorIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#discovery-s3-maliciousipcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#discovery-s3-maliciousipcaller) | TTPs/Discovery:S3-MaliciousIPCaller |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#exfiltration-iam-anomalousbehavior](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#exfiltration-iam-anomalousbehavior)  | TTPs/Exfiltration/IAMUser-AnomalousBehavior |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#execution-kubernetes-execinkubesystempod](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#execution-kubernetes-execinkubesystempod)  | TTPs/Execution/Execution:Kubernetes-ExecInKubeSystemPod |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#execution-kubernetes-anomalousbehvaior-execinprod](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#execution-kubernetes-anomalousbehvaior-execinprod)  | TTPs/AnomalousBehavior/Execution:Kubernetes-ExecInPod |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#exec-kubernetes-anomalousbehavior-workloaddeployed](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#exec-kubernetes-anomalousbehavior-workloaddeployed)  | TTPs/AnomalousBehavior/Execution:Kubernetes-WorkloadDeployed |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-maliciousdomainrequest-custom](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-maliciousdomainrequest-custom)  |  TTPs/Impact/Impact:EC2-MaliciousDomainRequest.Custom  |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#impact-kubernetes-maliciousipcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#impact-kubernetes-maliciousipcaller)  | TTPs/Impact/Impact:Kubernetes-MaliciousIPCaller |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#impact-kubernetes-maliciousipcallercustom](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#impact-kubernetes-maliciousipcallercustom)  | TTPs/Impact/Impact:Kubernetes-MaliciousIPCaller.Custom |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#impact-kubernetes-successfulanonymousaccess](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#impact-kubernetes-successfulanonymousaccess)  | TTPs/Impact/Impact:Kubernetes-SuccessfulAnonymousAccess |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#impact-kubernetes-toripcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#impact-kubernetes-toripcaller)  | TTPs/Impact/Impact:Kubernetes-TorIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#persistence-kubernetes-containerwithsensitivemount](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#persistence-kubernetes-containerwithsensitivemount) | TTPs/Persistence/Persistence:Kubernetes-ContainerWithSensitiveMount |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#privesc-kubernetes-anomalousbehavior-workloaddeployed-containerwithsensitivemount](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#privesc-kubernetes-anomalousbehavior-workloaddeployed-containerwithsensitivemount) | TTPs/AnomalousBehavior/Persistence:Kubernetes-WorkloadDeployed\!ContainerWithSensitiveMount |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#privesc-kubernetes-anomalousbehavior-workloaddeployed-privcontainer](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#privesc-kubernetes-anomalousbehavior-workloaddeployed-privcontainer)  | TTPs/AnomalousBehavior/PrivilegeEscalation:Kubernetes-WorkloadDeployed\!PrivilegedContainer |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#persistence-kubernetes-maliciousipcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#persistence-kubernetes-maliciousipcaller)  | TTPs/Persistence/Persistence:Kubernetes-MaliciousIPCaller |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#persistence-kubernetes-maliciousipcallercustom](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#persistence-kubernetes-maliciousipcallercustom)  | TTPs/Persistence/Persistence:Kubernetes-MaliciousIPCaller.Custom |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#persistence-kubernetes-successfulanonymousaccess](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#persistence-kubernetes-successfulanonymousaccess)  | TTPs/Persistence/Persistence:Kubernetes-SuccessfulAnonymousAccess |
|  [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#persistence-kubernetes-toripcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#persistence-kubernetes-toripcaller)  | TTPs/Persistence/Persistence:Kubernetes-TorIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-ec2-maliciousfile](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-ec2-maliciousfile) | TTPs/Execution/Execution:EC2-MaliciousFile |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-ecs-maliciousfile](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-ecs-maliciousfile) | TTPs/Execution/Execution:ECS-MaliciousFile |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-kubernetes-maliciousfile](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-kubernetes-maliciousfile) | TTPs/Execution/Execution:Kubernetes-MaliciousFile |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-container-maliciousfile](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-container-maliciousfile) | TTPs/Execution/Execution:Container-MaliciousFile |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-ec2-suspiciousfile](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-ec2-suspiciousfile) | TTPs/Execution/Execution:EC2-SuspiciousFile |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-ecs-suspiciousfile](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-ecs-suspiciousfile) | TTPs/Execution/Execution:ECS-SuspiciousFile |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-kubernetes-suspiciousfile](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-kubernetes-suspiciousfile) | TTPs/Execution/Execution:Kubernetes-SuspiciousFile |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-container-suspiciousfile](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-malware-container-suspiciousfile) | TTPs/Execution/Execution:Container-SuspiciousFile |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection-backup.html#execution-malware-ec2-maliciousfile-snapshot](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection-backup.html#execution-malware-ec2-maliciousfile-snapshot) | TTPs/Execution/Execution:EC2-MaliciousFile\!Snapshot |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection-backup.html#execution-malware-ec2-maliciousfile-ami](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection-backup.html#execution-malware-ec2-maliciousfile-ami) | TTPs/Execution/Execution:EC2-MaliciousFile\!AMI |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection-backup.html#execution-malware-ec2-maliciousfile-recoverypoint](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection-backup.html#execution-malware-ec2-maliciousfile-recoverypoint) | TTPs/Execution/Execution:EC2-MaliciousFile\!RecoveryPoint |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection-backup.html#execution-malware-s3-maliciousfile-recoverypoint](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection-backup.html#execution-malware-s3-maliciousfile-recoverypoint) | TTPs/Execution/Execution:S3-MaliciousFile\!RecoveryPoint |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-runtime-malicious-file-executed](https://docs.aws.amazon.com/guardduty/latest/ug/findings-malware-protection.html#execution-runtime-malicious-file-executed) | TTPs/Execution/Execution:Runtime-MaliciousFileExecuted |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-malicious-file-executed-custom](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-malicious-file-executed-custom) | TTPs/Execution/Execution:Runtime-MaliciousFileExecuted.Custom |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-newbinaryexecuted](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-newbinaryexecuted) | TTPs/Execution/Execution:Runtime-NewBinaryExecuted |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-newlibraryloaded](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-newlibraryloaded) | TTPs/Execution/Execution:Runtime-NewLibraryLoaded |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-reverseshell](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-reverseshell) | TTPs/Execution/Execution:Runtime-ReverseShell |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-suspiciouscommand](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-suspiciouscommand) | TTPs/Execution/Execution:Runtime-SuspiciousCommand |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-suspicious-shell-created](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-suspicious-shell-created) | TTPs/Execution/Execution:Runtime-SuspiciousShellCreated |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-suspicioustool](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#execution-runtime-suspicioustool) | TTPs/Execution/Execution:Runtime-SuspiciousTool |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#exfiltration-s3-anomalousbehavior](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#exfiltration-s3-anomalousbehavior) | TTPs/Exfiltration:S3-AnomalousBehavior |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#exfiltration-s3-objectreadunusual](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#exfiltration-s3-objectreadunusual) | TTPs/Exfiltration:S3-ObjectRead.Unusual |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#exfiltration-s3-maliciousipcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#exfiltration-s3-maliciousipcaller) | TTPs/Exfiltration:S3-MaliciousIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-abuseddomainrequestreputation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-abuseddomainrequestreputation) | TTPs/Impact:EC2-AbusedDomainRequest.Reputation |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-bitcoindomainrequestreputation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-bitcoindomainrequestreputation) | TTPs/Impact:EC2-BitcoinDomainRequest.Reputation |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-maliciousdomainrequestreputation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-maliciousdomainrequestreputation) | TTPs/Impact:EC2-MaliciousDomainRequest.Reputation |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-portsweep](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-portsweep) | TTPs/Impact/Impact:EC2-PortSweep |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-suspiciousdomainrequestreputation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-suspiciousdomainrequestreputation) | TTPs/Impact:EC2-SuspiciousDomainRequest.Reputation |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-winrmbruteforce](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#impact-ec2-winrmbruteforce) | TTPs/Impact/Impact:EC2-WinRMBruteForce |
| [Impact:IAMUser/AnomalousBehavior](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#impact-iam-anomalousbehavior) | TTPs/Impact/IAMUser-AnomalousBehavior |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#impact-runtime-abuseddomainrequestreputation](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#impact-runtime-abuseddomainrequestreputation) | TTPs/Impact/Impact:Runtime-AbusedDomainRequest.Reputation |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#impact-runtime-bitcoindomainrequestreputation](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#impact-runtime-bitcoindomainrequestreputation) | TTPs/Impact/Impact:Runtime-BitcoinDomainRequest.Reputation |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#impact-runtime-cryptominerexecuted](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#impact-runtime-cryptominerexecuted) | TTPs/Impact/Impact:Runtime-CryptoMinerExecuted |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#impact-runtime-maliciousdomainrequestreputation](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#impact-runtime-maliciousdomainrequestreputation) | TTPs/Impact/Impact:Runtime-MaliciousDomainRequest.Reputation |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#impact-runtime-suspiciousdomainrequestreputation](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#impact-runtime-suspiciousdomainrequestreputation) | TTPs/Impact/Impact:Runtime-SuspiciousDomainRequest.Reputatio |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#impact-s3-anomalousbehavior-delete](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#impact-s3-anomalousbehavior-delete) | TTPs/Impact:S3-AnomalousBehavior.Delete |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#impact-s3-anomalousbehavior-permission](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#impact-s3-anomalousbehavior-permission) | TTPs/Impact:S3-AnomalousBehavior.Permission |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#impact-s3-anomalousbehavior-write](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#impact-s3-anomalousbehavior-write) | TTPs/Impact:S3-AnomalousBehavior.Write |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#impact-s3-objectdeleteunusual](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#impact-s3-objectdeleteunusual) | TTPs/Impact:S3-ObjectDelete.Unusual |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#impact-s3-permissionsmodificationunusual](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#impact-s3-permissionsmodificationunusual) | TTPs/Impact:S3-PermissionsModification.Unusual |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#impact-s3-maliciousipcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#impact-s3-maliciousipcaller) | TTPs/Impact:S3-MaliciousIPCaller |
| [InitialAccess:IAMUser/AnomalousBehavior](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#initialaccess-iam-anomalousbehavior) | TTPs/Initial Access/IAMUser-AnomalousBehavior |
| [https://docs.aws.amazon.com/guardduty/latest/ug/gdu-malware-protection-s3-finding-types.html#s3-object-s3-malicious-file](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-malware-protection-s3-finding-types.html#s3-object-s3-malicious-file) | TTPs/Object/Object:S3-MaliciousFile |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#pentest-iam-kalilinux](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#pentest-iam-kalilinux) | TTPs/PenTest:IAMUser/KaliLinux |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#pentest-iam-parrotlinux](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#pentest-iam-parrotlinux) | TTPs/PenTest:IAMUser/ParrotLinux |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#pentest-iam-pentoolinux](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#pentest-iam-pentoolinux) | TTPs/PenTest:IAMUser/PentooLinux |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#pentest-iam-kalilinux](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#pentest-iam-kalilinux) | TTPs/PenTest:S3-KaliLinux |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#pentest-s3-parrotlinux](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#pentest-s3-parrotlinux) | TTPs/PenTest:S3-ParrotLinux |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#pentest-s3-pentoolinux](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#pentest-s3-pentoolinux) | TTPs/PenTest:S3-PentooLinux |
|  [Persistence:IAMUser/AnomalousBehavior](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#persistence-iam-anomalousbehavior)  | TTPs/Persistence/IAMUser-AnomalousBehavior |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#persistence-iam-networkpermissions](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#persistence-iam-networkpermissions) | TTPs/Persistence/Persistence:IAMUser-NetworkPermissions |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#persistence-iam-resourcepermissions](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#persistence-iam-resourcepermissions) | TTPs/Persistence/Persistence:IAMUser-ResourcePermissions |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#persistence-iam-userpermissions](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#persistence-iam-userpermissions) | TTPs/Persistence/Persistence:IAMUser-UserPermissions |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#persistence-runtime-suspicious-command](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#persistence-runtime-suspicious-command) | TTPs/Persistence/Persistence:Runtime-SuspiciousCommand |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#persistence-runtime-sensitive-file-modified](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#persistence-runtime-sensitive-file-modified) | TTPs/Persistence/Persistence:Runtime-SensitiveFileModified |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#policy-iam-rootcredentialusage](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#policy-iam-rootcredentialusage) | TTPs/Policy:IAMUser-RootCredentialUsage |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#policy-iam-user-short-term-root-credential-usage](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#policy-iam-user-short-term-root-credential-usage) | TTPs/Policy:IAMUser-ShortTermRootCredentialUsage |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#policy-kubernetes-adminaccesstodefaultserviceaccount](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#policy-kubernetes-adminaccesstodefaultserviceaccount) | Software and Configuration Checks/AWS Security Best Practices/Policy:Kubernetes-AdminAccessToDefaultServiceAccount |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#policy-kubernetes-anonymousaccessgranted](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#policy-kubernetes-anonymousaccessgranted) | Software and Configuration Checks/AWS Security Best Practices/Policy:Kubernetes-AnonymousAccessGranted |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#policy-kubernetes-exposeddashboard](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#policy-kubernetes-exposeddashboard) | Software and Configuration Checks/AWS Security Best Practices/Policy:Kubernetes-ExposedDashboard |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#policy-kubernetes-kubeflowdashboardexposed](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#policy-kubernetes-kubeflowdashboardexposed) | Software and Configuration Checks/AWS Security Best Practices/Policy:Kubernetes-KubeflowDashboardExposed |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#policy-s3-accountblockpublicaccessdisabled](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#policy-s3-accountblockpublicaccessdisabled) | TTPs/Policy:S3-AccountBlockPublicAccessDisabled |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#policy-s3-bucketanonymousaccessgranted](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#policy-s3-bucketanonymousaccessgranted) | TTPs/Policy:S3-BucketAnonymousAccessGranted |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#policy-s3-bucketblockpublicaccessdisabled](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#policy-s3-bucketblockpublicaccessdisabled) | Effects/Data Exposure/Policy:S3-BucketBlockPublicAccessDisabled |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#policy-s3-bucketpublicaccessgranted](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#policy-s3-bucketpublicaccessgranted) | TTPs/Policy:S3-BucketPublicAccessGranted |
|  [PrivilegeEscalation:IAMUser/AnomalousBehavior](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#privilegeescalation-iam-anomalousbehavior)  |  TTPs/Privilege Escalation/IAMUser-AnomalousBehavior  |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeescalation-iam-administrativepermissions](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeescalation-iam-administrativepermissions) | TTPs/Privilege Escalation/PrivilegeEscalation:IAMUser-AdministrativePermissions |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#privesc-kubernetes-anomalousbehavior-rolebindingcreated](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#privesc-kubernetes-anomalousbehavior-rolebindingcreated) | TTPs/AnomalousBehavior/PrivilegeEscalation:Kubernetes-RoleBindingCreated |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#privesc-kubernetes-anomalousbehavior-rolecreated](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-finding-types-eks-audit-logs.html#privesc-kubernetes-anomalousbehavior-rolecreated) | TTPs/AnomalousBehavior/PrivilegeEscalation:Kubernetes-RoleCreated |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeescalation-kubernetes-privilegedcontainer](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeescalation-kubernetes-privilegedcontainer) | TTPs/PrivilegeEscalation/PrivilegeEscalation:Kubernetes-PrivilegedContainer |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeesc-runtime-containermountshostdirectory](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeesc-runtime-containermountshostdirectory) | TTPs/Privilege Escalation/PrivilegeEscalation:Runtime-ContainerMountsHostDirectory |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeesc-runtime-cgroupsreleaseagentmodified](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeesc-runtime-cgroupsreleaseagentmodified) | TTPs/Privilege Escalation/PrivilegeEscalation:Runtime-CGroupsReleaseAgentModified |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeesc-runtime-dockersocketaccessed](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeesc-runtime-dockersocketaccessed) | TTPs/Privilege Escalation/PrivilegeEscalation:Runtime-DockerSocketAccessed |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeesc-runtime-elevation-to-root](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeesc-runtime-elevation-to-root) | TTPs/Privilege Escalation/PrivilegeEscalation:Runtime-ElevationToRoot |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeesc-runtime-runccontainerescape](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeesc-runtime-runccontainerescape) | TTPs/Privilege Escalation/PrivilegeEscalation:Runtime-RuncContainerEscape |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#privilege-escalation-runtime-suspicious-command](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#privilege-escalation-runtime-suspicious-command) | Software and Configuration Checks/PrivilegeEscalation:Runtime-SuspiciousCommand |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#privilege-escalation-runtime-sensitive-file-modified](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#privilege-escalation-runtime-sensitive-file-modified) | TTPs/Privilege Escalation/PrivilegeEscalation:Runtime-SensitiveFileModified |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeesc-runtime-userfaultfdusage](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#privilegeesc-runtime-userfaultfdusage) | TTPs/Privilege Escalation/PrivilegeEscalation:Runtime-UserfaultfdUsage |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#recon-ec2-portprobeemrunprotectedport](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#recon-ec2-portprobeemrunprotectedport) | TTPs/Discovery/Recon:EC2-PortProbeEMRUnprotectedPort |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#recon-ec2-portprobeunprotectedport](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#recon-ec2-portprobeunprotectedport) | TTPs/Discovery/Recon:EC2-PortProbeUnprotectedPort |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#recon-ec2-portscan](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#recon-ec2-portscan) | TTPs/Discovery/Recon:EC2-Portscan |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#recon-iam-maliciousipcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#recon-iam-maliciousipcaller) | TTPs/Discovery/Recon:IAMUser-MaliciousIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#recon-iam-maliciousipcallercustom](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#recon-iam-maliciousipcallercustom) | TTPs/Discovery/Recon:IAMUser-MaliciousIPCaller.Custom |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#recon-iam-networkpermissions](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#recon-iam-networkpermissions) | TTPs/Discovery/Recon:IAMUser-NetworkPermissions |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#recon-iam-resourcepermissions](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#recon-iam-resourcepermissions) | TTPs/Discovery/Recon:IAMUser-ResourcePermissions |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#recon-iam-toripcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#recon-iam-toripcaller) | TTPs/Discovery/Recon:IAMUser-TorIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#recon-iam-userpermissions](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#recon-iam-userpermissions) | TTPs/Discovery/Recon:IAMUser-UserPermissions |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#resourceconsumption-iam-computeresources](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#resourceconsumption-iam-computeresources) | Unusual Behaviors/User/ResourceConsumption:IAMUser-ComputeResources |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#stealth-iam-cloudtrailloggingdisabled](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#stealth-iam-cloudtrailloggingdisabled) | TTPs/Defense Evasion/Stealth:IAMUser-CloudTrailLoggingDisabled |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#stealth-iam-loggingconfigurationmodified](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#stealth-iam-loggingconfigurationmodified) | TTPs/Defense Evasion/Stealth:IAMUser-LoggingConfigurationModified |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#stealth-iam-passwordpolicychange](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#stealth-iam-passwordpolicychange) | TTPs/Defense Evasion/Stealth:IAMUser-PasswordPolicyChange |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#stealth-s3-serveraccessloggingdisabled](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#stealth-s3-serveraccessloggingdisabled) | TTPs/Defense Evasion/Stealth:S3-ServerAccessLoggingDisabled |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-blackholetraffic](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-blackholetraffic) | TTPs/Command and Control/Trojan:EC2-BlackholeTraffic |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-blackholetrafficdns](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-blackholetrafficdns) | TTPs/Command and Control/Trojan:EC2-BlackholeTraffic\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-dgadomainrequestb](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-dgadomainrequestb) | TTPs/Command and Control/Trojan:EC2-DGADomainRequest.B |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-dgadomainrequestcdns](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-dgadomainrequestcdns) | TTPs/Command and Control/Trojan:EC2-DGADomainRequest.C\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-dnsdataexfiltration](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-dnsdataexfiltration) | TTPs/Command and Control/Trojan:EC2-DNSDataExfiltration |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-drivebysourcetrafficdns](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-drivebysourcetrafficdns) | TTPs/Initial Access/Trojan:EC2-DriveBySourceTraffic\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-droppoint](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-droppoint) | Effects/Data Exfiltration/Trojan:EC2-DropPoint |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-droppointdns](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-droppointdns) | Effects/Data Exfiltration/Trojan:EC2-DropPoint\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-phishingdomainrequestdns](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#trojan-ec2-phishingdomainrequestdns) | TTPs/Command and Control/Trojan:EC2-PhishingDomainRequest\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#trojan-lambda-blackhole-traffic](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#trojan-lambda-blackhole-traffic) | TTPs/Command and Control/Trojan:Lambda-BlackholeTraffic |
| [https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#trojan-lambda-drop-point](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#trojan-lambda-drop-point) | Effects/Data Exfiltration/Trojan:Lambda-DropPoint |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-blackholetraffic](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-blackholetraffic) | TTPs/Command and Control/Trojan:Runtime-BlackholeTraffic |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-blackholetrafficdns](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-blackholetrafficdns) | TTPs/Command and Control/Trojan:Runtime-BlackholeTraffic\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-dgadomainrequestcdns](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-dgadomainrequestcdns) | TTPs/Command and Control/Trojan:Runtime-DGADomainRequest.C\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-drivebysourcetrafficdns](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-drivebysourcetrafficdns) | TTPs/Initial Access/Trojan:Runtime-DriveBySourceTraffic\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-droppoint](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-droppoint) | Effects/Data Exfiltration/Trojan:Runtime-DropPoint |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-droppointdns](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-droppointdns) | Effects/Data Exfiltration/Trojan:Runtime-DropPoint\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-phishingdomainrequestdns](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#trojan-runtime-phishingdomainrequestdns) | TTPs/Command and Control/Trojan:Runtime-PhishingDomainRequest\!DNS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#unauthorizedaccess-ec2-maliciousipcallercustom](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#unauthorizedaccess-ec2-maliciousipcallercustom) | TTPs/Command and Control/UnauthorizedAccess:EC2-MaliciousIPCaller.Custom |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#unauthorizedaccess-ec2-metadatadnsrebind](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#unauthorizedaccess-ec2-metadatadnsrebind) | TTPs/UnauthorizedAccess:EC2-MetadataDNSRebind |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#unauthorizedaccess-ec2-rdpbruteforce](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#unauthorizedaccess-ec2-rdpbruteforce) | TTPs/Initial Access/UnauthorizedAccess:EC2-RDPBruteForce |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#unauthorizedaccess-ec2-sshbruteforce](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#unauthorizedaccess-ec2-sshbruteforce) | TTPs/Initial Access/UnauthorizedAccess:EC2-SSHBruteForce |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#unauthorizedaccess-ec2-torclient](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#unauthorizedaccess-ec2-torclient) | Effects/Resource Consumption/UnauthorizedAccess:EC2-TorClient |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#unauthorizedaccess-ec2-torrelay](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-ec2.html#unauthorizedaccess-ec2-torrelay) | Effects/Resource Consumption/UnauthorizedAccess:EC2-TorRelay |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#unauthorizedaccess-iam-consolelogin](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-retired.html#unauthorizedaccess-iam-consolelogin) | Unusual Behaviors/User/UnauthorizedAccess:IAMUser-ConsoleLogin |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-consoleloginsuccessb](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-consoleloginsuccessb) | TTPs/UnauthorizedAccess:IAMUser-ConsoleLoginSuccess.B |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-instancecredentialexfiltrationinsideaws](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-instancecredentialexfiltrationinsideaws) | Effects/Data Exfiltration/UnauthorizedAccess:IAMUser-InstanceCredentialExfiltration.InsideAWS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-instancecredentialexfiltrationoutsideaws](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-instancecredentialexfiltrationoutsideaws) | Effects/Data Exfiltration/UnauthorizedAccess:IAMUser-InstanceCredentialExfiltration.OutsideAWS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-maliciousipcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-maliciousipcaller) | TTPs/UnauthorizedAccess:IAMUser-MaliciousIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-maliciousipcallercustom](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-maliciousipcallercustom) | TTPs/UnauthorizedAccess:IAMUser-MaliciousIPCaller.Custom |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-resourcecredentialexfiltrationinsideaws](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-resourcecredentialexfiltrationinsideaws) | Effects/Data Exfiltration/UnauthorizedAccess:IAMUser-ResourceCredentialExfiltration.InsideAWS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-resourcecredentialexfiltrationoutsideaws](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-resourcecredentialexfiltrationoutsideaws) | Effects/Data Exfiltration/UnauthorizedAccess:IAMUser-ResourceCredentialExfiltration.OutsideAWS |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-toripcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#unauthorizedaccess-iam-toripcaller) | TTPs/Command and Control/UnauthorizedAccess:IAMUser-TorIPCaller |
| [https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#unauthorized-access-lambda-maliciousIPcaller-custom](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#unauthorized-access-lambda-maliciousIPcaller-custom) | TTPs/Command and Control/UnauthorizedAccess:Lambda-MaliciousIPCaller.Custom |
| [https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#unauthorized-access-lambda-tor-client](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#unauthorized-access-lambda-tor-client) | Effects/Resource Consumption/UnauthorizedAccess:Lambda-TorClient |
| [https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#unauthorized-access-lambda-tor-relay](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection-finding-types.html#unauthorized-access-lambda-tor-relay) | Effects/Resource Consumption/UnauthorizedAccess:Lambda-TorRelay |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#unauthorizedaccess-runtime-metadatadnsrebind](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#unauthorizedaccess-runtime-metadatadnsrebind) | TTPs/UnauthorizedAccess:Runtime-MetadataDNSRebind |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#unauthorizedaccess-runtime-torrelay](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#unauthorizedaccess-runtime-torrelay) | Effects/Resource Consumption/UnauthorizedAccess:Runtime-TorRelay |
| [https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#unauthorizedaccess-runtime-torclient](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html#unauthorizedaccess-runtime-torclient) | Effects/Resource Consumption/UnauthorizedAccess:Runtime-TorClient |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#unauthorizedaccess-s3-maliciousipcallercustom](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#unauthorizedaccess-s3-maliciousipcallercustom) | TTPs/UnauthorizedAccess:S3-MaliciousIPCaller.Custom |
| [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#unauthorizedaccess-s3-toripcaller](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#unauthorizedaccess-s3-toripcaller) | TTPs/UnauthorizedAccess:S3-TorIPCaller |

### Typical finding from GuardDuty
<a name="securityhub-integration-finding-example"></a>

GuardDuty sends findings to Security Hub CSPM using the [AWS Security Finding Format (ASFF)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html).

Here is an example of a typical finding from GuardDuty.

```
  {
  "SchemaVersion": "2018-10-08",
  "Id": "arn:aws:guardduty:us-east-1:193043430472:detector/d4b040365221be2b54a6264dc9a4bc64/finding/46ba0ac2845071e23ccdeb2ae03bfdea",
  "ProductArn": "arn:aws:securityhub:us-east-1:product/aws/guardduty",
  "GeneratorId": "arn:aws:guardduty:us-east-1:193043430472:detector/d4b040365221be2b54a6264dc9a4bc64",
  "AwsAccountId": "193043430472",
  "Types": [
    "TTPs/Initial Access/UnauthorizedAccess:EC2-SSHBruteForce"
  ],
  "FirstObservedAt": "2020-08-22T09:15:57Z",
  "LastObservedAt": "2020-09-30T11:56:49Z",
  "CreatedAt": "2020-08-22T09:34:34.146Z",
  "UpdatedAt": "2020-09-30T12:14:00.206Z",
  "Severity": {
    "Product": 2,
    "Label": "MEDIUM",
    "Normalized": 40
  },
  "Title": "199.241.229.197 is performing SSH brute force attacks against i-0c10c2c7863d1a356.",
  "Description": "199.241.229.197 is performing SSH brute force attacks against i-0c10c2c7863d1a356. Brute force attacks are used to gain unauthorized access to your instance by guessing the SSH password.",
  "SourceUrl": "https://us-east-1.console.aws.amazon.com/guardduty/home?region=us-east-1#/findings?macros=current&fId=46ba0ac2845071e23ccdeb2ae03bfdea",
  "ProductFields": {
    "aws/guardduty/service/action/networkConnectionAction/remotePortDetails/portName": "Unknown",
    "aws/guardduty/service/archived": "false",
    "aws/guardduty/service/action/networkConnectionAction/remoteIpDetails/organization/asnOrg": "CENTURYLINK-US-LEGACY-QWEST",
    "aws/guardduty/service/action/networkConnectionAction/remoteIpDetails/geoLocation/lat": "42.5122",
    "aws/guardduty/service/action/networkConnectionAction/remoteIpDetails/ipAddressV4": "199.241.229.197",
    "aws/guardduty/service/action/networkConnectionAction/remoteIpDetails/geoLocation/lon": "-90.7384",
    "aws/guardduty/service/action/networkConnectionAction/blocked": "false",
    "aws/guardduty/service/action/networkConnectionAction/remotePortDetails/port": "46717",
    "aws/guardduty/service/action/networkConnectionAction/remoteIpDetails/country/countryName": "United States",
    "aws/guardduty/service/serviceName": "guardduty",
    "aws/guardduty/service/evidence": "",
    "aws/guardduty/service/action/networkConnectionAction/localIpDetails/ipAddressV4": "172.31.43.6",
    "aws/guardduty/service/detectorId": "d4b040365221be2b54a6264dc9a4bc64",
    "aws/guardduty/service/action/networkConnectionAction/remoteIpDetails/organization/org": "CenturyLink",
    "aws/guardduty/service/action/networkConnectionAction/connectionDirection": "INBOUND",
    "aws/guardduty/service/eventFirstSeen": "2020-08-22T09:15:57Z",
    "aws/guardduty/service/eventLastSeen": "2020-09-30T11:56:49Z",
    "aws/guardduty/service/action/networkConnectionAction/localPortDetails/portName": "SSH",
    "aws/guardduty/service/action/actionType": "NETWORK_CONNECTION",
    "aws/guardduty/service/action/networkConnectionAction/remoteIpDetails/city/cityName": "Dubuque",
    "aws/guardduty/service/additionalInfo": "",
    "aws/guardduty/service/resourceRole": "TARGET",
    "aws/guardduty/service/action/networkConnectionAction/localPortDetails/port": "22",
    "aws/guardduty/service/action/networkConnectionAction/protocol": "TCP",
    "aws/guardduty/service/count": "74",
    "aws/guardduty/service/action/networkConnectionAction/remoteIpDetails/organization/asn": "209",
    "aws/guardduty/service/action/networkConnectionAction/remoteIpDetails/organization/isp": "CenturyLink",
    "aws/securityhub/FindingId": "arn:aws:securityhub:us-east-1::product/aws/guardduty/arn:aws:guardduty:us-east-1:193043430472:detector/d4b040365221be2b54a6264dc9a4bc64/finding/46ba0ac2845071e23ccdeb2ae03bfdea",
    "aws/securityhub/ProductName": "GuardDuty",
    "aws/securityhub/CompanyName": "Amazon"
  },
  "Resources": [
    {
      "Type": "AwsEc2Instance",
      "Id": "arn:aws:ec2:us-east-1:193043430472:instance/i-0c10c2c7863d1a356",
      "Partition": "aws",
      "Region": "us-east-1",
      "Tags": {
        "Name": "kubectl"
      },
      "Details": {
        "AwsEc2Instance": {
          "Type": "t2.micro",
          "ImageId": "ami-02354e95b39ca8dec",
          "IpV4Addresses": [
            "18.234.130.16",
            "172.31.43.6"
          ],
          "VpcId": "vpc-a0c2d7c7",
          "SubnetId": "subnet-4975b475",
          "LaunchedAt": "2020-08-03T23:21:57Z"
        }
      }
    }
  ],
  "WorkflowState": "NEW",
  "Workflow": {
    "Status": "NEW"
  },
  "RecordState": "ACTIVE"
}
```

## Enabling and configuring the integration
<a name="securityhub-integration-enable"></a>

To use the integration with AWS Security Hub CSPM, you must enable Security Hub CSPM. For information on how to enable Security Hub CSPM, see [Setting up Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) in the *AWS Security Hub User Guide*.

When you enable both GuardDuty and Security Hub CSPM, the integration is enabled automatically. GuardDuty immediately begins to send findings to Security Hub CSPM.

## Using GuardDuty controls in Security Hub CSPM
<a name="securityhub-integration-using-guardduty-controls"></a>

AWS Security Hub CSPM uses security controls to evaluate your AWS resources, and check your compliance against security industry standards and best practices. You can use the controls related to GuardDuty resources and selected protection plans. For more information, see [Amazon GuardDuty controls](https://docs.aws.amazon.com/securityhub/latest/userguide/guardduty-controls.html) in the *AWS Security Hub User Guide*.

For a list of all the controls across AWS services and resources, see [Security Hub CSPM controls reference](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-controls-reference.html) in the *AWS Security Hub User Guide*.

## Stopping the publication of findings to Security Hub CSPM
<a name="securityhub-integration-disable"></a>

To stop sending findings to Security Hub CSPM, you can use either the Security Hub CSPM console or the API.

See [Disabling and enabling the flow of findings from an integration (console)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-integrations-managing.html#securityhub-integration-findings-flow-console) or [Disabling the flow of findings from an integration (Security Hub API, AWS CLI)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-integrations-managing.html#securityhub-integration-findings-flow-disable-api) in the *AWS Security Hub User Guide*.
