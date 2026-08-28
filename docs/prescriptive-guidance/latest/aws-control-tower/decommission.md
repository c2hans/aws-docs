---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-control-tower/decommission.html
---

# Decommissioning AWS Landing Zone
<a name="decommission"></a>

Before you decommission AWS Landing Zone resources, confirm that you have transitioned all required resources from AWS Landing Zone to the AWS Control Tower environment.

The decommissioning process is manual, and it requires Admin access to the management account where you deployed the AWS Landing Zone solution.

Before deleting any resources, understand the implications and any dependencies on those resources.

The following resources can be deleted from AWS Landing Zone after you have successfully transitioned to AWS Control Tower. You might also have custom resources that you want to remove from the environment.
+ The stack sets that begin with AWS-Landing-Zone-
  + You might need to retain certain stack sets, such as PrimaryVPC, if you are running resources in them.
+ The Amazon GuardDuty baseline template
  + The GuardDuty baseline template will not be automatically deleted. You need to delete the account association from the GuardDuty detector in each Region for all the accounts that the detector is monitoring. The most efficient way to do this is by using AWS Command Line Interface (AWS CLI) commands. Use the following commands to delete GuardDuty resources for every Region in which GuardDuty is enabled.

```
aws guardduty list-detectors --region
aws guardduty disassociate-members --detector-id <detector_id> --account-ids <SecurityAccountID> --region
aws guardduty delete-members --detector-id <detector_id> --account-ids <SecurityAccountID> --region
```

On the CloudFormation console, delete the GuardDuty stack set from the management account.
+ AWS Landing Zone initiation template
  + Before you delete the template, delete all the objects in S3 bucket that contains the AWS Landing Zone configuration file.
+ AWS Service Catalog
  + AWS-Landing-Zone-Account-Vending-Machine provisioned products
    + This step depends on whether you are ready to delete all the related stack sets, such as PrimaryVPC. Take extra caution when deleting the AVM-provisioned products, because all the AWS CloudFormation stack sets associated with the AVM, based on the AWS Landing Zone manifest file, will be deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
