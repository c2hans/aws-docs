---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/worklist-app.html
---

# Access the Worklist app in the Connect Customer agent workspace
<a name="worklist-app"></a>

The Worklist app enables agents with the required permissions and routing profile settings to manually prioritize and assign queued work to themselves. The following steps explain how to provide your users access to the Worklist app in their workspaces.

**Note**
An agent can only access the Worklist App in the Agent Workspace if they have a Security Profile with the appropriate permissions described below.

1. Update the security profiles by selecting one of these permissions:
   + **Allow 'Assign to me' for any contact** permission - Enables agents to view contacts under any of these conditions:
     + Current Agent is the only Preferred Agent on the Contact.
     + Current Agent is one of the Preferred Agents on the Contact.
     + Any Agent or set of Agents are Preferred Agents on the Contact.
     + Contact with no Preferred Agents.
   + **Allow 'Assign to me' for my contact** permission - Enables agents to view contacts under these conditions:
     + Current Agent is the only Preferred Agent on the Contact.
     + Current Agent is one of the Preferred Agents on the Contact.
![Contact actions for the Worklist app.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-app-1.png)

   Once these permissions are assigned, they will be reflected on the **Security Profile Page**.
![Security profile permissions for the Worklist app.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-security-profile.png)
![Security profile permissions for the Worklist app.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-security-profile-2.png)

1. Update the routing profile settings to specify queue / channels for manual assignment in the new section.
![Routing profile settings for the Worklist app.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-routing-profile.png)

1. Once the security profile and routing profile settings are updated, the agent will see the Worklist app in their workspace:
![Worklist app in the agent workspace.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-workspace-view.png)

## Available filter options
<a name="worklist-filter-options"></a>

The available filter options depend on the agent's permissions:
+ An Agent with **Allow 'Assign to me' for any contact** can view these filter options:
![Filter options for agents with Assign to me for any contact permission.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-filter-any-contact.png)
+ An Agent with **Allow 'Assign to me' for my contact** can view these filter options:
![Filter options for agents with Assign to me for my contact permission.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-filter-my-contact.png)

## Time Range filter for contact history
<a name="worklist-time-range-filter"></a>

By default, the Worklist app displays contacts created in the last 2 weeks. To view contacts created beyond this timeframe, use the Time Range filter to select a specific date range. The Time Range filter allows you to select any date range within the past 90 days.

![The Worklist app showing the Time Range filter for selecting contact history date ranges.](http://docs.aws.amazon.com/connect/latest/adminguide/images/worklist-time-range-filter.png)
