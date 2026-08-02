---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/wave-planning-management.html
---

# Wave Planning Management (WPM)
<a name="wave-planning-management"></a>

Wave Planning Management (WPM) is a feature that helps you organize and schedule your migration workloads in an optimal way. It allows you to break down large migration projects into manageable "waves" while considering various technical constraints and business requirements.

## Key Concepts
<a name="key-concepts"></a>
+  **Asset**: Any component that needs to be migrated, including applications and their infrastructure (servers, databases, storage, etc.).
+  **Move Group**: A set of related assets (such as applications and servers) that need to be migrated together due to their technical dependencies or business requirements.
+  **Wave**: A group of applications that will be migrated in the same event. This could be based on affinity between one another, or any other reason.
+  **Wave Planning Rules**: A set of pre-configured guidelines that help organize your migration in a systematic way. These rules automatically:
  + Prioritize which applications should be migrated first based on their characteristics and importance to your organization.
  + Group related assets together to ensure dependent components are migrated at the same time, maintaining system functionality throughout the migration process.
+  **Wave Planing Job**: A structured workflow for organizing migrations that processes applications through three key analyses: prioritization, dependency grouping, and wave planning. You provide a list of applications for migration, and the job produces organized move groups and waves according to the pre-defined wave planning rules and other job related settings, such as wave server and storage capacities.

## Creating a Wave Planning Job
<a name="creating-wave-planning-job"></a>

To create a new job, you select **Wave Planning** from menu, then **Planning Jobs**, and then click on the **Add** button. The Wave Planning Job Wizard will guide you through the following four steps:

### 1. Create job
<a name="create-job"></a>

The following attributes need to be populated in order to initiate a job:
+  **Job Name**: What you want to call this migration job. Choose a meaningful name that helps you identify it later.
+  **Max Wave Server Capacity**: The maximum number of servers that can be included in any single wave.
+  **Nomination Application Count**: How many unplanned applications you want to process in this job. For example, entering "10" will select the top 10 priority applications that haven’t been planned yet by default.
+  **Starting Wave Server Capacity**: The number of servers to include in your first wave of this job.
+  **Wave Server Capacity Increase**: How many additional servers to add to each subsequent wave in this job.
+  **Wave Storage Capacity**: The maximum total server storage allowed in each wave.

Once you complete the form, click **Next** button.

### 2. Manage applications
<a name="manage-applications"></a>

In this step, you will select which applications to include in your migration job.

Based on your **Nomination Application Count** (set in Step 1), the wizard automatically select the applications for your job. These suggestions come from the pool of unplanned applications and are sorted based on their prioritization ranking. The suggested applications appear in the **Applications included in new job** table.

