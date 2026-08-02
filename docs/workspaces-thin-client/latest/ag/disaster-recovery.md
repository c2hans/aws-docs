---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/disaster-recovery.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Business continuity
<a name="disaster-recovery"></a>

WorkSpaces Thin Client provides support for Business continuity as part of a [Business Continuity Plan (BCP)](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.html). WorkSpaces Thin Client business continuity is available for use with WorkSpaces Personal only. For more information on business continuity, see [Business continuity for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/business-continuity.html) in the *Amazon WorkSpaces Administration guide*.

## Prerequisites
<a name="dr-prerequisites"></a>

For business continuity to work on WorkSpaces Thin Client, the following prerequisites must be met:
+ For WorkSpaces Cross-Region Redirection – DNS service and routing polices have been configured. To set these up, see [Configure your DNS service and set up DNS routing policies](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html#cross-region-redirection-configure-DNS-routing).
+ For WorkSpaces Multi-Region Resilience – A standby WorkSpaces has been created. To create this, see [ Create a standby WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/multi-region-resilience.html#create-standby-workspace).
+ A connection alias in the region using WorkSpaces Thin Client. To verify your region, see [Covered regions](getting-started.md#regions).

## Configuring business continuity for WorkSpaces Thin Client
<a name="configuring-dr"></a>

To enable WorkSpaces Personal DR on Amazon WorkSpaces Thin Client, you will need to configure connection aliases to map to the environment using the SDK.

Sample doc explanation for setting up disaster recovery:

**Example**
An example command using the AWS CLI to create a new environment using a WorkSpaces connection alias for the streaming desktop:

```
aws workspaces-thin-client create-environment --region {{region}} --desktop-arn/
arn:aws:workspaces:{{region}}:{{account}}:connectionalias/{{wsca-id}}
```
Replace {{wsca-id}} with your WorkSpaces Personal connection alias. The ID of the WorkSpaces connection alias can be found in the WorkSpaces Management Console or from the SDK.

## End user experience
<a name="end-user-exp-dr"></a>

Once business continuity is configured, devices must be registered and active within the last 15 days. After that, should WorkSpaces Thin Client management services become unavailable, users then can stay connected to their sessions for up to 24 hours . In this condition, the device will not receive software updates, exchange posture information, and cannot be activated. The corresponding device entry in WorkSpaces Thin Client console will not show the latest information.

If the WorkSpaces Thin Client device management services remain unavailable beyond 24 hours, the following error message will display:

**"An error has occurred. Please try again. If the issue persists, contact your IT administrator. (Error Code: 3006)."**
