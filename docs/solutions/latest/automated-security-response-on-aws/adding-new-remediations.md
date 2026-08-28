---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/adding-new-remediations.html
---

# Adding new remediations
<a name="adding-new-remediations"></a>

Remediations can be added manually by updating the appropriate playbook files, or programmatically by extending the solution through CDK constructs, depending on your preferred workflow.

**Note**
The instructions that follow leverage resources installed by the solution as a starting point. By convention, most solution resource names contain **ASR** and/or **SO0111** to make it easy to locate and identify them.

## AI Toolkit for Custom Remediations
<a name="ai-toolkit-for-custom-remediations"></a>

To accelerate the workflows described in this section, the solution provides the AI Toolkit for Custom Remediations. The toolkit packages ASR’s remediation best practices, guardrails, and development patterns as an instruction prompt that you provide to an AI assistant in your integrated development environment (IDE). With this context, the assistant can help you author ASR-compatible remediation runbooks, control runbooks, IAM roles, and CDK constructs that follow the naming conventions and integration steps documented in the following sections — producing production-ready custom remediations with fewer iterations and greater confidence.

The toolkit is optional and does not change how remediations are built or deployed; it is a development aid that makes the solution’s conventions and constraints visible to your AI assistant. You remain responsible for reviewing and testing any generated code before deploying it.

## Overview of the manual workflow
<a name="remediation-overview"></a>

Automated Security Response on AWS runbooks must follow the following standard naming:

ASR-{{<standard>}}-{{<version>}}-{{<control>}}

 **Standard**: The abbreviation for the security standard. This must match standards supported by ASR. It must be one of "CIS", "AFSBP", "PCI", "NIST", or "SC".

 **Version**: The version of the standard. Again, this must match the version supported by ASR and the version in the finding data.

 **Control**: The control ID of the control to be remediated. This must match the finding data.

1. Create a runbook in the member account(s).

1. Create an IAM role in the member account(s).

1. (Optional) Create an automatic remediation rule in the admin account.

### Step 1. Create a runbook in the member account(s)
<a name="step-1-create-a-runbook-in-the-member-accounts"></a>

1. Sign in to the [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/home) and obtain an example of the finding JSON.

1. Create an automation runbook that remediates the finding. In the **Owned by me** tab, use any of the `ASR-` documents under the **Documents** tab as a starting point.

1. The AWS Step Functions in the admin account will run your runbook. Your runbook must specify the remediation role in order to be passed when calling the runbook.

### Step 2. Create an IAM role in the member account(s)
<a name="step-2-create-iam-role-in-the-member-accounts"></a>

