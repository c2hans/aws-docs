---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Step 2: Register a target node with the maintenance window using the AWS CLI
<a name="mw-cli-tutorial-targets"></a>

In this step, you register a target with your new maintenance window. In this case, you specify which node to update when the maintenance window runs.

For an example of registering more than one node at a time using node IDs, examples of using tags to identify multiple nodes, and examples of specifying resource groups as targets, see [Examples: Register targets with a maintenance window](mw-cli-tutorial-targets-examples.md).

**Note**
You should already have created an Amazon Elastic Compute Cloud (Amazon EC2) instance to use in this step, as described in the [Maintenance Windows tutorial prerequisites](maintenance-windows-tutorials.md).

**To register a target node with a maintenance window using the AWS CLI**

1. Run the following command on your local machine. Replace each {{example resource placeholder}} with your own information.

------
#### [ Linux & macOS ]

   ```
   aws ssm register-target-with-maintenance-window \
       --window-id "{{mw-0c50858d01EXAMPLE}}" \
       --resource-type "INSTANCE" \
       --target "Key=InstanceIds,Values={{i-02573cafcfEXAMPLE}}"
   ```

------
#### [ Windows ]

   ```
   aws ssm register-target-with-maintenance-window ^
       --window-id "{{mw-0c50858d01EXAMPLE}}" ^
       --resource-type "INSTANCE" ^
       --target "Key=InstanceIds,Values={{i-02573cafcfEXAMPLE}}"
   ```

------

   The system returns information similar to the following.

   ```
   {
      "WindowTargetId":"e32eecb2-646c-4f4b-8ed1-205fbEXAMPLE"
   }
   ```

1. Now run the following command on your local machine to view details about your maintenance window target.

------
#### [ Linux & macOS ]

   ```
   aws ssm describe-maintenance-window-targets \
       --window-id "{{mw-0c50858d01EXAMPLE}}"
   ```

------
#### [ Windows ]

   ```
   aws ssm describe-maintenance-window-targets ^
       --window-id "{{mw-0c50858d01EXAMPLE}}"
   ```

------

   The system returns information similar to the following.

   ```
   {
       "Targets": [
           {
               "WindowId": "mw-0c50858d01EXAMPLE",
               "WindowTargetId": "e32eecb2-646c-4f4b-8ed1-205fbEXAMPLE",
               "ResourceType": "INSTANCE",
               "Targets": [
                   {
                       "Key": "InstanceIds",
                       "Values": [
                           "i-02573cafcfEXAMPLE"
                       ]
                   }
               ]
           }
       ]
   }
   ```

Continue to [Step 3: Register a task with the maintenance window using the AWS CLI](mw-cli-tutorial-tasks.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
