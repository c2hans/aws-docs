---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/pipeline-template-creation-visual-tools.html
---

# Pipeline Template Creation Using Visual Tools
<a name="pipeline-template-creation-visual-tools"></a>

This section describes how to create Cloud Migration Factory pipeline templates using visual diagramming tools. The solution supports template creation using either DrawIO or Lucid Chart.

## Check Prerequisites
<a name="check-prerequisites"></a>
+ Access to either DrawIO or Lucid Chart diagramming tool
+ Access to your Cloud Migration Factory environment
+ List of valid automation script IDs from your CMF instance

## Template Components
<a name="template-components"></a>

A pipeline template consists of the following core components:

| Element Type | Shape | Use When…​ |
| --- | --- | --- |
| Start Node | Circle | Indicating the start of a flow and when indicating the start of a branch |
| Automated Task | Rectangle | Indicating that the automation exists already as part of the automation library of CMF |
| Manual Task | Rectangle | Indicating that the task at hand is manual |
| Connection | Line/Arrow | Shows task sequence |

## Data Attributes
<a name="data-attributes"></a>

Each shape requires specific attributes for CMF conversion:

| Element Type | Required Attribute | Example |
| --- | --- | --- |
| Start Circle | Start | "Start": "Wave 1 Migration" |
| Automated Task | TaskType, AutomationID | "TaskType": "Automated", "AutomationID": "<VALID\_CMF\_SCRIPT\_NAME>" |
| Manual Task | TaskType | "TaskType": "Manual" |

## Important Concepts
<a name="important-concepts"></a>

Before creating your diagram, understand these key elements that enable successful conversion to CMF templates:

1. Template Naming

   1. Your diagram’s tab/sheet name becomes your CMF template name.

   1. Names must be unique across CMF.

   1. Each tab creates a separate CMF template, allowing you to design multiple templates in a single file.

1. Task Naming

   1. The task name will be identical to the text/label you give to each shape in your diagram.

   1. Ensure each task has a unique and descriptive label for clear identification.

1. Attribute Requirements

   1. TaskType must be exactly "manual" or "automated"

   1. AutomationID must match existing CMF scripts name

   1. Start circle’s "Start" property defines template description

## Creating templates in DrawIO
<a name="creating-templates-in-drawio"></a>

1. Create Start Node:

   1. Drag a Circle shape onto the canvas

   1. Double-click and label it "Start"

      1. Add Start attribute:

         1. Right-click circle → Edit Data

             **DrawIO Shape Right-click panel**
![create drawio right click panel](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/create-drawio-right-click-panel.png)

         1. Add Data Attribute key "Start" and value (e.g., "Wave 1 Migration")

             **DrawIO Shape Data**
![create drawio shape data](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/create-drawio-shape-data.png)

1. Manual Task:

   1. Drag a Rectangle shape onto the canvas

   1. Double-click and add a descriptive label

   1. Add attributes:

      1. Right-click rectangle → Edit Data

      1. Add Data Attribute key "TaskType" with value "Manual"

          **DrawIO Manual Task Configuration**
![create drawio manual task data](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/create-drawio-manual-task-data.png)

1. Automated task:

   1. Drag a Rectangle shape onto the canvas

   1. Double-click and add a descriptive label, this will be Task Name in CMF

   1. Add attributes:

      1. Right-click rectangle → Edit Data

      1. Add Data Attribute key "TaskType" with value "Automated"

      1. Add Data Attribute key "AutomationID" with a valid CMF script name.

         1. To find valid AutomationID:

            1. Log into CMF portal

            1. Navigate to "Scripts" under Automation in the left navigation bar

            1. Browse or search for your desired script

                **CMF Scripts List**
![scripts list](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/scripts-list.png)

            1. Use the script name as your AutomationID in your diagram

                **DrawIO Automated Task Configuration**
![create drawio automated task data](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/create-drawio-automated-task-data.png)

1. Set template name

   1. Rename the diagram tab to your desired template name

1. Saving & Exporting

   1. File → Save As → Format: .drawio

1. Uploading to CMF

   1. Log into CMF portal

   1. Navigate to "Pipeline Templates" in the left navigation bar

   1. Click on "Actions" and select "Import"

       **Pipeline Templates Action→Import**