1. Sign in to the [AWS Identity and Access Management console](https://console.aws.amazon.com/iam/home).

1. Obtain an example from the IAM **SO0111** roles and create a new role. The role name must start with SO0111-Remediate-{{<standard>}}-{{<version>}}-{{<control>}}. For example, if adding CIS v1.2.0 control 5.6 the role must be `SO0111-Remediate-CIS-1.2.0-5.6`.

1. Using the example, create a properly scoped role that allows only the necessary API calls to perform remediation.

At this point, your remediation is active and available for automated remediation from the ASR Custom Action in AWS Security Hub.

### Step 3: (Optional) Create an automatic remediation rule in the admin account
<a name="step-3-create-an-automatio-remediation-rule-in-the-admin-account"></a>

Automatic (not "automated") remediation is the immediate execution of the remediation as soon as the finding is received by AWS Security Hub. Carefully consider the risks before using this option.

1. View an example rule for the same security standard in Amazon EventBridge. The naming standard for rules is `standard_control_*AutoTrigger*`.

1. Copy the event pattern from the example to be used.

1. Change the `GeneratorId` value to match the `GeneratorId` in your Finding JSON.

1. Save and activate the rule.

## Overview of CDK workflow
<a name="cdk-remediation-overview"></a>

In summary, the following files in the ASR repo will be modified or added. In this example, a new remediation for ElastiCache.2 was added to the SC and AFSBP playbooks.

**Note**
All new remediations should be added to the SC playbook, since it consolidates all remediations available in ASR. If you intend to deploy only a specific set of playbooks (such as AFSBP), then you can either: (1) add the remediation to **only** your intended playbook(s), or (2) add the remediation to all playbooks for which it exists in the corresponding Security Hub Standard, in addition to the SC playbook. The second option is recommended for flexibility.

In this example, ElastiCache.2 is included in the following Security Hub Standards:
+ AFSBP
+ NIST.800-53.r5 SI-2
+ NIST.800-53.r5 SI-2(2)
+ NIST.800-53.r5 SI-2(4)
+ NIST.800-53.r5 SI-2(5)
+ PCI DSS v4.0.1/6.3.3

Since, by default, ASR only implements playbooks for AFSBP and NIST.800-53, we will add this new remediation to those playbooks in addition to SC.

 **Modify**
+ source/lib/remediation-runbook-stack.ts
+ source/playbooks/AFSBP/lib/[standard name]\_remediations.ts
+ source/playbooks/NIST80053/lib/control\_runbooks-construct.ts
+ source/playbooks/NIST80053/lib/[standard name]\_remediations.ts
+ source/playbooks/SC/lib/control\_runbooks-construct.ts
+ source/playbooks/SC/lib/sc\_remediations.ts
+ source/test/regex\_registry.ts

 **Add**
+ source/playbooks/SC/ssmdocs/SC\_ElastiCache.2.ts
+ source/playbooks/SC/ssmdocs/descriptions/ElastiCache.2.md
+ source/remediation\_runbooks/EnableElastiCacheVersionUpgrades.yaml

**Note**
The name chosen for the runbook can be any string, as long as it is consistent with the rest of the changes made.
+ source/playbooks/NIST80053/ssmdocs/NIST80053\_ElastiCache.2.ts
+ source/playbooks/AFSBP/ssmdocs/AFSBP\_ElastiCache.2.yaml

 **Development steps**

1. Create the Remediation Runbook.

1. Create the Control Runbooks.

1. Integrate Each Control Runbook with a Playbook.

1. Create the Remediation IAM Role & Integrate Remediation Runbook

1. Update Unit Tests

### Step 1: Create the Remediation Runbook
<a name="step-1-create-the-remediation-runbook"></a>

This is the SSM document used to remediate resources. It must include the `AutomationAssumeRole` parameter, which is the IAM role with permissions to execute the remediation. View the existing file `source/remediation_runbooks/EnableElastiCacheVersionUpgrades.yaml` as a reference when creating new remediation runbooks.

All new runbooks should be added to the `source/remediation_runbooks/` directory.

### Step 2: Create the Control Runbooks
<a name="step-2-create-the-control-runbook"></a>

A control runbook is a playbook-specific runbook that parses the finding data from the given standard and executes the appropriate Remediation Runbook. Since we are adding the ElastiCache.2 remediation to the SC, AFSBP, and NIST80053 playbooks, we must create a new control runbook for each. The following files are created:
+ source/playbooks/SC/ssmdocs/SC\_ElastiCache.2.ts
+ source/playbooks/NIST80053/ssmdocs/NIST80053\_ElastiCache.2.ts
+ source/playbooks/AFSBP/ssmdocs/AFSBP\_ElastiCache.2.yaml

**Example**
The naming of these files is important and must follow the format <PLAYBOOK\_NAME>\_<CONTROL.ID>.ts/yaml

Some playbooks in ASR support IaC control runbooks in TypeScript, while others must be written in raw YAML. Reference the existing remediations in the respective playbook as examples. In this example, we will cover the SC playbook, which uses IaC.

In the SC playbook, your new control runbook should export a class that extends ControlRunbookDocument and matches the name of your remediation runbook. Take a look at the example below:

```
export class EnableElastiCacheVersionUpgrades extends ControlRunbookDocument {
  constructor(scope: Construct, id: string, props: ControlRunbookProps) {
    super(scope, id, {
      ...props,
      securityControlId: 'ElastiCache.2',
      remediationName: 'EnableElastiCacheVersionUpgrades',
      scope: RemediationScope.REGIONAL,
      resourceIdRegex: <Regex>,
      resourceIdName: 'ClusterId',
      updateDescription: new StringFormat('Automatic minor version upgrades enabled for cluster %s.', [
        StringVariable.of(`ParseInput.ClusterId`),
      ]),
    });
  }
}
```
+  `securityControlId` is the control ID for the remediation that you are adding, as it is defined in the [consolidated controls view in Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/asff-changes-consolidation.html#securityhub-findings-format-changes-ids-titles).
+  `remediationName` is the name you have chosen for your remediation runbook.
+  `scope` is the scope of the resource you are remediating, indicating whether it exists globally or in a specific region.
+  `resourceIdRegex` is the regex used to capture the resource ID that you would like to pass to the remediation runbook as a parameter. Only one group should be captured, all other groups should be non-capturing. If you would like to pass the entire ARN, omit this field.
+  `resourceIdName` is the name you would like to set for the resource ID captured using `resourceIdRegex`, this should match the resource ID parameter name in your remediation runbook.
+  `updateDescription` is the string you would like to assign to the "notes" section of the finding in Security Hub once the remediation succeeds.

You must also export a function called `createControlRunbook` which returns a new instance of your class. For ElastiCache.2, this looks like:

```
export function createControlRunbook(scope: Construct, id: string, props: PlaybookProps): ControlRunbookDocument {
  return new EnableElastiCacheVersionUpgrades(scope, id, { ...props, controlId: 'ElastiCache.2' });
}
```

where `controlId` is the control ID as defined in the Security Standard associated with the playbook under which you are operating.

If the Security Hub control has parameters that you would like to pass to your remediation runbook, you can pass them by adding overrides to the following methods: - `getExtraSteps`: defines default values for each parameter implemented for the control in Security Hub

**Note**
Each parameter from Security Hub must be given a default value
+  `getInputParamsStepOutput`: defines the outputs for the GetInputParams step of the control runbook
+ Each output has a `name`, `outputType`, and `selector`. The `selector` should be the same selector used in the `getExtraSteps` method override.
+  `getRemediationParams`: defines the parameters passed to the remediation runbook, fetched from the GetInputParams step outputs.

To view an example, navigate to the `source/playbooks/SC/ssmdocs/SC_DynamoDB.1.ts` file.

### Step 3: Integrate Each Control Runbook with a Playbook
<a name="step-3-integrate-each-control-runbook-with-a-playbook"></a>

For each control runbook created in the previous step, you must now integrate it with the infrastructure definitions in the associated playbook. Follow the steps below for each control runbook.

**Important**
If you created the control runbook using raw YAML instead of typescript IaC, skip to the next section.

In `/<playbook_name>/control_runbooks-construct.ts` Import your newly created control runbook file like:

```
import * as elasticache_2 from '../ssmdocs/SC_ElastiCache.2';
```

Next, go to the array for

```
const controlRunbooksRecord: Record<string, any>
```

And add a new entry mapping the control ID (playbook-specific) to the `createControlRunbook` method you’ve created:

```
'ElastiCache.2': elasticache_2.createControlRunbook,
```

Add the playbook-specific control ID to the list of remediations in ` <playbook_name>\_remediations.ts` like below:

```
{ control: 'ElastiCache.2', versionAdded: '2.3.0' },
```

The `versionAdded` field should be the latest version of the solution. If adding the remediation breaches the template size limit, increase the `versionAdded`. You can adjust the number of remediations included in each playbook member stack in `solution_env.sh`.

### Step 4: Create the Remediation IAM Role & Integrate Remediation Runbook
<a name="step-4-create-the-remediation-iam-role-integrate-remediation-runbook"></a>

Each remediation has its own IAM role with custom permissions required to execute the remediation runbook. In addition, the `RunbookFactory.createRemediationRunbook` method needs to be invoked to add the remediation runbook you created in Step 1 to the solution’s CloudFormation templates.

In the `remediation-runbook-stack.ts`, each remediation has its own code block in the `RemediationRunbookStack` class. The following code block shows the creation of a new IAM role and remediation runbook integration for the ElastiCache.2 remediation:

```
    //-----------------------
    // EnableElastiCacheVersionUpgrades
    //
    {
      const remediationName = 'EnableElastiCacheVersionUpgrades'; // should match the name of your remediation runbook
      const inlinePolicy = new Policy(props.roleStack, `ASR-Remediation-Policy-${remediationName}`);

      const remediationPolicy = new PolicyStatement();
      remediationPolicy.addActions('elasticache:ModifyCacheCluster');
      remediationPolicy.effect = Effect.ALLOW;
      remediationPolicy.addResources(`arn:${this.partition}:elasticache:*:${this.account}:cluster:*`);
      inlinePolicy.addStatements(remediationPolicy);

      new SsmRole(props.roleStack, 'RemediationRole ' + remediationName, { // creates the remediation IAM role
        solutionId: props.solutionId,
        ssmDocName: remediationName,
        remediationPolicy: inlinePolicy,
        remediationRoleName: `${remediationRoleNameBase}${remediationName}`,
      });

      RunbookFactory.createRemediationRunbook(this, 'ASR ' + remediationName, { // adds the remediation runbook to the solution's cloudformation templates
        ssmDocName: remediationName,
        ssmDocPath: ssmdocs,
        ssmDocFileName: `${remediationName}.yaml`,
        scriptPath: `${ssmdocs}/scripts`,
        solutionVersion: props.solutionVersion,
        solutionDistBucket: props.solutionDistBucket,
        solutionId: props.solutionId,
        namespace: namespace,
      });
    }
```

### Step 5: Update Unit Tests
<a name="step-5-update-unit-tests"></a>

We recommend updating and running the unit tests after adding a new remediation.

First, you must add any new regular expressions (that are not already added) into the `source/test/regex_registry.ts` file. This file enforces testing for each new regular expression included in the solution’s runbooks. Take a look at the `addElastiCacheClusterTestCases` function as an example, which is used to test regular expressions used in ElastiCache remediations.

Finally, you’ll need to update the snapshots for each stack. Snapshots are version-controlled CloudFormation template definitions that are used to track changes made to ASR’s infrastructure. Update the snapshot files by running the following command from the `deployment` directory:

```
./run-unit-tests.sh update
```

Now you are ready to deploy your new remediation\! Navigate to the **Build and Deploy** section below for instructions on building and deploying the solution with your new changes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