If you haven’t, you can click on the **Additional Options** (three-dots) icon in the top right and choose **Recalculate app ranks** to calculate the ranks for all the applications based on the based on the [pre-defined prioritization rules](#prioritization-rules).

Optionally you can modify the suggested list in two ways:
+ Remove Applications: To remove an application from your job, select it and click **Remove from job** button. Removed applications will return to the **Unassigned applications** table.
+ Add Additional Applications: Select any additional applications in **Unassigned applications** table you want to include in, and click **Add to job** button. Added application will show in the **Applications included in new job** table.

After finalizing your application selection, click **Next** button.

### 3. Manage move groups
<a name="manage-move-groups"></a>

The job creates a move group request. While the backend processes the request based on the [pre-defined grouping rules](#grouping-rules), the wizard polls the progress and refreshes the page periodically.

Once the request has been processed successfully, the auto created move groups display in the **Move Groups** table. You can select one group to view group details such as included applications, servers and databases in the tabs below the table. Under **Entity Visualization** tab a diagram visualize the entity relationships.

Optionally you can modify an auto-created move group:
+ Select the move group and click **Manage Assets** button.
+ A dialog box with two tables pops up. The upper **Assets in Selected Move Group** table shows the assets included in the move group, and the lower **Available Assets** table shows the assets that are not assigned to any group.
+ To remove one or more assets from the move group, select them and click **Remove from Move Group** button. Removed assets will return to the **Available Assets** table.
+ To add one more available assets to the move group, select them from **Available Assets** table and click **Add to Move Group** button. Added assets will show in the **Assets in Selected Move Group** table.
+ Click on **Confirm** button to confirm the change, or **Cancel** to discard the change. The dialog box closes and the main screen refreshes to reflect the change you has made to the move group.

After you are happy with the move groups, click **Next** button.

### 4. Manage waves
<a name="manage-waves"></a>

The job creates waves based on the job settings and display the auto created waves in the **Waves** table. You can select one wave to view wave details such as included move groups, applications, servers and databases. Under **Entity Visualization** tab a diagram visualize the entity relationships.

Optionally you can modify an auto-created wave:
+ Select the wave and click **Manage Move Groups** button.
+ A dialog box with two tables pops up. The upper **Move Groups in selected Wave** table shows the move groups included in the move group, and the lower **Available Move Groups** table shows the move groups that are not assigned to any wave.
+ To remove one or more move groups from the wave, select them and click **Remove from Wave** button. Removed move groups will return to the **Available Move Groups** table.
+ To add one more available move groups to the wave, select them from **Available Move Groups** table and click **Add to Wave** button. Added move groups will show in the **Move Groups in selected Wave** table.
+ Click on **Confirm** button to confirm the change, or **Cancel** to discard the change. The dialog box closes and the main screen refreshes to reflect the change you has made to the wave.

After you are happy with the waves, click **Confirm Wave Plan** button to return to the Wave Planning Job list page.

### Notes
<a name="notes"></a>
+ The Job wizard persists the wave planning progress, and the changes you made to the move groups and waves upon the **Next** button and the **Confirm** button in the dialog box are clicked.
+ You can go back to previous steps of the wizard by clicking **Previous** button but they are in read-only mode and for your information only.
+ If you would like to make changes to the previous steps, you will need to cancel the job and start it over. Refer to [Cancelling / deleting a wave planning job](#cancelling-deleting-wave-planning-job).

## Cancelling / deleting a wave planning job
<a name="cancelling-deleting-wave-planning-job"></a>
+ To cancel a job in the create a job wizard, click **Cancel** button.
+ To delete a created job, you select **Wave Planning** from menu, then **Planning Jobs**, and then select the job and click the **Delete** button.

Both operation will revert the wave planning made by the job by deleting the related move groups and waves.

## Managing Wave Planning Rules
<a name="managing-wave-planning-rules"></a>

Wave Planning Rules are a set of configurable guidelines that control how assets are processed during wave planning. WPM pre-defines a list of most frequently used rules as default rules.

The rules consist of two major categories:
+   **Prioritization Rules**
  +  **Scoring Rules**: Define scoring criteria (0-100) for entity/attribute/value combinations to determine application priority. For example, "Production" environments might score 10 while "Development" environments score 100, indicating Dev environments should be migrated first.
  +  **Sorting Rules**: Control the order of applications in the selection process, including options to keep different environments of the same application together.
+   **Grouping Rules**
  +  **Joiner (inclusive) Rules**: Define criteria for combining assets into the same move group. Default rules include grouping applications that share servers, databases, app owners, etc.
  +  **Splitter (exclusive) Rules**: Define criteria for keeping assets in separate groups, typically based on attributes like environment, owner, or department.

The default grouping rules are crucial for the wave planning to work properly therefore administrators can only enable or disable these rules. Other than that, administrators can create new rules, and modify existing ones to align with specific migration requirements from their organization.

### Viewing wave planning rules
<a name="viewing-wave-planning-rules"></a>

To view the existing wave planning rules, you select **Administration** from menu, choose **Wave Planning**, and then click **Planning rules** tab.

System displays the grouping rules and prioritizing rules in **Grouping Rules** and **Prioritizing Rules** tables respectively.

### Enabling/disabling planning rules
<a name="enabling-disabling-planning-rules"></a>

You cannot modify the default grouping rules but only enable/disable them. To disable a default grouping rule:
+ Select one rule with "ENABLED" status by ticking the checkbox, and click **Edit** button.
+ Click **Disable Rule** button on the Edit Rule page.

You can enable a disabled grouping rule by doing the similar.

To disable a default prioritizing rule:
+ Select one rule with "ENABLED" status by ticking the checkbox, and click **Edit** button.
+ In the **Rule JSON** field, change the **status** value from "ENABLED" to "DISABLED", and click **Update Rule** to save the change.

You can enable a disabled prioritizing rule by doing the similar.

### Adding planning rules
<a name="adding-planning-rules"></a>

To add a new rule, you click **Add** button on top of the respective rule table, and then type in the rule in JSON format into **Rule JSON** field. It will be a lot easier if you copy and paste the value of an existing rule instead of starting from scratch.

If AWS Bedrock and required LLM model are available in your deployment region, the **Rule Description Prompt** section will appear which allows you to describe your rule in natural language and Bedrock will generate the rule in JSON format:
+ You type in the description of the rule into the text box below **Rule Description Prompt**. The following is an example for a scoring rule:

```
Score applications based on server storage size.
Less sizes means less app complexity scores.
```
+ You click **Generate Rule** button for Bedrock to generate the rule in JSON format and populate the **Rule JSON** field.
  + It may take 30 seconds or even longer for Bedrock to generate the rule.
+ You review the rule and click **Save Rule** button to save the rule.

### Rule JSON properties
<a name="rule-json-properties"></a>

 **Grouping rule JSON properties**

| Property Name | Required | Type | Allowed Values | Description |
| --- | --- | --- | --- | --- |
| rule\_type | Y | string | GROUPING\_INCLUSIVE, GROUPING\_EXCLUSIVE | Determines if the rule combines assets (inclusive) or separates them (exclusive) |
| rule\_name | Y | string | Any text | Name of the rule |
| rule\_description | N | string | Any text | Optional description of the rule |
| status | Y | string | ENABLED, DISABLED | Whether the rule is active |
| relationships | Y | array | Array of objects | List of asset relationships |
| relationships[].asset\_type | Y | string | Valid asset types | Type of asset for the relationship |
| relationships[].asset\_key | Y | string | Valid asset keys | Key attribute for the relationship |

 **Prioritizing scoring rule JSON properties**

| Property Name | Required | Type | Allowed Values | Description |
| --- | --- | --- | --- | --- |
| rule\_type | Y | string | PRIORITIZING | Must be "PRIORITIZING" |
| rule\_name | Y | string | Any text | Name of the rule |
| rule\_description | N | string | Any text | Optional description of the rule |
| sub\_type | Y | string | SCORING | Must be "SCORING" |
| status | Y | string | ENABLED, DISABLED | Whether the rule is active |
| asset\_type | Y | string | Valid asset types | Type of asset to score |
| attr\_key | Y | string | Valid non-relationship attributes | Attribute to base scoring on |
| scoring\_criteria | Y | array | Array of scoring objects | List of scoring conditions |
| scoring\_criteria[].value | N | string | Any text | Value to match |
| scoring\_criteria[].lower\_bound | N | number | Any number | Lower bound for numeric ranges |
| scoring\_criteria[].upper\_bound | N | number | Any number | Upper bound for numeric ranges |
| scoring\_criteria[].name | N | string | Any text | Name of the criterion |
| scoring\_criteria[].pattern | N | string | Any text | Pattern to match |
| scoring\_criteria[].complexity\_score | Y | number | 0-100 | Score to assign when criteria match |

 **Prioritizing sorting rule JSON properties**

| Property Name | Required | Type | Allowed Values | Description |
| --- | --- | --- | --- | --- |
| rule\_type | Y | string | PRIORITIZING | Must be "PRIORITIZING" |
| rule\_name | Y | string | Any text | Name of the rule |
| rule\_description | N | string | Any text | Optional description of the rule |
| sub\_type | Y | string | SORTING | Must be "SORTING" |
| status | Y | string | ENABLED, DISABLED | Whether the rule is active |
| asset\_type | Y | string | Valid asset types | Type of asset to sort |
| attr\_key | Y | string | Valid non-relationship attributes | Attribute to sort by |
| sort\_order | Y | string | ASC, DSC | Ascending or descending sort |
| sort\_level | Y | number | Any number | Priority level of the sort |
| sort\_by\_value | N | array | Array of strings | Specific values to sort by |

Roles allow one or more policies to be assigned to one or more groups. The combination of all policies assigned to a role provides access permissions. Roles can be created based on job roles or functions within the project or organization.

## Wave Assignment Changes
<a name="wave-assignment-changes"></a>

With the Wave Planning Manager (WPM) feature enabled, assigning servers to waves through the user interface has been updated to incorporate move groups, which are essential for organizing related assets that need to be migrated together.

Key Changes:
+ Direct server-to-wave assignments through the user interface are no longer supported.
+ Servers need to be assigned to move groups, which are then assigned to waves.

For servers that were imported through [legacy import](metadata-management.md#importing-data):
+ Existing wave assignments will be maintained.
+ To change the wave of a server imported by legacy import:

  1. Create a move group and assign it to a wave

  1. Edit a server and assign the server to the move group