![pipeline template action import](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/pipeline-template-action-import.png)

   1. Choose your saved .drawio file

   1. Click "Submit" to complete the import

       **Template Import Submit**
![pipeline template import submit](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/pipeline-template-import-submit.png)

### After drawIO import is complete
<a name="after-drawio-import-is-complete"></a>

1. A new template will be created under Pipeline Templates

1. To see how your diagram attributes are converted in CMF:
   + Locate your newly created template in the Pipeline Templates list
   + Click on the template to open it
   + You’ll see a visual representation of your workflow under Visual task Editor

      **Pipeline Template Visual Task Editor**
![pipeline template visual](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/pipeline-template-visual.png)
   + Each shape from your diagram is now a task in CMF
   + Click on a task to view its details:
     + Task names correspond to the labels you gave shapes
     + For automated tasks, you’ll see the assigned AutomationID under Scripts dropdown.

        **Pipeline Template Task Edit**
![pipeline template task edit](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/pipeline-template-task-edit.png)

## Creating Templates in Lucid Chart
<a name="creating-templates-in-lucid-chart"></a>

Follow these steps to create pipeline templates using Lucid Chart:

1. Create Start Node

   1. Drag a Circle shape onto the canvas

   1. Double-click and label it "Start"

   1. Add Start attribute:

      1. Click the data icon (marked by red arrow in UI)

      1. Select the "Data" tab

      1. Add Data Attribute key "Start" and value (e.g., "Rehost Servers")

          **Lucid Chart Start Node Configuration**
![create lucid data tab](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/create-lucid-data-tab.png)

1. Add Manual Tasks

   1. Drag a Rectangle shape onto the canvas

   1. Double-click and add a descriptive label

   1. Add attributes:

      1. Click the data icon

      1. Select the "Data" tab

      1. Add Data Attribute key "TaskType" with value "Manual"

          **Lucid Chart Manual Task Configuration**
![create lucid manual task data](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/create-lucid-manual-task-data.png)

1. Add Automated Tasks

   1. Drag a Rectangle shape onto the canvas

   1. Double-click and add a descriptive label

   1. Add attributes:

      1. Click the data icon

      1. Select the "Data" tab

      1. Add Data Attribute key "TaskType" with value "Automated"

      1. Add Data Attribute key "AutomationID" with a valid CMF script name

         1. To find valid AutomationID:

            1. Log into CMF portal

            1. Navigate to "Scripts" under Automation in the left navigation bar

            1. Browse or search for your desired script

                **CMF Scripts List**
![create drawio scripts list](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/create-drawio-scripts-list.png)

            1. Use the script name as your AutomationID in your diagram

                **Lucid Chart Automated Task Configuration**
![create lucid automated task data](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/create-lucid-automated-task-data.png)

1. Set template name

   1. Rename the diagram tab to your desired template name

1. Saving & Exporting

   1. File → Export → CSV of Shape Data

1. Uploading to CMF

   1. Log into CMF portal

   1. Navigate to "Pipeline Templates" in the left navigation bar

   1. Click on "Actions" and select "Import"

       **Pipeline Templates Action→Import**
![pipeline template action import](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/pipeline-template-action-import.png)

   1. Choose your saved lucid file

   1. Click "Submit" to complete the import

       **Template Import Submit**
![pipeline template import submit](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/pipeline-template-import-submit.png)

### After Lucid import is complete
<a name="after-lucid-import-is-complete"></a>

1. A new template will be created under Pipeline Templates

1. To see how your diagram attributes are converted in CMF:
   + Locate your newly created template in the Pipeline Templates list
   + Click on the template to open it
   + You’ll see a visual representation of your workflow under Visual task Editor

      **Pipeline Template Visual Task Editor**
![pipeline template visual](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/pipeline-template-visual.png)
   + Each shape from your diagram is now a task in CMF
   + Click on a task to view its details:
     + Task names correspond to the labels you gave shapes
     + For automated tasks, you’ll see the assigned AutomationID under Scripts dropdown.

        **Pipeline Template Task Edit**
![pipeline template task edit](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/pipeline-template-task-edit.png)
