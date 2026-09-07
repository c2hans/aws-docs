---
source_url: https://docs.aws.amazon.com/res/archive/release-minus-4/ug/project-launch-template.html
---

# Add a launch template
<a name="project-launch-template"></a>

When creating or editing a project, you can add launch templates using the **Advanced Options** within the project configuration. Launch templates provide additional configurations, such as security groups, IAM policies, and launch scripts to all VDI instances within the project.

## Add policies
<a name="add-policies"></a>

You can add an IAM policy to control VDI access for all instances deployed under your project. To onboard a policy, tag the policy with the following key-value pair:

```
res:Resource/vdi-host-policy
```

For more information on IAM roles, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

### Add security groups
<a name="add-security-groups"></a>

You can add a security group to control the egress and ingress data for all VDI instances under your project. To onboard a security group, tag the security group with the following key-value pair:

```
res:Resource/vdi-security-group
```

For more information on security groups, see [Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) in the *Amazon VPC User Guide*.

### Add launch scripts
<a name="project-launch-scripts"></a>

You can add launch scripts that will initiate on all VDI sessions within your project. RES supports script initiation for Linux and Windows. For script initiation, you can choose either:

**Run Script When VDI Starts**
This option initiates the script at the beginning of a VDI instance before any RES configurations or installations run.

**Run Script when VDI is Configured**
This option initiates the script after RES configurations complete.

Scripts support the following options:

| Script configuration | Example |
| --- | --- |
| S3 URI | s3://bucketname/script.sh |
| HTTPS URL | https://sample.samplecontent.com/sample |
| Local file | file:///user/scripts/example.sh |

For **Arguments**, provide any arguments separated by a comma.

![Example of a project configuration](https://docs.aws.amazon.com/res/archive/release-minus-4/ug/images/res-projectconfigexample.png)
