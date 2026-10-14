---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/aws-systems-manager-parameter-store.html
---

# AWS Systems Manager Parameter Store
<a name="aws-systems-manager-parameter-store"></a>

Automated Security Response on AWS uses AWS Systems Manager Parameter Store for storage of operational data. The following parameters are stored in Parameter Store:

| Name | Value | Use |
| --- | --- | --- |
|  `/Solutions/SO0111/CMK_REMEDIATION_ARN`  | AWS KMS key that will encrypt data for FSBP remediations | Encryption of customer data, such as CloudTrail logs, as part of remediations |
|  `/Solutions/SO0111/CMK_ARN`  | AWS KMS key that ASR will use to encrypt data | Encryption of solution data |
|  `/Solutions/SO0111/SNS_Topic_ARN`  | ARN of the Amazon SNS topic for the solution | Notification of remediation events |
|  `/Solutions/SO0111/SNS_Topic_Config.1`  | SNS topic for AWS Config updates | Config.1 remediation |
|  `/Solutions/SO0111/version`  | Solution version |  |
|  `/Solutions/SO0111`/{{<security standard long name>}}/{{<version>}}/status |  `enabled`  | Indicates whether the standard is active in the solution. A standard can be disabled for automated remediation by changing this to `disabled`  |
|  `/Solutions/SO0111`/{{<security standard long name>}}/shortname |  `String`  | Short name for the security standard. For example: `CIS`, `AFSBP`, `PCI`  |
|  `/Solutions/SO0111`/{{<security standard long name>}}/{{<version>}}/{{<control>}}/remap |  `String`  | When one control uses the same remediation as another, these parameters accomplish the remap |
