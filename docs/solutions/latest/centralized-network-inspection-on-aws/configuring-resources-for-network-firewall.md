---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/configuring-resources-for-network-firewall.html
---

# Configuring resources for Network Firewall
<a name="configuring-resources-for-network-firewall"></a>

After deploying the guidance, you can customize the resources for your network. This guidance creates a S3 bucket to store all the Network Firewall conﬁguration ﬁles. You can find out the bucket name by going to the CloudFormation stack outputs and searching for the parameter `CodeBuildsourcecodebucket`. The files are saved with prefix `{{BUCKET_NAME}}/centralized-network-inspection-on-aws/configuration`. After downloading the configuration files, you can update and create new resources in the respective folders and upload the archive file to the location mentioned above. After the files have been updated, start the CodePipeline to apply the changes by selecting the option **Release Changes**. You can review the changes to the firewall, firewall policy, and rule groups after the CodePipeline has finished running successfully. We recommend [monitoring the pipeline status](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view-console.html) to confirm that the changes were deployed successfully. You can also review [CodeBuild stage](https://docs.aws.amazon.com/codebuild/latest/userguide/view-project-details.html) logs in CodePipeline.

**Note**
 All references to the `FirewallPolicyArn` and `ResourceARN` attributes should contain the reference path to the actual JSON files. These values are used by this guidance to retrieve the configurations. Refer to the example configurations that are provided in the S3 bucket.

 A unique string is added to the network firewall and firewall policy to allow you to deploy the guidance more than once in a Region. The deployed resources have a unique name for each Region.

 If there are existing resources in the network firewall that have the same name as those being referenced in the guidance, they will be updated with the configuration provided in the S3 bucket. Before committing changes, we recommend reviewing the resource names for any resources previously created in the AWS Network Firewall console in the account and Region.

## CodeBuild validation stage
<a name="codebuild-validation-stage"></a>

 This guidance creates two CodeBuild stages. The first stage validates the configuration files (firewall, firewall policy, and rule group) and checks if the JSON format is valid. This guidance uses these files to validate the Network Firewall APIs to ensure that the attributes defined in the files have valid data. If any files have formatting issues or invalid data, the CodeBuild stage will be in a Failed state, and the deployment of the files to Network Firewall will not continue. The CodeBuild validation stage will provide error details for the files, similar to the ones in the following log example.

```
[TIMESTAMP] : "-----------INVALID FILES START-----------"
[TIMESTAMP]: {
   "path": "./firewallPolicies/firewall-policy-1.json",
   "error": "Unexpected key 'key' found in params.FirewallPolicy”
}
[TIMESTAMP]: "-----------INVALID FILES END-----------"
[TIMESTAMP]: "Validation failed."
[TIMESTAMP]: "Error in firewall config validation" : "Validation failed."
```

 After the guidance is deployed, the configuration archive named `centralized-network-inspection-on-aws.zip` in the S3 bucket will have the following default directory structure:
+  **Examples** – This directory contains example configuration files.
+  **Firewalls** – This directory contains the firewall configuration in JSON format. It includes the attributes as a document in the [CreateFirewallAPI](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateFirewall.html) action.
**Note**
 `FirewallPolicyArn` has a value which exactly matches the file path of the firewall policy file in the configuration archive file.

   As shown in the following example JSON file, this guidance uses `firewall-policy-1.json` for the firewall policy in the `./firewallPolicies/firewall-policy-1.json` commit repository path.

  ```
  {
     "FirewallName": "Firewall-1",
     "FirewallPolicyARN”: "./firewallPolicies/firewall-policy-1.json",
     "Description": "Network Firewall 1".
     "DeleteProtection": true,
     "SubnetChangeProtection": true
  }
  ```
+  **FirewallPolicies** – This directory contains the firewall policy configuration in JSON format, which will have attributes as documented in [CreateFirewallPolicy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateFirewallPolicy.html). The attribute `ResourceArn` will have a value which exactly matches the file path of the rule group file in the configuration archive file in the S3 bucket. The following is an example of the network firewall policy.

  ```
  {
  "FirewallPolicyName": "Firewall-Policy-1",
  "Description": "Firewall Policy 1",
  "FirewallPolicy": {
    "StatelessDefaultActions": [
      "aws:drop"
    ],
    "StatelessRuleGroupReferences": [
      {
        "Priority": 30,
        "ResourceArn":"./ruleGroups/stateless-fwd-to-stateful.example.json"
      },
      {
        "Priority": 20,
        "ResourceArn":"./ruleGroups/stateless-pass-action.example.json"

  }
    ],
    "StatefulRuleGroupReferences":[
       {
        "ResourceArn":"./ruleGroups/stateful-domainblock.example.json"
      },
      {
        "ResourceArn":"./ruleGroups/suricata-rule-reference.json"
      }
    ]
   }
  }
  ```
**Note**
 The `ResourceArn` attribute in the firewall policy file should have the file path to the rule group file in the configuration archive file.
+  **RuleGroup –** This directory contains the rule groups configuration in JSON format which will have attributes as documented in [CreateRuleGroup](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateRuleGroup.html). The rule group can be defined by providing details in the `RuleGroup` attribute or the rules (Suricata flat format) attribute, as shown in the following stateful rule group file example.

  ```
  {
     "RuleGroupName": "StatefulRulesExample1",
     "RuleGroup": {
      "RulesSource": {
        "RulesSourceList": {
          "TargetTypes": ["HTTP_HOST"],
          "Targets": [
            "test.example.com",
            "test2.example.com"
          ],
          "GeneratedRulesType": "DENYLIST"
         }
        }
      },
      "Type": "STATEFUL",
      "Description": "Stateful Rule",
      "Capacity": 100
  }
  ```

   In this following example Suricata file, the rules attribute references the drop.rules file where the rules are defined. For more information, refer to the [Drop.rules example file](https://rules.emergingthreats.net/open/suricata-5.0/rules/drop.rules).

  ```
  {
     "RuleGroupName": "suricata-drop-rules",
     "Rules": "./ruleGroups/drop.rules",
     "Type": "STATEFUL".
     "Description": "Suricata rule group",
     "Type": 100
  }
  ```
**Note**
 The `drop.rules` file must be added to the configuration package, and only a local path is allowed. Amazon S3 and HTTP links are not allowed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Network Inspection on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
