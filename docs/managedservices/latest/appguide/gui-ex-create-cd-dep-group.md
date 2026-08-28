---
source_url: https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-cd-dep-group.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Create a CodeDeploy Deployment Group
<a name="gui-ex-create-cd-dep-group"></a>

Create the CodeDeploy deployment group.

A CodeDeploy deployment group defines a set of individual instances targeted for a deployment.

REQUIRED DATA:
+ `VpcId`: The VPC that you are using, this should be the same as the previously used VPC.
+ `CodeDeployApplicationName`: Use the value you previously created.
+ `CodeDeployAutoScalingGroups`: Use the name of the Auto Scaling group that you created previously.
+ `CodeDeployDeploymentGroupName`: A name for the deployment group. This name must be unique for each application associated with the deployment group.
+ `CodeDeployServiceRoleArn`: Use the formula given in the example.

1. On the **Create RFC** page, select the Category **Deployment**, subcategory **Applications**, item **CodeDeploy deployment group**, and operation **Create** from the RFC CT pick list. Choose **Advanced** and set the values as shown (only a **Subject** is needed for the RFC). Click **Submit** when finished.
**Note**
Reference the CodeDeploy service role ARN in this format `"arn:aws:iam::085398962942:role/aws-codedeploy-role"` and use the previously-created Auto scaling group name for "ASG\_NAME".

   ```
   Description:                      Create CodeDeploy Deployment Group for WP
   CodeDeployApplicationName:        {{WordPress}}
   CodeDeployAutoScalingGroups:      {{ASG_NAME}}
   CodeDeployDeploymentConfigName:   CodeDeployDefault.HalfAtATime
   CodeDeployDeploymentGroupName:    {{WP CD Group}}
   CodeDeployServiceRoleArn:         arn:aws:iam::{{ACCOUNT_ID}}:role/aws-codedeploy-role

   VpcId:                            {{VPC_ID}}
   Name:                             WP Deployment Group
   ```

1. Click **Submit** when finished.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
